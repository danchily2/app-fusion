#!/usr/bin/env python3
"""Does the new app call the same API as the legacy apps did, capability by capability?

    python3 api_parity.py <program> [--capability CAP-NNN ...] [--workspace DIR]
    python3 api_parity.py har <legacy.har> <new.har> [--out FILE] [--mask REGEX ...]
    python3 api_parity.py sanitize <in.har> <out.har>

Static mode (the default) compares, for each capability, the endpoints its legacy implementations call
(capabilities.json) with the endpoints the new app calls, extracted with the same rules as the inventory. The new
side is the endpoints defined in the capability's own files (the `## Files` section of docs/fusion/CAP-NNN.md) plus
the call sites its `## API` section lists as `path:line` in shared clients; a shared client named elsewhere credits
nothing by itself. Two endpoints match when their normalized paths are equal or one is a suffix of the other at a
segment boundary ({} matches any segment) and their methods agree (an unknown method matches any). A native pair is
checked per half. A backend move is written in docs/fusion/api-map.json ({"<METHOD> <legacy path>": "<METHOD> <new
path>"}): the mapped endpoint must then be called. A legacy endpoint the new app does not call is a difference,
unless a person recorded a decision `api: replaced | dropped | accepted` about "CAP-NNN:<METHOD> <path>". When the
map lists no endpoint for a capability, the legacy inventory is searched for endpoints in the capability's own files:
finding some is a gap, finding none is n/a. An endpoint string that cannot be read is reported, never dropped.

HAR mode compares two recordings of the same journey (for example from a proxy while Maestro drives each app):
the sets of request signatures (method, normalized path, sorted query keys, top-level JSON body keys). Values are
never compared; --mask drops whole paths that legitimately differ. `sanitize` writes a copy of a recording with
authorization headers, cookies and secret-looking query values removed: record, sanitize, then keep only the copy.

Writes analysis/<program>/evidence/api-parity.json (static) or --out (HAR). Exit 0 when nothing fails.
Standard library only.
"""

import argparse
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import newapp, parity, proofkit  # noqa: E402
from fusionlib.common import (check_name, die, endpoints_match, load_json, looks_secret, normalize_endpoint,  # noqa: E402
                              now_iso, workspace, write_json)

MAP = "docs/fusion/api-map.json"
SECRET_HEADERS = {"authorization", "cookie", "set-cookie", "proxy-authorization", "x-api-key", "x-auth-token", "x-csrf-token",
                  "x-xsrf-token", "ocp-apim-subscription-key"}


def parse_endpoint(text):
    """'GET /a/b' or '/a/b' -> (method or None, normalized path or None)."""
    s = str(text or "").strip()
    m = re.match(r"^(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|\?)\s+(.+)$", s, re.I)
    method, path = (m.group(1).upper(), m.group(2)) if m else (None, s)
    if method == "?":
        method = None
    return method, normalize_endpoint(path) if path.startswith(("/", "http")) or "/" in path else None


def _covered(legacy, new):
    lm, lp = legacy
    for nm, np_ in new:
        if endpoints_match(lp, np_) and (lm is None or nm is None or lm == nm):
            return f"{nm or '?'} {np_}"
    return None


def _new_side(inv_by_file, info, half):
    """Endpoints the capability's own files define plus those at the call sites its notes list."""
    out = []
    for f in info["files"]:
        if newapp.in_half(f, half):
            out += [(m, p) for m, p, _ in inv_by_file.get(f, [])]
    for f, line in info["api"]:
        if newapp.in_half(f, half):
            out += [(m, p) for m, p, l in inv_by_file.get(f, []) if l is not None and abs(l - line) <= 3]
    return list(dict.fromkeys(out))


