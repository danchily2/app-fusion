#!/usr/bin/env python3
"""Record test evidence in analysis/<program>/evidence/test-runs.json: files and their hashes, never counts.

    python3 evidence.py run <program> --capability CAP-NNN|all --name NAME [--platform ios|android] [--cwd DIR]
                              [--env K=V ...] [--collect GLOB ...] [--timeout SECONDS] [--note N] -- <test command> [args ...]
    python3 evidence.py run <program> --journey JRN-NNN --platform ios|android --flow PATH [--device D]
                              [--cwd DIR] [--env K=V ...] [--collect GLOB ...] [--timeout SECONDS] [--note N] -- maestro test ...
    python3 evidence.py dir <program> suite|journey <CAP-NNN|all|JRN-NNN> [--platform ios|android]
                                                       print (and create) a fresh folder for one run's results
    python3 evidence.py suite <program> --capability CAP-NNN|all --name NAME --command "CMD" --junit PATH [--junit ...]
                              [--platform ios|android] [--log PATH] [--note N]      (recorded by hand: a gap in the proof)
    python3 evidence.py journey <program> --journey JRN-NNN --platform ios|android --flow PATH --junit PATH [--device D] [--note N]
    python3 evidence.py shot <program> --screen <fileKey>:<nodeId> --capability CAP-NNN --app PATH
    python3 evidence.py show <program>

`run` is how a result becomes evidence: this script makes a fresh run folder, runs the test command itself (no shell;
the runner and its arguments only), with `{run}` in any argument or --env value replaced by that folder and
FUSION_RUN_DIR set to it, keeps the command's exit code, stdout and stderr, and records the JUnit XML the command left
in the folder. Runners that write elsewhere (Gradle, Xcode) are covered by --collect: files matching the glob (relative
to --cwd, the new app by default) and written during the run are copied into the folder, an .xcresult bundle converted
with scripts/xcresult_junit.py. The proof counts only suites, journeys and canaries recorded this way: a result file
typed by hand and recorded with `suite` or `journey` is kept, but listed as a gap. Canaries are recorded by
scripts/canary.py, which runs the tests the same way and restores the code they break.

Each entry keeps the SHA-256 of every result file and, for every built capability, the hash of the files its porting
notes name. The proof accepts a result only while both still match: an edited or removed result file is rejected (each
entry also keeps the ids its tests named), and a result is stale for a capability whose code changed since the run.
For a native pair (ios/ and android/ in the new app), each half's suite is recorded with --platform, and the proof
checks each half on its own results. Each command replaces the earlier entry for the same capability, name and
platform (or journey and platform, or screen). Standard library only.
"""

import argparse
import glob
import json
import os
import re
import shlex
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import proofkit  # noqa: E402
from fusionlib.common import check_name, die, load_json, now_iso, program_dir, today, workspace, write_json  # noqa: E402

VERSION = 2
OUTPUT_LIMIT = 2_000_000
DEFAULT_TIMEOUT = 3600

# what a test command is not: a shell, a file writer or a wrapper that hides the real command
NOT_RUNNERS = {"sh", "bash", "zsh", "dash", "ksh", "fish", "csh", "tcsh", "cat", "echo", "printf", "tee", "cp", "mv", "dd", "touch",
               "ln", "eval", "exec", "xargs", "find", "sed", "awk", "tar", "curl", "wget", "install", "rsync", "env", "sudo",
               "nohup", "time", "nice", "script", "expect", "true", "false"}
# interpreters that are test runners only when they run a script or a module, never inline code or stdin
INTERPRETERS = {"python", "python2", "python3", "node", "nodejs", "perl", "ruby", "osascript", "deno", "bun"}
INLINE_FLAGS = {"-c", "-e", "-E", "--eval", "-p", "--print", "-"}
SHELL_SYNTAX = re.compile(r"[<>|;&`]|\$\(|\$\{")


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


# ---------------------------------------------------------------- running a test command

def legacy_roots(ws, program):
    prog = load_json(os.path.join(program_dir(ws, program), "program.json")) or {}
    roots = []
    for a in prog.get("apps") or []:
        if not isinstance(a, dict):
            continue
        link = os.path.join(ws, a.get("path") or f"legacy/{a.get('name')}")
        roots.append(os.path.realpath(link))
        if a.get("snapshotOf"):
            roots.append(os.path.realpath(a["snapshotOf"]))
    legacy = os.path.join(ws, "legacy")
    if os.path.isdir(legacy):
        roots += [os.path.realpath(os.path.join(legacy, n)) for n in os.listdir(legacy)]
    return roots


