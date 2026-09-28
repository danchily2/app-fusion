import json
import os
import subprocess
import unittest

import helpers
from helpers import Workspace

KEY = "B" * 22
FIGMA = f"https://www.figma.com/design/{KEY}/New-app"
LOGIC = "src/features/approvals/approve/logic.ts"


def junit(path, cases):
    """cases: [(classname, name, status)] with status passed|failed|skipped."""
    body = []
    for cls, name, status in cases:
        inner = {"failed": "<failure message=\"x\"/>", "skipped": "<skipped/>"}.get(status, "")
        body.append(f'<testcase classname="{cls}" name="{name}">{inner}</testcase>')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f'<?xml version="1.0"?><testsuites><testsuite name="s">{"".join(body)}</testsuite></testsuites>')
    return path


GREEN = [("CAP-001 approvals", "RULE-001 reject needs a comment", "passed"), ("CAP-001 approvals", "RULE-002 approve toast", "passed")]


def base_map(**over):
    cap1 = {"name": "Approve a request", "domain": "Approvals", "description": "d", "fusion": "unique",
            "implementations": {"mgr": {"endpoints": ["POST /approval/rest/tasks/approve", "GET /approval/rest/tasks/{}"],
                                        "strings": ["approve", "reject"], "events": ["approval_approve"],
                                        "files": ["src/services/api.ts"], "evidence": "src/services/api.ts:3"}}}
    cap2 = {"name": "See the request list", "domain": "Approvals", "description": "d", "fusion": "unique",
            "implementations": {"mgr": {"screens": ["ApprovalsScreen"], "files": ["src/screens/approvals/ApprovalsScreen.tsx"],
                                        "evidence": "src/screens/approvals/ApprovalsScreen.tsx:1"}}}
    cap1.update(over.get("cap1") or {})
    return {"capabilities": [cap1, cap2],
            "journeys": over.get("journeys") or [{"name": "Manager approves", "persona": "manager",
                                                  "steps": [{"label": "a", "capabilities": ["Approve a request"]}]}]}


