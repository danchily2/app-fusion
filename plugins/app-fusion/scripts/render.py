#!/usr/bin/env python3
"""Render workflow results into the program's catalogs, keeping every id stable across re-runs.

    python3 render.py capabilities <program> [--result FILE]   map_result.json (+ design/new_capabilities.json) -> capabilities.json,
                                                               capability_index.json (compact, for the workflows), CAPABILITIES.md
    python3 render.py rules <program> [--result FILE]          rules_result.json -> rules.json, BUSINESS_RULES.md, DATA_OBJECTS.md
    python3 render.py platform <program>                       inventories (+ map_result platformItems) -> platform.json, PLATFORM.md
    python3 render.py design <program>                         design/design.json -> DESIGN_INVENTORY.md
    python3 render.py overlap <program>                        inventories -> overlap.json (shared endpoints, copy, locales)

Ids never move: an existing CAP-/RULE-/PLT- id is kept for the entry with the same normalized key (see
docs/DESIGN.md), new entries are numbered after the highest id ever issued, and an id is never reused. Every value
comes from the input files; the text is escaped for Markdown tables. Standard library only.
"""

import argparse
import collections
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from decisions import conflict_keys  # noqa: E402
from fusionlib.common import (check_name, die, load_json, load_program, md_table, normalize_endpoint, now_iso,  # noqa: E402
                              one_line, program_dir, workspace, write_json, write_text)

FUSION = ["unique", "shared-same", "shared-diverged", "new"]
CATEGORIES = ["Calculation", "Validation", "Eligibility", "Lifecycle", "Policy", "Formatting"]
PRIORITY = {"P0": 0, "P1": 1, "P2": 2}


def norm(text):
    return " ".join(re.findall(r"[a-z0-9]+", str(text or "").lower()))


def next_id(prefix, used):
    nums = [int(m.group(1)) for u in used for m in [re.match(rf"^{prefix}-(\d+)$", u or "")] if m]
    return f"{prefix}-{(max(nums) + 1) if nums else 1:03d}"


# ---------------------------------------------------------------- capabilities

def evidence_tokens(impls):
    """What a capability's implementations cite, as comparable tokens: per app, each screen, file and endpoint."""
    toks = set()
    for app, impl in (impls or {}).items():
        if not isinstance(impl, dict):
            continue
        for kind in ("screens", "files", "endpoints"):
            for v in impl.get(kind) or []:
                v = str(v)
                if kind == "files":
                    v = v.split(":")[0]
                elif kind == "endpoints":
                    parts = v.split(None, 1)
                    path = normalize_endpoint(parts[-1]) or parts[-1]
                    v = f"{parts[0].upper() if len(parts) == 2 else '?'} {path}"
                toks.add(f"{app}|{kind}|{v.strip().lower()}")
    return toks


def references(ws, program, pdir, cid):
    """Where a capability id is still used: decisions, rules, design links, porting notes."""
    refs = []
    decisions = (load_json(os.path.join(pdir, "DECISIONS.json")) or {}).get("decisions") or {}
    refs += [f"{k} ({d.get('kind')})" for k, d in decisions.items()
             if (d.get("about") == cid or str(d.get("about") or "").startswith(cid + ":") or d.get("choice") == cid)
             and not (d.get("kind") == "gap" and d.get("choice") == "drop") and not (d.get("kind") == "scope" and d.get("choice") == "out")]
    refs += [r["id"] for r in (load_json(os.path.join(pdir, "rules.json")) or {}).get("rules", []) if r.get("capability") == cid]
    if any(cid in (l.get("capabilities") or []) for l in (load_json(os.path.join(pdir, "design", "trace_result.json")) or {}).get("links") or []):
        refs.append("design/trace_result.json")
    prog = load_json(os.path.join(pdir, "program.json")) or {}
    notes = os.path.join(ws, (prog.get("target") or {}).get("path") or f"new-app/{program}", "docs", "fusion", f"{cid}.md")
    if os.path.isfile(notes):
        refs.append(os.path.relpath(notes, ws))
    return refs


