#!/usr/bin/env python3
"""Record a person's decisions, and list the questions still open.

    python3 decisions.py open <program> [--json]                          what a person still has to decide
    python3 decisions.py add <program> --about X --kind K --choice C [--question Q] [--note N] [--by NAME]
    python3 decisions.py add-json <program> <file.json>                   a list of {about, kind, choice, question?, note?, by?}
    python3 decisions.py render <program>                                 rewrite DECISIONS.md from DECISIONS.json

Only a person decides: this script records answers exactly as given and never infers one. Every question has its own
`about` key (a capability conflict is about "CAP-014", a rule conflict inside it about "CAP-014:RULE-003+RULE-021"),
so two questions never share an answer. A new answer to the same question (same `about` and `kind`) replaces the
earlier one, keeps its DEC id and records what it replaced. `about` and `choice` are validated per kind (see
docs/DESIGN.md). The plugin's guard asks the person to confirm every `add` and `add-json`. Standard library only.
"""

import argparse
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib.common import (check_name, die, load_json, md_table, now_iso, one_line, person_name, program_dir, workspace,  # noqa: E402
                              write_json, write_text)

STACKS = {"react-native", "native", "swiftui", "compose", "flutter", "kmp"}
RULES = r"(?:RULE-\d+(?:\+RULE-\d+)+(?::[0-9a-f]{8})?|conflict-[0-9a-f]{8})"
EVENT_OR_KEY = r"(?:CAP-\d+:)?[A-Za-z0-9_.-]+:\S.*"
KINDS = {
    "conflict": (rf"^(?:CAP-\d+|CAP-\d+:{RULES}|rules:{RULES})$",
                 lambda c, apps: c in {"design", "both-by-role", "new-spec", "defer"} or (c.startswith("take:") and c[5:] in apps)),
    "gap": (r"^CAP-\d+$", lambda c, apps: c in {"design-it", "carry-as-is", "drop", "defer"}),
    "rule": (r"^RULE-\d+$", lambda c, apps: c in {"confirmed", "wrong", "discuss"}),
    "attach": (r"^RULE-\d+$", lambda c, apps: c == "none" or bool(re.match(r"^CAP-\d+$", c))),
    "design": (r"^[0-9A-Za-z]{10,128}:\d+[:-]\d+$", lambda c, apps: c in {"in-scope", "out-of-scope", "new-spec"}),
    "platform": (r"^PLT-\d+$", lambda c, apps: c in {"keep", "drop", "decide-later"}),
    "scope": (r"^CAP-\d+$", lambda c, apps: c in {"in", "out", "defer"}),
    "stack": (r"^stack$", lambda c, apps: c in STACKS),
    "continuity": (r"^continuity:[a-z0-9-]+$", lambda c, apps: bool(c.strip())),
    "api": (r"^CAP-\d+:(?:(?:GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS|\?) )?/\S*$", lambda c, apps: c in {"replaced", "dropped", "accepted"}),
    "strings": (rf"^{EVENT_OR_KEY}$", lambda c, apps: c == "drop"),
    "analytics": (rf"^(?:analytics:taxonomy|{EVENT_OR_KEY})$", lambda c, apps: c in {"keep-names", "new-taxonomy", "drop", "rename"}),
    "roles": (r"^CAP-\d+$", lambda c, apps: bool(re.match(r"^[A-Za-z][\w -]*(?:,\s*[A-Za-z][\w -]*)*$", c))),
}
CHOICES_HELP = {
    "conflict": "take:<app>, design, both-by-role, new-spec, defer (about CAP-NNN, CAP-NNN:RULE-a+RULE-b or rules:RULE-a+RULE-b)",
    "gap": "design-it, carry-as-is, drop, defer (about CAP-NNN)", "rule": "confirmed, wrong, discuss (about RULE-NNN)",
    "attach": "CAP-NNN or none (about RULE-NNN: which capability the rule belongs to)",
    "design": "in-scope, out-of-scope, new-spec (about <fileKey>:<nodeId>)", "platform": "keep, drop, decide-later (about PLT-NNN)",
    "scope": "in, out, defer (about CAP-NNN)", "stack": ", ".join(sorted(STACKS)) + " (about stack)",
    "continuity": "free text, verbatim (about continuity:<topic>)",
    "api": "replaced, dropped, accepted (about 'CAP-NNN:<METHOD> <path>')",
    "strings": "drop (about '<app>:<key>' or 'CAP-NNN:<app>:<key>')",
    "analytics": "keep-names or new-taxonomy (about analytics:taxonomy); drop or rename (about '<app>:<event>')",
    "roles": "the personas who see the capability, comma separated (about CAP-NNN)",
}
BLOCKING_PLATFORM_AREAS = {"identity", "links", "push", "extensions", "sharing", "storage", "i18n", "privacy"}