class Base(unittest.TestCase):
    figma = True

    def setUp(self):
        self.w = w = Workspace()
        w.run("workspace.py", "init", "p", "--source", f"mgr={w.rn}", "--source", f"emp={w.ios}",
              "--product", "mgr=Manager", "--product", "emp=Employee", *(["--figma", FIGMA] if self.figma else []))
        w.run("workspace.py", "intent", "p", "--platforms", "ios")
        w.run("inventory.py", "p", "--all")
        w.put_json("analysis/p/map_result.json", self.map_result())
        w.run("render.py", "capabilities", "p")
        w.put_json("analysis/p/rules_result.json", {"rules": self.rules()})
        w.run("render.py", "rules", "p")
        w.put_json("analysis/p/design/design.json", {"program": "p", "version": 1, "files": [], "screens": [
            {"id": f"{KEY}:1:2", "fileKey": KEY, "nodeId": "1:2", "name": "Approvals", "kind": "screen",
             "texts": ["Approve", "Reject", "3 requests", "12:30", "Jane Doe"]}]})
        w.put_json("analysis/p/design/placeholders.json", ["Jane Doe"])
        w.put_json("analysis/p/design/trace_result.json", {"links": [{"screen": f"{KEY}:1:2", "capabilities": ["CAP-001"],
                                                                      "confidence": "High", "evidence": "t"}]})
        w.run("trace.py", "p")
        app = self.app = w.path("new-app", "p")
        helpers.write(app, "package.json", json.dumps({"name": "newapp", "dependencies": {"react-native": "0.81.0"}}))
        helpers.write(app, "src/features/approvals/approve/api.ts", """
            export const approve = builder.mutation({ query: body => ({ url: 'api/approval/rest/tasks/approve', method: 'POST', body }) })
            export const task = builder.query({ query: id => ({ url: `api/approval/rest/tasks/${id}` }) })
        """)
        helpers.write(app, LOGIC, "export const needsComment = (action: string) => action === 'reject'\n")
        helpers.write(app, "src/features/approvals/approve/logic.test.ts", "it('RULE-001 reject needs a comment', () => {})\n")
        helpers.write(app, "src/analytics/events.ts", "export const APPROVAL_EVENTS = { APPROVE: 'approval_approve' }\n")
        helpers.write(app, "src/i18n/locales/en.json", json.dumps({"approvals": {"approve": "Approve", "reject": "Reject", "count": "{{count}} requests"}}))
        helpers.write(app, "src/i18n/locales/da.json", json.dumps({"approvals": {"approve": "Godkend"}}))
        helpers.write(app, "docs/fusion/i18n-map.json", json.dumps({"mgr:approve": "approvals.approve", "mgr:reject": "approvals.reject"}))
        helpers.write(app, "docs/fusion/CAP-001.md", "# CAP-001\n## Files\n- `src/features/approvals/approve/api.ts`\n"
                                                     f"- `{LOGIC}`\n- `src/missing.ts`\n- `../../legacy/mgr/package.json`\n"
                                                     "## Tests\n- `src/features/approvals/approve/logic.test.ts`\n")
        helpers.git_init(app)

    def tearDown(self):
        self.w.close()

    def map_result(self):
        return base_map()

    def rules(self):
        common = {"app": "mgr", "capability": "CAP-001", "category": "Validation", "source": "src/services/api.ts:3-4",
                  "plainEnglish": "p", "given": "g", "when": "w", "then": "t", "confidence": "High"}
        return [dict(common, name="Reject needs a comment", priority="P0"), dict(common, name="Approve shows a toast", priority="P1")]

    # ---- recording helpers, the way the skills do it
    def suite(self, cases, name="unit", cap="CAP-001"):
        run = self.w.run("evidence.py", "dir", "p", "suite", cap).stdout.strip()
        junit(self.w.path(run, "unit.xml"), cases)
        self.w.run("evidence.py", "suite", "p", "--capability", cap, "--name", name, "--command", "jest", "--junit", run)
        return self.w.path(run, "unit.xml")

    def canary(self, cases, file=LOGIC, mutate=True, check=True):
        self.w.run("canary.py", "start", "p", "CAP-001", "--file", file, "--change", "flip the reject check")
        pending = self.w.json("analysis", "p", "evidence", "canary", "CAP-001", "pending.json")
        if mutate:
            with open(os.path.join(self.app, file), "a", encoding="utf-8") as fh:
                fh.write("export const broken = true\n")
        junit(self.w.path(pending["run"], "unit.xml"), cases)
        return self.w.run("canary.py", "finish", "p", "CAP-001", check=check)

    def journey(self, cases, jid="JRN-001"):
        flow = helpers.write(self.app, f".maestro/{jid}-approve.yaml", "appId: x\n---\n- launchApp\n")
        run = self.w.run("evidence.py", "dir", "p", "journey", jid, "--platform", "ios").stdout.strip()
        junit(self.w.path(run, "maestro.xml"), cases)
        self.w.run("evidence.py", "journey", "p", "--journey", jid, "--platform", "ios", "--flow", flow, "--junit", run)

    def parity(self):
        for script in ("api_parity.py", "i18n_parity.py", "events_parity.py", "design_text.py"):
            self.w.run(script, "p", check=False)

    def verdict(self, *caps):
        out = self.w.run("fusion_proof.py", "p", *caps, check=False)
        return self.w.json("analysis", "p", "VERIFICATION.json")["capabilities"], out

    def translate(self):
        helpers.write(self.app, "src/i18n/locales/da.json", json.dumps({"approvals": {"approve": "Godkend", "reject": "Afvis"}}))

    def all_green(self):
        self.translate()
        self.parity()
        self.suite(GREEN)
        self.canary([("CAP-001 approvals", "RULE-001 reject needs a comment", "failed")])
        self.journey([("JRN-001", "JRN-001-approve", "passed")])