def render_capabilities(ws, program, result_path=None):
    pdir = program_dir(ws, program)
    result = load_json(result_path or os.path.join(pdir, "map_result.json"))
    if not result:
        die(f"{os.path.relpath(result_path or os.path.join(pdir, 'map_result.json'), ws)} not found: save the "
            "fuse-map-capabilities result there first")
    prog = load_program(ws, program)
    apps = [a["name"] for a in prog.get("apps", [])]
    previous = load_json(os.path.join(pdir, "capabilities.json")) or {}
    prev_caps = previous.get("capabilities", [])
    issued = set(previous.get("issuedIds") or []) | {c["id"] for c in prev_caps}
    by_key = {(norm(c["name"]), norm(c.get("domain"))): c["id"] for c in prev_caps}
    by_name = {}
    for c in prev_caps:
        by_name.setdefault(norm(c["name"]), []).append(c["id"])
    alias_file = load_json(os.path.join(pdir, "map_aliases.json")) or {}
    aliases = {norm(v): k for k, v in alias_file.items() if re.match(r"^CAP-\d+$", str(k)) and isinstance(v, str)}
    let_go = {k for k, v in alias_file.items() if v is None}

    design_only = load_json(os.path.join(pdir, "design", "new_capabilities.json")) or []
    raws = [r for r in list(result.get("capabilities", [])) + [
        {**d, "fusion": "new", "implementations": {}, "designScreens": [str(x) for x in d.get("screens") or []]}
        for d in design_only if isinstance(d, dict) and d.get("name")] if one_line(r.get("name"), 120)]
    # ids, in three passes: a person's alias, the same name, then the same evidence (a re-run renames freely)
    assigned, taken = {}, set()
    for i, raw in enumerate(raws):
        name = one_line(raw.get("name"), 120)
        cid = aliases.get(norm(name))
        if cid is None:
            key = (norm(name), norm(raw.get("domain")))
            cid = by_key.get(key) or (by_name[key[0]][0] if len(by_name.get(key[0], [])) == 1 else None)
        if cid and cid not in taken:
            assigned[i] = cid
            taken.add(cid)
    left = [c for c in prev_caps if c["id"] not in taken]
    pairs = []
    for i, raw in enumerate(raws):
        if i in assigned:
            continue
        mine = evidence_tokens(raw.get("implementations"))
        for c in left:
            theirs = evidence_tokens(c.get("implementations"))
            if mine and theirs:
                score = len(mine & theirs) / len(mine | theirs)
                if score >= 0.5:
                    pairs.append((score, i, c["id"]))
    for score, i, cid in sorted(pairs, key=lambda p: -p[0]):
        if i not in assigned and cid not in taken:
            assigned[i] = cid
            taken.add(cid)
    caps = []
    for i, raw in enumerate(raws):
        name = one_line(raw.get("name"), 120)
        cid = assigned.get(i) or next_id("CAP", issued | taken)
        taken.add(cid)
        impls = {}
        for app, impl in (raw.get("implementations") or {}).items():
            if app not in apps or not isinstance(impl, dict):
                continue
            impls[app] = {k: impl.get(k) or [] for k in ("screens", "files", "endpoints", "events", "strings", "storage", "platform")}
            impls[app]["evidence"] = impl.get("evidence") or ""
        fusion = raw.get("fusion")
        if fusion not in FUSION:
            products = {next((a.get("product") for a in prog["apps"] if a["name"] == app), app) for app in impls}
            fusion = "new" if not impls else ("unique" if len(products) == 1 else "shared-diverged")
        caps.append({
            "id": cid, "name": name, "domain": one_line(raw.get("domain") or "Other", 60),
            "personas": [one_line(p, 40) for p in raw.get("personas") or []],
            "description": one_line(raw.get("description"), 400), "fusion": fusion, "implementations": impls,
            "divergence": [one_line(d, 300) for d in raw.get("divergence") or []],
            "confidence": raw.get("confidence") if raw.get("confidence") in ("High", "Medium", "Low") else "Medium",
            "notes": one_line(raw.get("notes"), 400),
        })
        if raw.get("designScreens"):
            caps[-1]["designScreens"] = raw["designScreens"][:40]
    caps.sort(key=lambda c: int(c["id"].split("-")[1]))
    retired = []
    for c in prev_caps:
        if c["id"] not in taken and c["id"] not in let_go:
            refs = references(ws, program, pdir, c["id"])
            if refs:
                retired.append({"id": c["id"], "name": c["name"], "referencedBy": refs})
    name_to_id = {norm(c["name"]): c["id"] for c in caps}

    journeys, jissued = [], set(previous.get("issuedJourneyIds") or []) | {j["id"] for j in previous.get("journeys", [])}
    jprev = {norm(j["name"]): j["id"] for j in previous.get("journeys", [])}
    jby_caps = {(norm(j.get("persona")), tuple(x for st in j.get("steps", []) for x in st.get("capabilities", []))): j["id"]
                for j in previous.get("journeys", [])}
    jtaken = set()
    for raw in result.get("journeys", []):
        name = one_line(raw.get("name"), 120)
        if not name:
            continue
        steps = []
        for st in raw.get("steps") or []:
            ids = []
            for ref in st.get("capabilities") or []:
                ref_id = ref if re.match(r"^CAP-\d+$", str(ref)) and ref in taken else name_to_id.get(norm(ref))
                if ref_id and ref_id not in ids:
                    ids.append(ref_id)
            steps.append({"label": one_line(st.get("label"), 200), "capabilities": ids})
        jid = jprev.get(norm(name))
        if jid is None or jid in jtaken:
            jid = jby_caps.get((norm(raw.get("persona")), tuple(x for st in steps for x in st["capabilities"])))
        if jid is None or jid in jtaken:
            jid = next_id("JRN", jissued | jtaken)
        jtaken.add(jid)
        journeys.append({"id": jid, "name": name, "persona": one_line(raw.get("persona"), 40),
                         "description": one_line(raw.get("description"), 300), "steps": steps})
    journeys.sort(key=lambda j: int(j["id"].split("-")[1]))

    domains = []
    seen = set()
    for d in result.get("domains") or []:
        if norm(d.get("name")) and norm(d.get("name")) not in seen:
            seen.add(norm(d.get("name")))
            domains.append({"name": one_line(d.get("name"), 60), "description": one_line(d.get("description"), 300)})
    for c in caps:
        if norm(c["domain"]) not in seen:
            seen.add(norm(c["domain"]))
            domains.append({"name": c["domain"], "description": ""})

    out = {
        "program": program, "version": 1, "generated": now_iso(), "sources": apps, "domains": domains,
        "capabilities": caps, "journeys": journeys,
        "observations": [one_line(o, 400) for o in result.get("observations") or []],
        "rejected": [{"name": one_line(r.get("name"), 120), "why": one_line(r.get("why"), 300)} for r in result.get("rejected") or []],
        "issuedIds": sorted(issued | taken, key=lambda x: int(x.split("-")[1])),
        "issuedJourneyIds": sorted(jissued | jtaken, key=lambda x: int(x.split("-")[1])),
        "stats": result.get("stats") or {},
        "retired": retired,
    }
    write_json(os.path.join(pdir, "capabilities.json"), out)
    write_json(os.path.join(pdir, "capability_index.json"), {"program": program, "version": 1, "capabilities": [
        {"id": c["id"], "name": c["name"], "domain": c["domain"], "fusion": c["fusion"], "personas": c["personas"],
         "apps": sorted(c["implementations"]), "description": c["description"][:200]} for c in caps]})
    write_text(os.path.join(pdir, "CAPABILITIES.md"), capabilities_md(out, prog))
    counts = collections.Counter(c["fusion"] for c in caps)
    print(f"{len(caps)} capabilities ({', '.join(f'{counts[f]} {f}' for f in FUSION if counts[f])}), {len(journeys)} journeys, "
          f"{len(domains)} domains -> analysis/{program}/capabilities.json, CAPABILITIES.md")
    for r in retired:
        print(f"WARNING: {r['id']} ({r['name']}) is gone from the new map but still used by {', '.join(r['referencedBy'][:6])}. "
              f"If a capability of the new map is the same one, name it in analysis/{program}/map_aliases.json "
              f"({{\"{r['id']}\": \"<its name in map_result.json>\"}}) and render again.")
    return out