def static(ws, program, only=None):
    pdir, caps, prog, decisions = parity.load_context(ws, program)
    if not caps:
        die(f"analysis/{program}/capabilities.json not found")
    approved = {d["about"]: (k, d["choice"]) for k, d in decisions.items() if d.get("kind") == "api"}
    api_map = {}
    for k, v in (load_json(os.path.join(newapp.root(ws, program), MAP)) or {}).items():
        lk, nk = parse_endpoint(k), parse_endpoint(v)
        if lk[1] and nk[1]:
            api_map[lk] = nk
    halves = newapp.halves(ws, program)
    by_half = {}
    for platform, half in halves:
        inv = newapp.inventory(ws, program, platform) if platform else newapp.inventory(ws, program)
        idx = {}
        for e in inv.get("endpoints", []):
            f, _, line = (e.get("file") or "").partition(":")
            idx.setdefault(f, []).append((e.get("method"), e["path"], int(line) if line.isdigit() else None))
        by_half[half] = idx
    results = {}
    for c, exists in parity.targets(ws, program, caps, only):
        cid = c["id"]
        if not exists:
            results[cid] = {"verdict": "gap", "reason": "no porting notes: the capability is not built yet"}
            continue
        info = proofkit.notes(ws, program, cid)
        legacy, unreadable = [], []
        for app, impl in (c.get("implementations") or {}).items():
            for raw in impl.get("endpoints") or []:
                parsed = parse_endpoint(raw)
                if not parsed[1]:
                    unreadable.append(f"{app}: {raw}")
                elif parsed not in legacy:
                    legacy.append(parsed)
        matched, mapped, missing, approved_rows, used, extra, missing_halves = [], [], [], [], [], set(), {}
        for platform, half in halves:
            new = _new_side(by_half[half], info, half)
            where = f" ({platform})" if platform else ""
            for lm, lp in legacy:
                key, alt = f"{cid}:{lm or '?'} {lp}", f"{cid}:{lp}"
                target = next((n for l, n in api_map.items() if endpoints_match(lp, l[1]) and (l[0] in (None, lm) or lm is None)), None)
                hit = _covered(target or (lm, lp), new)
                if hit and target:
                    mapped.append({"legacy": f"{lm or '?'} {lp}", "new": hit, "via": MAP, "half": platform})
                elif hit:
                    matched.append({"legacy": f"{lm or '?'} {lp}", "new": hit, "half": platform})
                elif key in approved or alt in approved:
                    did, choice = approved.get(key) or approved.get(alt)
                    approved_rows.append({"legacy": f"{lm or '?'} {lp}", "decision": did, "choice": choice, "half": platform})
                    used.append(did)
                else:
                    missing.append(f"{lm or '?'} {lp}")
                    if platform:
                        missing_halves.setdefault(f"{lm or '?'} {lp}", []).append(platform)
            extra |= {f"{m or '?'} {p}{where}" for m, p in new if not any(endpoints_match(p, lp) for _, lp in legacy)}
        files = info["files"] + [f for f, _ in info["api"]] + [MAP]
        stamp = parity.stamp(ws, program, cid, files, decisions, used)
        if not legacy and not unreadable:
            seen = []
            for app, impl in (c.get("implementations") or {}).items():
                cited = parity.cited_files(impl)
                seen += [f"{app}: {e.get('method') or '?'} {e['path']}" for e in parity.legacy_inventory(pdir, app).get("endpoints", [])
                         if parity.in_cited(e.get("file"), cited)]
            if seen:
                verdict, reason = "gap", (f"the map lists no endpoint, but the inventory finds {len(seen)} in the capability's legacy "
                                          f"files ({'; '.join(seen[:4])}{' …' if len(seen) > 4 else ''}): add them to the map")
            else:
                verdict, reason = "n/a", "no endpoint in the map, and the inventory finds none in the capability's legacy files"
        elif not info["files"]:
            verdict, reason = "gap", "the porting notes name no new-app file that exists"
        elif missing:
            verdict, reason = "fail", f"{len(missing)} legacy endpoint(s) not called by the new code and not approved"
        elif unreadable:
            verdict, reason = "gap", f"{len(unreadable)} legacy endpoint string(s) could not be read: {'; '.join(unreadable[:3])}"
        else:
            verdict, reason = "pass", f"{len(matched)} matched, {len(mapped)} through {MAP}, {len(approved_rows)} approved differences"
        missing = list(dict.fromkeys(missing))
        results[cid] = {"verdict": verdict, "reason": reason, "legacy": [f"{m or '?'} {p}" for m, p in legacy],
                        "unreadable": unreadable, "files": info["files"], "callSites": [f"{f}:{l}" for f, l in info["api"]],
                        "matched": matched, "mapped": mapped, "missing": missing, "missingIn": missing_halves, "approved": approved_rows,
                        "extra": sorted(extra), **stamp}
    path, counts = parity.write_result(
        ws, program, "api-parity.json",
        "legacy endpoints of the capability, matched by normalized path suffix and method, against the endpoints its own "
        "files and listed call sites define (per half of a native pair); differences need a person's api decision",
        results, {"mode": "static"})
    print(f"api parity: {', '.join(f'{v} {k}' for k, v in sorted(counts.items())) or 'nothing built yet'} -> "
          f"{os.path.relpath(path, ws)}")
    return 1 if counts.get("fail") else 0