class Proof(Base):
    def test_parity_checks(self):
        self.parity()
        j = lambda name: self.w.json("analysis", "p", "evidence", name)["capabilities"]["CAP-001"]
        api = j("api-parity.json")
        self.assertEqual(api["verdict"], "pass", api)
        i18n = j("i18n-parity.json")
        self.assertEqual(i18n["required"], ["da", "en"], "the locales the legacy app ships")
        self.assertEqual(i18n["verdict"], "fail")
        self.assertEqual(i18n["missingLocale"], [{"key": "approvals.reject", "missing": ["da"]}])
        self.assertIn("inputs", i18n, "a result records the files it read")
        events = j("events-parity.json")
        self.assertEqual((events["verdict"], events["kept"]), ("pass", ["mgr:approval_approve"]))
        dt = j("design-text.json")
        screen = dt["screens"][0]
        self.assertEqual(screen["matched"], 3, "Approve, Reject and the '{{count}} requests' template")
        self.assertIn("12:30", screen["leftOut"])
        self.assertIn("Jane Doe", screen["leftOut"], "listed in analysis/p/design/placeholders.json")
        self.assertEqual(dt["verdict"], "pass")

    def test_proven_on_content_not_file_times(self):
        # a suite recorded before the capability existed (the scaffold) never makes it stale
        self.suite([("smoke", "app launches", "passed")], name="scaffold", cap="all")
        self.all_green()
        v, out = self.verdict()
        c = v["CAP-001"]
        self.assertEqual(c["verdict"], "PROVEN", c)
        self.assertEqual(out.returncode, 0)
        self.assertEqual(c["checks"]["Built"]["detail"], "2 source file(s) named in docs/fusion/CAP-001.md",
                         "a missing file and a path outside the new app do not count")
        # a restore, checkout or copy changes file times, not content: still PROVEN
        later = os.path.getmtime(os.path.join(self.app, LOGIC)) + 3600
        os.utime(os.path.join(self.app, LOGIC), (later, later))
        v, _ = self.verdict()
        self.assertEqual(v["CAP-001"]["verdict"], "PROVEN", v["CAP-001"])

    def test_stale_and_tampered_results(self):
        self.all_green()
        with open(os.path.join(self.app, LOGIC), "a", encoding="utf-8") as fh:
            fh.write("// changed after the run\n")
        v, _ = self.verdict()
        c = v["CAP-001"]["checks"]
        self.assertEqual(v["CAP-001"]["verdict"], "PARTLY PROVEN")
        self.assertIn("predate the capability's current code", c["Tests ran"]["detail"])
        self.assertEqual(c["Canary"]["status"], "gap")
        self.assertIn("changed since it ran", c["API parity"]["detail"])
        xml = self.suite(GREEN)
        self.parity()
        self.canary([("CAP-001 approvals", "RULE-001 reject needs a comment", "failed")])
        self.journey([("JRN-001", "JRN-001-approve", "passed")])
        v, _ = self.verdict()
        self.assertEqual(v["CAP-001"]["verdict"], "PROVEN", v["CAP-001"])
        with open(xml, "a", encoding="utf-8") as fh:
            fh.write("<!-- edited -->")
        v, _ = self.verdict()
        self.assertEqual(v["CAP-001"]["checks"]["Tests ran"]["status"], "fail")
        self.assertIn("changed after they were recorded", v["CAP-001"]["checks"]["Tests ran"]["detail"])

    def test_canary_is_safe_and_specific(self):
        # uncommitted work in the new app survives the canary byte for byte
        path = os.path.join(self.app, LOGIC)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write("// uncommitted work\n")
        before = helpers.read(path)
        out = self.canary([], mutate=False, check=False)
        self.assertNotEqual(out.returncode, 0, "finish refuses when no break was made")
        self.w.run("canary.py", "abort", "p", "CAP-001")
        refused = self.w.run("canary.py", "start", "p", "CAP-001", "--file", "src/features/approvals/approve/logic.test.ts",
                             "--change", "x", check=False)
        self.assertNotEqual(refused.returncode, 0, "a test file is never the canary's target")
        self.suite(GREEN)
        self.canary([("CAP-001 approvals", "RULE-001 reject needs a comment", "passed"), ("other", "unrelated", "failed")])
        self.assertEqual(helpers.read(path), before)
        v, _ = self.verdict()
        self.assertEqual(v["CAP-001"]["checks"]["Canary"]["status"], "fail", "only an unrelated test failed")
        # a failure in a test that never passed on the real code proves nothing either
        self.canary([("other suite", "RULE-009 never ran", "failed")])
        v, _ = self.verdict()
        self.assertEqual(v["CAP-001"]["checks"]["Canary"]["status"], "fail", "RULE-009 does not belong to CAP-001")
        self.canary([("CAP-001 approvals", "a new case", "failed")])
        v, _ = self.verdict()
        self.assertEqual(v["CAP-001"]["checks"]["Canary"]["status"], "gap")
        self.assertIn("did not pass in a fresh recorded suite", v["CAP-001"]["checks"]["Canary"]["detail"])
        # status points at a canary left in place
        self.w.run("canary.py", "start", "p", "CAP-001", "--file", LOGIC, "--change", "x")
        st = json.loads(self.w.run("status.py", "p", "--json").stdout)
        self.assertIn("canary.py finish p CAP-001", st["next"]["command"])
        v, _ = self.verdict()
        self.assertIn("still in place", v["CAP-001"]["checks"]["Canary"]["detail"])

    def test_gaps_failures_and_legacy(self):
        prog = self.w.json("analysis", "p", "program.json")
        prog["locales"] = ["en"]
        self.w.put_json("analysis/p/program.json", prog)
        self.suite([("CAP-001 approvals", "renders", "passed"), ("x", "RULE-001 pending", "skipped")])
        self.parity()
        v, out = self.verdict()
        c = v["CAP-001"]
        self.assertEqual(c["verdict"], "PARTLY PROVEN", c)
        self.assertIn("named, not passed: RULE-001", c["checks"]["Rules traced"]["detail"])
        self.assertIn("not named by any passing test: RULE-002", c["checks"]["Rules traced"]["detail"], "P1 rules are pinned too")
        self.assertEqual(c["checks"]["Canary"]["status"], "gap")
        self.assertIn("no run recorded for JRN-001 on ios", c["checks"]["Journeys"]["detail"])
        self.assertEqual(out.returncode, 1)
        with open(os.path.join(self.w.rn, "package.json"), "a", encoding="utf-8") as fh:
            fh.write("\n")
        v, _ = self.verdict()
        self.assertEqual(v["CAP-001"]["checks"]["Legacy untouched"]["status"], "fail")
        subprocess.run(["git", "-C", self.w.rn, "checkout", "--", "package.json"], check=True)
        helpers.write(self.w.rn, "untracked.txt", "x")
        v, _ = self.verdict()
        self.assertEqual(v["CAP-001"]["checks"]["Legacy untouched"]["status"], "fail", "untracked files count")

    def test_merge_signoff_and_no_ping_pong(self):
        helpers.write(self.app, "src/features/approvals/list/List.tsx", "export const List = () => null\n")
        helpers.write(self.app, "docs/fusion/CAP-002.md", "# CAP-002\n## Files\n- `src/features/approvals/list/List.tsx`\n")
        self.all_green()
        v, _ = self.verdict("CAP-001")
        self.assertEqual(set(v), {"CAP-001"})
        v, _ = self.verdict("CAP-002")
        self.assertEqual(set(v), {"CAP-001", "CAP-002"}, "judging one capability keeps the other's verdict")
        self.assertEqual(v["CAP-001"]["verdict"], "PROVEN")
        refused = self.w.run("signoff.py", "p", "proof", "--by", "Kari Nordmann", "--caps", "CAP-002", check=False)
        self.assertNotEqual(refused.returncode, 0, "a NOT PROVEN capability cannot be signed")
        self.assertNotEqual(self.w.run("signoff.py", "p", "proof", "--by", "claude", "--caps", "CAP-001", check=False).returncode, 0)
        self.w.run("signoff.py", "p", "proof", "--by", "Kari Nordmann", "--caps", "CAP-001")
        md = self.w.text("analysis", "p", "VERIFICATION.md")
        self.assertIn("Sign-off", md)
        self.w.run("fusion_proof.py", "p", "CAP-001", check=False)
        self.assertIn("Proof signed for: CAP-001", self.w.text("analysis", "p", "VERIFICATION.md"), "the sign-off survives a re-run")
        with open(os.path.join(self.app, LOGIC), "a", encoding="utf-8") as fh:
            fh.write("// a later change\n")
        state = json.loads(self.w.run("signoff.py", "p", "show", "--json").stdout)
        self.assertEqual(len(state["proof"]), 1)
        self.w.run("fusion_proof.py", "p", "CAP-001", check=False)
        self.assertIn("Proof signed for: none", self.w.text("analysis", "p", "VERIFICATION.md"), "a code change voids the sign-off")

    def test_decisions_that_excuse_differences(self):
        # API: a missing endpoint is a failure until a person records why
        with open(os.path.join(self.app, "src/features/approvals/approve/api.ts"), "w", encoding="utf-8") as fh:
            fh.write("export const approve = builder.mutation({ query: b => ({ url: 'api/approval/rest/tasks/approve', method: 'POST' }) })\n")
        self.w.run("api_parity.py", "p", check=False)
        api = self.w.json("analysis", "p", "evidence", "api-parity.json")["capabilities"]["CAP-001"]
        self.assertEqual((api["verdict"], api["missing"]), ("fail", ["GET /approval/rest/tasks/{}"]))
        qs = json.loads(self.w.run("decisions.py", "open", "p", "--json").stdout)
        self.assertIn(("api", "CAP-001:GET /approval/rest/tasks/{}"), {(q["kind"], q["about"]) for q in qs})
        self.w.run("decisions.py", "add", "p", "--about", "CAP-001:GET /approval/rest/tasks/{}", "--kind", "api", "--choice", "replaced",
                   "--note", "the list endpoint returns the task inline")
        self.w.run("api_parity.py", "p")
        api = self.w.json("analysis", "p", "evidence", "api-parity.json")["capabilities"]["CAP-001"]
        self.assertEqual((api["verdict"], api["approved"][0]["choice"]), ("pass", "replaced"))
        # strings: a null in the key map is a missing key until a person decides the drop
        helpers.write(self.app, "docs/fusion/i18n-map.json", json.dumps({"mgr:approve": "approvals.approve", "mgr:reject": None}))
        self.w.run("i18n_parity.py", "p", check=False)
        i18n = self.w.json("analysis", "p", "evidence", "i18n-parity.json")["capabilities"]["CAP-001"]
        self.assertEqual(i18n["verdict"], "fail")
        self.assertIn("without a person's decision", i18n["missingKeys"][0]["why"])
        self.w.run("decisions.py", "add", "p", "--about", "mgr:reject", "--kind", "strings", "--choice", "drop")
        self.w.run("i18n_parity.py", "p", check=False)
        i18n = self.w.json("analysis", "p", "evidence", "i18n-parity.json")["capabilities"]["CAP-001"]
        self.assertEqual(i18n["dropped"][0]["legacy"], "mgr:reject")
        # events: a rename waits for the taxonomy decision, then follows it
        helpers.write(self.app, "docs/fusion/analytics-map.json", json.dumps({"mgr:approval_approve": "request_approved"}))
        helpers.write(self.app, "src/analytics/events.ts", "export const APPROVAL_EVENTS = { APPROVE: 'request_approved' }\n")
        self.w.run("events_parity.py", "p", check=False)
        ev = lambda: self.w.json("analysis", "p", "evidence", "events-parity.json")["capabilities"]["CAP-001"]["verdict"]
        self.assertEqual(ev(), "gap")
        self.w.run("decisions.py", "add", "p", "--about", "analytics:taxonomy", "--kind", "analytics", "--choice", "keep-names")
        self.w.run("events_parity.py", "p", check=False)
        self.assertEqual(ev(), "fail")
        self.w.run("decisions.py", "add", "p", "--about", "analytics:taxonomy", "--kind", "analytics", "--choice", "new-taxonomy")
        self.w.run("events_parity.py", "p", check=False)
        self.assertEqual(ev(), "pass")

    def test_har_mode_and_sanitize(self):
        def har(entries):
            return {"log": {"entries": [{"request": {"method": m, "url": u, "queryString": [{"name": q, "value": "v"} for q in qs],
                                                     "headers": [{"name": "Authorization", "value": "Bearer abc"}, {"name": "Accept", "value": "*/*"}],
                                                     "cookies": [{"name": "sid", "value": "s"}],
                                                     "postData": {"text": json.dumps(b)} if b else {}}} for m, u, qs, b in entries]}}
        a = self.w.put_json("a.har", har([("GET", "https://x.net/api/tasks/1?x=1", ["x"], None), ("POST", "https://x.net/api/tasks/1/approve", [], {"comment": "c"})]))
        b = self.w.put_json("b.har", har([("GET", "https://y.net/v2/api/tasks/2?x=2&token=t", ["x", "token"], None), ("POST", "https://y.net/v2/api/tasks/2/approve", [], {"note": "c"})]))
        out = subprocess.run(["python3", os.path.join(helpers.SCRIPTS, "api_parity.py"), "har", a, b, "--out", self.w.path("har.json")],
                             capture_output=True, text=True)
        self.assertEqual(out.returncode, 1, out.stderr)
        res = self.w.json("har.json")
        self.assertEqual(res["missing"], [])
        self.assertEqual(len(res["shapeDiffers"]), 2, "the body key changed, and the query gained a key")
        subprocess.run(["python3", os.path.join(helpers.SCRIPTS, "api_parity.py"), "sanitize", b, self.w.path("b.clean.har")], check=True,
                       capture_output=True)
        clean = helpers.read(self.w.path("b.clean.har"))
        self.assertNotIn("Bearer abc", clean)
        self.assertNotIn('"sid"', clean)
        self.assertNotIn("token=t", clean)