def capabilities_md(data, prog):
    apps = data["sources"]
    products = {a["name"]: a.get("product") or a["name"] for a in prog.get("apps", [])}
    caps = data["capabilities"]
    counts = collections.Counter(c["fusion"] for c in caps)
    lines = [f"# Capabilities: {data['program']}", "",
             f"{len(caps)} capabilities across {len(apps)} apps ({', '.join(f'{a} = {products[a]}' for a in apps)}), "
             f"generated {data['generated']}. Each capability is one thing a person can do. Its fusion class says what "
             "the new app must do with it:", "",
             "- **unique**: one product has it. Carry it over, or a person drops it.",
             "- **shared-same**: both products do it the same way. Build it once.",
             "- **shared-diverged**: both do it differently. A person decides which behavior survives (`fuse-review`).",
             "- **new**: only the design has it. It needs a spec before it can be built.", "",
             md_table(["Fusion class", "Capabilities"], [[f, counts[f]] for f in FUSION if counts[f]]), ""]
    by_domain = collections.OrderedDict()
    for d in data["domains"]:
        by_domain[d["name"]] = [c for c in caps if c["domain"] == d["name"]]
    lines += ["## Matrix", "", md_table(["Id", "Capability", "Domain", "Fusion"] + apps + ["Confidence"],
                                          [[c["id"], c["name"], c["domain"], c["fusion"]] +
                                           ["yes" if a in c["implementations"] else "" for a in apps] + [c["confidence"]]
                                           for c in caps]), ""]
    for domain, items in by_domain.items():
        if not items:
            continue
        desc = next((d["description"] for d in data["domains"] if d["name"] == domain), "")
        lines += [f"## {domain}", ""] + ([desc, ""] if desc else [])
        for c in items:
            lines += [f"### {c['id']}: {c['name']}", "",
                      f"**Fusion:** {c['fusion']} · **Personas:** {', '.join(c['personas']) or '-'} · **Confidence:** {c['confidence']}", "",
                      c["description"] or "_no description_", ""]
            for app, impl in c["implementations"].items():
                bits = []
                for key in ("screens", "endpoints", "events", "storage", "platform"):
                    vals = impl.get(key) or []
                    if vals:
                        bits.append(f"{key}: " + ", ".join(f"`{one_line(v, 80)}`" for v in vals[:8]) + (" …" if len(vals) > 8 else ""))
                lines.append(f"- **{app}** ({products.get(app, app)}): " + ("; ".join(bits) or "no detail") +
                             (f" · evidence `{one_line(impl.get('evidence'), 120)}`" if impl.get("evidence") else ""))
            if c["divergence"]:
                lines += ["", "**How they differ:**"] + [f"- {d}" for d in c["divergence"]]
            if c["notes"]:
                lines += ["", f"_Note: {c['notes']}_"]
            lines.append("")
    if data["journeys"]:
        lines += ["## Journeys", ""]
        for j in data["journeys"]:
            lines += [f"### {j['id']}: {j['name']}", "", f"**Persona:** {j['persona'] or '-'}. {j['description']}", ""]
            lines += [f"{i}. {st['label']} ({', '.join(st['capabilities']) or 'no capability matched'})"
                      for i, st in enumerate(j["steps"], 1)] + [""]
    if data.get("retired"):
        lines += ["## Retired ids still in use", "",
                  "These capabilities are not in the new map, but decisions, rules, design links or porting notes still name "
                  "them. When a capability of the new map is the same one, name it in `map_aliases.json` and render again, "
                  "so everything attached to the old id stays attached:", ""]
        lines += [f"- **{r['id']}** {r['name']}: {', '.join(r['referencedBy'][:8])}" for r in data["retired"]] + [""]
    if data["observations"]:
        lines += ["## Observations", ""] + [f"- {o}" for o in data["observations"]] + [""]
    if data["rejected"]:
        lines += ["## Rejected by the referees", "", "Candidates a second agent could not confirm from the cited code:", ""]
        lines += [f"- {r['name']}: {r['why']}" for r in data["rejected"][:40]] + [""]
    return "\n".join(lines)


# ---------------------------------------------------------------- rules