def check_runner(argv):
    """Refuse what is not a test runner: a shell, a file writer, inline code, or arguments that only a shell reads."""
    if not argv:
        die("give the test command after `--`, for example: -- npx jest --ci")
    verb = os.path.basename(argv[0])
    if verb in NOT_RUNNERS:
        die(f"`{verb}` is not a test runner. evidence.py run executes the runner itself, without a shell: give the runner "
            "and its arguments after `--`, put environment in --env K=V, and let the runner write into {run} or FUSION_RUN_DIR "
            "(or name where it writes with --collect)")
    if verb in INTERPRETERS or re.match(r"^python\d(\.\d+)?$", verb):
        if any(a in INLINE_FLAGS for a in argv[1:4]):
            die(f"inline code is not a test runner (`{verb} {argv[1]}`): call the runner directly, or run a script the "
                "new app keeps in its repository")
    for a in argv:
        if SHELL_SYNTAX.search(a):
            die(f"{a!r} holds shell syntax. The command runs without a shell, so a redirect, pipe or substitution would "
                "reach the runner as text; give the runner and its arguments only, and let it write into {run}")


def execute(ws, program, run_rel, argv, cwd, env_pairs, collect, timeout):
    """Run `argv` (no shell) with cwd inside the workspace and outside every legacy app, `{run}` replaced by the run
    folder and FUSION_RUN_DIR set to it; keep exit code, timing, stdout and stderr; copy collected results in.

    Returns {"command", "argv", "cwd", "exitCode", "timedOut", "startedAt", "durationMs", "output", "outputHashes",
             "collected", "leftOut", "unreadable", "junit"}."""
    check_runner(argv)
    run_abs = os.path.join(ws, run_rel)
    cwd_abs = os.path.realpath(os.path.join(ws, cwd) if not os.path.isabs(cwd) else cwd)
    if not os.path.isdir(cwd_abs):
        die(f"--cwd {cwd} is not a directory")
    real_ws = os.path.realpath(ws)
    if not (cwd_abs == real_ws or cwd_abs.startswith(real_ws + os.sep)):
        die(f"--cwd {cwd} is outside the workspace")
    for root in legacy_roots(ws, program):
        if cwd_abs == root or cwd_abs.startswith(root + os.sep):
            die(f"--cwd {cwd} is inside a legacy app: tests run in the new app, never in the legacy code")
    subst = lambda s: s.replace("{run}", run_abs)
    command = [subst(a) for a in argv]
    env = dict(os.environ)
    for kv in env_pairs or []:
        key, sep, value = kv.partition("=")
        if not sep or not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", key):
            die(f"--env expects NAME=value, got {kv!r}")
        env[key] = subst(value)
    env["FUSION_RUN_DIR"] = run_abs
    out_path, err_path = os.path.join(run_abs, "stdout.txt"), os.path.join(run_abs, "stderr.txt")
    started = time.time()
    t0 = time.monotonic()
    timed_out = False
    try:
        with open(out_path, "wb") as out, open(err_path, "wb") as err:
            try:
                code = subprocess.run(command, cwd=cwd_abs, env=env, stdout=out, stderr=err, timeout=timeout).returncode
            except subprocess.TimeoutExpired:
                code, timed_out = None, True
    except FileNotFoundError:
        die(f"{command[0]} was not found: install the runner, or give its full path")
    except PermissionError:
        die(f"{command[0]} is not executable")
    duration = int((time.monotonic() - t0) * 1000)
    for path in (out_path, err_path):
        if os.path.getsize(path) > OUTPUT_LIMIT:
            with open(path, "rb+") as fh:
                head = fh.read(OUTPUT_LIMIT)
                fh.seek(0)
                fh.truncate()
                fh.write(head + b"\n[cut here by evidence.py: the runner wrote more]\n")
    collected, left_out = collect_results(ws, cwd_abs, collect or [], run_abs, started)
    junit = proofkit.xml_files([run_rel], ws)
    _, bad = proofkit.junit_cases(junit, ws)
    junit = [r for r in junit if r not in bad]
    output = [os.path.relpath(out_path, real_ws), os.path.relpath(err_path, real_ws)]
    return {"command": shlex.join(command), "argv": argv, "cwd": os.path.relpath(cwd_abs, real_ws), "exitCode": code,
            "timedOut": timed_out, "startedAt": datetime.fromtimestamp(started, timezone.utc).replace(microsecond=0).isoformat(),
            "durationMs": duration, "output": output, "outputHashes": {o: proofkit.sha256_file(os.path.join(ws, o)) for o in output},
            "collected": collected, "leftOut": left_out, "unreadable": bad, "junit": junit}


