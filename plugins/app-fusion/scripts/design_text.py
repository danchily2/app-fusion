#!/usr/bin/env python3
"""Does each designed screen's text exist in the new app's strings?

    python3 design_text.py <program> [--capability CAP-NNN ...] [--threshold 0.9] [--workspace DIR]

For every built capability with design screens (traceability.json), the texts of each linked screen (design.json:
text-layer names from metadata, or TEXT characters from the REST path, or strings from a cached design context) are
compared with the values of the new app's string catalog, all locales. Placeholder texts are left out and listed:
digits-only, dates, times, amounts, e-mail addresses, lorem ipsum, single characters and sample people's names
listed in docs/fusion/design-placeholders.json. A text matches when it equals a catalog value after normalizing case,
whitespace and edge punctuation, or fits a catalog template ({{count}}, {name}, %@, %d, %1$s ... match anything).

A screen passes when at least the threshold (default 90%) of its texts match; a capability passes when all its
screens do. This checks copy, not layout: look and feel is signed by a person from the side-by-side screenshots.
Writes analysis/<program>/evidence/design-text.json. Exit 0 all pass, 1 any screen below the threshold.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import newapp  # noqa: E402
from fusionlib.common import check_name, die, load_json, now_iso, program_dir, workspace, write_json  # noqa: E402

PLACEHOLDER = re.compile(
    r"^\s*(?:[\d\s.,:/+\-%€$£¥]+|\d{1,2}[:.]\d{2}(?:\s?[ap]m)?|[\w.+-]+@[\w-]+\.[\w.]+|lorem ipsum.*|.|\W+|"
    r"(?:mon|tue|wed|thu|fri|sat|sun)[a-z]*,?\s*\d.*|\d+\s*(?:kr|nok|sek|dkk|eur|usd|h|min|days?|hours?)\.?)\s*$", re.I)
TEMPLATE = re.compile(r"\{\{[^}]*\}\}|\{[A-Za-z0-9_]*\}|%(?:\d+\$)?[@sdifu]|%\.\d+f|\$\{[^}]*\}|<\d+>|<[a-z]+>|</[a-z]+>")


def norm(text):
    s = re.sub(r"\s+", " ", str(text or "").strip().casefold())
    return s.strip(" .,:;!?…'\"“”‘’()[]-–—")


def template_regex(value):
    parts = TEMPLATE.split(value)
    if len(parts) == 1:
        return None
    body = ".+?".join(re.escape(norm(p)) if p.strip() else "" for p in parts)
    return re.compile("^" + body + "$") if body.replace(".+?", "") else None


def run(ws, program, only=None, threshold=0.9):
    pdir = program_dir(ws, program)
    trace = load_json(os.path.join(pdir, "traceability.json"))
    design = load_json(os.path.join(pdir, "design", "design.json"))
    if not trace or not design:
        die(f"analysis/{program}/traceability.json and design/design.json are needed: run /app-fusion:fuse-design {program}")
    extra_placeholders = set(norm(x) for x in (load_json(os.path.join(newapp.root(ws, program), "docs", "fusion", "design-placeholders.json")) or []))
    screens = {s["id"]: s for s in design.get("screens", [])}
    cat = newapp.catalog(ws, program)
    values = set()
    templates = []
    # every locale, not only the source one: design copy may be written in the product's main language
    for loc_values in list((cat.get("allValues") or {}).values()) or [cat.get("values") or {}]:
        for v in loc_values.values():
            n = norm(v)
            if n:
                values.add(n)
            t = template_regex(v)
            if t:
                templates.append(t)
    results = {}
    for cid, info in (trace.get("capabilities") or {}).items():
        if only and cid not in only:
            continue
        if not os.path.isfile(newapp.notes_path(ws, program, cid)):
            if only:
                results[cid] = {"verdict": "gap", "reason": "no porting notes: the capability is not built yet"}
            continue
        if not info.get("screens"):
            results[cid] = {"verdict": "n/a", "reason": f"no design screen ({info.get('status')})", "screens": []}
            continue
        rows, failing = [], 0
        for sid in info["screens"]:
            s = screens.get(sid) or {}
            texts = [t for t in s.get("texts") or [] if t]
            counted, left_out, matched, unmatched = [], [], [], []
            for t in texts:
                n = norm(t)
                if not n or PLACEHOLDER.match(t) or n in extra_placeholders:
                    left_out.append(t)
                    continue
                counted.append(t)
                if n in values or any(tp.match(n) for tp in templates):
                    matched.append(t)
                else:
                    unmatched.append(t)
            score = (len(matched) / len(counted)) if counted else 1.0
            ok = score >= threshold
            failing += 0 if ok else 1
            rows.append({"screen": sid, "name": s.get("name"), "texts": len(counted), "matched": len(matched),
                         "score": round(score, 3), "pass": ok, "unmatched": unmatched[:50], "leftOut": left_out[:50]})
        results[cid] = {"verdict": "pass" if not failing else "fail",
                        "reason": f"{len(rows) - failing} of {len(rows)} screen(s) at or above {int(threshold * 100)}%",
                        "screens": rows}
    out = {"program": program, "version": 1, "generated": now_iso(), "threshold": threshold,
           "rule": "texts of each linked screen, placeholders left out, found among the new app's catalog values after normalizing case, whitespace and edge punctuation, or fitting a catalog template",
           "capabilities": results}
    path = os.path.join(pdir, "evidence", "design-text.json")
    write_json(path, out)
    counts = {}
    for r in results.values():
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print(f"design text: {', '.join(f'{v} {k}' for k, v in sorted(counts.items())) or 'nothing built yet'} -> {os.path.relpath(path, ws)}")
    return 1 if counts.get("fail") else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("--capability", action="append")
    ap.add_argument("--threshold", type=float, default=0.9)
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    if not 0 < args.threshold <= 1:
        die("--threshold must be between 0 and 1")
    sys.exit(run(ws, args.program, set(args.capability or []), args.threshold))


if __name__ == "__main__":
    main()
