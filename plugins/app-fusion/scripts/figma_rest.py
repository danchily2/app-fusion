#!/usr/bin/env python3
"""Snapshot a Figma file through the Figma REST API: pages, frames, texts, frame images and variables.

    FIGMA_TOKEN=... python3 figma_rest.py pages <program> <fileKey>
    FIGMA_TOKEN=... python3 figma_rest.py snapshot <program> <fileKey> [--pages ID,ID] [--images] [--scale 1] [--max-images N]

The token is read from the FIGMA_TOKEN environment variable only: it is never written to a file, printed or put
in a URL. Responses are cached in the same layout the MCP path uses (analysis/<program>/design/cache/<fileKey>/),
so `figma_index.py build` merges both. One REST call returns a whole page with every text layer, so a file with
hundreds of screens costs a handful of requests instead of hundreds of MCP calls. A 429 stops the run, keeps what
was fetched and prints how long Figma asked to wait. FIGMA_API_BASE overrides the API root (for tests).
Standard library only.
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import figma_index as fx  # noqa: E402
from fusionlib.common import check_name, die, load_json, workspace, write_json  # noqa: E402

API = os.environ.get("FIGMA_API_BASE", "https://api.figma.com").rstrip("/")
FRAME_TYPES = {"FRAME", "COMPONENT", "COMPONENT_SET", "INSTANCE", "GROUP"}


class RateLimited(Exception):
    pass


def _token():
    token = os.environ.get("FIGMA_TOKEN", "").strip()
    if not token:
        die("FIGMA_TOKEN is not set. Create a personal access token (Figma > Settings > Security) with file_content:read "
            "(and file_variables:read for tokens), export it in this shell, and run again. It is never stored.", code=4)
    return token


def get(path, params=None, binary=False, retries=2, fatal=True):
    url = f"{API}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"X-Figma-Token": _token(), "User-Agent": "app-fusion/1"})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                body = resp.read()
                return body if binary else json.loads(body.decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code == 429:
                raise RateLimited(exc.headers.get("Retry-After") or "unknown")
            if exc.code in (500, 502, 503, 504) and attempt < retries:
                time.sleep(2 * (attempt + 1))
                continue
            detail = ""
            try:
                detail = json.loads(exc.read().decode("utf-8")).get("err") or ""
            except Exception:
                pass
            if not fatal and exc.code in (400, 403, 404):
                return None
            if exc.code == 403:
                die(f"Figma refused access ({detail or 'forbidden'}): the token lacks the scope, or you cannot open this file", code=4)
            if exc.code == 404:
                die(f"Figma says the file or node does not exist ({detail or 'not found'})", code=4)
            die(f"Figma API error {exc.code}: {detail}", code=4)
        except urllib.error.URLError as exc:
            if attempt < retries:
                time.sleep(2 * (attempt + 1))
                continue
            die(f"cannot reach the Figma API: {exc.reason}", code=4)


def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "app-fusion/1"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = resp.read()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as fh:
        fh.write(data)


def walk_frames(page, file_key):
    """Frames on a page or directly in a section, with every TEXT node's characters and the instance names."""
    screens, instances = [], {}

    def texts(node, out):
        if node.get("type") == "TEXT":
            chars = (node.get("characters") or "").strip()
            if chars and chars not in out and len(chars) <= 300:
                out.append(chars)
        if node.get("type") == "INSTANCE" and node.get("name"):
            instances[node["name"]] = instances.get(node["name"], 0) + 1
        for child in node.get("children") or []:
            texts(child, out)
        return out

    def visit(node, section):
        for child in node.get("children") or []:
            if child.get("type") == "SECTION":
                visit(child, child.get("name") or "")
                continue
            if child.get("type") not in FRAME_TYPES:
                continue
            box = child.get("absoluteBoundingBox") or {}
            w, h = box.get("width") or 0, box.get("height") or 0
            kind = fx.classify(child.get("name") or "", w, h)
            if child.get("type") in ("COMPONENT", "COMPONENT_SET"):
                kind = "component"
            found = texts(child, []) if kind in ("screen", "state") else []
            screens.append({"id": f"{file_key}:{child['id']}", "fileKey": file_key, "nodeId": child["id"],
                            "name": child.get("name") or "", "page": page.get("name") or "", "section": section,
                            "width": round(w), "height": round(h), "kind": kind, "shot": None, "texts": found})

    visit(page, "")
    return screens, instances


def resolve_variables(payload):
    """{name: value} for the default mode of each collection, following aliases (the REST variables endpoint)."""
    meta = (payload or {}).get("meta") or {}
    variables = meta.get("variables") or {}
    collections = meta.get("variableCollections") or {}

    def value_of(var_id, depth=0):
        var = variables.get(var_id)
        if not var or depth > 10:
            return None
        coll = collections.get(var.get("variableCollectionId")) or {}
        mode = coll.get("defaultModeId") or next(iter(var.get("valuesByMode") or {}), None)
        val = (var.get("valuesByMode") or {}).get(mode)
        if isinstance(val, dict) and val.get("type") == "VARIABLE_ALIAS":
            return value_of(val.get("id"), depth + 1)
        if isinstance(val, dict) and {"r", "g", "b"} <= set(val):
            a = val.get("a", 1)
            hexv = "#" + "".join(f"{round(val[c] * 255):02X}" for c in ("r", "g", "b"))
            return hexv + (f"{round(a * 255):02X}" if a < 1 else "")
        return val

    return {v.get("name"): value_of(vid) for vid, v in variables.items() if v.get("name")}