def collect_results(ws, cwd_abs, patterns, run_abs, started):
    """Copy result files the runner wrote elsewhere into the run folder: only files matching a --collect glob (relative
    to cwd, inside it) whose modification time is not before the run started. Older matches are reported, never
    copied. An .xcresult bundle is converted to JUnit XML."""
    collected, left_out = [], []
    dest_dir = os.path.join(run_abs, "collected")
    real_run = os.path.realpath(run_abs)
    for pattern in patterns:
        if os.path.isabs(pattern) or re.search(r"(^|/)\.\.(/|$)", pattern):
            die(f"--collect {pattern!r} must be a relative glob without '..'")
        for match in sorted(glob.glob(os.path.join(cwd_abs, pattern), recursive=True)):
            real = os.path.realpath(match)
            if not real.startswith(cwd_abs + os.sep) or real.startswith(real_run + os.sep):
                continue
            rel = os.path.relpath(real, cwd_abs)
            if os.path.getmtime(real) < started - 2:
                left_out.append(rel)
                continue
            os.makedirs(dest_dir, exist_ok=True)
            flat = rel.replace(os.sep, "__")
            if real.endswith(".xcresult") and os.path.isdir(real):
                import xcresult_junit  # the converter script, next to this one
                root, total = xcresult_junit.convert(xcresult_junit.load(real))
                dest = os.path.join(dest_dir, flat + ".xml")
                ET.ElementTree(root).write(dest, encoding="utf-8", xml_declaration=True)
                collected.append({"from": rel, "to": os.path.relpath(dest, ws), "converted": True, "cases": total})
            elif os.path.isfile(real):
                dest = os.path.join(dest_dir, flat)
                with open(real, "rb") as src, open(dest, "wb") as out:
                    out.write(src.read())
                collected.append({"from": rel, "to": os.path.relpath(dest, ws), "converted": False})
    return collected, left_out


def parse_with_command(parser, raw):
    """Parse the options before `--`; what follows `--` is the test command, kept exactly as given (argparse would
    otherwise read the runner's own options as ours, or swallow ours into the command)."""
    command = None
    if "--" in raw:
        at = raw.index("--")
        raw, command = raw[:at], raw[at + 1:]
    return parser.parse_args(raw), command


def summarize(cases):
    return f"{len(cases)} test case(s), {sum(1 for c in cases if c['status'] == 'failed')} failed, " \
           f"{sum(1 for c in cases if c['status'] == 'skipped')} skipped"