def render_rules(ws, program, result_path=None):
    pdir = program_dir(ws, program)
    result = load_json(result_path or os.path.join(pdir, "rules_result.json"))
    if not result:
        die(f"analysis/{program}/rules_result.json not found: save the fuse-extract-rules result there first")
    previous = load_json(os.path.join(pdir, "rules.json")) or {}
    issued = set(previous.get("issuedIds") or []) | {r["id"] for r in previous.get("rules", [])}
    prev_key = {(r.get("app"), (r.get("source") or "").split(":")[0], norm(r.get("name"))): r["id"] for r in previous.get("rules", [])}
    caps = {c["id"] for c in (load_json(os.path.join(pdir, "capabilities.json")) or {}).get("capabilities", [])}
    decisions = (load_json(os.path.join(pdir, "DECISIONS.json")) or {}).get("decisions") or {}
    attach = {d["about"]: d["choice"] for d in decisions.values() if d.get("kind") == "attach"}
    # a rule no referee could check is kept, at Low confidence and with a question, so it is never silently lost
    unverified = [{**r, "confidence": "Low", "question": r.get("question") or
                   f"No referee could check this rule ({one_line(r.get('why') or 'no verdict', 80)}): confirm it against the code."}
                  for r in result.get("unverified") or [] if isinstance(r, dict) and r.get("name")]
    raw_rules = sorted((result.get("rules") or []) + unverified, key=lambda r: (
        CATEGORIES.index(r.get("category")) if r.get("category") in CATEGORIES else 99,
        PRIORITY.get(r.get("priority"), 3), str(r.get("app")), str(r.get("source"))))
    aliases = {}
    for old_id, name in (load_json(os.path.join(pdir, "rules_aliases.json")) or {}).items():
        if re.match(r"^RULE-\d+$", str(old_id)):
            aliases[old_id] = norm(name) if isinstance(name, str) else None
    by_alias = {n: rid for rid, n in aliases.items() if n}

    def span(source):
        """(file, first line, last line) of a 'path:12-30' citation."""
        path, _, lines = str(source or "").partition(":")
        m = re.match(r"^(\d+)(?:-(\d+))?", lines)
        return path, (int(m.group(1)) if m else 0), (int(m.group(2) or m.group(1)) if m else 0)

    # ids, in three passes: a person's alias, the same app, file and name, then the same app and file with overlapping
    # lines (a re-run rewords rule names freely)
    assigned, taken = {}, set()
    for i, r in enumerate(raw_rules):
        rid = by_alias.get(norm(r.get("name"))) or prev_key.get((r.get("app"), (r.get("source") or "").split(":")[0], norm(r.get("name"))))
        if rid and rid not in taken:
            assigned[i] = rid
            taken.add(rid)
    pairs = []
    for i, r in enumerate(raw_rules):
        if i in assigned:
            continue
        f, a1, a2 = span(r.get("source"))
        for old in previous.get("rules", []):
            if old["id"] in taken or old.get("app") != r.get("app"):
                continue
            g, b1, b2 = span(old.get("source"))
            if f and f == g and a1 and b1:
                overlap = min(a2, b2) - max(a1, b1) + 1
                if overlap > 0:
                    pairs.append((overlap / (max(a2, b2) - min(a1, b1) + 1), i, old["id"]))
    for score, i, rid in sorted(pairs, key=lambda p: -p[0]):
        if score >= 0.5 and i not in assigned and rid not in taken:
            assigned[i] = rid
            taken.add(rid)
    rules = []
    for i, r in enumerate(raw_rules):
        rid = assigned.get(i) or next_id("RULE", issued | taken)
        taken.add(rid)
        cap = r.get("capability") if r.get("capability") in caps else None
        if attach.get(rid) in caps:
            cap = attach[rid]
        rules.append({
            "id": rid, "name": one_line(r.get("name"), 120), "app": r.get("app"), "capability": cap,
            "category": r.get("category") if r.get("category") in CATEGORIES else "Policy",
            "priority": r.get("priority") if r.get("priority") in PRIORITY else "P1",
            "source": one_line(r.get("source"), 200), "plainEnglish": one_line(r.get("plainEnglish"), 400),
            "given": one_line(r.get("given"), 400), "when": one_line(r.get("when"), 400), "then": one_line(r.get("then"), 400),
            "parameters": one_line(r.get("parameters"), 400), "edgeCases": one_line(r.get("edgeCases"), 400),
            "suspectedDefect": one_line(r.get("suspectedDefect"), 400),
            "confidence": r.get("confidence") if r.get("confidence") in ("High", "Medium", "Low") else "Medium",
            "question": one_line(r.get("question"), 400),
        })
    name_to_id = {(r["app"], norm(r["name"])): r["id"] for r in rules}

    def resolve(ref, capability):
        """A conflict names its rules by (app, name); the finder may paraphrase, so fall back to the closest name of
        the same app in the same capability (word overlap of at least 0.6)."""
        app, name = (ref.get("app"), ref.get("name")) if isinstance(ref, dict) else (None, ref)
        if not isinstance(ref, dict) and ref in taken:
            return ref
        exact = name_to_id.get((app, norm(name))) if app else next((v for (a, n), v in name_to_id.items() if n == norm(name)), None)
        if exact:
            return exact
        words = set(norm(name).split())
        best, score = None, 0.0
        for r in rules:
            if (app and r["app"] != app) or (capability and r["capability"] not in (capability, None)):
                continue
            other = set(norm(r["name"]).split())
            s_ = len(words & other) / len(words | other) if words | other else 0
            if s_ > score:
                best, score = r["id"], s_
        return best if score >= 0.6 else None

    conflicts = []
    for c in result.get("conflicts") or []:
        capability = c.get("capability") if c.get("capability") in caps else None
        ids, unresolved = [], []
        for ref in c.get("rules") or []:
            rid = resolve(ref, capability)
            if rid and rid not in ids:
                ids.append(rid)
            elif not rid:
                unresolved.append(one_line(f"{ref.get('app')}: {ref.get('name')}" if isinstance(ref, dict) else ref, 160))
        conflicts.append({"capability": capability, "rules": ids, "unresolved": unresolved, "difference": one_line(c.get("difference"), 400)})
    conflict_keys(conflicts)
    decisions_all = (load_json(os.path.join(pdir, "DECISIONS.json")) or {}).get("decisions") or {}
    retired = []
    for old in previous.get("rules", []):
        if old["id"] in taken or (old["id"] in aliases and aliases[old["id"]] is None):
            continue
        refs = [f"{k} ({d.get('kind')})" for k, d in decisions_all.items()
                if d.get("about") == old["id"] or old["id"] in re.findall(r"RULE-\d+", str(d.get("about") or ""))]
        if refs:
            retired.append({"id": old["id"], "name": old.get("name"), "app": old.get("app"), "referencedBy": refs})
    out = {"program": program, "version": 1, "generated": now_iso(), "rules": rules, "conflicts": conflicts, "retired": retired,
           "dataObjects": result.get("dataObjects") or [],
           "issuedIds": sorted(issued | taken, key=lambda x: int(x.split("-")[1])),
           "stats": result.get("stats") or {}, "injectionFlags": result.get("injectionFlags") or [],
           "rejectedCount": len(result.get("rejected") or []), "rerunShards": result.get("rerunShards") or []}
    write_json(os.path.join(pdir, "rules.json"), out)
    write_text(os.path.join(pdir, "BUSINESS_RULES.md"), rules_md(out, result))
    write_text(os.path.join(pdir, "DATA_OBJECTS.md"), data_objects_md(out))
    for r in retired:
        print(f"WARNING: {r['id']} ({r['name']}) is gone from the new rules but decisions still name it: "
              f"{', '.join(r['referencedBy'][:6])}. If a rule of the new result is the same one, name it in "
              f"analysis/{program}/rules_aliases.json ({{\"{r['id']}\": \"<its name in rules_result.json>\"}}), or map it to "
              "null to let it go, and render again.")
    by_priority = collections.Counter(r["priority"] for r in rules)
    doubt = [r for r in rules if r["confidence"] != "High" or r["suspectedDefect"] or r["question"]]
    flagged = collections.Counter(r["priority"] for r in doubt)
    print(f"{len(rules)} rules ({', '.join(f'{by_priority[p]} {p}' for p in PRIORITY if by_priority[p])}; "
          f"{len(unverified)} kept unverified), {len(doubt)} flagged for a person "
          f"({', '.join(f'{flagged[p]} {p}' for p in PRIORITY if flagged[p]) or 'none'}), "
          f"{sum(1 for r in rules if r['suspectedDefect'])} with a suspected defect, {len(conflicts)} cross-app conflicts, "
          f"{sum(1 for r in rules if not r['capability'])} without a capability "
          f"-> analysis/{program}/BUSINESS_RULES.md, DATA_OBJECTS.md, rules.json")
    return out