def _path(ws, program):
    return os.path.join(program_dir(ws, program), "DECISIONS.json")


def load(ws, program):
    return load_json(_path(ws, program)) or {"program": program, "version": 1, "decisions": {}}


def _apps(ws, program):
    prog = load_json(os.path.join(program_dir(ws, program), "program.json")) or {}
    return {a["name"] for a in prog.get("apps", [])}


def find(decisions, about, kind):
    """(DEC id, decision) of the answer to one question, or (None, None)."""
    for k, d in decisions.items():
        if d.get("about") == about and d.get("kind") == kind:
            return k, d
    return None, None


def rule_conflict_about(capability, rule_ids):
    ids = "+".join(sorted(set(rule_ids), key=lambda r: int(r.split("-")[1])))
    return f"{capability}:{ids}" if capability else f"rules:{ids}"


def conflict_keys(conflicts):
    """Give every rule conflict its own key. When two conflicts name the same rules (the same pair of cards can differ
    in two ways), each gets its difference's hash as a suffix, whatever their order, so one answer never answers
    both."""
    for c in conflicts:
        c.pop("key", None)
        c["key"] = conflict_key(c)
    counts = {}
    for c in conflicts:
        counts[c["key"]] = counts.get(c["key"], 0) + 1
    for c in conflicts:
        if counts[c["key"]] > 1 and ":conflict-" not in c["key"]:
            c["key"] = f"{c['key']}:{hashlib.sha1(one_line(c.get('difference'), 400).encode('utf-8')).hexdigest()[:8]}"
    return conflicts


def conflict_key(conf):
    """The question key of a rule conflict: its rule ids when two or more were resolved, else a key made from its
    difference, so a conflict whose rule names did not resolve is still asked, never lost."""
    if conf.get("key"):
        return conf["key"]
    ids = [r for r in conf.get("rules") or [] if isinstance(r, str) and re.match(r"^RULE-\d+$", r)]
    if len(set(ids)) >= 2:
        return rule_conflict_about(conf.get("capability"), ids)
    digest = hashlib.sha1(one_line(conf.get("difference"), 400).encode("utf-8")).hexdigest()[:8]
    return f"{conf.get('capability') or 'rules'}:conflict-{digest}"


def add(ws, program, items):
    data = load(ws, program)
    apps = _apps(ws, program)
    decisions = data["decisions"]
    changed = []
    for item in items:
        kind = item.get("kind")
        choice = str(item.get("choice") or "").strip()
        about = str(item.get("about") or "").strip()
        if kind not in KINDS:
            die(f"kind {kind!r} is not one of {', '.join(sorted(KINDS))}")
        pattern, valid = KINDS[kind]
        if not re.match(pattern, about):
            die(f"about {about!r} does not fit kind {kind!r} ({CHOICES_HELP[kind]})")
        if not valid(choice, apps):
            die(f"choice {choice!r} is not valid for kind {kind!r} (valid: {CHOICES_HELP[kind]})")
        by = one_line(item.get("by"), 80)
        if by and not person_name(by):
            die(f"by {by!r} is not a person's name: a decision carries the name of the person who made it, or none")
        existing, old = find(decisions, about, kind)
        did = existing or _next_id(decisions)
        decisions[did] = {"about": about, "kind": kind, "question": one_line(item.get("question") or (old or {}).get("question"), 400),
                          "choice": choice, "note": str(item.get("note") or "").strip()[:2000], "by": by,
                          "at": item.get("at") or now_iso(), "replaces": old.get("choice") if old else None}
        changed.append(did)
    data["decisions"] = dict(sorted(decisions.items(), key=lambda kv: int(kv[0].split("-")[1])))
    write_json(_path(ws, program), data)
    render(ws, program, data)
    return changed


def _next_id(decisions):
    nums = [int(k.split("-")[1]) for k in decisions if re.match(r"^DEC-\d+$", k)]
    return f"DEC-{(max(nums) + 1) if nums else 1:03d}"


def render(ws, program, data=None):
    data = data or load(ws, program)
    rows = [[k, d["kind"], d["about"], d["choice"], d.get("note") or "", d.get("by") or "-", d.get("at", "")[:10]]
            for k, d in data["decisions"].items()]
    lines = [f"# Decisions: {program}", "",
             "What a person decided, in their words. The plan (`fuse-brief`) and the build (`fuse-build`) read these, and "
             "only a person changes them. Run `/app-fusion:fuse-review` to answer open questions or change an answer.", "",
             md_table(["Id", "Kind", "About", "Choice", "Note", "By", "When"], rows) if rows else "_No decisions yet._", ""]
    write_text(os.path.join(program_dir(ws, program), "DECISIONS.md"), "\n".join(lines))


def _brief_state(ws, program):
    try:
        from fusionlib.signatures import brief_approval
        return brief_approval(ws, program)["approved"]
    except Exception:  # noqa: BLE001  (a missing or broken sign-off file means: not approved)
        return False


