#!/usr/bin/env python3
"""Keep Figma reads cached, counted and indexed.

    python3 figma_index.py path <program> <fileKey> <nodeId|pages> <tool>     where to save one response
    python3 figma_index.py pages <program> <fileKey> <file> [--name NAME] [--url URL]
                                                                     parse a get_metadata page listing into design.json
    python3 figma_index.py scope <program> <fileKey> --pages ID[,ID...]   mark the pages that hold the new app
    python3 figma_index.py budget <program> [--spend N] [--limit N]      calls spent today and in this run
    python3 figma_index.py plan <program> [--limit N] [--json]           the next calls needed, cheapest first
    python3 figma_index.py build <program>                               cache -> design/design.json

Cache layout (docs/DESIGN.md): analysis/<program>/design/cache/<fileKey>/<node>.<tool>.<ext>, with node ids written
as 12-345. Tools: pages (txt), metadata (xml), variables (txt/json), context (txt), shot (png, stored under
design/shots/). `build` never calls Figma: it parses what is cached, so it is free to re-run. A frame is a screen
when it sits on a page or directly in a section and has a phone or tablet shape; its texts are the names of its
text layers (Figma names a text layer after its content unless someone renamed it). Standard library only.
"""

import argparse
import collections
import glob
import html
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib.common import check_name, die, load_json, now_iso, program_dir, read_text, workspace, write_json  # noqa: E402

FILE_KEY = re.compile(r"^[0-9A-Za-z]{22,128}$")
NODE = re.compile(r"^(?:\d+[:-]\d+|[IT]\d+[:-]\d+(?:;\d+[:-]\d+)*)$")
TOOLS = {"pages": "txt", "metadata": "xml", "variables": "txt", "context": "txt", "shot": "png", "rest-file": "json",
         "rest-images": "json", "rest-variables": "json"}
STATE_WORDS = re.compile(r"\b(state|empty|error|loading|skeleton|success|failure|disabled|selected|hover|pressed|variant|dark|light)\b", re.I)
COMPONENT_WORDS = re.compile(r"\b(component|components|icon|icons|button|buttons|token|tokens|library|kit|cover|thumbnail|legend|annotation|notes?)\b", re.I)
FLOW_WORDS = re.compile(r"\b(flow|flows|journey|user ?flow|prototype)\b", re.I)


def node_slug(node):
    return node.replace(":", "-").replace(";", "_")


def design_dir(ws, program):
    return os.path.join(program_dir(ws, program), "design")


def cache_path(ws, program, file_key, node, tool):
    if not FILE_KEY.match(file_key):
        die(f"{file_key!r} is not a Figma file key")
    if node != "pages" and not NODE.match(node):
        die(f"{node!r} is not a Figma node id (like 12:345)")
    if tool not in TOOLS:
        die(f"tool {tool!r} is not one of {', '.join(TOOLS)}")
    base = design_dir(ws, program)
    if tool == "shot":
        return os.path.join(base, "shots", file_key, f"{node_slug(node)}.png")
    return os.path.join(base, "cache", file_key, f"{node_slug(node)}.{tool}.{TOOLS[tool]}")


# ---------------------------------------------------------------- design.json skeleton

def load_design(ws, program):
    path = os.path.join(design_dir(ws, program), "design.json")
    data = load_json(path)
    if not data:
        prog = load_json(os.path.join(program_dir(ws, program), "program.json")) or {}
        data = {"program": program, "version": 1, "source": "mcp",
                "files": [{"fileKey": f["fileKey"], "name": f.get("name"), "url": f.get("url"), "pages": []}
                          for f in prog.get("figma", [])],
                "screens": [], "components": [], "tokens": {"colors": {}, "typography": {}, "spacing": {}, "other": {}},
                "budget": {"used": 0, "limit": 0}, "notCaptured": []}
    return data


def save_design(ws, program, data):
    write_json(os.path.join(design_dir(ws, program), "design.json"), data)


def _file_entry(data, file_key, name=None, url=None):
    entry = next((f for f in data["files"] if f["fileKey"] == file_key), None)
    if entry is None:
        entry = {"fileKey": file_key, "name": name or file_key, "url": url or f"https://www.figma.com/design/{file_key}", "pages": []}
        data["files"].append(entry)
    if name:
        entry["name"] = name
    if url:
        entry["url"] = url
    return entry


def parse_pages(text):
    """Pages from a get_metadata call made without a node id: lines like '- 14522:92030: -> Cover'."""
    pages = []
    for m in re.finditer(r"(?m)^\s*-\s*(\d+:\d+)\s*:\s*(.+?)\s*$", text or ""):
        pages.append({"id": m.group(1), "name": html.unescape(m.group(2)), "inScope": False})
    if not pages:
        for m in re.finditer(r"<canvas[^>]*\bid=\"(\d+:\d+)\"[^>]*\bname=\"([^\"]*)\"", text or ""):
            pages.append({"id": m.group(1), "name": html.unescape(m.group(2)), "inScope": False})
    return pages