def named_in(cases):
    return sorted(set().union(*[proofkit.case_ids(c) for c in cases]) if cases else [])


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("dir")
    p.add_argument("program")
    p.add_argument("kind", choices=["suite", "journey"])
    p.add_argument("ident")
    p.add_argument("--platform", choices=["ios", "android"])
    p.add_argument("--workspace")
    p = sub.add_parser("run", description="run the test command and record what it produced")
    p.add_argument("program")
    p.add_argument("--capability")
    p.add_argument("--name")
    p.add_argument("--journey")
    p.add_argument("--flow")
    p.add_argument("--device", default="")
    p.add_argument("--platform", choices=["ios", "android"])
    p.add_argument("--cwd", help="where the command runs: the new app by default")
    p.add_argument("--env", action="append", default=[], metavar="K=V")
    p.add_argument("--collect", action="append", default=[], metavar="GLOB",
                   help="result files the runner writes outside the run folder, relative to --cwd (an .xcresult is converted)")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    p.add_argument("--note", default="")
    p.add_argument("--workspace")
    p.epilog = "After the options, `--` and then the test runner with its arguments."
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
            p.add_argument("--platform", choices=["ios", "android"])
        if name == "journey":
            p.add_argument("--journey", required=True)
            p.add_argument("--platform", choices=["ios", "android"])
            p.add_argument("--flow", required=True)
            p.add_argument("--device", default="")
        if name == "shot":
            p.add_argument("--screen", required=True)
            p.add_argument("--app", required=True)
    args, command = parse_with_command(ap, sys.argv[1:])
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
    if args.cmd == "run":
        argv = command or []
        check_runner(argv)  # before a run folder is made: a refused command leaves nothing behind
        if args.journey:
            if not re.match(r"^JRN-\d+$", args.journey):
                die(f"{args.journey!r} is not a journey id (JRN-NNN)")
            if not args.flow:
                die("--flow is required with --journey: the Maestro flow the journey runs")
            wanted = platforms_of(ws, args.program)
            platform = args.platform or (wanted[0] if len(wanted) == 1 else None)
            if not platform:
                die("--platform is required: the new app targets " + (", ".join(wanted) or "no platform yet"))
            flow = rel_inside(ws, args.flow)
            run_rel = new_run_dir(ws, args.program, "journey", args.journey, platform)
        else:
            if not cap or not args.name:
                die("--capability CAP-NNN|all and --name are required (or --journey JRN-NNN --platform P --flow PATH)")
            platform = args.platform
            run_rel = new_run_dir(ws, args.program, "suite", cap, platform)
        cwd = args.cwd or os.path.relpath(proofkit.target_root(ws, args.program), ws)
        if not os.path.isdir(os.path.join(ws, cwd) if not os.path.isabs(cwd) else cwd):
            die(f"{cwd} does not exist: the new app is not there yet (or give --cwd)")
        result = execute(ws, args.program, run_rel, argv, cwd, args.env, args.collect, args.timeout)
        cases, _ = proofkit.junit_cases(result["junit"], ws)
        common = {"executed": True, "command": result["command"][:400], "argv": result["argv"], "cwd": result["cwd"],
                  "exitCode": result["exitCode"], "timedOut": result["timedOut"], "runner": os.path.basename(argv[0]),
                  "startedAt": result["startedAt"], "durationMs": result["durationMs"], "run": run_rel,
                  "junit": result["junit"], "hashes": {r: proofkit.sha256_file(os.path.join(ws, r)) for r in result["junit"]},
                  "named": named_in(cases), "codeHashes": proofkit.code_hashes(ws, args.program), "output": result["output"],
                  "outputHashes": result["outputHashes"], "collected": result["collected"], "leftOut": result["leftOut"],
                  "unreadable": result["unreadable"], "note": args.note[:250], "recordedAt": now_iso()}
        if args.journey:
            entry = dict(common, journey=args.journey, platform=platform, flow=flow,
                         flowHash=proofkit.sha256_file(os.path.join(ws, flow)), device=args.device[:120])
            data["journeys"] = [j for j in data["journeys"]
                                if not (j.get("journey") == args.journey and j.get("platform", platform) == platform)] + [entry]
            what = f"journey {args.journey} on {platform}"
        else:
            entry = dict(common, capability=cap, name=args.name[:60], platform=platform)
            data["suites"] = [s for s in data["suites"] if not (s.get("capability") == cap and s.get("name") == entry["name"]
                                                                and s.get("platform") == platform)] + [entry]
            what = f"suite {entry['name']} for {cap}" + (f" ({platform})" if platform else "")
        save(ws, args.program, data)
        exit_word = "timed out" if result["timedOut"] else f"exit {result['exitCode']}"
        print(f"ran: {result['command']}  ({exit_word}, {result['durationMs'] / 1000:.1f} s, in {result['cwd']})")
        print(f"recorded {what}: {summarize(cases)} in {len(result['junit'])} file(s) -> {run_rel}")
        if result["collected"]:
            print(f"  collected {len(result['collected'])} result file(s) into {run_rel}/collected/")
        if result["leftOut"]:
            print(f"  left out {len(result['leftOut'])} older file(s) matching --collect (written before this run): "
                  + ", ".join(result["leftOut"][:5]))
        if result["unreadable"]:
            print(f"  not JUnit XML, ignored: {', '.join(result['unreadable'][:5])}")
        if not result["junit"]:
            print("  WARNING: the command left no JUnit XML in the run folder ({run} / FUSION_RUN_DIR) and --collect found "
                  "nothing written during the run: the proof counts nothing from this run")
        if result["exitCode"] != 0:
            with open(os.path.join(ws, result["output"][1]), encoding="utf-8", errors="replace") as fh:
                tail = fh.read().splitlines()[-15:]
            if tail:
                print("  stderr (tail):\n    " + "\n    ".join(tail))
        sys.exit(0 if result["exitCode"] == 0 and cases and not any(c["status"] == "failed" for c in cases) else 1)
    if args.cmd == "suite":
        files, hashes = result_files(ws, args.junit)
        cases, _ = proofkit.junit_cases(files, ws)
        entry = {"capability": cap, "name": args.name[:60], "platform": args.platform, "command": args.command[:400], "executed": False,
                 "junit": files, "hashes": hashes, "named": named_in(cases),
                 "codeHashes": proofkit.code_hashes(ws, args.program), "log": [rel_inside(ws, l) for l in args.log],
                 "note": args.note[:250], "recordedAt": now_iso()}
        data["suites"] = [s for s in data["suites"] if not (s.get("capability") == cap and s.get("name") == entry["name"]
                                                            and s.get("platform") == args.platform)] + [entry]
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
        named = proofkit.junit_cases(files, ws)[0]
        entry = {"journey": args.journey, "platform": platform, "flow": flow, "executed": False,
                 "flowHash": proofkit.sha256_file(os.path.join(ws, flow)), "junit": files, "hashes": hashes,
                 "named": named_in(named), "codeHashes": proofkit.code_hashes(ws, args.program), "device": args.device[:120],
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
    if args.cmd in ("suite", "journey"):
        print("  NOTE: recorded by hand, so the proof lists it as a gap. Run the tests through evidence.py instead: "
              f"evidence.py run {args.program} " + ("--capability ... --name ..." if args.cmd == "suite" else "--journey ... --platform ... --flow ...")
              + " -- <runner> ...")


if __name__ == "__main__":
    main()
