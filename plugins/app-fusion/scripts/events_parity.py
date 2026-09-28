#!/usr/bin/env python3
"""Does the new app still send the analytics events the legacy apps sent, capability by capability?

    python3 events_parity.py <program> [--capability CAP-NNN ...] [--workspace DIR]

Dashboards, funnels and alerts are keyed on event names, so a renamed or lost event breaks them silently. For each
built capability the legacy events come from capabilities.json (implementations.<app>.events) and the new app's from
its own inventory, extracted with the same rules (event catalogs, enums, logEvent/track literals), in each half of a
native pair. An event matches when the new app has the same name (compared without case and punctuation). A rename
is written in new-app/<program>/docs/fusion/analytics-map.json ({"<app>:<event>": "<new event>"}) and counts only
when a person chose a new taxonomy (decision `analytics` about "analytics:taxonomy": new-taxonomy) or approved that
rename (`analytics: rename` about "<app>:<event>"). A dropped event (null in the map) needs `analytics: drop`. When
the map lists no event for a capability, the legacy inventory is searched for events in the capability's own files:
finding some is a gap, finding none is n/a. Writes analysis/<program>/evidence/events-parity.json. Exit 0 when
nothing fails. Standard library only.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import newapp, parity, proofkit  # noqa: E402
from fusionlib.common import check_name, die, load_json, workspace  # noqa: E402

MAP = "docs/fusion/analytics-map.json"


def key(name):
    return re.sub(r"[^a-z0-9]", "", str(name or "").lower())


def run(ws, program, only=None):
    pdir, caps, prog, decisions = parity.load_context(ws, program)
    if not caps:
        die(f"analysis/{program}/capabilities.json not found")
    emap = load_json(os.path.join(newapp.root(ws, program), MAP)) or {}
    taxonomy_id = parity.decision_for(decisions, "analytics", {"analytics:taxonomy"}, {"keep-names", "new-taxonomy"})
    taxonomy = (decisions.get(taxonomy_id) or {}).get("choice")
    halves = newapp.halves(ws, program)
    new_events = {}
    for platform, half in halves:
        inv = newapp.inventory(ws, program, platform) if platform else newapp.inventory(ws, program)
        names = set()
        for e in inv.get("events", []):
            names |= {key(e.get("name")), key(e.get("key"))} - {""}
        new_events[half] = names
    results = {}
    for c, exists in parity.targets(ws, program, caps, only):
        cid = c["id"]
        if not exists:
            results[cid] = {"verdict": "gap", "reason": "no porting notes: the capability is not built yet"}
            continue
        info = proofkit.notes(ws, program, cid)
        kept, renamed, dropped, missing, undecided, used = [], [], [], [], [], []
        total = 0
        for app, impl in (c.get("implementations") or {}).items():
            for ev in impl.get("events") or []:
                total += 1
                abouts = {f"{app}:{ev}", f"{cid}:{app}:{ev}"}
                raw = emap.get(f"{app}:{ev}", emap.get(ev, ev))
                if raw is None:
                    did = parity.decision_for(decisions, "analytics", abouts, {"drop"})
                    if did:
                        dropped.append({"legacy": f"{app}:{ev}", "decision": did})
                        used.append(did)
                    else:
                        missing.append({"legacy": f"{app}:{ev}", "why": "dropped in the map without a person's decision (analytics: drop)"})
                    continue
                for platform, half in halves:
                    target = raw.get(platform or "", raw.get("default")) if isinstance(raw, dict) else raw
                    where = f" ({platform})" if platform else ""
                    if key(target) not in new_events[half]:
                        missing.append({"legacy": f"{app}:{ev}", "new": target, "why": f"the new app sends no such event{where}"})
                        continue
                    if key(target) == key(ev):
                        kept.append(f"{app}:{ev}{where}")
                        continue
                    did = parity.decision_for(decisions, "analytics", abouts, {"rename"})
                    if did or taxonomy == "new-taxonomy":
                        renamed.append({"legacy": f"{app}:{ev}", "new": f"{target}{where}", "decision": did or taxonomy_id})
                        used.append(did or taxonomy_id)
                    elif taxonomy == "keep-names":
                        missing.append({"legacy": f"{app}:{ev}", "new": target,
                                        "why": f"renamed{where}, but a person chose to keep the legacy names ({taxonomy_id})"})
                        used.append(taxonomy_id)
                    else:
                        undecided.append(f"{app}:{ev} -> {target}{where}")
        files = info["files"] + info["shared"] + [MAP]
        stamp = parity.stamp(ws, program, cid, files, decisions, used)
        if total == 0:
            seen = []
            for app, impl in (c.get("implementations") or {}).items():
                cited = parity.cited_files(impl)
                seen += [f"{app}:{e.get('name')}" for e in parity.legacy_inventory(pdir, app).get("events", [])
                         if parity.in_cited(e.get("file"), cited)]
            if seen:
                verdict, reason = "gap", (f"the map lists no event, but the inventory finds {len(seen)} in the capability's legacy files "
                                          f"({', '.join(seen[:5])}{' …' if len(seen) > 5 else ''}): add them to the map")
            else:
                verdict, reason = "n/a", "no event in the map, and the inventory finds none in the capability's legacy files"
        elif missing:
            verdict, reason = "fail", f"{len(missing)} legacy event(s) not sent by the new app and not decided"
        elif undecided:
            verdict, reason = "gap", (f"{len(undecided)} rename(s) wait for a person's taxonomy decision "
                                      "(fuse-review: analytics:taxonomy)")
        else:
            verdict, reason = "pass", f"{len(kept)} kept, {len(renamed)} renamed by decision, {len(dropped)} dropped by decision"
        results[cid] = {"verdict": verdict, "reason": reason, "events": total, "kept": kept, "renamed": renamed,
                        "dropped": dropped, "missing": missing, "undecided": undecided, **stamp}
    path, counts = parity.write_result(
        ws, program, "events-parity.json",
        "each legacy event of the capability is sent by the new app under the same name (case and punctuation ignored), "
        "or under a mapped name a person approved, or was dropped by a person's decision", results,
        {"taxonomy": taxonomy or "undecided"})
    print(f"events parity: {', '.join(f'{v} {k}' for k, v in sorted(counts.items())) or 'nothing built yet'} -> {os.path.relpath(path, ws)}")
    return 1 if counts.get("fail") else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("--capability", action="append")
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    sys.exit(run(ws, args.program, set(args.capability or [])))


if __name__ == "__main__":
    main()
