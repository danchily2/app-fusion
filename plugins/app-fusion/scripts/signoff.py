#!/usr/bin/env python3
"""Record what a named person signed: the brief, the proof of capabilities, their visual conformance.

    python3 signoff.py <program> brief  --by NAME [--covers "Phase 0, Phase 1" | all] [--note N]
    python3 signoff.py <program> proof  --by NAME (--caps CAP-001,CAP-002 | --all-proven) [--accept "WHY"] [--note N]
    python3 signoff.py <program> visual --by NAME --caps CAP-001,... [--note N]
    python3 signoff.py <program> show [--json]

Sign-offs live in analysis/<program>/SIGNOFF.json, never in a file a model rewrites. Each binds to what was signed:
the brief's SHA-256, each capability's verdict and code hash, each screenshot's hash. When the signed thing changes,
the sign-off no longer counts (fuse-status says so) and a person signs again. A proof sign-off takes PROVEN
capabilities; a PARTLY PROVEN one only with --accept and the person's reason; a NOT PROVEN one never. Run this only
with a person's words: the plugin's guard asks the person to confirm every call. Standard library only.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import proofkit  # noqa: E402
from fusionlib.common import check_name, die, load_json, now_iso, one_line, program_dir, workspace, write_json  # noqa: E402
from fusionlib.signatures import brief_approval, brief_hash, load, path_of, signed_state  # noqa: E402,F401

PLACEHOLDER_NAME = re.compile(r"^(?:_+|\.+|-+|<[^>]*>|tbd|todo|n/?a|none|claude|assistant|ai|model|agent)$", re.I)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("kind", choices=["brief", "proof", "visual", "show"])
    ap.add_argument("--by")
    ap.add_argument("--covers")
    ap.add_argument("--caps")
    ap.add_argument("--all-proven", action="store_true")
    ap.add_argument("--accept")
    ap.add_argument("--note", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    pdir = program_dir(ws, args.program)
    data = load(ws, args.program)
    if args.kind == "show":
        if args.json:
            print(json.dumps(data, indent=2, ensure_ascii=False))
            return
        a = brief_approval(ws, args.program)
        print("brief: " + (f"approved by {a['by']} ({a['at'][:10]}), covers {a['covers'] or 'all'}" if a["approved"] else
                           (f"sign-off by {a['by']} is for an earlier version of the brief" if a["stale"] and a["by"] else "not approved")))
        for cap, s in sorted(signed_state(ws, args.program).items()):
            print(f"{cap}: proof {'signed' if s['proof'] else 'not signed'}" +
                  ("" if s["visual"] is None else f", visual {'signed' if s['visual'] else 'not signed'}"))
        return
    who = one_line(args.by, 80)
    if not who or PLACEHOLDER_NAME.match(who):
        die("--by must be the name of the person signing, as they gave it")
    entry = {"by": who, "at": now_iso(), "note": one_line(args.note, 400)}
    if args.kind == "brief":
        h = brief_hash(ws, args.program)
        if not h:
            die(f"analysis/{args.program}/FUSION_BRIEF.md not found: write it with /app-fusion:fuse-brief first")
        entry.update({"hash": h, "covers": one_line(args.covers, 120) or "all"})
        data["brief"].append(entry)
        what = f"the brief (covers {entry['covers']})"
    else:
        verification = (load_json(os.path.join(pdir, "VERIFICATION.json")) or {}).get("capabilities") or {}
        if args.all_proven:
            caps = [c for c, r in verification.items() if r.get("verdict") == "PROVEN"]
        else:
            caps = [c.strip() for c in (args.caps or "").split(",") if c.strip()]
        if not caps:
            die("name the capabilities (--caps CAP-001,CAP-002) or pass --all-proven")
        signed = {}
        runs = load_json(os.path.join(pdir, "evidence", "test-runs.json")) or {}
        for cap in caps:
            if not re.match(r"^CAP-\d+$", cap):
                die(f"{cap!r} is not a capability id")
            r = verification.get(cap)
            if not r:
                die(f"{cap} has no verdict: run /app-fusion:fuse-verify {args.program} {cap} first")
            current = proofkit.code_hash(ws, args.program, cap)
            if r.get("codeHash") != current:
                die(f"{cap}'s verdict is older than its code: verify it again before signing")
            if args.kind == "proof":
                if r["verdict"] == "NOT PROVEN":
                    die(f"{cap} is NOT PROVEN: fix it, or record the difference as a decision; a sign-off cannot cover a failure")
                if r["verdict"] == "PARTLY PROVEN" and not args.accept:
                    die(f"{cap} is PARTLY PROVEN: sign it only with --accept \"<the person's reason for accepting the open checks>\"")
                signed[cap] = {"verdict": r["verdict"], "codeHash": current, "judgedAt": r.get("judgedAt")}
            else:
                shots = {s.get("screen"): s.get("hash") for s in runs.get("screenshots") or [] if s.get("capability") == cap}
                if not shots:
                    die(f"{cap} has no recorded app screenshot to compare with its design (evidence.py shot)")
                signed[cap] = {"codeHash": current, "shots": shots}
        entry["capabilities"] = signed
        if args.accept:
            entry["accept"] = one_line(args.accept, 400)
        data[args.kind].append(entry)
        what = f"{args.kind} of {', '.join(signed)}"
    write_json(path_of(ws, args.program), data)
    print(f"recorded: {who} signed {what} -> analysis/{args.program}/SIGNOFF.json")


if __name__ == "__main__":
    main()
