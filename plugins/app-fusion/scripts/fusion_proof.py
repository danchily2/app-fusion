#!/usr/bin/env python3
"""Independent proof: one verdict per built capability, computed from evidence files by fixed rules.

    python3 fusion_proof.py <program> [CAP-NNN ...] [--workspace DIR]

Writes analysis/<program>/VERIFICATION.md (for people) and VERIFICATION.json (for the report). A model never gives
the verdict: this script does, from files it parses itself, and every rule is written into the output.

  1 Built           new-app/<program>/docs/fusion/CAP-NNN.md exists and names at least one new-app file that exists.
  2 Tests ran       in the JUnit results listed in evidence/test-runs.json, tests whose name or class names the
                    capability (CAP-012, cap012) or one of its rules executed, none failed, and the result files are
                    newer than the capability's files. Nothing executed, a failure, or only skipped tests is a failure;
                    results older than the code are a gap. A count typed into test-runs.json counts for nothing.
  3 Rules traced    every P0 rule of the capability is named by a test that ran and passed. A rule a person marked
                    `wrong` is left out (it is not the oracle); one marked `discuss` is a gap; one named only by a
                    skipped or failing test is "named, not run" (a gap).
  4 Journeys        every journey through the capability has a Maestro (or other UI) run whose JUnit passed.
  5 API parity      evidence/api-parity.json says pass (or n/a) for the capability.
  6 Strings         evidence/i18n-parity.json says pass (or n/a).
  7 Design text     evidence/design-text.json says pass (or n/a: no design screen).
  8 Canary          a deliberate break of the capability's code made at least one test fail (evidence/test-runs.json
                    canaries). A canary that nothing caught is a failure: the tests do not pin the behavior.
  9 Legacy          every legacy/<app> is still a clean git checkout (read-only git).

  PROVEN        all nine checks pass (n/a counts as a pass).
  NOT PROVEN    any check failed.
  PARTLY PROVEN nothing failed, but a check could not pass; each such check is listed with its reason.

Visual conformance is never computed: a named person signs it from the side-by-side screenshots. Exit 0 when every
judged capability is PROVEN, 1 otherwise. Standard library only.
"""

import argparse
import glob
import os
import re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import workspace as wsmod  # noqa: E402
from fusionlib import newapp  # noqa: E402
from fusionlib.common import (check_name, die, load_json, md_table, now_iso, one_line, program_dir, workspace,  # noqa: E402
                              write_json, write_text)

CHECKS = ["Built", "Tests ran", "Rules traced", "Journeys", "API parity", "Strings", "Design text", "Canary", "Legacy untouched"]
ID = re.compile(r"(CAP|RULE)[-_ ]?0*(\d{1,5})", re.I)


def ids_in(text):
    return {f"{m.group(1).upper()}-{int(m.group(2)):03d}" for m in ID.finditer(text or "")}


def junit_cases(paths, ws):
    """Test cases from JUnit-style XML files or folders of them: [{name, classname, status, file}]."""
    cases, files = [], []
    for p in paths or []:
        full = p if os.path.isabs(p) else os.path.join(ws, p)
        if os.path.isdir(full):
            files += sorted(glob.glob(os.path.join(full, "**", "*.xml"), recursive=True))
        elif os.path.isfile(full):
            files.append(full)
    for f in files:
        try:
            root = ET.parse(f).getroot()
        except (ET.ParseError, OSError):
            continue
        for tc in root.iter("testcase"):
            status = "passed"
            children = {c.tag for c in tc}
            if "failure" in children or "error" in children:
                status = "failed"
            elif "skipped" in children:
                status = "skipped"
            attr_status = (tc.get("status") or "").lower()
            if attr_status in ("failed", "failure", "error", "errored"):
                status = "failed"
            elif attr_status in ("skipped", "disabled", "pending"):
                status = "skipped"
            cases.append({"name": tc.get("name") or "", "classname": tc.get("classname") or "", "status": status,
                          "file": os.path.relpath(f, ws)})
    return cases, [os.path.relpath(f, ws) for f in files]


