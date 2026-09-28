#!/usr/bin/env python3
"""Where does the program stand, what is stale, and what is the exact next command?

    python3 status.py <program> [--json] [--workspace DIR]
    python3 status.py --list                      the programs in this workspace

Reads only. Standard library only.
"""

import argparse
import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import decisions as dec  # noqa: E402
import workspace as wsmod  # noqa: E402
from fusionlib import status as st  # noqa: E402
from fusionlib.common import check_name, find_programs, load_json, program_dir, workspace  # noqa: E402


def summary(ws, program):
    stages, prog, target = st.artifacts(ws, program)
    pdir = program_dir(ws, program)
    questions = dec.open_questions(ws, program) if prog else []
    blocking = [q for q in questions if q["priority"] <= 2]
    command, reason = st.next_step(ws, program, open_count=len(blocking))
    caps = load_json(os.path.join(pdir, "capabilities.json")) or {}
    trace = load_json(os.path.join(pdir, "traceability.json")) or {}
    verification = (load_json(os.path.join(pdir, "VERIFICATION.json")) or {}).get("capabilities") or {}
    built = st.built_capabilities(target)
    brief = st.parse_brief(os.path.join(pdir, "FUSION_BRIEF.md"))
    verdicts = {}
    for r in verification.values():
        verdicts[r["verdict"]] = verdicts.get(r["verdict"], 0) + 1
    return {
        "program": program, "stages": stages, "stale": st.stale(ws, program),
        "legacy": wsmod.legacy_state(ws, prog) if prog else [],
        "capabilities": len(caps.get("capabilities", [])), "journeys": len(caps.get("journeys", [])),
        "coverage": trace.get("coverage"), "openQuestions": len(questions), "blockingQuestions": len(blocking),
        "brief": {"exists": brief["exists"], "approved": brief["approved"], "approvedBy": brief["approvedBy"],
                  "phases": len(brief["phases"])},
        "built": sorted(built), "verdicts": verdicts, "next": {"command": command, "reason": reason},
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program", nargs="?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    if args.list or not args.program:
        progs = find_programs(ws)
        print("\n".join(progs) if progs else "no program here yet: start with /app-fusion:fuse <name> --source <app>=<path> ...")
        return
    check_name(args.program, "program")
    s = summary(ws, args.program)
    if args.json:
        print(json.dumps(s, indent=2, default=str))
        return
    print(f"Program {args.program}")
    for stage in s["stages"]:
        when = datetime.fromtimestamp(stage["mtime"]).strftime("%Y-%m-%d %H:%M") if stage["mtime"] else "-"
        mark = "done" if stage["present"] == stage["total"] else ("partial" if stage["present"] else "-")
        print(f"  {stage['stage']:<10} {mark:<8} {stage['present']}/{stage['total']}  {when}")
    for r in s["legacy"]:
        state = "missing" if not r["exists"] else ("clean" if r["clean"] else ("CHANGED" if r["clean"] is False else "not git"))
        print(f"  legacy/{r['app']}: {state}")
    if s["capabilities"]:
        cov = s["coverage"] or {}
        print(f"  {s['capabilities']} capabilities, {s['journeys']} journeys; design coverage {cov.get('percent', '-')}%; "
              f"{len(s['built'])} built; verdicts {s['verdicts'] or '-'}")
    print(f"  open questions: {s['openQuestions']} ({s['blockingQuestions']} blocking)")
    b = s["brief"]
    if b["exists"]:
        print(f"  brief: {b['phases']} phase(s), " + (f"approved by {b['approvedBy']}" if b["approved"] else "NOT approved"))
    for line in s["stale"]:
        print(f"  stale: {line}")
    print(f"Next: {s['next']['command']}")
    print(f"      ({s['next']['reason']})")


if __name__ == "__main__":
    main()
