"""What the parity checks share: the capabilities to judge, the legacy side's own evidence for a cross-check, the
decisions that excuse a difference, and the result file every check writes.

A check never trusts an empty list from the map. When the map lists nothing for a capability (no endpoint, no string
key, no event), the check looks at the capability's own legacy files: when the inventory finds something there, the
result is a gap, not an n/a.
"""

import os
import re

from . import newapp, proofkit
from .common import load_json, now_iso, program_dir, write_json


def load_context(ws, program):
    pdir = program_dir(ws, program)
    caps = load_json(os.path.join(pdir, "capabilities.json"))
    prog = load_json(os.path.join(pdir, "program.json")) or {}
    decisions = (load_json(os.path.join(pdir, "DECISIONS.json")) or {}).get("decisions") or {}
    return pdir, caps, prog, decisions


def targets(ws, program, caps, only):
    """(capability, built?) for the capabilities to judge: the given ids, or every built one."""
    for c in (caps or {}).get("capabilities", []):
        if only and c["id"] not in only:
            continue
        exists = os.path.isfile(newapp.notes_path(ws, program, c["id"]))
        if exists or only:
            yield c, exists


def cited_files(impl):
    """The legacy files a capability's implementation cites (paths relative to legacy/<app>, line numbers dropped)."""
    out = []
    for f in (impl.get("files") or []) + ([impl["evidence"]] if impl.get("evidence") else []):
        rel = str(f).split(":")[0].strip().lstrip("./")
        if rel and rel not in out:
            out.append(rel)
    return out


def legacy_inventory(pdir, app):
    return load_json(os.path.join(pdir, "apps", app, "inventory.json")) or {}


def in_cited(entry_file, cited):
    return (entry_file or "").split(":")[0] in cited


def decision_for(decisions, kind, abouts, choices):
    """The DEC id of a decision of `kind` about any of `abouts` whose choice is in `choices`, else None."""
    for did, d in decisions.items():
        if d.get("kind") == kind and d.get("about") in abouts and d.get("choice") in choices:
            return did
    return None


def dec_ids(text):
    return re.findall(r"DEC-\d+", str(text or ""))


def write_result(ws, program, name, rule, results, extra=None):
    out = {"program": program, "version": 2, "generated": now_iso(), "rule": rule, "capabilities": results}
    out.update(extra or {})
    path = os.path.join(program_dir(ws, program), "evidence", name)
    write_json(path, out)
    counts = {}
    for r in results.values():
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    return path, counts


def stamp(ws, program, cap, files, decisions, used):
    """What a result depends on: the hashes of the files it read and the decisions it relied on."""
    return {"codeHash": proofkit.code_hash(ws, program, cap), "inputs": newapp.input_hashes(ws, program, files),
            "decisionsUsed": proofkit.decisions_used(decisions, used)}