# ---------------------------------------------------------------- metadata XML

def extract_xml(text):
    """The XML part of a get_metadata response (tools append guidance text after it)."""
    if not text:
        return None
    start = text.find("<")
    if start < 0:
        return None
    m = re.match(r"<([A-Za-z][A-Za-z0-9_-]*)", text[start:])
    if not m:
        return None
    root = m.group(1)
    end = text.rfind(f"</{root}>")
    if end < 0:
        close = text.find("/>", start)
        return text[start: close + 2] if close > 0 else None
    return text[start: end + len(root) + 3]


def _num(el, key):
    try:
        return float(el.get(key) or 0)
    except ValueError:
        return 0.0


def classify(name, w, h):
    if w <= 0 or h <= 0:
        return "other"
    if COMPONENT_WORDS.search(name or "") and not re.search(r"screen|page|view", name or "", re.I):
        return "component"
    if FLOW_WORDS.search(name or "") and (w > 1200 or h > 3000):
        return "flow"
    phone = 300 <= w <= 480 and h >= 480
    tablet = 700 <= w <= 1400 and h >= 700 and h > w * 0.6 and not (w == 1920 or (w >= 1200 and h <= 1100 and w > h * 1.6))
    if phone or tablet:
        return "state" if STATE_WORDS.search(name or "") else "screen"
    if w < 300 or h < 300:
        return "component"
    return "other"


def parse_metadata(xml_text, file_key, page_name):
    """Screens (frames on the page or directly inside a section) with their text-layer names, and instance counts."""
    xml_text = extract_xml(xml_text)
    if not xml_text:
        return [], collections.Counter()
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return [], collections.Counter()
    screens, instances = [], collections.Counter()

    def texts_of(el):
        out = []
        for t in el.iter("text"):
            name = html.unescape(t.get("name") or "").strip()
            if name and name not in out and len(name) <= 300:
                out.append(name)
        return out

    def visit(el, section):
        for child in list(el):
            tag = child.tag
            if tag == "section":
                visit(child, html.unescape(child.get("name") or ""))
                continue
            if tag not in ("frame", "component", "component-set", "instance", "group"):
                continue
            node = child.get("id")
            if not node:
                continue
            name = html.unescape(child.get("name") or "")
            w, h = _num(child, "width"), _num(child, "height")
            kind = classify(name, w, h)
            if tag in ("component", "component-set"):
                kind = "component"
            screens.append({"id": f"{file_key}:{node}", "fileKey": file_key, "nodeId": node, "name": name,
                            "page": page_name, "section": section, "width": round(w), "height": round(h), "kind": kind,
                            "shot": None, "texts": texts_of(child) if kind in ("screen", "state") else []})

    visit(root, "")
    for inst in root.iter("instance"):
        name = html.unescape(inst.get("name") or "")
        if name:
            instances[name] += 1
    return screens, instances


# ---------------------------------------------------------------- variables and design context

def parse_variables(text):
    """get_variable_defs returns a mapping such as {'icon/default/secondary': '#949494', 'Body/regular': 'Font(...)'}."""
    out = {}
    if not text:
        return out
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            return {str(k): str(v) for k, v in data.items()}
    except ValueError:
        pass
    for m in re.finditer(r"['\"]([^'\"\n]{1,120})['\"]\s*:\s*(?:['\"]([^'\"\n]{0,200})['\"]|([^,}\n]{1,200}))", text):
        out[m.group(1)] = (m.group(2) if m.group(2) is not None else m.group(3) or "").strip()
    return out


def token_group(name, value):
    v = str(value)
    if re.match(r"^#[0-9A-Fa-f]{3,8}$", v) or v.startswith(("rgb", "hsl")):
        return "colors"
    if "font" in v.lower() or re.search(r"(typography|font|text|body|heading|title|label|caption)", name, re.I) and not v.startswith("#"):
        return "typography"
    if re.match(r"^-?\d+(\.\d+)?(px)?$", v) or re.search(r"(spacing|space|padding|gap|radius|size)", name, re.I):
        return "spacing"
    return "other"