def rules_md(data, result):
    rules = data["rules"]
    lines = [f"# Business rules: {data['program']}", "",
             f"{len(rules)} rules mined from the source apps, generated {data['generated']}. Each card cites the code "
             "it comes from (`file:line` under `legacy/<app>`), and a second agent checked every citation. "
             f"{data.get('rejectedCount', 0)} candidates were rejected by that check.", "",
             md_table(["Id", "Rule", "App", "Capability", "Category", "Priority", "Confidence", "Source"],
                      [[r["id"], r["name"], r["app"], r["capability"] or "-", r["category"], r["priority"], r["confidence"],
                        r["source"]] for r in rules]), ""]
    if data["conflicts"]:
        lines += ["## Cross-app conflicts", "",
                  "The same decision is made differently by two apps. A person picks the behavior the new app keeps "
                  "(`/app-fusion:fuse-review`).", "",
                  md_table(["Question", "Capability", "Rules", "Difference"],
                           [[c.get("key") or "-", c["capability"] or "-",
                             ", ".join(c["rules"] + [f"(not resolved: {u})" for u in c.get("unresolved") or []]) or "-",
                             c["difference"]] for c in data["conflicts"]]), ""]
    for cat in CATEGORIES:
        items = [r for r in rules if r["category"] == cat]
        if not items:
            continue
        lines += [f"## {cat}", ""]
        for r in items:
            lines += [f"### {r['id']}: {r['name']}",
                      f"**App:** {r['app']}", f"**Capability:** {r['capability'] or '-'}", f"**Category:** {r['category']}",
                      f"**Priority:** {r['priority']}", f"**Source:** `{r['source']}`",
                      f"**Plain English:** {r['plainEnglish']}", "**Specification:**",
                      f"  Given {r['given']}", f"  When  {r['when']}", f"  Then  {r['then']}"]
            if r["parameters"]:
                lines.append(f"**Parameters:** {r['parameters']}")
            if r["edgeCases"]:
                lines.append(f"**Edge cases handled:** {r['edgeCases']}")
            if r["suspectedDefect"]:
                lines.append(f"**Suspected defect:** {r['suspectedDefect']}")
            lines.append(f"**Confidence:** {r['confidence']}" + (f": {r['question']}" if r["question"] else ""))
            lines.append("")
    asks = [r for r in rules if r["confidence"] != "High" or r["question"]]
    if asks:
        lines += ["## Rules requiring SME confirmation", ""]
        lines += [f"- **{r['id']}** ({r['priority']}, {r['app']}): {r['question'] or 'confidence ' + r['confidence']}" for r in asks] + [""]
    if data.get("injectionFlags"):
        lines += ["## Instruction-shaped text found in the code", "",
                  "These lines look aimed at manipulating automated analysis. They were treated as data:", ""]
        lines += [f"- `{one_line(f, 200)}`" for f in data["injectionFlags"]] + [""]
    if data.get("rerunShards"):
        lines += ["## Coverage gaps", "", "These shards returned no verified result and can be re-run: " +
                  ", ".join(f"`{s}`" for s in data["rerunShards"]), ""]
    return "\n".join(lines)


