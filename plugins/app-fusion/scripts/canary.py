#!/usr/bin/env python3
"""The canary: break one line of a capability's code on purpose, prove its tests catch it, and put the code back
exactly as it was.

    python3 canary.py start <program> <CAP-NNN> --file <path in the new app> --change "what you will break"
    python3 canary.py finish <program> <CAP-NNN>
    python3 canary.py abort <program> <CAP-NNN>
    python3 canary.py status <program>

`start` checks that no other canary is in place (one break at a time, whatever the capability), that the file is
the capability's own production code (its notes' `## Files`, never a test), copies its bytes to
analysis/<program>/evidence/canary/<CAP>/run-N/, and prints that folder. Then make the break (one small change that
matters: a threshold by one, a rounding mode, a flipped condition) and run the covering tests with their JUnit output
into the run folder with `canary.py run` (it executes the test command itself, so the proof knows the tests ran).
`finish` checks the saved copy's hash first, then restores the saved bytes and checks the file's hash; a damaged
saved copy leaves the file exactly as it is and says so. It records the canary only when the break changed at most six
lines, and more than whitespace, and it reads results only from the run folder, so a result from another run can never
be credited. `abort` restores without recording.
The restore never uses git, so uncommitted work in the new app is never lost, and nothing is left broken: a pending
canary shows in fuse-status until it is finished or aborted.

The proof accepts a canary only when a test that names the capability or one of its rules failed under the break
and passed in a fresh recorded suite, and when the capability's code still hashes to the value recorded here.
Standard library only.
"""

import argparse
import difflib
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import evidence as ev  # noqa: E402
from fusionlib import proofkit  # noqa: E402
from fusionlib.common import check_name, die, is_test_path, load_json, now_iso, program_dir, workspace, write_json  # noqa: E402


def cap_dir(ws, program, cap):
    return os.path.join(program_dir(ws, program), "evidence", "canary", cap)


def pending_path(ws, program, cap):
    return os.path.join(cap_dir(ws, program, cap), "pending.json")


def pending_all(ws, program):
    root = os.path.join(program_dir(ws, program), "evidence", "canary")
    out = {}
    if os.path.isdir(root):
        for cap in sorted(os.listdir(root)):
            p = load_json(os.path.join(root, cap, "pending.json"))
            if p:
                out[cap] = p
    return out


def rule_ids(ws, program, cap):
    rules = (load_json(os.path.join(program_dir(ws, program), "rules.json")) or {}).get("rules") or []
    return {r["id"] for r in rules if r.get("capability") == cap}


MAX_LINES = 6


def start(ws, program, cap, file, change):
    busy = pending_all(ws, program)
    if busy:
        other = next(iter(busy))
        die(f"a canary is already in place for {other} ({busy[other].get('file')}): finish or abort it first, "
            "one break at a time")
    info = proofkit.notes(ws, program, cap)
    if not info["exists"]:
        die(f"{cap} has no porting notes: build it before its canary")
    base = proofkit.target_root(ws, program)
    rel = proofkit.target_rel(ws, program, file)
    if not rel:
        die(f"{file} is not a file inside the new app ({os.path.relpath(base, ws)})")
    if rel in info["tests"] or is_test_path(rel):
        die(f"{rel} is a test: the canary breaks the capability's production code, never its tests")
    if rel not in info["files"]:
        die(f"{rel} is not in the ## Files section of {cap}'s porting notes: break the capability's own code")
    full = os.path.join(base, rel)
    folder = cap_dir(ws, program, cap)
    os.makedirs(folder, exist_ok=True)
    nums = [int(m.group(1)) for n in os.listdir(folder) for m in [re.match(r"^run-(\d+)$", n)] if m]
    run = os.path.join(folder, f"run-{(max(nums) + 1) if nums else 1}")
    os.makedirs(run)
    saved = os.path.join(run, "original.bin")
    shutil.copy2(full, saved)
    digest = proofkit.sha256_file(full)
    if proofkit.sha256_file(saved) != digest:
        os.remove(saved)
        die(f"could not save an exact copy of {rel}: nothing was changed, try again")
    os.chmod(saved, 0o444)  # the restore reads it; nothing should write it
    write_json(pending_path(ws, program, cap), {
        "capability": cap, "file": rel, "sha256": digest, "mode": os.stat(full).st_mode & 0o7777,
        "codeHash": proofkit.code_hash(ws, program, cap, info), "change": change[:200],
        "run": os.path.relpath(run, ws), "startedAt": now_iso()})
    print(f"saved {rel}. Now make the one break in it, run the tests that cover {cap} with JUnit output into "
          f"{os.path.relpath(run, ws)}/, then run: canary.py finish {program} {cap}")