def sanitize(src, dst):
    data = load_json(src)
    if not data or "log" not in data:
        die(f"{src} is not a HAR file")
    removed = 0
    for entry in data["log"].get("entries") or []:
        for part in (entry.get("request") or {}, entry.get("response") or {}):
            headers = part.get("headers") or []
            kept = [h for h in headers if (h.get("name") or "").lower() not in SECRET_HEADERS]
            removed += len(headers) - len(kept)
            part["headers"] = kept
            removed += len(part.get("cookies") or [])
            part["cookies"] = []
        req = entry.get("request") or {}
        for q in req.get("queryString") or []:
            if looks_secret(q.get("name") or ""):
                q["value"] = "****"
                removed += 1
        if req.get("url"):
            parts = urllib.parse.urlsplit(req["url"])
            query = urllib.parse.urlencode([(k, "****" if looks_secret(k) else v) for k, v in urllib.parse.parse_qsl(parts.query)])
            req["url"] = urllib.parse.urlunsplit(parts._replace(query=query, netloc=parts.netloc.split("@")[-1]))
    write_json(dst, data)
    print(f"sanitized {src} -> {dst}: {removed} header(s), cookie(s) or secret value(s) removed")
    return 0


def _har_signatures(path, masks):
    data = load_json(path)
    if not data or "log" not in data:
        die(f"{path} is not a HAR file")
    sigs = []
    for entry in data["log"].get("entries") or []:
        req = entry.get("request") or {}
        url = req.get("url") or ""
        parsed = urllib.parse.urlparse(url)
        norm = normalize_endpoint(parsed.path) or parsed.path
        if any(re.search(m, norm) for m in masks):
            continue
        qkeys = sorted({q.get("name") for q in req.get("queryString") or [] if q.get("name")})
        body_keys = []
        text = ((req.get("postData") or {}).get("text") or "").strip()
        if text.startswith("{"):
            try:
                body_keys = sorted(json.loads(text).keys())
            except ValueError:
                body_keys = []
        sigs.append({"method": (req.get("method") or "GET").upper(), "path": norm, "query": qkeys, "body": body_keys,
                     "host": parsed.hostname})
    return sigs


def har(legacy, new, out, masks):
    a, b = _har_signatures(legacy, masks), _har_signatures(new, masks)
    key = lambda s: (s["method"], s["path"])
    a_keys = {key(s) for s in a}
    b_keys = {key(s) for s in b}
    missing = sorted(k for k in a_keys if not any(k[0] == m and endpoints_match(k[1], p) for m, p in b_keys))
    extra = sorted(k for k in b_keys if not any(k[0] == m and endpoints_match(k[1], p) for m, p in a_keys))
    shape = []
    for s in a:
        twin = next((t for t in b if t["method"] == s["method"] and endpoints_match(s["path"], t["path"])), None)
        if twin and (s["query"] != twin["query"] or s["body"] != twin["body"]):
            shape.append({"request": f"{s['method']} {s['path']}", "legacy": {"query": s["query"], "body": s["body"]},
                          "new": {"query": twin["query"], "body": twin["body"]}})
    result = {"version": 1, "generated": now_iso(), "mode": "har", "legacy": legacy, "new": new, "masks": masks,
              "rule": "request signatures (method, normalized path) compared as sets; query keys and top-level JSON body keys compared per matched request; values never compared",
              "requests": {"legacy": len(a), "new": len(b)},
              "missing": [f"{m} {p}" for m, p in missing], "extra": [f"{m} {p}" for m, p in extra], "shapeDiffers": shape,
              "verdict": "pass" if not missing and not shape else "fail"}
    if out:
        write_json(out, result)
    print(f"har: {len(a)} legacy vs {len(b)} new requests; {len(missing)} missing, {len(extra)} extra, "
          f"{len(shape)} with a different shape -> {result['verdict']}")
    return 0 if result["verdict"] == "pass" else 1


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "sanitize":
        ap = argparse.ArgumentParser(prog="api_parity.py sanitize")
        ap.add_argument("cmd")
        ap.add_argument("src")
        ap.add_argument("dst")
        args = ap.parse_args()
        sys.exit(sanitize(args.src, args.dst))
    if len(sys.argv) > 1 and sys.argv[1] == "har":
        ap = argparse.ArgumentParser(prog="api_parity.py har")
        ap.add_argument("cmd")
        ap.add_argument("legacy")
        ap.add_argument("new")
        ap.add_argument("--out")
        ap.add_argument("--mask", action="append", default=[])
        args = ap.parse_args()
        sys.exit(har(args.legacy, args.new, args.out, args.mask))
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("--capability", action="append")
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    sys.exit(static(ws, args.program, set(args.capability or [])))


if __name__ == "__main__":
    main()
