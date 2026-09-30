"""Where a program stands: artifacts per stage, what is stale, the brief's phases and approval, the next command."""

import os
import re

from . import proofkit, signatures
from .common import load_json, program_dir

PREFIX = "/app-fusion:"
SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def script(name):
    """The command that runs one of the plugin's scripts from any folder."""
    return f'python3 "{os.path.join(SCRIPTS, name)}"'


def _mtime(path):
    try:
        return os.path.getmtime(path)
    except OSError:
        return None


def parse_brief(path, ws=None, program=None):
    """Phases from FUSION_BRIEF.md ('#### Phase N — name' followed by 'Key: value' lines) and the approval, which
    lives in SIGNOFF.json (scripts/signoff.py), never in the brief itself: a model writes the brief."""
    empty = {"exists": False, "phases": [], "approved": False, "approvedBy": None, "covers": None, "stale": False}
    if not os.path.isfile(path):
        return empty
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
    out = dict(empty, exists=True, phases=phases)
    if ws and program:
        a = signatures.brief_approval(ws, program)
        out.update({"approved": a["approved"], "approvedBy": a["by"] if a["approved"] else None, "covers": a["covers"],
                    "stale": a["stale"] and bool(a["by"])})
    return out


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
         "traceability predates {what}: re-run trace.py (fuse-design step 5)"),
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
    brief = parse_brief(os.path.join(pdir, "FUSION_BRIEF.md"), ws, program)
    if brief["stale"]:
        out.append("the brief changed after it was approved: the approval no longer counts (fuse-brief approve)")
    return out


def _waiting_only(r, built):
    """True when a verdict's only open checks are journeys that wait for capabilities not built yet."""
    open_checks = {k: v for k, v in (r.get("checks") or {}).items() if v.get("status") != "pass"}
    return bool(open_checks) and set(open_checks) == {"Journeys"} and "waits for" in open_checks["Journeys"].get("detail", "") \
        and open_checks["Journeys"].get("status") == "gap" and "no run recorded" not in open_checks["Journeys"]["detail"] \
        and "stale" not in open_checks["Journeys"]["detail"]


def intent_open_items(ws, program):
    """The `OPEN:` lines of INTENT.md: answers a headless run of the front door recorded as documented defaults."""
    path = os.path.join(program_dir(ws, program), "INTENT.md")
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8", errors="replace") as fh:
        return [line.strip()[5:].strip() for line in fh if line.strip().startswith("OPEN:")]


