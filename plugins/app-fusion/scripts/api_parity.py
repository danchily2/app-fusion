#!/usr/bin/env python3
"""Does the new app call the same API as the legacy apps did, capability by capability?

    python3 api_parity.py <program> [--capability CAP-NNN ...] [--workspace DIR]
    python3 api_parity.py har <legacy.har> <new.har> [--out FILE] [--mask REGEX ...]

Static mode (the default) compares, for each capability, the endpoints its legacy implementations call
(capabilities.json) with the endpoints the new app calls in the files its porting notes name
(new-app/<program>/docs/fusion/CAP-NNN.md), extracted with the same rules as the inventory. Two endpoints match when
their normalized paths are equal or one is a suffix of the other at a segment boundary ({} matches any segment) and
their methods agree (an unknown method matches any). A legacy endpoint the new app does not call is a difference,
unless a person recorded a decision `api: replaced | dropped | accepted` about "CAP-NNN:<METHOD> <path>".
A capability passes when every legacy endpoint is matched or approved.

HAR mode compares two recordings of the same journey (for example from a proxy while Maestro drives each app):
the sets of request signatures (method, normalized path, sorted query keys, top-level JSON body keys). Values are
never compared, so tokens, ids and timestamps need no masking; --mask drops whole paths that legitimately differ.

Writes analysis/<program>/evidence/api-parity.json (static) or --out (HAR). Exit 0 all pass, 1 any difference.
Standard library only.
"""

import argparse
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import newapp  # noqa: E402
from fusionlib.common import (check_name, die, endpoints_match, load_json, normalize_endpoint, now_iso,  # noqa: E402
                              program_dir, workspace, write_json)


def parse_endpoint(text):
    """'GET /a/b' or '/a/b' -> (method or None, normalized path)."""
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


def static(ws, program, only=None):
    pdir = program_dir(ws, program)
    caps = load_json(os.path.join(pdir, "capabilities.json"))
    if not caps:
        die(f"analysis/{program}/capabilities.json not found")
    decisions = (load_json(os.path.join(pdir, "DECISIONS.json")) or {}).get("decisions") or {}
    approved = {d["about"]: d["choice"] for d in decisions.values() if d.get("kind") == "api"}
    inv = newapp.inventory(ws, program)
    by_file = {}
    for e in inv.get("endpoints", []):
        by_file.setdefault((e.get("file") or "").split(":")[0], []).append((e.get("method"), e["path"]))
    results = {}
    for c in caps.get("capabilities", []):
        cid = c["id"]
        if only and cid not in only:
            continue
        files = newapp.notes_files(ws, program, cid)
        if not os.path.isfile(newapp.notes_path(ws, program, cid)):
            if only:
                results[cid] = {"verdict": "gap", "reason": "no porting notes: the capability is not built yet"}
            continue
        new = [ep for f in files for ep in by_file.get(f, [])]
        legacy = []
        for app, impl in (c.get("implementations") or {}).items():
            for raw in impl.get("endpoints") or []:
                parsed = parse_endpoint(raw)
                if parsed[1] and parsed not in legacy:
                    legacy.append(parsed)
        matched, missing, approved_rows = [], [], []
        for lm, lp in legacy:
            hit = _covered((lm, lp), new)
            key = f"{cid}:{lm or '?'} {lp}"
            alt = f"{cid}:{lp}"
            if hit:
                matched.append({"legacy": f"{lm or '?'} {lp}", "new": hit})
            elif key in approved or alt in approved:
                approved_rows.append({"legacy": f"{lm or '?'} {lp}", "decision": approved.get(key) or approved.get(alt)})
            else:
                missing.append(f"{lm or '?'} {lp}")
        extra = sorted({f"{m or '?'} {p}" for m, p in new if not any(endpoints_match(p, lp) for _, lp in legacy)})
        if not legacy:
            verdict, reason = "n/a", "the legacy implementations call no endpoint the map recorded"
        elif not files:
            verdict, reason = "gap", "the porting notes name no new-app file that exists"
        elif missing:
            verdict, reason = "fail", f"{len(missing)} legacy endpoint(s) not called by the new files and not approved"
        else:
            verdict, reason = "pass", f"{len(matched)} matched, {len(approved_rows)} approved differences"
        results[cid] = {"verdict": verdict, "reason": reason, "legacy": [f"{m or '?'} {p}" for m, p in legacy],
                        "files": files, "matched": matched, "missing": missing, "approved": approved_rows, "extra": extra}
    out = {"program": program, "version": 1, "generated": now_iso(), "mode": "static",
           "rule": "legacy endpoints of the capability, matched by normalized path suffix and method, against endpoints in the files the porting notes name",
           "capabilities": results}
    path = os.path.join(pdir, "evidence", "api-parity.json")
    write_json(path, out)
    counts = {}
    for r in results.values():
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print(f"api parity: {', '.join(f'{v} {k}' for k, v in sorted(counts.items())) or 'nothing built yet'} -> "
          f"{os.path.relpath(path, ws)}")
    return 1 if counts.get("fail") else 0


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