def newest_mtime(paths):
    times = [os.path.getmtime(p) for p in paths if os.path.exists(p)]
    return max(times) if times else 0


def oldest_mtime(paths):
    times = [os.path.getmtime(p) for p in paths if os.path.exists(p)]
    return min(times) if times else 0


def judge(ws, program, only=None):
    pdir = program_dir(ws, program)
    caps = load_json(os.path.join(pdir, "capabilities.json"))
    if not caps:
        die(f"analysis/{program}/capabilities.json not found")
    prog = load_json(os.path.join(pdir, "program.json")) or {}
    rules = (load_json(os.path.join(pdir, "rules.json")) or {}).get("rules") or []
    decisions = (load_json(os.path.join(pdir, "DECISIONS.json")) or {}).get("decisions") or {}
    verdict_of = {(d["about"], d["kind"]): d["choice"] for d in decisions.values()}
    runs = load_json(os.path.join(pdir, "evidence", "test-runs.json")) or {}
    api = (load_json(os.path.join(pdir, "evidence", "api-parity.json")) or {}).get("capabilities")
    i18n = (load_json(os.path.join(pdir, "evidence", "i18n-parity.json")) or {}).get("capabilities")
    dtext = (load_json(os.path.join(pdir, "evidence", "design-text.json")) or {}).get("capabilities")
    legacy = wsmod.legacy_state(ws, prog)
    base = newapp.root(ws, program)
    trace_caps = (load_json(os.path.join(pdir, "traceability.json")) or {}).get("capabilities") or {}

    suite_paths = [p for s in runs.get("suites") or [] for p in (s.get("junit") or [])]
    all_cases, suite_files = junit_cases(suite_paths, ws)
    results = {}
    for c in caps.get("capabilities", []):
        cid = c["id"]
        if only and cid not in only:
            continue
        notes = newapp.notes_path(ws, program, cid)
        if not os.path.isfile(notes) and not only:
            continue
        checks = {}
        files = newapp.notes_files(ws, program, cid)
        full_files = [os.path.join(base, f) for f in files]
        checks["Built"] = ("pass", f"{len(files)} new-app file(s) named in {os.path.relpath(notes, ws)}") if files else \
            ("fail", "no porting notes" if not os.path.isfile(notes) else "the porting notes name no new-app file that exists")

        cap_rules = [r for r in rules if r.get("capability") == cid]
        rule_ids = {r["id"] for r in cap_rules}
        mine = [tc for tc in all_cases if (ids_in(tc["name"] + " " + tc["classname"]) & ({cid} | rule_ids))]
        ran = [tc for tc in mine if tc["status"] != "skipped"]
        failed = [tc for tc in mine if tc["status"] == "failed"]
        fresh = oldest_mtime([os.path.join(ws, f) for f in suite_files]) >= newest_mtime(full_files) if suite_files and full_files else False
        if not suite_files:
            checks["Tests ran"] = ("fail", "evidence/test-runs.json lists no JUnit result file")
        elif failed:
            checks["Tests ran"] = ("fail", f"{len(failed)} failing: " + ", ".join(one_line(t['name'], 60) for t in failed[:5]))
        elif not ran:
            checks["Tests ran"] = ("fail", "no executed test names the capability or its rules" + (" (only skipped ones do)" if mine else ""))
        elif not fresh:
            checks["Tests ran"] = ("gap", f"{len(ran)} passed, but the results are older than the capability's code: run the tests again")
        else:
            checks["Tests ran"] = ("pass", f"{len(ran)} executed and passed")

        p0 = [r for r in cap_rules if r.get("priority") == "P0"]
        excluded = [r["id"] for r in p0 if verdict_of.get((r["id"], "rule")) == "wrong"]
        discuss = [r["id"] for r in p0 if verdict_of.get((r["id"], "rule")) == "discuss"]
        untested, named_not_run = [], []
        for r in p0:
            if r["id"] in excluded or r["id"] in discuss:
                continue
            naming = [tc for tc in all_cases if r["id"] in ids_in(tc["name"] + " " + tc["classname"])]
            if any(tc["status"] == "passed" for tc in naming):
                continue
            (named_not_run if naming else untested).append(r["id"])
        if not p0:
            checks["Rules traced"] = ("pass", "no P0 rule belongs to this capability")
        elif untested or named_not_run or discuss:
            parts = []
            if untested:
                parts.append(f"not named by any test: {', '.join(untested)}")
            if named_not_run:
                parts.append(f"named, not run: {', '.join(named_not_run)}")
            if discuss:
                parts.append(f"under discussion: {', '.join(discuss)}")
            checks["Rules traced"] = ("gap", "; ".join(parts))
        else:
            checks["Rules traced"] = ("pass", f"{len(p0) - len(excluded)} P0 rule(s) backed by passing tests"
                                      + (f"; {', '.join(excluded)} left out (marked wrong by a person)" if excluded else ""))

        journeys = [j for j in caps.get("journeys", []) if any(cid in st.get("capabilities", []) for st in j.get("steps", []))]
        if not journeys:
            checks["Journeys"] = ("pass", "n/a: no journey runs through this capability")
        else:
            missing, failing = [], []
            for j in journeys:
                entries = [e for e in runs.get("journeys") or [] if e.get("journey") == j["id"]]
                cases, _ = junit_cases([p for e in entries for p in e.get("junit") or []], ws)
                if not cases:
                    missing.append(j["id"])
                elif any(tc["status"] == "failed" for tc in cases) or not any(tc["status"] == "passed" for tc in cases):
                    failing.append(j["id"])
            if failing:
                checks["Journeys"] = ("fail", f"failing: {', '.join(failing)}")
            elif missing:
                checks["Journeys"] = ("gap", f"no UI run recorded for {', '.join(missing)}")
            else:
                checks["Journeys"] = ("pass", f"{len(journeys)} journey(s) passed")

        for label, source, name in (("API parity", api, "api_parity.py"), ("Strings", i18n, "i18n_parity.py"),
                                    ("Design text", dtext, "design_text.py")):
            if source is None:
                checks[label] = ("gap", f"not run: python3 scripts/{name} {program}")
                continue
            r = source.get(cid)
            if not r:
                checks[label] = ("gap", f"{name} has no result for {cid}: run it again")
            elif r["verdict"] in ("pass", "n/a"):
                checks[label] = ("pass", ("n/a: " if r["verdict"] == "n/a" else "") + one_line(r.get("reason"), 200))
            elif r["verdict"] == "fail":
                checks[label] = ("fail", one_line(r.get("reason"), 200))
            else:
                checks[label] = ("gap", one_line(r.get("reason"), 200))

        canaries = [e for e in runs.get("canaries") or [] if e.get("capability") == cid]
        if not canaries:
            checks["Canary"] = ("gap", "no canary recorded for this capability")
        else:
            cases, cfiles = junit_cases([p for e in canaries for p in e.get("junit") or []], ws)
            broke = [tc for tc in cases if tc["status"] == "failed"]
            if not cfiles:
                checks["Canary"] = ("gap", "the canary's JUnit result is missing")
            elif broke:
                checks["Canary"] = ("pass", f"{canaries[0].get('change', 'a deliberate break')}: {len(broke)} test(s) failed")
            else:
                checks["Canary"] = ("fail", f"{canaries[0].get('change', 'the deliberate break')} made no test fail: the tests do not pin the behavior")

        dirty = [r["app"] for r in legacy if r["clean"] is False]
        missing_apps = [r["app"] for r in legacy if not r["exists"]]
        unknown = [r["app"] for r in legacy if r["exists"] and r["clean"] is None]
        if dirty:
            checks["Legacy untouched"] = ("fail", f"local changes in {', '.join(dirty)}")
        elif missing_apps:
            checks["Legacy untouched"] = ("gap", f"{', '.join(missing_apps)} not linked")
        elif unknown:
            checks["Legacy untouched"] = ("gap", f"{', '.join(unknown)} is not a git checkout, so it cannot be checked")
        else:
            moved = [r["app"] for r in legacy if r["recordedCommit"] and not r["atRecordedCommit"]]
            checks["Legacy untouched"] = ("pass", "clean" + (f" ({', '.join(moved)} moved to a newer commit since preflight)" if moved else ""))

        states = [s for s, _ in checks.values()]
        verdict = "NOT PROVEN" if "fail" in states else ("PARTLY PROVEN" if "gap" in states else "PROVEN")
        results[cid] = {"name": c["name"], "verdict": verdict,
                        "checks": {k: {"status": checks[k][0], "detail": checks[k][1]} for k in CHECKS},
                        "screens": len((trace_caps.get(cid) or {}).get("screens") or [])}
    return results


