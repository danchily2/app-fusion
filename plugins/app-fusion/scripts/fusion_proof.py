#!/usr/bin/env python3
"""Independent proof: one verdict per built capability, computed from evidence files by fixed rules.

    python3 fusion_proof.py <program> [CAP-NNN ...] [--workspace DIR]

Writes analysis/<program>/VERIFICATION.md (for people) and VERIFICATION.json (for the report and fuse-status). A model
never gives the verdict: this script does, from files it parses itself, and every rule is written into the output.
Every run judges every built capability (a verdict kept from an earlier run could hide a change in a shared catalog, a
decision or another capability's code); the ids given only choose what is printed and the exit code. A result is fresh for a capability while the files its porting notes name still
hash to the value recorded with the result; file times never count.

  1 Built           new-app/<program>/docs/fusion/CAP-NNN.md names at least one source file inside the new app (for a
                    native pair, one in each half: ios/ and android/).
  2 Tests ran       a recorded suite whose result files are unchanged since they were recorded, run on the
                    capability's current code, has tests naming the capability (CAP-012, cap012) or its rules; at least
                    one executed and none failed. A result recorded before the code changed is a gap; a result file
                    edited after it was recorded is a failure. A count typed anywhere counts for nothing.
  3 Rules traced    every P0 and P1 rule of the capability is named by a test that passed in such a fresh suite. Left
                    out: a rule a person marked `wrong`, and the rules of an app a person did not keep (`take:<app>` for
                    the capability or for a rule conflict). A gap: a rule under `discuss`; a rule with a suspected legacy
                    defect (or a P0 rule with an open question) that no person has confirmed or marked wrong; an
                    undecided conflict; a behavior a person chose to redesign (`design`, `new-spec`) without a passing
                    test naming that DEC id.
  4 Journeys        every journey through the capability passed on every target platform, in a Maestro (or other UI)
                    result that names the journey (JRN-NNN), recorded after the current code of every capability on
                    it and with the flow unchanged. A journey through a capability that is not built yet is a gap.
  5 API parity      evidence/api-parity.json passes (or is n/a) for the capability, and nothing it read changed since.
  6 Strings         evidence/i18n-parity.json likewise.
  7 Analytics       evidence/events-parity.json likewise.
  8 Design text     evidence/design-text.json likewise.
  9 Canary          scripts/canary.py broke the capability's code on purpose and restored it; a test naming the
                    capability or one of its rules failed under the break and passed in a fresh suite, and the code is
                    unchanged since. A break nothing caught is a failure; a canary still in place is a gap.
 10 Legacy          every legacy/<app> is still a clean git checkout (untracked files count) at the commit recorded in
                    program.json. A change is a failure; a moved commit is a gap (the analysis describes the old one).

  PROVEN        all ten checks pass (n/a counts as a pass: a check that has nothing to compare, confirmed by the
                capability's own legacy files, or excused by a person's decision).
  NOT PROVEN    any check failed.
  PARTLY PROVEN nothing failed, but a check could not pass; each such check is listed with its reason.

Platform continuity is judged once for the app (evidence/platform-parity.json, from scripts/platform_parity.py) and
shown beside the verdicts. Visual conformance is never computed: a named person signs it, and the proof, with
scripts/signoff.py. Exit 0 when every judged capability is PROVEN, 1 otherwise. Standard library only.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import canary as canarymod  # noqa: E402
import decisions as decmod  # noqa: E402
import workspace as wsmod  # noqa: E402
from fusionlib import newapp, proofkit  # noqa: E402
from fusionlib import signatures as signoff  # noqa: E402
from fusionlib.status import script as runner  # noqa: E402
from fusionlib.common import (check_name, die, load_json, md_table, now_iso, one_line, program_dir, workspace,  # noqa: E402
                              write_json, write_text)

CHECKS = ["Built", "Tests ran", "Rules traced", "Journeys", "API parity", "Strings", "Analytics", "Design text", "Canary",
          "Legacy untouched"]
PARITY = [("API parity", "api-parity.json", "api_parity.py"), ("Strings", "i18n-parity.json", "i18n_parity.py"),
          ("Analytics", "events-parity.json", "events_parity.py"), ("Design text", "design-text.json", "design_text.py")]


def entry_state(ws, e):
    """'ok', 'old' (recorded by an earlier version, no hashes) or 'tampered' (a result file changed or is gone)."""
    if "hashes" not in e:
        return "old"
    return "tampered" if proofkit.changed_inputs(ws, e["hashes"]) else "ok"


def fresh_for(e, cid, current):
    return current is not None and (e.get("codeHashes") or {}).get(cid) == current


class Evidence:
    """test-runs.json, parsed once."""

    def __init__(self, ws, program):
        self.ws = ws
        self.runs = load_json(os.path.join(program_dir(ws, program), "evidence", "test-runs.json")) or {}
        self.suites = []
        for e in self.runs.get("suites") or []:
            cases, _ = proofkit.junit_cases(proofkit.xml_files(e.get("junit"), ws), ws)
            self.suites.append((e, entry_state(ws, e), cases))
        self.pending = {}

    def fresh_cases(self, cid, current, wanted, platform=None):
        """(cases naming `wanted` in fresh valid suites, stale count, tampered suite names, old-format count). With a
        platform, only suites recorded for that half of a native pair count. A suite whose result files changed or
        are gone is tampered when it named `wanted` at recording time, so deleting a failing file never hides it."""
        fresh, stale, tampered, old = [], 0, [], 0
        for e, state, cases in self.suites:
            if platform is not None and e.get("platform") != platform:
                continue
            named = [tc for tc in cases if proofkit.case_ids(tc) & wanted]
            if state == "tampered":
                if named or set(e.get("named") or []) & wanted:
                    tampered.append(e.get("name") or "?")
                continue
            if not named:
                continue
            if state == "old":
                old += 1
            elif not fresh_for(e, cid, current):
                stale += 1
            else:
                fresh += named
        return fresh, stale, tampered, old


def decision_effects(decisions, cid, cap, cap_rules, rules_by_id, conflicts):
    """What the person's decisions do to the rules check: ({rule: why left out}, [DEC ids a test must name], [gaps]).
    A decision about a rule conflict is the more specific answer: for the rules it names it wins over the capability's
    `take:<app>`."""
    excluded, required, gaps = {}, [], []
    mine = {r["id"] for r in cap_rules}
    by_rule, decided_keys = {}, set()
    for k, dd in decisions.items():
        about = dd.get("about") or ""
        if dd.get("kind") != "conflict":
            continue
        decided_keys.add(about)
        m = re.match(r"^(?:CAP-\d+|rules):((?:RULE-\d+\+?)+)$", about)
        if not m:
            continue
        ids = set(m.group(1).split("+"))
        if not ids & mine:
            continue
        if dd["choice"].startswith("take:"):
            keep = dd["choice"][5:]
            for rid in ids & mine:
                by_rule[rid] = f"{k} keeps {keep}'s rule" if (rules_by_id.get(rid) or {}).get("app") != keep else None
        elif dd["choice"] in ("design", "new-spec"):
            for rid in ids & mine:
                by_rule[rid] = f"{k} replaces it with a new behavior"
            required.append(k)
        elif dd["choice"] == "defer":
            gaps.append(f"{k} defers the rule conflict {'+'.join(sorted(ids))}")
        else:  # both-by-role: every rule of the set stays
            for rid in ids & mine:
                by_rule[rid] = None
    cap_dec = next(((k, d) for k, d in decisions.items() if d.get("kind") == "conflict" and d.get("about") == cid), (None, None))
    if cap.get("fusion") == "shared-diverged" and not cap_dec[0]:
        gaps.append("no decision yet on which app's behavior the new app keeps (fuse-review conflicts)")
    did, d = cap_dec
    if d:
        if d["choice"].startswith("take:"):
            keep = d["choice"][5:]
            for r in cap_rules:
                if r.get("app") != keep and r["id"] not in by_rule:
                    excluded[r["id"]] = f"{did} keeps {keep}'s behavior"
        elif d["choice"] in ("design", "new-spec"):
            required.append(did)
        elif d["choice"] == "defer":
            gaps.append(f"{did} defers this capability: it is not to be built yet")
    excluded.update({rid: why for rid, why in by_rule.items() if why})
    for conf in conflicts:
        ids = set(conf.get("rules") or [])
        key = conf.get("key")
        if (ids & mine or conf.get("capability") == cid) and key and key not in decided_keys:
            gaps.append(f"rule conflict {key} is not decided (fuse-review conflicts)")
    return excluded, sorted(set(required)), gaps


def judge(ws, program, only=None):  # noqa: ARG001  (every built capability is judged; see the loop)
    pdir = program_dir(ws, program)
    caps = load_json(os.path.join(pdir, "capabilities.json"))
    if not caps:
        die(f"analysis/{program}/capabilities.json not found")
    prog = load_json(os.path.join(pdir, "program.json")) or {}
    rules_doc = load_json(os.path.join(pdir, "rules.json")) or {}
    rules = rules_doc.get("rules") or []
    decisions = (load_json(os.path.join(pdir, "DECISIONS.json")) or {}).get("decisions") or {}
    attach = {d["about"]: d["choice"] for d in decisions.values() if d.get("kind") == "attach"}
    for r in rules:
        if r["id"] in attach:
            r["capability"] = attach[r["id"]] if attach[r["id"]] != "none" else None
    rules_by_id = {r["id"]: r for r in rules}
    verdict_of = {(d["about"], d["kind"]): (k, d["choice"]) for k, d in decisions.items()}
    ev = Evidence(ws, program)
    pending = canarymod.pending_all(ws, program)
    parity = {label: (load_json(os.path.join(pdir, "evidence", name)) or {}).get("capabilities") for label, name, _ in PARITY}
    legacy = wsmod.legacy_state(ws, prog)
    trace_caps = (load_json(os.path.join(pdir, "traceability.json")) or {}).get("capabilities") or {}
    platforms = (prog.get("target") or {}).get("platforms") or []
    halves = newapp.halves(ws, program)
    pair = [p for p, _ in halves if p] if sum(1 for p, _ in halves if p) > 1 else [None]
    conflicts = [dict(c, key=decmod.conflict_key(c)) for c in rules_doc.get("conflicts") or []]
    built = proofkit.built(ws, program)
    by_id = {c["id"]: c for c in caps.get("capabilities", [])}
    hashes = {cid: proofkit.code_hash(ws, program, cid) for cid in built}
    # capabilities a person parked (dropped, out of scope, deferred) are not on any journey until they come back
    not_building = {cid for cid in by_id if verdict_of.get((cid, "gap"), (None, ""))[1] in ("drop", "defer")
                    or verdict_of.get((cid, "scope"), (None, ""))[1] in ("out", "defer")
                    or verdict_of.get((cid, "conflict"), (None, ""))[1] == "defer"}
    results = {}
    # every built capability is judged on every run: a kept verdict could hide a change in a shared catalog, a
    # decision or another capability's code; `only` just names the ones the caller asked about
    for cid in sorted(built, key=lambda x: int(x.split("-")[1])):
        c = by_id.get(cid)
        if not c:
            continue
        info = proofkit.notes(ws, program, cid)
        current = hashes.get(cid) if cid in built else None
        checks = {}

        # 1 Built
        sources = [f for f in info["files"] if proofkit.is_source(f)]
        if not info["exists"]:
            checks["Built"] = ("fail", "no porting notes")
        elif not sources:
            checks["Built"] = ("fail", "the porting notes' ## Files section names no source file that exists inside the new app")
        else:
            missing_half = [p for p, h in halves if p and not any(newapp.in_half(f, h) for f in sources)]
            checks["Built"] = (("fail", f"no source file in the {', '.join(missing_half)} half of the native pair") if missing_half
                               else ("pass", f"{len(sources)} source file(s) named in docs/fusion/{cid}.md"))

        # 2 Tests ran: each half of a native pair on its own suites
        cap_rules = [r for r in rules if r.get("capability") == cid]
        wanted = {cid} | {r["id"] for r in cap_rules}
        per_half = {p: ev.fresh_cases(cid, current, wanted, platform=p) for p in pair}
        states, details = [], []
        for p, (fresh, stale, tampered, old) in per_half.items():
            where = f"{p}: " if p else ""
            ran = [tc for tc in fresh if tc["status"] != "skipped"]
            failed = [tc for tc in fresh if tc["status"] == "failed"]
            if tampered:
                st, dt = "fail", f"result file(s) of suite {', '.join(tampered)} changed or were removed after they were recorded"
            elif not fresh and not (stale or old):
                if p and ev.fresh_cases(cid, current, wanted, platform=None)[0] and any(
                        not e.get("platform") and any(proofkit.case_ids(tc) & wanted for tc in cases) for e, _, cases in ev.suites):
                    st, dt = "gap", f"a suite was recorded without --platform: record this half's suite with --platform {p}"
                elif p:
                    st, dt = "fail", f"no recorded result of the {p} half has a test naming the capability or its rules"
                else:
                    st, dt = "fail", ("no recorded result has a test naming the capability or its rules" if ev.suites
                                      else "evidence/test-runs.json lists no suite")
            elif not fresh:
                st, dt = "gap", ("the recorded results predate the capability's current code" if stale else
                                 "the results were recorded by an older version of the plugin: record them again")
            elif failed:
                st, dt = "fail", f"{len(failed)} failing: " + ", ".join(one_line(t['name'], 60) for t in failed[:5])
            elif not ran:
                st, dt = "fail", "only skipped tests name the capability or its rules"
            else:
                st, dt = "pass", f"{len(ran)} executed and passed on the current code"
            states.append(st)
            details.append(where + dt)
        checks["Tests ran"] = ("fail" if "fail" in states else ("gap" if "gap" in states else "pass"), "; ".join(details))
        passed_keys = {tc["key"] for f, *_ in per_half.values() for tc in f if tc["status"] == "passed"}

        # 3 Rules traced
        excluded, required_decs, conflict_gaps = decision_effects(decisions, cid, c, cap_rules, rules_by_id, conflicts)
        p0 = [r for r in cap_rules if r.get("priority") in ("P0", "P1")]
        untested, named_not_run, discuss, wrong, undecided = [], [], [], [], []
        for r in p0:
            v = verdict_of.get((r["id"], "rule"), (None, None))[1]
            if v == "wrong":
                wrong.append(r["id"])
                continue
            if r["id"] in excluded:
                continue
            if v == "discuss":
                discuss.append(r["id"])
                continue
            if v is None and (r.get("suspectedDefect") or (r.get("priority") == "P0" and (r.get("confidence") != "High" or r.get("question")))):
                undecided.append(r["id"])
                continue
            for p, (fresh, *_rest) in per_half.items():
                naming = [tc for tc in fresh if r["id"] in proofkit.case_ids(tc)]
                if not any(tc["status"] == "passed" for tc in naming):
                    (named_not_run if naming else untested).append(r["id"] + (f" ({p})" if p else ""))
        dec_untested = []
        for d in required_decs:
            for p in pair:
                dec_fresh = ev.fresh_cases(cid, current, {d}, platform=p)[0]
                if not any(tc["status"] == "passed" and d in proofkit.case_ids(tc) for tc in dec_fresh):
                    dec_untested.append(d + (f" ({p})" if p else ""))
        parts = []
        if untested:
            parts.append(f"not named by any passing test: {', '.join(untested)}")
        if named_not_run:
            parts.append(f"named, not passed: {', '.join(named_not_run)}")
        if discuss:
            parts.append(f"under discussion: {', '.join(discuss)}")
        if undecided:
            parts.append(f"a person has not decided whether the new app keeps or fixes {', '.join(undecided)} (a suspected "
                         "legacy defect or an open question: fuse-build asks in its plan, or fuse-review rules)")
        if dec_untested:
            parts.append(f"the behavior decided in {', '.join(dec_untested)} has no passing test naming that decision")
        parts += conflict_gaps
        left_out = [f"{rid} ({why})" for rid, why in sorted(excluded.items())] + [f"{rid} (marked wrong)" for rid in wrong]
        if parts:
            checks["Rules traced"] = ("gap", "; ".join(parts) + (f"; left out {', '.join(left_out)}" if left_out else ""))
        elif not p0 and not required_decs:
            checks["Rules traced"] = ("pass", "no P0 or P1 rule belongs to this capability" + (f"; left out {', '.join(left_out)}" if left_out else ""))
        else:
            kept = len(p0) - len([r for r in p0 if r["id"] in excluded]) - len(wrong)
            checks["Rules traced"] = ("pass", f"{kept} P0/P1 rule(s) backed by passing tests" + (" in each half" if pair != [None] else "") +
                                      (f", {len(required_decs)} decided behavior(s) tested" if required_decs else "") +
                                      (f"; left out {', '.join(left_out)}" if left_out else ""))

        # 4 Journeys
        journeys = [j for j in caps.get("journeys", []) if any(cid in st.get("capabilities", []) for st in j.get("steps", []))]
        if not journeys:
            checks["Journeys"] = ("pass", "n/a: no journey runs through this capability")
        else:
            failing, missing, stale_j, waiting, ok = [], [], [], [], 0
            runs = ev.runs.get("journeys") or []
            for j in journeys:
                on = sorted({x for st in j.get("steps", []) for x in st.get("capabilities", [])} - not_building)
                unbuilt = [x for x in on if x not in built]
                if unbuilt:
                    waiting.append(f"{j['id']} waits for {', '.join(unbuilt)}")
                    continue
                for platform in platforms or [None]:
                    entries = [e for e in runs if e.get("journey") == j["id"] and (platform is None or e.get("platform", platform) == platform)]
                    label = j["id"] + (f" on {platform}" if platform else "")
                    if not entries:
                        missing.append(label)
                        continue
                    e = entries[-1]
                    state = entry_state(ws, e)
                    cases, _ = proofkit.junit_cases(proofkit.xml_files(e.get("junit"), ws), ws)
                    named = [tc for tc in cases if j["id"] in proofkit.case_ids(tc)]
                    if state == "tampered":
                        failing.append(f"{label}: result changed after it was recorded")
                    elif state == "old":
                        stale_j.append(f"{label} (recorded by an older version)")
                    elif not named:
                        failing.append(f"{label}: the result names no {j['id']} test")
                    elif any(tc["status"] == "failed" for tc in named) or not any(tc["status"] == "passed" for tc in named):
                        failing.append(label)
                    elif proofkit.changed_inputs(ws, {e["flow"]: e.get("flowHash")}) if e.get("flow") else False:
                        stale_j.append(f"{label} (the flow changed since)")
                    elif any(not fresh_for(e, x, hashes.get(x)) for x in on):
                        stale_j.append(f"{label} (code on the journey changed since)")
                    else:
                        ok += 1
            if failing:
                checks["Journeys"] = ("fail", "failing: " + "; ".join(failing))
            elif missing or stale_j or waiting:
                bits = ([f"no run recorded for {', '.join(missing)}"] if missing else []) + \
                       ([f"stale: {', '.join(stale_j)}"] if stale_j else []) + waiting
                checks["Journeys"] = ("gap", "; ".join(bits))
            else:
                checks["Journeys"] = ("pass", f"{len(journeys)} journey(s) passed" + (f" on {', '.join(platforms)}" if platforms else ""))

        # 5-8 parity results
        for label, name, script in PARITY:
            source = parity[label]
            r = (source or {}).get(cid) if source is not None else None
            if source is None:
                checks[label] = ("gap", f"not run: {runner(script)} {program}")
            elif not r:
                checks[label] = ("gap", f"{script} has no result for {cid}: run it again")
            elif "inputs" not in r and r.get("verdict") != "gap":
                checks[label] = ("gap", f"recorded by an older version of the plugin: run {script} again")
            elif r.get("codeHash") != current or proofkit.changed_inputs(ws, r.get("inputs")) or \
                    proofkit.changed_decisions(decisions, r.get("decisionsUsed")):
                checks[label] = ("gap", f"what {script} read changed since it ran: run it again")
            elif r["verdict"] in ("pass", "n/a"):
                checks[label] = ("pass", ("n/a: " if r["verdict"] == "n/a" else "") + one_line(r.get("reason"), 200))
            elif r["verdict"] == "fail":
                checks[label] = ("fail", one_line(r.get("reason"), 200))
            else:
                checks[label] = ("gap", one_line(r.get("reason"), 200))

        # 9 Canary
        entry = next((e for e in ev.runs.get("canaries") or [] if e.get("capability") == cid), None)
        if cid in pending:
            checks["Canary"] = ("gap", f"a canary is still in place in {pending[cid].get('file')}: run canary.py finish or abort")
        elif not entry:
            checks["Canary"] = ("gap", "no canary recorded for this capability (scripts/canary.py)")
        elif "codeHash" not in entry:
            checks["Canary"] = ("gap", "recorded by an older version of the plugin: run a new canary with scripts/canary.py")
        elif entry_state(ws, entry) == "tampered":
            checks["Canary"] = ("fail", "the canary's result file changed after it was recorded")
        elif entry.get("codeHash") != current:
            checks["Canary"] = ("gap", "the capability's code changed since the canary: run a new one")
        elif not entry.get("failedCases"):
            checks["Canary"] = ("fail", f"{entry.get('change', 'the deliberate break')} made no test naming the capability or "
                                        "its rules fail: the tests do not pin the behavior")
        else:
            caught = [k for k in entry["failedCases"] if k in passed_keys]
            if not caught:
                checks["Canary"] = ("gap", "the tests that failed under the canary did not pass in a fresh recorded suite: record "
                                           "the suite after the canary")
            else:
                checks["Canary"] = ("pass", f"{one_line(entry.get('change'), 80)} ({entry.get('linesChanged', '?')} line(s) in "
                                            f"{entry.get('file')}): {len(caught)} test(s) that pass on the real code failed")

        # 10 Legacy
        dirty = [r["app"] for r in legacy if r["clean"] is False]
        missing_apps = [r["app"] for r in legacy if not r["exists"]]
        unknown = [r["app"] for r in legacy if r["exists"] and r["clean"] is None]
        moved = [r for r in legacy if r["recordedCommit"] and r["exists"] and r["clean"] is not None and not r["atRecordedCommit"]]
        if dirty:
            checks["Legacy untouched"] = ("fail", f"local changes in {', '.join(dirty)}")
        elif missing_apps:
            checks["Legacy untouched"] = ("gap", f"{', '.join(missing_apps)} not linked")
        elif unknown:
            checks["Legacy untouched"] = ("gap", f"{', '.join(unknown)} is not a git checkout, so it cannot be checked")
        elif moved:
            checks["Legacy untouched"] = ("gap", "; ".join(f"{r['app']} moved from {r['recordedCommit'][:10]} to {(r['commit'] or '?')[:10]}: "
                                                           "the analysis describes the recorded commit" for r in moved))
        else:
            checks["Legacy untouched"] = ("pass", "clean, at the recorded commit")

        states = [s for s, _ in checks.values()]
        verdict = "NOT PROVEN" if "fail" in states else ("PARTLY PROVEN" if "gap" in states else "PROVEN")
        results[cid] = {"name": c["name"], "verdict": verdict,
                        "checks": {k: {"status": checks[k][0], "detail": checks[k][1]} for k in CHECKS},
                        "screens": len((trace_caps.get(cid) or {}).get("screens") or []),
                        "codeHash": current, "judgedAt": now_iso()}
    return results


def continuity(ws, program):
    p = load_json(os.path.join(program_dir(ws, program), "evidence", "platform-parity.json"))
    if not p:
        return {"verdict": "gap", "detail": f"not run: {runner('platform_parity.py')} {program}"}
    decisions = (load_json(os.path.join(program_dir(ws, program), "DECISIONS.json")) or {}).get("decisions") or {}
    if proofkit.changed_inputs(ws, p.get("inputs")) or proofkit.changed_decisions(decisions, p.get("decisionsUsed")):
        return {"verdict": "gap", "detail": "the new app's platform files or decisions changed since platform_parity.py ran: run it again",
                "checks": p.get("checks")}
    bad = [f"{r['check']}: {r['why']}" for r in p.get("checks") or [] if r["verdict"] in ("fail", "gap")]
    return {"verdict": p.get("verdict"), "detail": "; ".join(bad) or "every required or kept platform item is present",
            "checks": p.get("checks"), "generated": p.get("generated")}


def render(ws, program, results, cont):
    signed = signoff.signed_state(ws, program, results)
    lines = [f"# Verification: {program}", "",
             f"Rendered {now_iso()} by `scripts/fusion_proof.py` from evidence files, never by a model. Each verdict carries the "
             "time it was judged; one marked *stale* was judged on code that has changed since. The rules are fixed and listed "
             "at the end.", ""]
    if not results:
        lines += ["No built capability yet: nothing to judge. Build one with `/app-fusion:fuse-build`.", ""]
    else:
        rows = []
        for cid, r in results.items():
            stale = r.get("codeHash") != proofkit.code_hash(ws, program, cid)
            s = signed.get(cid) or {}
            sign = ("proof signed" if s.get("proof") else "proof not signed") + \
                   ("" if s.get("visual") is None else (", visual signed" if s.get("visual") else ", visual not signed"))
            rows.append([cid, r["name"], r["verdict"] + (" (stale)" if stale else ""), (r.get("judgedAt") or "")[:16], sign] +
                        [r["checks"][k]["status"] for k in CHECKS])
        lines += [md_table(["Capability", "Name", "Verdict", "Judged", "Sign-off"] + CHECKS, rows), ""]
        for cid, r in results.items():
            lines += [f"## {cid}: {r['name']}: {r['verdict']}", ""]
            lines += [f"- **{k}** ({r['checks'][k]['status']}): {r['checks'][k]['detail']}" for k in CHECKS]
            lines.append("")
    lines += ["## Continuity for existing users (the whole app)", "",
              f"**Platform parity: {cont['verdict']}.** {cont['detail']}", ""]
    if cont.get("checks"):
        lines += [md_table(["Check", "Item", "Verdict", "Why"], [[r["check"], r.get("item") or "-", r["verdict"], r["why"]] for r in cont["checks"]]), ""]
    approval = signoff.brief_approval(ws, program)
    lines += ["## What this does not prove", "",
              "- **Look and feel.** The design-text check proves the copy, not the layout, spacing or colour. A person compares "
              "the screenshots side by side (REPORT.html, Design tab; the reviewer's notes are in VISUAL_REVIEW.md) and signs.",
              "- **Behaviour the tests do not exercise.** A rule no test names is listed as a gap, never assumed.",
              "- **Production data and services.** Runs use simulators and the test backends a person named.",
              "- **Store, migration and rollout steps.** CONTINUITY.md holds them, and people run them.", "",
              "## Sign-off", "",
              "Sign-offs are recorded by a person with `scripts/signoff.py` (`/app-fusion:fuse-verify <program> sign`) in "
              "SIGNOFF.json, never in this file. Each binds to the verdict and code it covers: when either changes, it no "
              "longer counts.", "",
              f"- Brief: " + (f"approved by {approval['by']} ({(approval['at'] or '')[:10]}), covers {approval['covers']}" if approval["approved"]
                              else ("the approval is for an earlier version of the brief" if approval["stale"] and approval["by"] else "not approved")),
              f"- Proof signed for: {', '.join(c for c, s in signed.items() if s['proof']) or 'none'}",
              f"- Visual conformance signed for: {', '.join(c for c, s in signed.items() if s['visual']) or 'none'}", "",
              "## Rules", "", "```"] + __doc__[__doc__.index("  1 Built"):__doc__.index("Platform continuity")].rstrip().splitlines() + ["```", ""]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("capabilities", nargs="*")
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    for c in args.capabilities:
        if not re.match(r"^CAP-\d+$", c):
            die(f"{c!r} is not a capability id (CAP-NNN)")
    results = judge(ws, args.program, set(args.capabilities))
    pdir = program_dir(ws, args.program)
    asked = [c for c in args.capabilities if c in results] if args.capabilities else list(results)
    missing = [c for c in args.capabilities if c not in results]
    cont = continuity(ws, args.program)
    write_json(os.path.join(pdir, "VERIFICATION.json"), {"program": args.program, "version": 2, "generated": now_iso(),
                                                          "checks": CHECKS, "capabilities": results, "continuity": cont})
    write_text(os.path.join(pdir, "VERIFICATION.md"), render(ws, args.program, results, cont))
    counts = {}
    for c in asked:
        counts[results[c]["verdict"]] = counts.get(results[c]["verdict"], 0) + 1
    print(", ".join(f"{v} {k}" for k, v in sorted(counts.items())) or "nothing built yet",
          f"-> analysis/{args.program}/VERIFICATION.md (every built capability judged: {len(results)}; platform parity {cont['verdict']})")
    for c in asked:
        r = results[c]
        reasons = [f"{k}: {v['detail']}" for k, v in r["checks"].items() if v["status"] != "pass"]
        print(f"  {c} {r['verdict']}" + (f" ({'; '.join(reasons[:3])})" if reasons else ""))
    for c in missing:
        print(f"  {c} is not built: no docs/fusion/{c}.md in the new app")
    others = [c for c in results if c not in asked and results[c]["verdict"] != "PROVEN"]
    if others:
        print(f"  also not PROVEN now: {', '.join(others)}")
    sys.exit(0 if asked and not missing and all(results[c]["verdict"] == "PROVEN" for c in asked) else 1)


if __name__ == "__main__":
    main()