def open_questions(ws, program):
    pdir = program_dir(ws, program)
    data = load(ws, program)
    decided = {(d["about"], d["kind"]) for d in data["decisions"].values()}
    caps = load_json(os.path.join(pdir, "capabilities.json")) or {}
    trace = load_json(os.path.join(pdir, "traceability.json")) or {}
    rules = load_json(os.path.join(pdir, "rules.json")) or {}
    platform = load_json(os.path.join(pdir, "platform.json")) or {}
    prog = load_json(os.path.join(pdir, "program.json")) or {}
    api = (load_json(os.path.join(pdir, "evidence", "api-parity.json")) or {}).get("capabilities") or {}
    apps = sorted(_apps(ws, program))
    names = {c["id"]: c["name"] for c in caps.get("capabilities", [])}
    out = []
    for c in caps.get("capabilities", []):
        if c["fusion"] == "shared-diverged" and (c["id"], "conflict") not in decided:
            out.append({"about": c["id"], "kind": "conflict", "priority": 1,
                        "question": f"{c['id']} {c['name']}: the apps do this differently. Which behavior does the new app keep?",
                        "detail": c.get("divergence") or [], "options": [f"take:{a}" for a in c.get("implementations", {})] + ["design", "both-by-role", "defer"]})
        if c["fusion"] == "new" and (c["id"], "scope") not in decided:
            out.append({"about": c["id"], "kind": "scope", "priority": 1,
                        "question": f"{c['id']} {c['name']} is in the design but in no legacy app. Is it in scope for the new app?",
                        "detail": [c.get("description") or ""] + [f"screen {s}" for s in (c.get("designScreens") or [])[:6]],
                        "options": ["in", "out", "defer"]})
    for cid, t in (trace.get("capabilities") or {}).items():
        if t.get("status") == "no-design" and (cid, "gap") not in decided:
            out.append({"about": cid, "kind": "gap", "priority": 2,
                        "question": f"{cid} {names.get(cid, cid)} has no screen in the new design. What happens to it?",
                        "options": ["design-it", "carry-as-is", "drop", "defer"]})
    for sid in (trace.get("gaps") or {}).get("screensWithoutCapability") or []:
        if (sid, "design") not in decided:
            out.append({"about": sid, "kind": "design", "priority": 3,
                        "question": f"Figma frame {sid} matches no legacy capability. Is it a new feature in scope?",
                        "options": ["in-scope", "out-of-scope", "new-spec"]})
    for r in rules.get("rules", []):
        # a P0 rule with any doubt blocks the plan; a P1/P2 rule with a suspected defect or a question is asked when
        # its capability is built (fuse-build's plan), or in `fuse-review <program> rules`
        doubt = r["confidence"] != "High" or r.get("suspectedDefect") or r.get("question")
        if doubt and (r["id"], "rule") not in decided and (r["priority"] == "P0" or r.get("suspectedDefect") or r.get("question")):
            out.append({"about": r["id"], "kind": "rule", "priority": 1 if r["priority"] == "P0" else 3, "capability": r.get("capability"),
                        "question": f"{r['id']} {r['name']} ({r['app']}, {r['source']}): {r.get('question') or r.get('suspectedDefect') or 'confirm the rule'}",
                        "detail": [f"Given {r['given']}", f"When {r['when']}", f"Then {r['then']}"],
                        "options": ["confirmed", "wrong", "discuss"]})
        if r["priority"] == "P0" and not r.get("capability") and (r["id"], "attach") not in decided:
            src = (r.get("source") or "").split(":")[0]
            near = [c["id"] for c in caps.get("capabilities", [])
                    if src and any(src == f.split(":")[0] for f in ((c.get("implementations") or {}).get(r["app"]) or {}).get("files") or [])]
            out.append({"about": r["id"], "kind": "attach", "priority": 2,
                        "question": f"{r['id']} {r['name']} ({r['app']}, {r['source']}) is a P0 rule no capability owns, so no "
                                    "proof checks it. Which capability does it belong to?",
                        "options": near[:3] + ["none"]})
    conflicts = rules.get("conflicts", [])
    if any(not c.get("key") for c in conflicts):  # rules.json from an older version
        conflicts = conflict_keys([dict(c) for c in conflicts])
    for conf in conflicts:
        ids = conf.get("rules") or []
        about = conf["key"]
        if (about, "conflict") not in decided:
            owners = sorted({r["app"] for r in rules.get("rules", []) if r["id"] in ids})
            owners = owners if len(owners) >= 2 else apps
            named = ", ".join(ids) if len(ids) >= 2 else "Two rules (" + (", ".join(ids + list(conf.get("unresolved") or [])) or "names not resolved") + ")"
            out.append({"about": about, "kind": "conflict", "priority": 1,
                        "question": f"{'Rules ' if len(ids) >= 2 else ''}{named} decide the same thing differently"
                                    + (f" in {conf['capability']} {names.get(conf['capability'], '')}" if conf.get("capability") else "")
                                    + f": {conf.get('difference')}",
                        "options": [f"take:{a}" for a in owners] + ["design", "new-spec", "defer"]})
    for cid, r in api.items():
        for missing in dict.fromkeys(re.sub(r" \((?:ios|android)\)$", "", m) for m in r.get("missing") or []):
            about = f"{cid}:{missing}"
            if (about, "api") not in decided:
                out.append({"about": about, "kind": "api", "priority": 2,
                            "question": f"{cid} {names.get(cid, '')}: the legacy app calls {missing}, the new code does not. Why?",
                            "options": ["replaced", "dropped", "accepted"]})
    for it in platform.get("items", []):
        if it.get("newApp") == "decide" and (it["id"], "platform") not in decided and len(it.get("apps") or {}) >= 1:
            out.append({"about": it["id"], "kind": "platform", "priority": 2 if it.get("area") in BLOCKING_PLATFORM_AREAS else 4,
                        "question": f"{it['id']} {it['name']} ({'; '.join(f'{a}: {v}' for a, v in it['apps'].items())}). Keep it in the new app?",
                        "options": ["keep", "drop", "decide-later"]})
    has_events = any((impl.get("events") for c in caps.get("capabilities", []) for impl in (c.get("implementations") or {}).values()))
    if has_events and ("analytics:taxonomy", "analytics") not in decided:
        out.append({"about": "analytics:taxonomy", "kind": "analytics", "priority": 2,
                    "question": "Do the legacy analytics event names stay (dashboards and funnels keep working), or does the new app "
                                "get a new event taxonomy (each rename listed in docs/fusion/analytics-map.json)?",
                    "options": ["keep-names", "new-taxonomy"]})
    # the stack and the store listing are recommended by the brief and settled when a person approves it
    approved = _brief_state(ws, program)
    target = (prog.get("target") or {}).get("stack")
    if target in (None, "", "undecided") and ("stack", "stack") not in decided:
        out.append({"about": "stack", "kind": "stack", "priority": 1 if approved else 3,
                    "question": "Which stack does the new app use?", "options": sorted(STACKS)})
    store = prog.get("storeIdentity")
    store_open = store in (None, "", "undecided") or (isinstance(store, dict) and (not store or "undecided" in store.values()))
    if store_open and ("continuity:store-identity", "continuity") not in decided:
        out.append({"about": "continuity:store-identity", "kind": "continuity", "priority": 1 if approved else 3,
                    "question": "Which store listing and bundle id does the new app ship under on each platform (an existing "
                                "app's, so its users update in place, or a new listing)? The answer may differ per platform.",
                    "options": []})
    out.sort(key=lambda q: (q["priority"], q["kind"], q["about"]))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("open")
    p.add_argument("program")
    p.add_argument("--json", action="store_true")
    p.add_argument("--workspace")
    p = sub.add_parser("add")
    p.add_argument("program")
    p.add_argument("--about", required=True)
    p.add_argument("--kind", required=True)
    p.add_argument("--choice", required=True)
    p.add_argument("--question")
    p.add_argument("--note")
    p.add_argument("--by")
    p.add_argument("--workspace")
    p = sub.add_parser("add-json")
    p.add_argument("program")
    p.add_argument("file")
    p.add_argument("--workspace")
    p = sub.add_parser("render")
    p.add_argument("program")
    p.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    if args.cmd == "open":
        qs = open_questions(ws, args.program)
        if args.json:
            print(json.dumps(qs, indent=2, ensure_ascii=False))
        else:
            counts = {}
            for q in qs:
                counts[q["kind"]] = counts.get(q["kind"], 0) + 1
            print(f"{len(qs)} open question(s)" + (": " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())) if qs else ""))
            for q in qs[:60]:
                print(f"  [{q['kind']}, priority {q['priority']}] {q['question']}")
    elif args.cmd == "add":
        ids = add(ws, args.program, [{"about": args.about, "kind": args.kind, "choice": args.choice, "question": args.question,
                                      "note": args.note, "by": args.by}])
        print(f"recorded {', '.join(ids)} -> analysis/{args.program}/DECISIONS.json, DECISIONS.md")
    elif args.cmd == "add-json":
        items = load_json(args.file)
        if not isinstance(items, list):
            die(f"{args.file} must hold a JSON list of decisions")
        ids = add(ws, args.program, items)
        print(f"recorded {len(ids)} decision(s): {', '.join(ids)}")
    else:
        render(ws, args.program)
        print(f"wrote analysis/{args.program}/DECISIONS.md")


if __name__ == "__main__":
    main()
