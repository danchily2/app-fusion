"""Where a program stands: artifacts per stage, what is stale, the brief's phases and approval, the next command."""

import os
import re

from .common import load_json, program_dir

PREFIX = "/app-fusion:"


def _mtime(path):
    try:
        return os.path.getmtime(path)
    except OSError:
        return None


def parse_brief(path):
    """Phases and approval from FUSION_BRIEF.md. A phase is '#### Phase N — name' followed by 'Key: value' lines."""
    if not os.path.isfile(path):
        return {"exists": False, "phases": [], "approved": False, "approvedBy": None, "covers": None}
    text = open(path, encoding="utf-8", errors="replace").read()
    phases = []
    for m in re.finditer(r"(?m)^####\s+Phase\s+(\d+)\s*[—–-]+\s*(.+?)\s*$", text):
        body = text[m.end(): text.find("\n####", m.end()) if text.find("\n####", m.end()) > 0 else len(text)]
        fields = {}
        for fm in re.finditer(r"(?m)^([A-Z][A-Za-z ]+):\s*(.*)$", body):
            fields[fm.group(1).strip().lower()] = fm.group(2).strip()
        caps = re.findall(r"CAP-\d+", fields.get("capabilities", ""))
        phases.append({"number": int(m.group(1)), "name": m.group(2), "command": fields.get("command", ""),
                       "capabilities": caps, "journeys": re.findall(r"JRN-\d+", fields.get("journeys", "")),
                       "scale": fields.get("scale", ""), "risk": fields.get("risk", ""),
                       "entry": re.findall(r"(?m)^- \[( |x|X)\]\s*(.+)$", body.split("Exit criteria")[0]),
                       "exit": re.findall(r"(?m)^- \[( |x|X)\]\s*(.+)$", body.split("Exit criteria")[1]) if "Exit criteria" in body else []})
    approved_by = re.search(r"(?m)^Approved by:\s*(.*?)\s{2,}Date:\s*(.*)$", text) or re.search(r"(?m)^Approved by:\s*(.*)$", text)
    who = approved_by.group(1).strip() if approved_by else ""
    signed = bool(who) and not re.fullmatch(r"_+|<[^>]*>|\.+", who)
    covers = re.search(r"(?m)^Approval covers:\s*(.*)$", text)
    return {"exists": True, "phases": phases, "approved": signed, "approvedBy": who if signed else None,
            "covers": covers.group(1).strip() if covers else None}


def artifacts(ws, program):
    pdir = program_dir(ws, program)
    prog = load_json(os.path.join(pdir, "program.json")) or {}
    apps = [a["name"] for a in prog.get("apps", [])]
    target = os.path.join(ws, (prog.get("target") or {}).get("path") or f"new-app/{program}")
    f = lambda *p: os.path.join(pdir, *p)
    stages = [
        ("intent", [f("INTENT.md"), f("program.json")]),
        ("preflight", [f("PREFLIGHT.md")]),
        ("assess", [f("apps", a, "inventory.json") for a in apps] + [f("ASSESSMENT.md")]),
        ("map", [f("capabilities.json"), f("CAPABILITIES.md"), f("platform.json")]),
        ("design", [f("design", "design.json"), f("traceability.json")]),
        ("rules", [f("rules.json"), f("BUSINESS_RULES.md")]),
        ("review", [f("DECISIONS.json")]),
        ("brief", [f("CONTINUITY.md"), f("FUSION_BRIEF.md")]),
        ("scaffold", [os.path.join(target, "docs", "fusion", "SCAFFOLD.md")]),
        ("verify", [f("VERIFICATION.json")]),
        ("harden", [f("SECURITY_FINDINGS.md")]),
    ]
    out = []
    for name, paths in stages:
        present = [p for p in paths if os.path.exists(p)]
        out.append({"stage": name, "files": [os.path.relpath(p, ws) for p in paths], "present": len(present),
                    "total": len(paths), "mtime": max((_mtime(p) or 0) for p in present) if present else None})
    return out, prog, target


def built_capabilities(target):
    folder = os.path.join(target, "docs", "fusion")
    if not os.path.isdir(folder):
        return {}
    return {m.group(1): _mtime(os.path.join(folder, name)) for name in os.listdir(folder)
            for m in [re.match(r"^(CAP-\d+)\.md$", name)] if m}


