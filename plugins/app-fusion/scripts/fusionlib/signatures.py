"""Sign-offs a named person recorded (analysis/<program>/SIGNOFF.json): the brief, the proof, visual conformance.

Each binds to what was signed (the brief's hash, a capability's verdict and code hash, its screenshots' hashes), so
a sign-off stops counting when the signed thing changes. Written only by scripts/signoff.py.
"""

import os
import re

from . import proofkit
from .common import load_json, program_dir


def path_of(ws, program):
    return os.path.join(program_dir(ws, program), "SIGNOFF.json")


def load(ws, program):
    data = load_json(path_of(ws, program)) or {}
    for key in ("brief", "proof", "visual"):
        data.setdefault(key, [])
    return data


def brief_hash(ws, program):
    p = os.path.join(program_dir(ws, program), "FUSION_BRIEF.md")
    return proofkit.sha256_file(p) if os.path.isfile(p) else None


def brief_approval(ws, program):
    """{approved, by, at, covers, stale}: the latest brief sign-off, and whether the brief changed since."""
    entries = load(ws, program)["brief"]
    if not entries:
        return {"approved": False, "by": None, "at": None, "covers": None, "stale": False}
    last = entries[-1]
    current = brief_hash(ws, program)
    stale = current is None or last.get("hash") != current
    return {"approved": not stale, "by": last.get("by"), "at": last.get("at"), "covers": last.get("covers"), "stale": stale}


def covered_phases(covers):
    """None for every phase, else the set of phase numbers an approval covers ("Phase 0, Phase 1", "0-2")."""
    text = str(covers or "").strip().lower()
    if not text or text in ("all", "every phase", "all phases"):
        return None
    nums = set()
    for a, b in re.findall(r"(\d+)\s*(?:-|–|to)\s*(\d+)", text):
        nums |= set(range(int(a), int(b) + 1))
    nums |= {int(n) for n in re.findall(r"\d+", text)}
    return nums or None


def capability_signoffs(ws, program, kind):
    """{CAP: latest entry for it} for kind proof or visual."""
    out = {}
    for e in load(ws, program)[kind]:
        for cap, detail in (e.get("capabilities") or {}).items():
            out[cap] = {**detail, "by": e.get("by"), "at": e.get("at"), "accept": e.get("accept")}
    return out


def signed_state(ws, program, verification=None):
    """{CAP: {"proof": bool, "visual": bool|None}}: whether each judged capability's current verdict and code are
    signed. visual is None when the capability has no design screen to compare."""
    pdir = program_dir(ws, program)
    verification = verification if verification is not None else (load_json(os.path.join(pdir, "VERIFICATION.json")) or {}).get("capabilities") or {}
    runs = load_json(os.path.join(pdir, "evidence", "test-runs.json")) or {}
    shots = {}
    for s in runs.get("screenshots") or []:
        shots.setdefault(s.get("capability"), {})[s.get("screen")] = s.get("hash")
    proof = capability_signoffs(ws, program, "proof")
    visual = capability_signoffs(ws, program, "visual")
    out = {}
    for cap, r in verification.items():
        current = proofkit.code_hash(ws, program, cap)
        p = proof.get(cap)
        ok_proof = bool(p) and p.get("codeHash") == current and p.get("verdict") == r.get("verdict")
        if r.get("screens"):
            v = visual.get(cap)
            ok_visual = bool(v) and v.get("codeHash") == current and v.get("shots") == shots.get(cap, {}) and bool(shots.get(cap))
        else:
            ok_visual = None
        out[cap] = {"proof": ok_proof, "visual": ok_visual}
    return out