def _restore(ws, program, cap, p):
    base = proofkit.target_root(ws, program)
    full = os.path.join(base, p["file"])
    saved = os.path.join(ws, p["run"], "original.bin")
    pending = os.path.relpath(pending_path(ws, program, cap), ws)
    if not os.path.isfile(saved):
        die(f"the saved copy {os.path.relpath(saved, ws)} is gone: {p['file']} was left as it is. Restore it by hand "
            f"(git, or your editor's history), then delete {pending}")
    have = proofkit.sha256_file(saved)
    if have != p["sha256"]:
        # never copy a damaged backup over the code: the file keeps the break until a person restores it
        die(f"the saved copy {os.path.relpath(saved, ws)} no longer holds the original bytes ({have[:12]} is not "
            f"{p['sha256'][:12]}): {p['file']} was left as it is. Restore it by hand, then delete {pending}")
    shutil.copyfile(saved, full)
    os.chmod(full, p.get("mode") or 0o644)
    now = proofkit.sha256_file(full)
    if now != p["sha256"]:
        die(f"restoring {p['file']} did not give back the original bytes ({now[:12]} is not {p['sha256'][:12]}): "
            "stop and compare it with the saved copy by hand")
    return full


def _lines(path):
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read().splitlines()


def finish(ws, program, cap):
    p = load_json(pending_path(ws, program, cap))
    if not p:
        die(f"no canary in place for {cap}: start one with `canary.py start`")
    base = proofkit.target_root(ws, program)
    full = os.path.join(base, p["file"])
    broken = _lines(full)
    original = _lines(os.path.join(ws, p["run"], "original.bin")) or []
    if broken is not None and proofkit.sha256_file(full) == p["sha256"]:
        die(f"{p['file']} is unchanged: make the break first, run the tests, then finish (or abort)")
    diff = [l for l in difflib.unified_diff(original, broken or [], "before", "canary", n=0, lineterm="")][2:]
    changed = sum(1 for l in diff if l[:1] in "+-")
    only_space = [re.sub(r"\s+", "", l[1:]) for l in diff if l[:1] == "-"] == [re.sub(r"\s+", "", l[1:]) for l in diff if l[:1] == "+"]
    _restore(ws, program, cap, p)
    refusal = ("the break deleted the file" if broken is None else
               "the break changed only whitespace" if only_space else
               f"the break changed {changed} lines (at most {MAX_LINES}: one small change that matters)" if changed > MAX_LINES else None)
    if refusal:
        os.remove(pending_path(ws, program, cap))
        die(f"restored {p['file']} (hash checked), but recorded nothing: {refusal}. Start a new canary.")
    rels = proofkit.xml_files([p["run"]], ws)
    cases, bad = proofkit.junit_cases(rels, ws)
    mine = {cap} | rule_ids(ws, program, cap)
    failed_mine = sorted({tc["key"] for tc in cases if tc["status"] == "failed" and proofkit.case_ids(tc) & mine})
    failed_other = sum(1 for tc in cases if tc["status"] == "failed" and not proofkit.case_ids(tc) & mine)
    data = ev.load(ws, program)
    entry = {"capability": cap, "change": p["change"], "file": p["file"], "linesChanged": changed,
             "diff": "\n".join(diff)[:2000], "junit": rels,
             "hashes": {r: proofkit.sha256_file(os.path.join(ws, r)) for r in rels}, "unreadable": bad,
             "cases": len(cases), "failedCases": failed_mine, "failedOther": failed_other,
             "codeHash": proofkit.code_hash(ws, program, cap), "codeChangedDuringCanary":
                 proofkit.code_hash(ws, program, cap) != p.get("codeHash"),
             "run": p["run"], "startedAt": p.get("startedAt"), "recordedAt": now_iso()}
    data["canaries"] = [c for c in data["canaries"] if c.get("capability") != cap] + [entry]
    ev.save(ws, program, data)
    os.remove(pending_path(ws, program, cap))
    print(f"restored {p['file']} (hash checked). {len(cases)} test case(s) ran under the break ({changed} line(s) changed).")
    if not rels:
        print(f"  no JUnit result in {p['run']}: the canary proves nothing until its tests write results there")
    elif failed_mine:
        print(f"  {len(failed_mine)} test(s) naming {cap} or its rules failed: the tests catch this break")
    else:
        print(f"  no test naming {cap} or its rules failed ({failed_other} other failure(s)): strengthen the tests")
    if entry["codeChangedDuringCanary"]:
        print(f"  note: other files of {cap} changed while the canary was in place; run the suite again")
    print(f"recorded the canary in analysis/{program}/evidence/test-runs.json")


def abort(ws, program, cap):
    p = load_json(pending_path(ws, program, cap))
    if not p:
        die(f"no canary in place for {cap}")
    _restore(ws, program, cap, p)
    os.remove(pending_path(ws, program, cap))
    print(f"restored {p['file']} (hash checked); nothing recorded")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("start", "finish", "abort", "status"):
        p = sub.add_parser(name)
        p.add_argument("program")
        if name != "status":
            p.add_argument("capability")
        if name == "start":
            p.add_argument("--file", required=True)
            p.add_argument("--change", required=True)
        p.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    cap = getattr(args, "capability", None)
    if cap and not re.match(r"^CAP-\d+$", cap):
        die(f"{cap!r} is not a capability id (CAP-NNN)")
    if args.cmd == "start":
        start(ws, args.program, cap, args.file, args.change)
    elif args.cmd == "finish":
        finish(ws, args.program, cap)
    elif args.cmd == "abort":
        abort(ws, args.program, cap)
    else:
        pend = pending_all(ws, args.program)
        print(json.dumps(pend, indent=2) if pend else "no canary in place")


if __name__ == "__main__":
    main()