class TakeDecision(Base):
    def map_result(self):
        return base_map(cap1={"fusion": "shared-diverged", "divergence": ["emp asks twice"], "implementations": {
            "mgr": {"endpoints": ["POST /approval/rest/tasks/approve", "GET /approval/rest/tasks/{}"], "strings": ["approve", "reject"],
                    "events": ["approval_approve"], "files": ["src/services/api.ts"], "evidence": "src/services/api.ts:3"},
            "emp": {"evidence": "Services/Expense/Sources/Expense/GetReceipts.swift:1"}}})

    def rules(self):
        emp = {"name": "Confirm twice", "app": "emp", "capability": "CAP-001", "category": "Validation", "priority": "P0",
               "source": "Services/Expense/Sources/Expense/GetReceipts.swift:1-2", "plainEnglish": "p", "given": "g", "when": "w",
               "then": "t", "confidence": "High"}
        return super().rules() + [emp]

    def test_take_leaves_out_the_other_apps_rules(self):
        ids = {r["name"]: r["id"] for r in self.w.json("analysis", "p", "rules.json")["rules"]}
        self.translate()
        self.parity()
        self.suite([("CAP-001 approvals", f"{ids['Reject needs a comment']} reject", "passed"),
                    ("CAP-001 approvals", f"{ids['Approve shows a toast']} toast", "passed")])
        self.canary([("CAP-001 approvals", f"{ids['Reject needs a comment']} reject", "failed")])
        self.journey([("JRN-001", "JRN-001-approve", "passed")])
        v, _ = self.verdict()
        rules = v["CAP-001"]["checks"]["Rules traced"]
        self.assertEqual(rules["status"], "gap")
        self.assertIn("no decision yet", rules["detail"])
        self.w.run("decisions.py", "add", "p", "--about", "CAP-001", "--kind", "conflict", "--choice", "take:mgr")
        v, _ = self.verdict()
        rules = v["CAP-001"]["checks"]["Rules traced"]
        self.assertEqual(rules["status"], "pass", rules)
        self.assertIn(f"{ids['Confirm twice']} (DEC-001 keeps mgr's behavior)", rules["detail"])
        self.w.run("decisions.py", "add", "p", "--about", "CAP-001", "--kind", "conflict", "--choice", "design")
        v, _ = self.verdict()
        self.assertIn("has no passing test naming that decision", v["CAP-001"]["checks"]["Rules traced"]["detail"])