def next_step(ws, program, open_count=None):
    """(command, reason): the single most useful next step, in the order docs/DESIGN.md gives."""
    stages, prog, target = artifacts(ws, program)
    have = {s["stage"]: s["present"] == s["total"] for s in stages}
    pdir = program_dir(ws, program)
    p = program
    if not prog:
        return f"{PREFIX}fuse {p} --source <app>=<path> --source <app>=<path>", "nothing is set up yet"
    pending = sorted(os.listdir(os.path.join(pdir, "evidence", "canary"))) if os.path.isdir(os.path.join(pdir, "evidence", "canary")) else []
    pending = [c for c in pending if os.path.isfile(os.path.join(pdir, "evidence", "canary", c, "pending.json"))]
    if pending:
        return (f"{script('canary.py')} finish {p} {pending[0]}  (or: canary.py abort {p} {pending[0]})",
                f"a deliberate break is still in {pending[0]}'s code: finish or abort the canary first")
    if not have["preflight"]:
        return f"{PREFIX}fuse-preflight {p}", "check the environment and ask the five questions first"
    if not have["assess"]:
        return f"{PREFIX}fuse-assess {p}", "inventory both apps"
    caps = load_json(os.path.join(pdir, "capabilities.json"))
    if not caps:
        return f"{PREFIX}fuse-map {p}", "build the capability map across the apps"
    if caps.get("retired"):
        r = caps["retired"][0]
        return (f"(map the retired ids) name the capability that replaces {r['id']} in analysis/{p}/map_aliases.json "
                f"(or null to let it go), then {script('render.py')} capabilities {p}",
                f"{len(caps['retired'])} capability id(s) left the map but are still used by decisions, rules or notes")
    rules_doc = load_json(os.path.join(pdir, "rules.json")) or {}
    if rules_doc.get("retired"):
        r = rules_doc["retired"][0]
        return (f"(map the retired rule ids) name the rule that replaces {r['id']} in analysis/{p}/rules_aliases.json "
                f"(or null to let it go), then {script('render.py')} rules {p}",
                f"{len(rules_doc['retired'])} rule id(s) left the rules but decisions still name them")
    if prog.get("figma") and not have["design"]:
        return f"{PREFIX}fuse-design {p}", "read the new app's Figma designs and trace them to the capabilities"
    if not os.path.exists(os.path.join(pdir, "rules.json")):
        return f"{PREFIX}fuse-rules {p}", "mine the business rules of both apps"
    if open_count:
        return f"{PREFIX}fuse-review {p}", f"{open_count} question(s) only a person can answer"
    brief = parse_brief(os.path.join(pdir, "FUSION_BRIEF.md"), ws, p)
    open_intent = intent_open_items(ws, p)
    if open_intent and not brief["approved"]:
        # a headless first run wrote documented defaults into INTENT.md; the plan is bound by a person's words, so they
        # are asked before the brief is written or approved
        return f"{PREFIX}fuse {p}", (f"{len(open_intent)} intent answer(s) are documented defaults from a headless run, not a "
                                     f"person's words: the front door asks exactly those ({open_intent[0][:80]})")
    if not brief["exists"]:
        return f"{PREFIX}fuse-brief {p}", "write the phased plan"
    if not brief["approved"]:
        why = "the brief changed after it was approved" if brief["stale"] else "nothing is built before the brief is approved"
        return f"(a person) {PREFIX}fuse-brief {p} approve", why
    if prog.get("goal") == "understand":
        return "(done) the analysis is complete: the brief and REPORT.html are the result", \
            "the goal is to understand the apps, not to build (workspace.py intent --goal build to go on)"
    if not have["scaffold"]:
        return f"{PREFIX}fuse-scaffold {p}", "Phase 0: the new app's foundation"
    covered = signatures.covered_phases(brief["covers"])
    decisions = (load_json(os.path.join(pdir, "DECISIONS.json")) or {}).get("decisions") or {}
    parked = {d["about"] for d in decisions.values()
              if (d.get("kind") == "gap" and d.get("choice") in ("drop", "defer")) or (d.get("kind") == "scope" and d.get("choice") in ("out", "defer"))
              or (d.get("kind") == "conflict" and d.get("choice") == "defer" and re.match(r"^CAP-\d+$", d.get("about") or ""))}
    built = built_capabilities(target)
    # the legacy apps first: no build step can fix a changed or moved checkout
    import workspace as wsmod  # the script module: legacy state is read with read-only git
    for r in wsmod.legacy_state(ws, prog):
        if r["exists"] and r["clean"] is False:
            return (f"(a person) restore legacy/{r['app']} to a clean checkout",
                    f"legacy/{r['app']} has local changes; the plugin never writes there, so someone else did, and every "
                    "verdict waits for it (untracked files count)")
        if r["exists"] and r["recordedCommit"] and r["clean"] is not None and not r["atRecordedCommit"]:
            return (f"(a person) check out {r['recordedCommit'][:12]} in legacy/{r['app']}, or record the new commit with "
                    f"{script('workspace.py')} init {p} --source {r['app']}=<path> and re-run fuse-assess and fuse-map",
                    f"legacy/{r['app']} moved from {r['recordedCommit'][:12]} to {(r['commit'] or '?')[:12]}: the analysis "
                    "describes the recorded commit")
    verification = load_json(os.path.join(pdir, "VERIFICATION.json")) or {}
    judged = verification.get("capabilities") or {}
    unverified = [c for c in built if c not in judged or judged[c].get("codeHash") != proofkit.code_hash(ws, p, c)]
    if unverified:
        return f"{PREFIX}fuse-verify {p} {' '.join(sorted(unverified, key=lambda x: int(x.split('-')[1]))[:5])}", \
            "built capabilities are not proven until verify judges their current code"
    signed = signatures.signed_state(ws, p, judged)
    # a PARTLY PROVEN capability a person signed with their reason for accepting its open checks is settled
    accepted = {c for c, r in judged.items() if r.get("verdict") == "PARTLY PROVEN" and (signed.get(c) or {}).get("proof")}
    to_fix = [c for c, r in judged.items() if r.get("verdict") != "PROVEN" and c in built and c not in accepted
              and not _waiting_only(r, built)]
    if to_fix:
        first = sorted(to_fix, key=lambda x: int(x.split("-")[1]))[0]
        return f"{PREFIX}fuse-build {p} {first}", f"{len(to_fix)} capability(ies) not PROVEN yet: fix the first reason"
    waiting = sorted(c for c, r in judged.items() if r.get("verdict") != "PROVEN" and _waiting_only(r, built))
    for phase in brief["phases"]:
        if covered is not None and phase["number"] not in covered:
            if any(cap not in built and cap not in parked for cap in phase["capabilities"]):
                return (f"(a person) {PREFIX}fuse-brief {p} approve",
                        f"the approval covers Phase(s) {', '.join(map(str, sorted(covered)))}; Phase {phase['number']} "
                        f"({phase['name']}) needs a person's approval before it is built")
            continue
        for cap in phase["capabilities"]:
            if cap not in built and cap not in parked:
                why = f"next capability of Phase {phase['number']} ({phase['name']})"
                if waiting:
                    why += f"; {', '.join(waiting)} wait(s) for it or others on a shared journey"
                return f"{PREFIX}fuse-build {p} {cap}", why
    if waiting:
        return f"{PREFIX}fuse-verify {p} {' '.join(waiting[:5])}", "every capability is built: verify the journeys that were waiting"
    cont = verification.get("continuity") or {}
    if cont.get("verdict") != "pass":
        rows = cont.get("checks") or []
        undecided = [r for r in rows if r.get("verdict") == "gap" and "not decided" in (r.get("why") or "")]
        failing = [r for r in rows if r.get("verdict") == "fail"]
        if undecided and not failing:
            if any(r.get("check") == "identity" for r in undecided):
                return f"(a person) {PREFIX}fuse-brief {p} approve", "the store listing the new app ships under is not decided"
            return f"{PREFIX}fuse-review {p} platform", "platform items existing users depend on are not decided: " + \
                "; ".join(f"{r['check']}: {r['why']}" for r in undecided[:3])
        if failing:
            return (f"{PREFIX}fuse-scaffold {p}", "the app shell lacks what existing users rely on (fuse-scaffold adds it to an "
                    "existing scaffold): " + "; ".join(f"{r['check']}: {r['why']}" for r in failing[:3]))
        return f"{PREFIX}fuse-verify {p}", "platform continuity for existing users is not proven yet: " + \
            (cont.get("detail") or "platform_parity.py has not run")
    unsigned = [c for c, st in signed.items() if not st["proof"] or st["visual"] is False]
    if unsigned:
        return f"(a person) {PREFIX}fuse-verify {p} sign", f"{len(unsigned)} proven capability(ies) wait for a person's sign-off"
    security = os.path.join(pdir, "SECURITY_FINDINGS.md")
    newest = max((t or 0) for t in built.values()) if built else 0
    if not os.path.isfile(security) or (_mtime(security) or 0) < newest:
        return f"{PREFIX}fuse-harden {p}", "security review of the new app as it is now"
    return "(done) plan the rollout in CONTINUITY.md", "every phase is built, proven and signed"
