#!/usr/bin/env python3
"""Trace every capability to the new design and to the new app, and list the gaps.

    python3 trace.py <program> [--result FILE] [--workspace DIR]

Reads capabilities.json, design/design.json, the mapping links (design/trace_result.json, written from the
fuse-trace-design workflow: {"links": [{screen, capabilities, confidence, evidence}], "unmapped": [...]}),
DECISIONS.json and the porting notes under new-app/<program>/docs/fusion/. Writes traceability.json and
TRACEABILITY.md. A link to a screen or capability that does not exist is dropped and reported, never kept.

A capability's status is computed with these rules, in this order:
  dropped        a person decided `gap: drop` or `scope: out`
  designed       at least one link to a design screen
  new            fusion class `new` (only the design has it)
  design-exempt  a person decided `gap: carry-as-is` (built from the legacy screens, restyled)
  no-design      none of the above: a gap a person must answer in fuse-review
Standard library only.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib.common import (check_name, die, load_json, md_table, now_iso, one_line, program_dir, workspace,  # noqa: E402
                              write_json, write_text)


def compute(ws, program, result_path=None):
    pdir = program_dir(ws, program)
    caps = load_json(os.path.join(pdir, "capabilities.json"))
    if not caps:
        die(f"analysis/{program}/capabilities.json not found: run /app-fusion:fuse-map {program} first")
    design = load_json(os.path.join(pdir, "design", "design.json")) or {"screens": []}
    result = load_json(result_path or os.path.join(pdir, "design", "trace_result.json")) or {"links": []}
    decisions = (load_json(os.path.join(pdir, "DECISIONS.json")) or {}).get("decisions") or {}
    prog = load_json(os.path.join(pdir, "program.json")) or {}

    cap_ids = {c["id"]: c for c in caps.get("capabilities", [])}
    screens = {s["id"]: s for s in design.get("screens", [])}
    dropped_links, links = [], []
    for link in result.get("links") or []:
        sid = link.get("screen")
        cids = [c for c in link.get("capabilities") or [] if c in cap_ids]
        bad = [c for c in link.get("capabilities") or [] if c not in cap_ids]
        if sid not in screens or not cids:
            dropped_links.append({"screen": sid, "capabilities": link.get("capabilities"), "why":
                                  "unknown screen" if sid not in screens else f"unknown capability {', '.join(map(str, bad))}"})
            continue
        links.append({"screen": sid, "capabilities": cids,
                      "confidence": link.get("confidence") if link.get("confidence") in ("High", "Medium", "Low") else "Medium",
                      "evidence": one_line(link.get("evidence"), 300)})

    decided = {}
    for d in decisions.values():
        decided[(d.get("about"), d.get("kind"))] = d.get("choice")

    target = os.path.join(ws, (prog.get("target") or {}).get("path") or f"new-app/{program}", "docs", "fusion")
    notes = {}
    if os.path.isdir(target):
        for name in os.listdir(target):
            m = re.match(r"^(CAP-\d+)\.md$", name)
            if m:
                notes[m.group(1)] = os.path.relpath(os.path.join(target, name), ws)

    per_cap = {}
    for cid, c in cap_ids.items():
        linked = sorted({l["screen"] for l in links if cid in l["capabilities"]})
        gap = decided.get((cid, "gap"))
        if gap == "drop" or decided.get((cid, "scope")) == "out":
            status = "dropped"
        elif linked:
            status = "designed"
        elif c.get("fusion") == "new":
            status = "new"
        elif gap == "carry-as-is":
            status = "design-exempt"
        else:
            status = "no-design"
        per_cap[cid] = {"screens": linked, "status": status, "module": notes.get(cid), "gapDecision": gap}

    linked_screens = {l["screen"] for l in links}
    candidate_screens = [s for s in design.get("screens", []) if s.get("kind") in ("screen", "state")]
    screens_without = [s["id"] for s in candidate_screens if s["id"] not in linked_screens
                       and decided.get((s["id"], "design")) not in ("out-of-scope", "in-scope", "new-spec")]
    diverged = [cid for cid, c in cap_ids.items() if c.get("fusion") == "shared-diverged" and (cid, "conflict") not in decided]
    in_scope = [cid for cid, t in per_cap.items() if t["status"] != "dropped"]
    designed = [cid for cid in in_scope if per_cap[cid]["status"] in ("designed", "new")]
    out = {
        "program": program, "version": 1, "generated": now_iso(), "links": links, "capabilities": per_cap,
        "gaps": {"capabilitiesWithoutDesign": [cid for cid, t in per_cap.items() if t["status"] == "no-design"],
                 "screensWithoutCapability": screens_without, "divergedWithoutDecision": diverged},
        "coverage": {"capabilities": len(in_scope), "designed": len(designed),
                     "percent": round(100 * len(designed) / len(in_scope)) if in_scope else 0,
                     "built": sum(1 for cid in in_scope if per_cap[cid]["module"]),
                     "screens": len(candidate_screens), "screensLinked": len(linked_screens & {s["id"] for s in candidate_screens})},
        "droppedLinks": dropped_links, "unmapped": result.get("unmapped") or [],
    }
    write_json(os.path.join(pdir, "traceability.json"), out)
    write_text(os.path.join(pdir, "TRACEABILITY.md"), render(out, caps, screens))
    cov = out["coverage"]
    g = out["gaps"]
    print(f"{cov['designed']} of {cov['capabilities']} in-scope capabilities have a design ({cov['percent']}%), {cov['built']} built; "
          f"gaps: {len(g['capabilitiesWithoutDesign'])} without design, {len(g['screensWithoutCapability'])} frames without a "
          f"capability, {len(g['divergedWithoutDecision'])} diverged without a decision"
          + (f"; {len(dropped_links)} invalid link(s) dropped" if dropped_links else "")
          + f" -> analysis/{program}/traceability.json, TRACEABILITY.md")
    return out


def render(t, caps, screens):
    names = {c["id"]: c for c in caps.get("capabilities", [])}
    cov = t["coverage"]
    lines = [f"# Traceability: {t['program']}", "",
             f"{cov['designed']} of {cov['capabilities']} in-scope capabilities are designed ({cov['percent']}%), "
             f"{cov['built']} are built, and {cov['screensLinked']} of {cov['screens']} design frames trace to a capability. "
             "Status rules are at the top of `scripts/trace.py`.", "",
             md_table(["Id", "Capability", "Fusion", "Status", "Screens", "New-app notes"],
                      [[cid, names[cid]["name"], names[cid]["fusion"], v["status"],
                        ", ".join(f"{screens.get(s, {}).get('name', s)}" for s in v["screens"][:4]) + (" …" if len(v["screens"]) > 4 else ""),
                        v["module"] or "-"] for cid, v in t["capabilities"].items()]), ""]
    g = t["gaps"]
    if g["capabilitiesWithoutDesign"]:
        lines += ["## Capabilities with no design", "", "Each needs a decision in `fuse-review`: design it, carry it as it is, drop it, or defer it.", ""]
        lines += [f"- **{cid}** {names[cid]['name']} ({', '.join(names[cid].get('implementations', {}).keys()) or 'no app'})"
                  for cid in g["capabilitiesWithoutDesign"]] + [""]
    if g["screensWithoutCapability"]:
        lines += ["## Design frames that match no legacy capability", "", "New features, or a mapping the agents missed:", ""]
        lines += [f"- `{sid}` {screens.get(sid, {}).get('name', '')}" for sid in g["screensWithoutCapability"][:80]] + [""]
    if g["divergedWithoutDecision"]:
        lines += ["## Diverged capabilities without a decision", ""]
        lines += [f"- **{cid}** {names[cid]['name']}: " + "; ".join(names[cid].get("divergence") or []) for cid in g["divergedWithoutDecision"]] + [""]
    if t.get("droppedLinks"):
        lines += ["## Links dropped as invalid", ""] + [f"- `{l['screen']}` -> {l['capabilities']}: {l['why']}" for l in t["droppedLinks"][:40]] + [""]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("--result")
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    compute(ws, args.program, args.result)


if __name__ == "__main__":
    main()
