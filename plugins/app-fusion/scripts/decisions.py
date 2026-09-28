#!/usr/bin/env python3
"""Record a person's decisions, and list the questions still open.

    python3 decisions.py open <program> [--json]                          what a person still has to decide
    python3 decisions.py add <program> --about X --kind K --choice C [--question Q] [--note N] [--by NAME]
    python3 decisions.py add-json <program> <file.json>                   a list of {about, kind, choice, question?, note?, by?}
    python3 decisions.py render <program>                                 rewrite DECISIONS.md from DECISIONS.json

Only a person decides: this script records answers exactly as given and never infers one. A new answer about the
same thing (same `about` and `kind`) replaces the earlier one and keeps its DEC id. Choices are validated per kind
(see docs/DESIGN.md). Standard library only.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib.common import (check_name, die, load_json, md_table, now_iso, one_line, program_dir, workspace,  # noqa: E402
                              write_json, write_text)

STACKS = {"react-native", "native", "swiftui", "compose", "flutter", "kmp"}
KINDS = {
    "conflict": lambda c, apps: c in {"design", "both-by-role", "new-spec", "defer"} or (c.startswith("take:") and c[5:] in apps),
    "gap": lambda c, apps: c in {"design-it", "carry-as-is", "drop", "defer"},
    "rule": lambda c, apps: c in {"confirmed", "wrong", "discuss"},
    "design": lambda c, apps: c in {"in-scope", "out-of-scope", "new-spec"},
    "platform": lambda c, apps: c in {"keep", "drop", "decide-later"},
    "scope": lambda c, apps: c in {"in", "out"},
    "stack": lambda c, apps: c in STACKS,
    "continuity": lambda c, apps: bool(c.strip()),
    "api": lambda c, apps: c in {"replaced", "dropped", "accepted"},
}
CHOICES_HELP = {
    "conflict": "take:<app>, design, both-by-role, new-spec, defer", "gap": "design-it, carry-as-is, drop, defer",
    "rule": "confirmed, wrong, discuss", "design": "in-scope, out-of-scope, new-spec", "platform": "keep, drop, decide-later",
    "scope": "in, out", "stack": ", ".join(sorted(STACKS)), "continuity": "free text, verbatim",
    "api": "replaced, dropped, accepted (about is 'CAP-NNN:<METHOD> <path>')",
}


def _path(ws, program):
    return os.path.join(program_dir(ws, program), "DECISIONS.json")


def load(ws, program):
    return load_json(_path(ws, program)) or {"program": program, "version": 1, "decisions": {}}


def _apps(ws, program):
    prog = load_json(os.path.join(program_dir(ws, program), "program.json")) or {}
    return {a["name"] for a in prog.get("apps", [])}


def add(ws, program, items):
    data = load(ws, program)
    apps = _apps(ws, program)
    decisions = data["decisions"]
    changed = []
    for item in items:
        kind = item.get("kind")
        choice = str(item.get("choice") or "").strip()
        about = str(item.get("about") or "").strip()
        if kind not in KINDS:
            die(f"kind {kind!r} is not one of {', '.join(sorted(KINDS))}")
        if not about:
            die("every decision needs `about`: a CAP-, RULE-, PLT- id, a Figma screen id, 'scope', 'stack' or 'continuity:<topic>'")
        if not KINDS[kind](choice, apps):
            die(f"choice {choice!r} is not valid for kind {kind!r} (valid: {CHOICES_HELP[kind]})")
        existing = next((k for k, d in decisions.items() if d.get("about") == about and d.get("kind") == kind), None)
        did = existing or _next_id(decisions)
        decisions[did] = {"about": about, "kind": kind, "question": one_line(item.get("question"), 400), "choice": choice,
                          "note": str(item.get("note") or "").strip()[:2000], "by": one_line(item.get("by"), 80),
                          "at": item.get("at") or now_iso(), "replaces": decisions.get(did, {}).get("choice") if existing else None}
        changed.append(did)
    data["decisions"] = dict(sorted(decisions.items(), key=lambda kv: int(kv[0].split("-")[1])))
    write_json(_path(ws, program), data)
    render(ws, program, data)
    return changed


def _next_id(decisions):
    nums = [int(k.split("-")[1]) for k in decisions if re.match(r"^DEC-\d+$", k)]
    return f"DEC-{(max(nums) + 1) if nums else 1:03d}"


def render(ws, program, data=None):
    data = data or load(ws, program)
    rows = [[k, d["kind"], d["about"], d["choice"], d.get("note") or "", d.get("by") or "-", d.get("at", "")[:10]]
            for k, d in data["decisions"].items()]
    lines = [f"# Decisions: {program}", "",
             "What a person decided, in their words. The plan (`fuse-brief`) and the build (`fuse-build`) read these, and "
             "only a person changes them. Run `/app-fusion:fuse-review` to answer open questions or change an answer.", "",
             md_table(["Id", "Kind", "About", "Choice", "Note", "By", "When"], rows) if rows else "_No decisions yet._", ""]
    write_text(os.path.join(program_dir(ws, program), "DECISIONS.md"), "\n".join(lines))


def open_questions(ws, program):
    pdir = program_dir(ws, program)
    data = load(ws, program)
    decided = {(d["about"], d["kind"]) for d in data["decisions"].values()}
    caps = load_json(os.path.join(pdir, "capabilities.json")) or {}
    trace = load_json(os.path.join(pdir, "traceability.json")) or {}
    rules = load_json(os.path.join(pdir, "rules.json")) or {}
    platform = load_json(os.path.join(pdir, "platform.json")) or {}
    prog = load_json(os.path.join(pdir, "program.json")) or {}
    out = []
    for c in caps.get("capabilities", []):
        if c["fusion"] == "shared-diverged" and (c["id"], "conflict") not in decided:
            out.append({"about": c["id"], "kind": "conflict", "priority": 1,
                        "question": f"{c['id']} {c['name']}: the apps do this differently. Which behavior does the new app keep?",
                        "detail": c.get("divergence") or [], "options": [f"take:{a}" for a in c.get("implementations", {})] + ["design", "both-by-role"]})
    for cid, t in (trace.get("capabilities") or {}).items():
        if t.get("status") == "no-design" and (cid, "gap") not in decided:
            name = next((c["name"] for c in caps.get("capabilities", []) if c["id"] == cid), cid)
            out.append({"about": cid, "kind": "gap", "priority": 2,
                        "question": f"{cid} {name} has no screen in the new design. What happens to it?",
                        "options": ["design-it", "carry-as-is", "drop", "defer"]})
    for sid in (trace.get("gaps") or {}).get("screensWithoutCapability") or []:
        if (sid, "design") not in decided:
            out.append({"about": sid, "kind": "design", "priority": 3,
                        "question": f"Figma frame {sid} matches no legacy capability. Is it a new feature in scope?",
                        "options": ["in-scope", "out-of-scope", "new-spec"]})
    for r in rules.get("rules", []):
        flagged = r["priority"] == "P0" and (r["confidence"] != "High" or r.get("suspectedDefect") or r.get("question"))
        if flagged and (r["id"], "rule") not in decided:
            out.append({"about": r["id"], "kind": "rule", "priority": 1,
                        "question": f"{r['id']} {r['name']} ({r['app']}, {r['source']}): {r.get('question') or r.get('suspectedDefect') or 'confirm the rule'}",
                        "detail": [f"Given {r['given']}", f"When {r['when']}", f"Then {r['then']}"],
                        "options": ["confirmed", "wrong", "discuss"]})
    for conf in rules.get("conflicts", []):
        about = conf.get("capability") or ("+".join(conf.get("rules") or []) or "rules")
        if (about, "conflict") not in decided:
            out.append({"about": about, "kind": "conflict", "priority": 1,
                        "question": f"Rules {', '.join(conf.get('rules') or [])} decide the same thing differently: {conf.get('difference')}",
                        "options": [f"take:{a}" for a in sorted(_apps(ws, program))] + ["design", "new-spec"]})
    for it in platform.get("items", []):
        if it.get("newApp") == "decide" and (it["id"], "platform") not in decided and len(it.get("apps") or {}) >= 1:
            out.append({"about": it["id"], "kind": "platform", "priority": 4,
                        "question": f"{it['id']} {it['name']} ({'; '.join(f'{a}: {v}' for a, v in it['apps'].items())}). Keep it in the new app?",
                        "options": ["keep", "drop", "decide-later"]})
    target = (prog.get("target") or {}).get("stack")
    if target in (None, "", "undecided") and ("stack", "stack") not in decided:
        out.append({"about": "stack", "kind": "stack", "priority": 1, "question": "Which stack does the new app use?",
                    "options": sorted(STACKS)})
    if prog.get("storeIdentity") in (None, "", "undecided") and ("continuity:store-identity", "continuity") not in decided:
        out.append({"about": "continuity:store-identity", "kind": "continuity", "priority": 1,
                    "question": "Which store listing and bundle id does the new app ship under (an existing app's, so its users "
                                "update in place, or a new listing)?", "options": []})
    out.sort(key=lambda q: (q["priority"], q["kind"], q["about"]))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("open")
    p.add_argument("program")
    p.add_argument("--json", action="store_true")
    p.add_argument("--workspace")
    p = sub.add_parser("add")
    p.add_argument("program")
    p.add_argument("--about", required=True)
    p.add_argument("--kind", required=True)
    p.add_argument("--choice", required=True)
    p.add_argument("--question")
    p.add_argument("--note")
    p.add_argument("--by")
    p.add_argument("--workspace")
    p = sub.add_parser("add-json")
    p.add_argument("program")
    p.add_argument("file")
    p.add_argument("--workspace")
    p = sub.add_parser("render")
    p.add_argument("program")
    p.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    if args.cmd == "open":
        qs = open_questions(ws, args.program)
        if args.json:
            print(json.dumps(qs, indent=2, ensure_ascii=False))
        else:
            counts = {}
            for q in qs:
                counts[q["kind"]] = counts.get(q["kind"], 0) + 1
            print(f"{len(qs)} open question(s)" + (": " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())) if qs else ""))
            for q in qs[:60]:
                print(f"  [{q['kind']}] {q['question']}")
    elif args.cmd == "add":
        ids = add(ws, args.program, [{"about": args.about, "kind": args.kind, "choice": args.choice, "question": args.question,
                                      "note": args.note, "by": args.by}])
        print(f"recorded {', '.join(ids)} -> analysis/{args.program}/DECISIONS.json, DECISIONS.md")
    elif args.cmd == "add-json":
        items = load_json(args.file)
        if not isinstance(items, list):
            die(f"{args.file} must hold a JSON list of decisions")
        ids = add(ws, args.program, items)
        print(f"recorded {len(ids)} decision(s): {', '.join(ids)}")
    else:
        render(ws, args.program)
        print(f"wrote analysis/{args.program}/DECISIONS.md")


if __name__ == "__main__":
    main()