def cmd_pages(ws, program, file_key):
    data = get(f"/v1/files/{file_key}", {"depth": 1})
    path = fx.cache_path(ws, program, file_key, "pages", "rest-file")
    write_json(path, {"name": data.get("name"), "lastModified": data.get("lastModified"),
                      "pages": [{"id": p["id"], "name": p.get("name")} for p in (data.get("document") or {}).get("children") or []]})
    design = fx.load_design(ws, program)
    entry = fx._file_entry(design, file_key, data.get("name"))
    scoped = {p["id"] for p in entry.get("pages", []) if p.get("inScope")}
    entry["pages"] = [{"id": p["id"], "name": p.get("name"), "inScope": p["id"] in scoped}
                      for p in (data.get("document") or {}).get("children") or []]
    design["source"] = "rest"
    fx.save_design(ws, program, design)
    fx.budget(ws, program, spend=0)
    for p in entry["pages"]:
        print(f"{p['id']}\t{p['name']}")
    print(f"{len(entry['pages'])} page(s) of {data.get('name')!r}; mark the new app's pages with figma_index.py scope")


def cmd_snapshot(ws, program, file_key, page_ids, images, scale, max_images):
    design = fx.load_design(ws, program)
    entry = next((f for f in design["files"] if f["fileKey"] == file_key), None)
    if not entry or not entry.get("pages"):
        die(f"no page list for {file_key}: run `figma_rest.py pages {program} {file_key}` first")
    wanted = page_ids or [p["id"] for p in entry["pages"] if p.get("inScope")]
    if not wanted:
        die("no page is in scope: pass --pages or mark pages with figma_index.py scope")
    screens, instances, requests = [], {}, 1
    try:
        nodes = get(f"/v1/files/{file_key}/nodes", {"ids": ",".join(wanted)})
        write_json(fx.cache_path(ws, program, file_key, wanted[0], "rest-file"), {"pages": wanted, "nodes": list((nodes.get("nodes") or {}).keys())})
        for pid in wanted:
            doc = ((nodes.get("nodes") or {}).get(pid) or {}).get("document")
            if not doc:
                print(f"warning: page {pid} came back empty", file=sys.stderr)
                continue
            found, inst = walk_frames(doc, file_key)
            screens += found
            for k, v in inst.items():
                instances[k] = instances.get(k, 0) + v
        index_path = os.path.join(fx.design_dir(ws, program), "cache", file_key, f"{fx.node_slug(wanted[0])}.rest-index.json")
        write_json(index_path, {"fileKey": file_key, "pages": wanted, "screens": screens, "instances": instances})
        if images:
            targets = [s for s in screens if s["kind"] in ("screen", "state")
                       and not os.path.isfile(fx.cache_path(ws, program, file_key, s["nodeId"], "shot"))][: max_images or None]
            for i in range(0, len(targets), 50):
                batch = targets[i: i + 50]
                resp = get(f"/v1/images/{file_key}", {"ids": ",".join(s["nodeId"] for s in batch), "format": "png", "scale": scale})
                requests += 1
                for s in batch:
                    url = (resp.get("images") or {}).get(s["nodeId"])
                    if url:
                        download(url, fx.cache_path(ws, program, file_key, s["nodeId"], "shot"))
        payload = get(f"/v1/files/{file_key}/variables/local", fatal=False)
        requests += 1
        if payload:
            write_json(fx.cache_path(ws, program, file_key, "0:0", "rest-variables"), {"resolved": resolve_variables(payload)})
        else:
            print("note: variables were not read (the endpoint needs an Enterprise plan and the file_variables:read scope); "
                  "tokens will come from get_variable_defs on a representative frame instead", file=sys.stderr)
    except RateLimited as exc:
        print(f"Figma rate limit reached; it asked to wait {exc} second(s). What was fetched is cached; run the same command "
              "again later and it continues.", file=sys.stderr)
        sys.exit(5)
    fx.build(ws, program)
    print(f"REST snapshot of {file_key}: {len(screens)} frames on {len(wanted)} page(s), {requests + 1} request(s)")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pages")
    p.add_argument("program")
    p.add_argument("fileKey")
    p.add_argument("--workspace")
    p = sub.add_parser("snapshot")
    p.add_argument("program")
    p.add_argument("fileKey")
    p.add_argument("--pages")
    p.add_argument("--images", action="store_true")
    p.add_argument("--scale", type=float, default=1)
    p.add_argument("--max-images", type=int, default=0)
    p.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    if not fx.FILE_KEY.match(args.fileKey):
        die(f"{args.fileKey!r} is not a Figma file key")
    if args.cmd == "pages":
        cmd_pages(ws, args.program, args.fileKey)
    else:
        pages = [x.strip().replace("-", ":") for x in (args.pages or "").split(",") if x.strip()]
        cmd_snapshot(ws, args.program, args.fileKey, pages, args.images, args.scale, args.max_images)


if __name__ == "__main__":
    main()
