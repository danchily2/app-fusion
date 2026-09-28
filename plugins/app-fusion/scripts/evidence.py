#!/usr/bin/env python3
"""Record test evidence in analysis/<program>/evidence/test-runs.json: files and their hashes, never counts.

    python3 evidence.py dir <program> suite|journey <CAP-NNN|all|JRN-NNN> [--platform ios|android]
                                                       print (and create) a fresh folder for one run's results
    python3 evidence.py suite <program> --capability CAP-NNN|all --name NAME --command "CMD" --junit PATH [--junit ...]
                              [--log PATH] [--note N]
    python3 evidence.py journey <program> --journey JRN-NNN --platform ios|android --flow PATH --junit PATH [--device D] [--note N]
    python3 evidence.py shot <program> --screen <fileKey>:<nodeId> --capability CAP-NNN --app PATH
    python3 evidence.py show <program>

Canaries are recorded by scripts/canary.py, which also restores the code they break.

A --junit folder is expanded into the XML files it holds when the run is recorded, so files a later run leaves in
the same folder never count for this one. Each entry keeps the SHA-256 of every result file and, for every built
capability, the hash of the files its porting notes name. The proof accepts a result only while both still match: an
edited result file is rejected, and a result is stale for a capability whose code changed since the run. Each command
replaces the earlier entry for the same capability and name (or journey and platform, or screen). Standard library only.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import proofkit  # noqa: E402
from fusionlib.common import check_name, die, load_json, now_iso, program_dir, today, workspace, write_json  # noqa: E402

VERSION = 2


def path_of(ws, program):
    return os.path.join(program_dir(ws, program), "evidence", "test-runs.json")


def load(ws, program):
    data = load_json(path_of(ws, program)) or {}
    for key in ("suites", "journeys", "canaries", "screenshots"):
        data.setdefault(key, [])
    data.setdefault("date", today())
    return data


def save(ws, program, data):
    data["version"] = VERSION
    data["date"] = today()
    write_json(path_of(ws, program), data)


def rel_inside(ws, p, must_exist=True):
    if not p:
        return None
    full = os.path.abspath(os.path.join(ws, p) if not os.path.isabs(p) else p)
    if must_exist and not os.path.exists(full):
        die(f"{p} does not exist: run the tests first, then record where their result went")
    real_ws = os.path.realpath(ws)
    real = os.path.realpath(full)
    if not (real == real_ws or real.startswith(real_ws + os.sep)):
        die(f"{p} is outside the workspace")
    return os.path.relpath(real, real_ws)


def result_files(ws, paths):
    """Expand --junit files and folders into XML files that parse, with their hashes. Dies on a file that is not
    JUnit XML: a result nobody can read is not evidence."""
    rels = proofkit.xml_files([rel_inside(ws, p) for p in paths], ws)
    if not rels:
        die(f"no XML result file in {', '.join(paths)}: point --junit at the JUnit output of the run")
    _, bad = proofkit.junit_cases(rels, ws)
    if bad:
        die(f"not JUnit XML: {', '.join(bad)}")
    return rels, {r: proofkit.sha256_file(os.path.join(ws, r)) for r in rels}


def new_run_dir(ws, program, kind, ident, platform=None):
    base = os.path.join(program_dir(ws, program), "evidence", {"suite": "junit", "journey": "maestro"}[kind], ident)
    if platform:
        base = os.path.join(base, platform)
    os.makedirs(base, exist_ok=True)
    nums = [int(m.group(1)) for n in os.listdir(base) for m in [re.match(r"^run-(\d+)$", n)] if m]
    run = os.path.join(base, f"run-{(max(nums) + 1) if nums else 1}")
    os.makedirs(run)
    return os.path.relpath(run, ws)


def platforms_of(ws, program):
    prog = load_json(os.path.join(program_dir(ws, program), "program.json")) or {}
    return list((prog.get("target") or {}).get("platforms") or [])


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("dir")
    p.add_argument("program")
    p.add_argument("kind", choices=["suite", "journey"])
    p.add_argument("ident")
    p.add_argument("--platform", choices=["ios", "android"])
    p.add_argument("--workspace")
    for name in ("suite", "journey", "shot", "show"):
        p = sub.add_parser(name)
        p.add_argument("program")
        p.add_argument("--workspace")
        if name in ("suite", "shot"):
            p.add_argument("--capability", required=True)
        if name in ("suite", "journey"):
            p.add_argument("--junit", action="append", required=True)
            p.add_argument("--log", action="append", default=[])
            p.add_argument("--note", default="")
        if name == "suite":
            p.add_argument("--name", required=True)
            p.add_argument("--command", required=True)
        if name == "journey":
            p.add_argument("--journey", required=True)
            p.add_argument("--platform", choices=["ios", "android"])
            p.add_argument("--flow", required=True)
            p.add_argument("--device", default="")
        if name == "shot":
            p.add_argument("--screen", required=True)
            p.add_argument("--app", required=True)
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    if args.cmd == "dir":
        if not re.match(r"^(CAP-\d+|JRN-\d+|all|scaffold|verify)$", args.ident):
            die(f"{args.ident!r} is not CAP-NNN, JRN-NNN, all, scaffold or verify")
        print(new_run_dir(ws, args.program, args.kind, args.ident, args.platform))
        return
    data = load(ws, args.program)
    if args.cmd == "show":
        print(json.dumps(data, indent=2))
        return
    cap = getattr(args, "capability", None)
    if cap and cap != "all" and not re.match(r"^CAP-\d+$", cap):
        die(f"{cap!r} is not a capability id (CAP-NNN) or 'all'")
    if args.cmd == "suite":
        files, hashes = result_files(ws, args.junit)
        entry = {"capability": cap, "name": args.name[:60], "command": args.command[:400], "junit": files, "hashes": hashes,
                 "codeHashes": proofkit.code_hashes(ws, args.program), "log": [rel_inside(ws, l) for l in args.log],
                 "note": args.note[:250], "recordedAt": now_iso()}
        data["suites"] = [s for s in data["suites"] if not (s.get("capability") == cap and s.get("name") == entry["name"])] + [entry]
        cases, _ = proofkit.junit_cases(files, ws)
        summary = f"{len(cases)} test case(s) in {len(files)} file(s), {sum(1 for c in cases if c['status'] == 'failed')} failed"
    elif args.cmd == "journey":
        if not re.match(r"^JRN-\d+$", args.journey):
            die(f"{args.journey!r} is not a journey id (JRN-NNN)")
        wanted = platforms_of(ws, args.program)
        platform = args.platform or (wanted[0] if len(wanted) == 1 else None)
        if not platform:
            die("--platform is required: the new app targets " + (", ".join(wanted) or "no platform yet"))
        files, hashes = result_files(ws, args.junit)
        flow = rel_inside(ws, args.flow)
        entry = {"journey": args.journey, "platform": platform, "flow": flow,
                 "flowHash": proofkit.sha256_file(os.path.join(ws, flow)), "junit": files, "hashes": hashes,
                 "codeHashes": proofkit.code_hashes(ws, args.program), "device": args.device[:120],
                 "log": [rel_inside(ws, l) for l in args.log], "note": args.note[:250], "recordedAt": now_iso()}
        data["journeys"] = [j for j in data["journeys"]
                            if not (j.get("journey") == args.journey and j.get("platform", platform) == platform)] + [entry]
        cases, _ = proofkit.junit_cases(files, ws)
        summary = f"{args.journey} on {platform}: {len(cases)} case(s), {sum(1 for c in cases if c['status'] == 'failed')} failed"
    else:
        shot = rel_inside(ws, args.app)
        entry = {"screen": args.screen, "capability": cap, "app": shot, "hash": proofkit.sha256_file(os.path.join(ws, shot)),
                 "recordedAt": now_iso()}
        data["screenshots"] = [s for s in data["screenshots"] if s.get("screen") != args.screen] + [entry]
        summary = f"screen {args.screen}"
    save(ws, args.program, data)
    print(f"recorded {args.cmd} ({summary}) in analysis/{args.program}/evidence/test-runs.json")


if __name__ == "__main__":
    main()