def texts_from_context(text):
    """Visible strings in generated design-context code: JSX text children and string props such as title/label."""
    out = []
    for m in re.finditer(r">\s*([^<>{}\n][^<>{}\n]{0,200}?)\s*<", text or ""):
        s = html.unescape(m.group(1)).strip()
        if s and not s.startswith(("//", "import ")) and s not in out:
            out.append(s)
    for m in re.finditer(r"\b(?:title|label|text|placeholder|alt|aria-label)\s*=\s*\"([^\"]{1,200})\"", text or ""):
        s = html.unescape(m.group(1)).strip()
        if s and s not in out:
            out.append(s)
    return out


# ---------------------------------------------------------------- budget

def budget(ws, program, spend=0, limit=None):
    path = os.path.join(design_dir(ws, program), "budget.json")
    data = load_json(path) or {"version": 1, "days": {}, "runs": []}
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if spend:
        data["days"][day] = data["days"].get(day, 0) + int(spend)
        write_json(path, data)
    return {"today": day, "spentToday": data["days"].get(day, 0), "spentTotal": sum(data["days"].values()),
            "limit": limit}


# ---------------------------------------------------------------- plan and build

def build(ws, program):
    data = load_design(ws, program)
    base = design_dir(ws, program)
    screens, instances = [], collections.Counter()
    old = {s["id"]: s for s in data.get("screens", [])}
    for f in data["files"]:
        for page in f.get("pages", []):
            if not page.get("inScope"):
                continue
            path = os.path.join(base, "cache", f["fileKey"], f"{node_slug(page['id'])}.metadata.xml")
            found, inst = parse_metadata(read_text(path, limit=50_000_000), f["fileKey"], page["name"])
            screens += found
            instances.update(inst)
    for s in screens:
        shot = os.path.join(base, "shots", s["fileKey"], f"{node_slug(s['nodeId'])}.png")
        if os.path.isfile(shot):
            s["shot"] = os.path.relpath(shot, ws)
        ctx = os.path.join(base, "cache", s["fileKey"], f"{node_slug(s['nodeId'])}.context.txt")
        if os.path.isfile(ctx):
            for t in texts_from_context(read_text(ctx)):
                if t not in s["texts"]:
                    s["texts"].append(t)
            s["context"] = os.path.relpath(ctx, ws)
        prev = old.get(s["id"])
        if prev and prev.get("kindOverride"):
            s["kind"] = prev["kindOverride"]
            s["kindOverride"] = prev["kindOverride"]
    tokens = {"colors": {}, "typography": {}, "spacing": {}, "other": {}}
    for path in sorted(glob.glob(os.path.join(base, "cache", "*", "*.variables.*"))):
        for name, value in parse_variables(read_text(path)).items():
            tokens[token_group(name, value)].setdefault(name, value)
    for path in sorted(glob.glob(os.path.join(base, "cache", "*", "*.rest-variables.json"))):
        payload = load_json(path) or {}
        for name, value in (payload.get("resolved") or {}).items():
            tokens[token_group(name, value)].setdefault(name, value)
    rest_screens = []
    for path in sorted(glob.glob(os.path.join(base, "cache", "*", "*.rest-index.json"))):
        rest_screens += (load_json(path) or {}).get("screens", [])
    if rest_screens:
        known = {s["id"] for s in screens}
        for s in rest_screens:
            if s["id"] not in known and any(p.get("inScope") and p["name"] == s.get("page")
                                            for f in data["files"] if f["fileKey"] == s["fileKey"] for p in f["pages"]):
                shot = os.path.join(base, "shots", s["fileKey"], f"{node_slug(s['nodeId'])}.png")
                s["shot"] = os.path.relpath(shot, ws) if os.path.isfile(shot) else None
                screens.append(s)
    data["screens"] = sorted(screens, key=lambda s: (s["fileKey"], s["page"], s.get("section") or "", s["name"], s["nodeId"]))
    data["components"] = [{"name": n, "library": "", "instances": c} for n, c in instances.most_common(200)]
    data["tokens"] = tokens
    b = budget(ws, program)
    data["budget"] = {"used": b["spentTotal"], "limit": data.get("budget", {}).get("limit", 0)}
    data["notCaptured"] = [{"id": s["id"], "why": "no screenshot cached yet"} for s in data["screens"]
                           if s["kind"] in ("screen", "state") and not s["shot"]]
    data["generated"] = now_iso()
    save_design(ws, program, data)
    kinds = collections.Counter(s["kind"] for s in data["screens"])
    print(f"design.json: {len(data['screens'])} frames ({', '.join(f'{v} {k}' for k, v in kinds.most_common())}), "
          f"{sum(1 for s in data['screens'] if s['shot'])} with a screenshot, {sum(len(v) for v in tokens.values())} tokens, "
          f"{len(data['components'])} component names")
    return data