def data_objects_md(data):
    objs = data.get("dataObjects") or []
    lines = [f"# Data objects: {data['program']}", "", f"{len(objs)} core records the apps hold or exchange.", ""]
    for o in objs:
        lines += [f"## {one_line(o.get('name'), 80)} ({one_line(o.get('app'), 40)})", "",
                  f"Where: `{one_line(o.get('location'), 160)}`. Used by: {', '.join(o.get('usedBy') or []) or '-'}.", ""]
        fields = o.get("fields") or []
        if fields:
            lines += [md_table(["Field", "Type", "Notes"], [[f.get("name"), f.get("type"), f.get("notes", "")] for f in fields]), ""]
    return "\n".join(lines)


# ---------------------------------------------------------------- platform matrix

# Third-party SDKs worth a keep-or-drop decision, matched against dependency names and (Swift packages) repository URLs.
SDKS = [
    ("analytics", "Firebase Analytics", ("@react-native-firebase/analytics", "firebaseanalytics", "firebase-analytics")),
    ("analytics", "Firebase iOS SDK (which products are used is not visible in Package.resolved)", ("firebase-ios-sdk",)),
    ("analytics", "Snowplow", ("snowplow",)),
    ("analytics", "Amplitude", ("amplitude",)),
    ("analytics", "Mixpanel", ("mixpanel",)),
    ("crash", "Sentry", ("sentry",)),
    ("crash", "Crashlytics", ("crashlytics",)),
    ("crash", "App Center", ("appcenter",)),
    ("flags", "Firebase Remote Config", ("remote-config", "remoteconfig")),
    ("flags", "LaunchDarkly", ("launchdarkly",)),
    ("flags", "Unleash", ("unleash",)),
    ("surveys", "Survicate", ("survicate",)),
    ("surveys", "Wootric / InMoment", ("wootric",)),
    ("messaging", "Firebase In-App Messaging", ("in-app-messaging", "inappmessaging")),
    ("push", "Firebase Cloud Messaging", ("@react-native-firebase/messaging", "firebasemessaging")),
    ("push", "Notifee", ("notifee",)),
    ("maps", "Google Maps", ("google-maps", "googlemaps", "react-native-maps")),
    ("auth", "OAuth (AppAuth)", ("react-native-app-auth", "appauth")),
    ("auth", "MSAL", ("msal",)),
    ("storage", "Realm", ("realm",)),
    ("storage", "MMKV", ("mmkv",)),
    ("graphql", "Apollo GraphQL", ("@apollo/client", "apollo-ios")),
    ("ui", "Lottie", ("lottie",)),
]


def platform_items(prog, invs):
    items = []

    def add(area, name, per_app, recommendation="decide"):
        if any(per_app.values()):
            items.append({"area": area, "name": name, "apps": {a: v for a, v in per_app.items() if v}, "newApp": recommendation})

    apps = [a["name"] for a in prog.get("apps", [])]
    get = lambda a, k: ((invs.get(a) or {}).get("platform") or {}).get(k)
    add("identity", "Bundle / application ids", {a: ", ".join(get(a, "bundleIds") or []) for a in apps}, "decide")
    add("identity", "Minimum OS", {a: ", ".join(f"{k} {v}" for k, v in (get(a, "minOS") or {}).items()) for a in apps}, "decide")
    add("push", "Push notifications", {a: "yes" if get(a, "push") else "" for a in apps}, "required")
    add("push", "Notification categories and channels",
        {a: ", ".join(f"{c.get('kind')}:{c.get('id')}" for c in get(a, "notificationCategories") or []) for a in apps}, "required")
    add("links", "Universal / app links", {a: ", ".join((get(a, "associatedDomains") or []) + (get(a, "appLinkHosts") or [])) for a in apps}, "required")
    add("links", "Custom URL schemes", {a: ", ".join(get(a, "urlSchemes") or []) for a in apps}, "required")
    kinds = sorted({x.get("type") for a in apps for x in get(a, "extensions") or []})
    for kind in kinds:
        add("extensions", f"App extension: {kind}", {a: ", ".join(x.get("plist", "") for x in get(a, "extensions") or [] if x.get("type") == kind) for a in apps})
    add("background", "Background modes", {a: ", ".join(get(a, "backgroundModes") or []) for a in apps})
    perms = sorted({p["key"] for a in apps for p in get(a, "permissions") or []})
    for key in perms:
        add("permissions", f"Permission: {key}", {a: "yes" if any(p["key"] == key for p in get(a, "permissions") or []) else "" for a in apps})
    add("sharing", "App groups", {a: ", ".join(get(a, "appGroups") or []) for a in apps}, "decide")
    add("sharing", "Keychain access groups", {a: ", ".join(get(a, "keychainGroups") or []) for a in apps}, "decide")
    add("security", "ATS exceptions / cleartext traffic", {a: ", ".join((get(a, "atsExceptions") or []) + (get(a, "cleartext") or [])) for a in apps})
    add("privacy", "Privacy manifest", {a: ", ".join(get(a, "privacyManifest") or []) for a in apps}, "required")
    add("flags", "Remote-config flags", {a: f"{len(get(a, 'flags') or [])} keys" if get(a, "flags") else "" for a in apps})
    for a in apps:
        inv = invs.get(a) or {}
        deps = [((d.get("name") or "").lower(), (d.get("url") or "").lower(), d) for d in inv.get("dependencies") or []]
        for area, label, needles in SDKS:
            hits = [d for name, url, d in deps if any(n in name or (url and n in url) for n in needles)]
            if hits:
                items.append({"area": area, "name": label, "apps": {a: ", ".join(sorted({f"{h['name']} {h.get('version') or ''}".strip() for h in hits}))},
                              "newApp": "decide"})
        kinds_used = sorted({s.get("kind") for s in inv.get("storage") or []})
        if kinds_used:
            items.append({"area": "storage", "name": "Local storage", "apps": {a: ", ".join(kinds_used)}, "newApp": "decide"})
        s = inv.get("strings") or {}
        if s.get("locales"):
            items.append({"area": "i18n", "name": "Locales", "apps": {a: ", ".join(s["locales"])}, "newApp": "required"})
    merged = collections.OrderedDict()
    for it in items:
        key = (it["area"], norm(it["name"]))
        if key in merged:
            merged[key]["apps"].update(it["apps"])
        else:
            merged[key] = {**it, "apps": dict(it["apps"])}
    return list(merged.values())