class NoDesign(Base):
    figma = False

    def test_no_figma_means_no_design_by_intent(self):
        self.w.run("design_text.py", "p")
        dt = self.w.json("analysis", "p", "evidence", "design-text.json")["capabilities"]["CAP-001"]
        self.assertEqual(dt["verdict"], "n/a")
        self.assertIn("no design by intent", dt["reason"])


class Journeys(Base):
    def map_result(self):
        return base_map(journeys=[{"name": "Manager approves from the list", "persona": "manager",
                                   "steps": [{"label": "list", "capabilities": ["See the request list"]},
                                             {"label": "approve", "capabilities": ["Approve a request"]}]}])

    def test_a_journey_waits_for_unbuilt_capabilities(self):
        self.all_green()
        v, _ = self.verdict()
        j = v["CAP-001"]["checks"]["Journeys"]
        self.assertEqual(j["status"], "gap")
        self.assertIn("JRN-001 waits for CAP-002", j["detail"])
        from fusionlib import status as st
        self.assertTrue(st._waiting_only(v["CAP-001"], {"CAP-001": 0}), "status skips it instead of looping on fuse-build")
        # once CAP-002 is built, the journey must run again: its code is on the journey
        helpers.write(self.app, "src/features/approvals/list/List.tsx", "export const List = () => null\n")
        helpers.write(self.app, "docs/fusion/CAP-002.md", "# CAP-002\n## Files\n- `src/features/approvals/list/List.tsx`\n")
        v, _ = self.verdict("CAP-001")
        self.assertIn("stale", v["CAP-001"]["checks"]["Journeys"]["detail"])
        self.suite(GREEN)
        self.journey([("JRN-001", "JRN-001-approve", "passed")])
        v, _ = self.verdict("CAP-001")
        self.assertEqual(v["CAP-001"]["checks"]["Journeys"]["status"], "pass", v["CAP-001"]["checks"]["Journeys"])
        # a result that names another journey does not count
        self.journey([("JRN-009", "some other flow", "passed")])
        v, _ = self.verdict("CAP-001")
        self.assertIn("names no JRN-001 test", v["CAP-001"]["checks"]["Journeys"]["detail"])


if __name__ == "__main__":
    unittest.main()