def stale(ws, program):
    pdir = program_dir(ws, program)
    t = lambda *p: _mtime(os.path.join(pdir, *p))
    out = []
    pairs = [
        (("FUSION_BRIEF.md",), [("capabilities.json",), ("rules.json",), ("traceability.json",), ("DECISIONS.json",), ("CONTINUITY.md",)],
         "the brief predates {what}: re-run fuse-brief"),
        (("traceability.json",), [("capabilities.json",), ("design", "design.json"), ("DECISIONS.json",)],
         "traceability predates {what}: re-run trace.py (fuse-design step 6)"),
        (("CAPABILITIES.md",), [("map_result.json",)], "CAPABILITIES.md predates {what}: re-run render.py capabilities"),
        (("BUSINESS_RULES.md",), [("rules_result.json",)], "BUSINESS_RULES.md predates {what}: re-run render.py rules"),
        (("DESIGN_INVENTORY.md",), [("design", "design.json")], "DESIGN_INVENTORY.md predates {what}: re-run render.py design"),
        (("REPORT.html",), [("capabilities.json",), ("VERIFICATION.json",), ("FUSION_BRIEF.md",)], "REPORT.html predates {what}: re-run build_report.py"),
    ]
    for target, sources, message in pairs:
        tt = t(*target)
        if tt is None:
            continue
        newer = ["/".join(s) for s in sources if (t(*s) or 0) > tt + 1]
        if newer:
            out.append(message.format(what=", ".join(newer)))
    return out


def next_step(ws, program, open_count=None):
    """(command, reason): the single most useful next step, in the order docs/DESIGN.md gives."""
    stages, prog, target = artifacts(ws, program)
    have = {s["stage"]: s["present"] == s["total"] for s in stages}
    pdir = program_dir(ws, program)
    p = program
    if not prog:
        return f"{PREFIX}fuse {p} --source <app>=<path> --source <app>=<path>", "nothing is set up yet"
    if not have["preflight"]:
        return f"{PREFIX}fuse-preflight {p}", "check the environment and ask the five questions first"
    if not have["assess"]:
        return f"{PREFIX}fuse-assess {p}", "inventory both apps"
    if not os.path.exists(os.path.join(pdir, "capabilities.json")):
        return f"{PREFIX}fuse-map {p}", "build the capability map across the apps"
    if prog.get("figma") and not have["design"]:
        return f"{PREFIX}fuse-design {p}", "read the new app's Figma designs and trace them to the capabilities"
    if not os.path.exists(os.path.join(pdir, "rules.json")):
        return f"{PREFIX}fuse-rules {p}", "mine the business rules of both apps"
    if open_count:
        return f"{PREFIX}fuse-review {p}", f"{open_count} question(s) only a person can answer"
    brief = parse_brief(os.path.join(pdir, "FUSION_BRIEF.md"))
    if not brief["exists"]:
        return f"{PREFIX}fuse-brief {p}", "write the phased plan"
    if not brief["approved"]:
        return "(a person) sign the Approval block of FUSION_BRIEF.md", "nothing is built before the brief is approved"
    if not have["scaffold"]:
        return f"{PREFIX}fuse-scaffold {p}", "Phase 0: the new app's foundation"
    built = built_capabilities(target)
    verification = load_json(os.path.join(pdir, "VERIFICATION.json")) or {}
    vtime = _mtime(os.path.join(pdir, "VERIFICATION.json")) or 0
    judged = verification.get("capabilities") or {}
    unverified = [c for c, t in built.items() if c not in judged or (t or 0) > vtime]
    if unverified:
        return f"{PREFIX}fuse-verify {p} {' '.join(sorted(unverified)[:5])}", "built capabilities are not proven until verify says so"
    not_proven = [c for c, r in judged.items() if r.get("verdict") != "PROVEN"]
    if not_proven:
        return f"{PREFIX}fuse-build {p} {sorted(not_proven)[0]}", f"{len(not_proven)} capability(ies) not PROVEN yet: fix the first reason"
    for phase in brief["phases"]:
        for cap in phase["capabilities"]:
            if cap not in built:
                return f"{PREFIX}fuse-build {p} {cap}", f"next capability of Phase {phase['number']} ({phase['name']})"
    if not have["harden"]:
        return f"{PREFIX}fuse-harden {p}", "security review of the new app"
    return "(done) sign VERIFICATION.md and plan the rollout in CONTINUITY.md", "every phase is built and proven"