def render_platform(ws, program):
    pdir = program_dir(ws, program)
    prog = load_program(ws, program)
    invs = {a["name"]: load_json(os.path.join(pdir, "apps", a["name"], "inventory.json")) for a in prog.get("apps", [])}
    missing = [a for a, inv in invs.items() if not inv]
    if missing:
        die(f"no inventory for {', '.join(missing)}: run /app-fusion:fuse-assess {program} first")
    items = platform_items(prog, invs)
    extra = (load_json(os.path.join(pdir, "map_result.json")) or {}).get("platformItems") or []
    for it in extra:
        if it.get("area") and it.get("name"):
            items.append({"area": one_line(it["area"], 30), "name": one_line(it["name"], 120),
                          "apps": {k: one_line(v, 200) for k, v in (it.get("apps") or {}).items()},
                          "newApp": it.get("recommendation") if it.get("recommendation") in ("required", "decide", "drop") else "decide",
                          "note": one_line(it.get("note"), 300)})
    previous = load_json(os.path.join(pdir, "platform.json")) or {}
    issued = set(previous.get("issuedIds") or []) | {i["id"] for i in previous.get("items", [])}
    prev_key = {(i["area"], norm(i["name"])): i for i in previous.get("items", [])}
    decisions = (load_json(os.path.join(pdir, "DECISIONS.json")) or {}).get("decisions") or {}
    out_items, taken = [], set()
    for it in items:
        key = (it["area"], norm(it["name"]))
        if any((o["area"], norm(o["name"])) == key for o in out_items):
            continue
        old = prev_key.get(key)
        pid = old["id"] if old and old["id"] not in taken else next_id("PLT", issued | taken)
        taken.add(pid)
        dec = next((d for d_id, d in sorted(decisions.items()) if d.get("about") == pid and d.get("kind") == "platform"), None)
        out_items.append({"id": pid, **it, "decision": dec.get("choice") if dec else None})
    out = {"program": program, "version": 1, "generated": now_iso(), "items": out_items,
           "issuedIds": sorted(issued | taken, key=lambda x: int(x.split("-")[1]))}
    write_json(os.path.join(pdir, "platform.json"), out)
    apps = [a["name"] for a in prog.get("apps", [])]
    lines = [f"# Platform matrix: {program}", "",
             "What each app relies on from the operating system and its SDKs, from the inventories and the map. "
             "`New app` is the default recommendation: **required** means the new app must keep it for existing "
             "users (links, push, locales, privacy), and **decide** means a person chooses in `fuse-review`.", "",
             md_table(["Id", "Area", "Item"] + apps + ["New app", "Decision"],
                      [[i["id"], i["area"], i["name"]] + [i["apps"].get(a, "") for a in apps] + [i["newApp"], i["decision"] or "-"]
                       for i in out_items]), ""]
    write_text(os.path.join(pdir, "PLATFORM.md"), "\n".join(lines))
    print(f"{len(out_items)} platform items -> analysis/{program}/platform.json, PLATFORM.md")
    return out


# ---------------------------------------------------------------- design inventory