def plan(ws, program, limit):
    data = load_design(ws, program)
    base = design_dir(ws, program)
    steps = []
    for f in data["files"]:
        if not f.get("pages"):
            steps.append({"call": "get_metadata", "fileKey": f["fileKey"], "nodeId": None, "save": "pages",
                          "why": "list the pages"})
            continue
        for page in f["pages"]:
            if page.get("inScope") and not os.path.isfile(os.path.join(base, "cache", f["fileKey"], f"{node_slug(page['id'])}.metadata.xml")):
                steps.append({"call": "get_metadata", "fileKey": f["fileKey"], "nodeId": page["id"], "save": "metadata",
                              "why": f"frames on page {page['name']}"})
    shots = [s for s in data.get("screens", []) if s.get("kind") in ("screen", "state") and not s.get("shot")]
    for s in shots:
        steps.append({"call": "get_screenshot", "fileKey": s["fileKey"], "nodeId": s["nodeId"], "save": "shot",
                      "why": f"screenshot of {s['name']}"})
    have_vars = glob.glob(os.path.join(base, "cache", "*", "*.variables.*")) + glob.glob(os.path.join(base, "cache", "*", "*.rest-variables.json"))
    if not have_vars:
        reps = [s for s in data.get("screens", []) if s.get("kind") == "screen"][:2]
        for s in reps:
            steps.append({"call": "get_variable_defs", "fileKey": s["fileKey"], "nodeId": s["nodeId"], "save": "variables",
                          "why": f"design tokens used on {s['name']}"})
    return steps[:limit] if limit else steps, len(steps)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("path")
    p.add_argument("program")
    p.add_argument("fileKey")
    p.add_argument("node")
    p.add_argument("tool")
    p.add_argument("--workspace")
    p = sub.add_parser("pages")
    p.add_argument("program")
    p.add_argument("fileKey")
    p.add_argument("file")
    p.add_argument("--name")
    p.add_argument("--url")
    p.add_argument("--workspace")
    p = sub.add_parser("scope")
    p.add_argument("program")
    p.add_argument("fileKey")
    p.add_argument("--pages", required=True)
    p.add_argument("--workspace")
    p = sub.add_parser("budget")
    p.add_argument("program")
    p.add_argument("--spend", type=int, default=0)
    p.add_argument("--limit", type=int)
    p.add_argument("--workspace")
    p = sub.add_parser("plan")
    p.add_argument("program")
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--json", action="store_true")
    p.add_argument("--workspace")
    p = sub.add_parser("build")
    p.add_argument("program")
    p.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    if args.cmd == "path":
        path = cache_path(ws, args.program, args.fileKey, args.node, args.tool)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        print(os.path.relpath(path, ws))
    elif args.cmd == "pages":
        text = read_text(args.file)
        pages = parse_pages(text)
        if not pages:
            die(f"no pages found in {args.file}: save the raw get_metadata response (called without a node id)")
        data = load_design(ws, args.program)
        entry = _file_entry(data, args.fileKey, args.name, args.url)
        scoped = {p["id"] for p in entry.get("pages", []) if p.get("inScope")}
        entry["pages"] = [{**p, "inScope": p["id"] in scoped} for p in pages]
        save_design(ws, args.program, data)
        for p in pages:
            print(f"{p['id']}\t{p['name']}")
        print(f"{len(pages)} page(s) recorded for {args.fileKey}; mark the new app's pages with `scope`")
    elif args.cmd == "scope":
        data = load_design(ws, args.program)
        entry = next((f for f in data["files"] if f["fileKey"] == args.fileKey), None)
        if not entry or not entry.get("pages"):
            die(f"no page list for {args.fileKey} yet: run `pages` first")
        wanted = {x.strip().replace("-", ":") for x in args.pages.split(",") if x.strip()}
        unknown = wanted - {p["id"] for p in entry["pages"]}
        if unknown:
            die(f"unknown page id(s): {', '.join(sorted(unknown))}")
        for p in entry["pages"]:
            p["inScope"] = p["id"] in wanted
        save_design(ws, args.program, data)
        print(f"in scope: {', '.join(p['name'] for p in entry['pages'] if p['inScope'])}")
    elif args.cmd == "budget":
        b = budget(ws, args.program, args.spend, args.limit)
        print(json.dumps(b))
    elif args.cmd == "plan":
        steps, total = plan(ws, args.program, args.limit)
        if args.json:
            print(json.dumps({"total": total, "next": steps}, indent=2))
        else:
            print(f"{total} Figma call(s) still needed" + (f"; next {len(steps)}:" if steps else ""))
            for s in steps:
                print(f"  {s['call']} {s['fileKey']} {s['nodeId'] or '(no node: page list)'} -> {s['save']}  # {s['why']}")
    else:
        build(ws, args.program)


if __name__ == "__main__":
    main()
