#!/usr/bin/env python3
"""Record test evidence in analysis/<program>/evidence/test-runs.json: paths only, never counts.

    python3 evidence.py suite <program> --capability CAP-NNN|all --name NAME --command "CMD" --junit PATH [--log PATH] [--note N]
    python3 evidence.py journey <program> --journey JRN-NNN --flow PATH --junit PATH [--device D] [--note N]
    python3 evidence.py canary <program> --capability CAP-NNN --change "WHAT WAS BROKEN" --junit PATH [--log PATH]
    python3 evidence.py shot <program> --screen <fileKey>:<nodeId> --capability CAP-NNN --app PATH
    python3 evidence.py show <program>

Each command replaces the earlier entry for the same capability and name (or journey, or screen), so a re-run never
leaves a stale result beside a fresh one. Paths must exist and be inside the workspace; the proof script parses the
files themselves, so a number typed anywhere counts for nothing. Standard library only.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib.common import check_name, die, load_json, program_dir, today, workspace, write_json  # noqa: E402


def _path(ws, program):
    return os.path.join(program_dir(ws, program), "evidence", "test-runs.json")


def _load(ws, program):
    return load_json(_path(ws, program)) or {"date": today(), "suites": [], "journeys": [], "canaries": [], "screenshots": []}


def _rel(ws, p):
    if not p:
        return None
    full = os.path.abspath(os.path.join(ws, p) if not os.path.isabs(p) else p)
    if not os.path.exists(full):
        die(f"{p} does not exist: run the tests first, then record where their result went")
    if not (full == ws or full.startswith(os.path.realpath(ws) + os.sep) or full.startswith(ws + os.sep)):
        die(f"{p} is outside the workspace")
    return os.path.relpath(full, ws)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("suite", "journey", "canary", "shot", "show"):
        p = sub.add_parser(name)
        p.add_argument("program")
        p.add_argument("--workspace")
        if name in ("suite", "canary", "shot"):
            p.add_argument("--capability", required=True)
        if name in ("suite", "journey", "canary"):
            p.add_argument("--junit", action="append", required=True)
            p.add_argument("--log", action="append", default=[])
            p.add_argument("--note", default="")
        if name == "suite":
            p.add_argument("--name", required=True)
            p.add_argument("--command", required=True)
        if name == "journey":
            p.add_argument("--journey", required=True)
            p.add_argument("--flow", required=True)
            p.add_argument("--device", default="")
        if name == "canary":
            p.add_argument("--change", required=True)
        if name == "shot":
            p.add_argument("--screen", required=True)
            p.add_argument("--app", required=True)
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    data = _load(ws, args.program)
    if args.cmd == "show":
        print(json.dumps(data, indent=2))
        return
    cap = getattr(args, "capability", None)
    if cap and cap != "all" and not re.match(r"^CAP-\d+$", cap):
        die(f"{cap!r} is not a capability id (CAP-NNN) or 'all'")
    if args.cmd == "suite":
        entry = {"capability": cap, "name": args.name, "command": args.command, "junit": [_rel(ws, j) for j in args.junit],
                 "log": [_rel(ws, l) for l in args.log], "note": args.note[:250]}
        data["suites"] = [s for s in data["suites"] if not (s.get("capability") == cap and s.get("name") == args.name)] + [entry]
    elif args.cmd == "journey":
        if not re.match(r"^JRN-\d+$", args.journey):
            die(f"{args.journey!r} is not a journey id (JRN-NNN)")
        entry = {"journey": args.journey, "flow": _rel(ws, args.flow), "junit": [_rel(ws, j) for j in args.junit],
                 "device": args.device, "note": args.note[:250]}
        data["journeys"] = [j for j in data["journeys"] if j.get("journey") != args.journey] + [entry]
    elif args.cmd == "canary":
        entry = {"capability": cap, "change": args.change[:200], "junit": [_rel(ws, j) for j in args.junit],
                 "log": [_rel(ws, l) for l in args.log]}
        data["canaries"] = [c for c in data["canaries"] if c.get("capability") != cap] + [entry]
    else:
        entry = {"screen": args.screen, "capability": cap, "app": _rel(ws, args.app)}
        data["screenshots"] = [s for s in data["screenshots"] if s.get("screen") != args.screen] + [entry]
    data["date"] = today()
    write_json(_path(ws, args.program), data)
    print(f"recorded {args.cmd} in analysis/{args.program}/evidence/test-runs.json")


if __name__ == "__main__":
    main()