def render_design(ws, program):
    pdir = program_dir(ws, program)
    design = load_json(os.path.join(pdir, "design", "design.json"))
    if not design:
        die(f"analysis/{program}/design/design.json not found: run /app-fusion:fuse-design {program} first")
    screens = design.get("screens") or []
    kinds = collections.Counter(s.get("kind") for s in screens)
    lines = [f"# Design inventory: {program}", "",
             f"{len(screens)} frames from {len(design.get('files') or [])} Figma file(s), read through the {design.get('source', 'mcp')} path. "
             f"Figma calls spent: {design.get('budget', {}).get('used', 0)} of a {design.get('budget', {}).get('limit', 0)} budget.", "",
             md_table(["Kind", "Frames"], kinds.most_common()), ""]
    for f in design.get("files") or []:
        pages = f.get("pages") or []
        lines += [f"## {one_line(f.get('name'), 80)}", "", f"`{f.get('fileKey')}` · {f.get('url', '')}", "",
                  md_table(["Page", "In scope", "Frames"], [[p.get("name"), "yes" if p.get("inScope") else "no",
                                                            sum(1 for s in screens if s.get("fileKey") == f.get("fileKey") and s.get("page") == p.get("name"))]
                                                           for p in pages]), ""]
    shown = [s for s in screens if s.get("kind") in ("screen", "state")]
    if shown:
        lines += ["## Screens", "", md_table(["Id", "Name", "Page / section", "Size", "Shot", "Texts"],
                                             [[s["id"], s.get("name"), f"{s.get('page', '')} / {s.get('section', '') or '-'}",
                                               f"{s.get('width', 0)}×{s.get('height', 0)}", "yes" if s.get("shot") else "no",
                                               len(s.get("texts") or [])] for s in shown]), ""]
    tokens = design.get("tokens") or {}
    if any(tokens.values()):
        lines += ["## Tokens", ""]
        for group, values in tokens.items():
            if values:
                lines += [f"**{group}** ({len(values)}): " + ", ".join(f"`{k}` {one_line(v, 40)}" for k, v in list(values.items())[:40]), ""]
    comps = design.get("components") or []
    if comps:
        lines += ["## Components used", "", md_table(["Component", "Library", "Instances"],
                                                     [[c.get("name"), c.get("library", ""), c.get("instances", 0)] for c in comps[:80]]), ""]
    if design.get("notCaptured"):
        lines += ["## Not captured", "", "Frames the budget or an error left out; `fuse-design` resumes from the cache:", ""]
        lines += [f"- `{n.get('id')}`: {n.get('why')}" for n in design["notCaptured"][:60]] + [""]
    write_text(os.path.join(pdir, "DESIGN_INVENTORY.md"), "\n".join(lines))
    print(f"{len(screens)} frames ({', '.join(f'{v} {k}' for k, v in kinds.most_common())}) -> analysis/{program}/DESIGN_INVENTORY.md")


# ---------------------------------------------------------------- overlap

def render_overlap(ws, program):
    """Deterministic overlap between the apps before any agent runs: shared backend endpoints, shared UI copy, and
    the locales each app ships. A first signal of how much of the fusion is merging and how much is carrying over."""
    from fusionlib.common import endpoints_match
    from fusionlib.strings import base_locale
    pdir = program_dir(ws, program)
    prog = load_program(ws, program)
    apps = [a["name"] for a in prog.get("apps", [])]
    invs = {a: load_json(os.path.join(pdir, "apps", a, "inventory.json")) or {} for a in apps}
    strs = {a: load_json(os.path.join(pdir, "apps", a, "strings.json")) or {} for a in apps}
    pairs = []
    for i, a in enumerate(apps):
        for b in apps[i + 1:]:
            ea = sorted({(e.get("method"), e["path"]) for e in invs[a].get("endpoints", [])}, key=lambda x: x[1])
            eb = sorted({(e.get("method"), e["path"]) for e in invs[b].get("endpoints", [])}, key=lambda x: x[1])
            shared = []
            for m1, p1 in ea:
                hit = next(((m2, p2) for m2, p2 in eb if endpoints_match(p1, p2) and (m1 is None or m2 is None or m1 == m2)), None)
                if hit:
                    shared.append({a: f"{m1 or '?'} {p1}", b: f"{hit[0] or '?'} {hit[1]}"})
            va = {norm(v) for v in (strs[a].get("values") or {}).values() if len(norm(v)) >= 4}
            vb = {norm(v) for v in (strs[b].get("values") or {}).values() if len(norm(v)) >= 4}
            la = {base_locale(l) for l in strs[a].get("locales") or []}
            lb = {base_locale(l) for l in strs[b].get("locales") or []}
            pairs.append({"apps": [a, b], "sharedEndpoints": shared,
                          "endpointCounts": {a: len({p for _, p in ea}), b: len({p for _, p in eb})},
                          "sharedCopy": len(va & vb), "copyCounts": {a: len(va), b: len(vb)},
                          "locales": {"both": sorted(la & lb), f"only {a}": sorted(la - lb), f"only {b}": sorted(lb - la)}})
    out = {"program": program, "version": 1, "generated": now_iso(), "pairs": pairs,
           "rules": {"sharedEndpoints": "endpoint pairs whose normalized paths match by segment suffix ({} matches any segment) and whose methods agree",
                     "sharedCopy": "distinct source-locale string values (normalized, at least 4 characters) present in both apps",
                     "locales": "compared by language (nb-NO, nb and no are one)"}}
    write_json(os.path.join(pdir, "overlap.json"), out)
    for p in pairs:
        a, b = p["apps"]
        print(f"{a} x {b}: {len(p['sharedEndpoints'])} shared endpoint(s) ({p['endpointCounts'][a]} / {p['endpointCounts'][b]}), "
              f"{p['sharedCopy']} shared UI strings, locales both {','.join(p['locales']['both']) or '-'}; "
              f"only {a}: {','.join(p['locales'][f'only {a}']) or '-'}; only {b}: {','.join(p['locales'][f'only {b}']) or '-'}")
    print(f"-> analysis/{program}/overlap.json")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("kind", choices=["capabilities", "rules", "platform", "design", "overlap"])
    ap.add_argument("program")
    ap.add_argument("--result")
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    if args.kind == "capabilities":
        render_capabilities(ws, args.program, args.result)
    elif args.kind == "rules":
        render_rules(ws, args.program, args.result)
    elif args.kind == "platform":
        render_platform(ws, args.program)
    elif args.kind == "overlap":
        render_overlap(ws, args.program)
    else:
        render_design(ws, args.program)


if __name__ == "__main__":
    main()