def render(program, results, runs_date):
    lines = [f"# Verification: {program}", "",
             f"Computed {now_iso()} by `scripts/fusion_proof.py` from evidence files, never by a model. Test results "
             f"recorded {runs_date or 'never'}. The rules are fixed and listed at the end.", ""]
    if not results:
        lines += ["No built capability yet: nothing to judge. Build one with `/app-fusion:fuse-build`.", ""]
    else:
        lines += [md_table(["Capability", "Name", "Verdict"] + CHECKS,
                           [[cid, r["name"], r["verdict"]] + [r["checks"][k]["status"] for k in CHECKS]
                            for cid, r in results.items()]), ""]
        for cid, r in results.items():
            lines += [f"## {cid}: {r['name']}: {r['verdict']}", ""]
            lines += [f"- **{k}** ({r['checks'][k]['status']}): {r['checks'][k]['detail']}" for k in CHECKS]
            lines.append("")
    lines += ["## What this does not prove", "",
              "- **Look and feel.** The design-text check proves the copy, not the layout, spacing or colour. A person compares "
              "the screenshots side by side (REPORT.html, Design tab) and signs below.",
              "- **Behaviour the tests do not exercise.** A rule no test names is listed as a gap, never assumed.",
              "- **Production data and services.** Runs use simulators and the test backends a person named.",
              "- **Store, migration and rollout steps.** CONTINUITY.md holds them, and people run them.", "",
              "## Sign-off", "",
              "```", "Proof reviewed by: ________________  Date: __________",
              "Visual conformance signed by: ________________  Date: __________",
              "Covers: <capability ids>", "```", "",
              "## Rules", "", "```"] + __doc__[__doc__.index("  1 Built"):__doc__.index("Visual conformance")].rstrip().splitlines() + ["```", ""]
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
    runs = load_json(os.path.join(pdir, "evidence", "test-runs.json")) or {}
    write_json(os.path.join(pdir, "VERIFICATION.json"), {"program": args.program, "version": 1, "generated": now_iso(),
                                                          "checks": CHECKS, "capabilities": results})
    write_text(os.path.join(pdir, "VERIFICATION.md"), render(args.program, results, runs.get("date")))
    counts = {}
    for r in results.values():
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print(", ".join(f"{v} {k}" for k, v in sorted(counts.items())) or "nothing built yet",
          f"-> analysis/{args.program}/VERIFICATION.md")
    for cid, r in results.items():
        reasons = [f"{k}: {v['detail']}" for k, v in r["checks"].items() if v["status"] != "pass"]
        print(f"  {cid} {r['verdict']}" + (f" ({'; '.join(reasons[:3])})" if reasons else ""))
    sys.exit(0 if results and all(r["verdict"] == "PROVEN" for r in results.values()) else 1)


if __name__ == "__main__":
    main()
