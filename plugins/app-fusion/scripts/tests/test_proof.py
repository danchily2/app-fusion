import json
import os
import subprocess
import time
import unittest

import helpers
from helpers import Workspace

KEY = "B" * 22


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


class Proof(unittest.TestCase):
    def setUp(self):
        self.w = w = Workspace().init()
        w.run("inventory.py", "p", "--all")
        w.put_json("analysis/p/map_result.json", {"capabilities": [
            {"name": "Approve a request", "domain": "Approvals", "description": "d", "fusion": "unique",
             "implementations": {"mgr": {"endpoints": ["POST /approval/rest/tasks/approve", "GET /approval/rest/tasks/{}"],
                                         "strings": ["approve", "reject"], "evidence": "src/services/api.ts:3"}}}],
            "journeys": [{"name": "Manager approves", "persona": "manager", "steps": [{"label": "a", "capabilities": ["Approve a request"]}]}]})
        w.run("render.py", "capabilities", "p")
        w.put_json("analysis/p/rules_result.json", {"rules": [
            {"name": "Reject needs a comment", "app": "mgr", "capability": "CAP-001", "category": "Validation", "priority": "P0",
             "source": "src/services/api.ts:3-4", "plainEnglish": "p", "given": "g", "when": "w", "then": "t", "confidence": "High"}]})
        w.run("render.py", "rules", "p")
        w.put_json("analysis/p/design/design.json", {"program": "p", "version": 1, "files": [], "screens": [
            {"id": f"{KEY}:1:2", "fileKey": KEY, "nodeId": "1:2", "name": "Approvals", "kind": "screen",
             "texts": ["Approve", "Reject", "3 requests", "12:30", "Jane Doe"]}]})
        w.put_json("analysis/p/design/trace_result.json", {"links": [{"screen": f"{KEY}:1:2", "capabilities": ["CAP-001"], "confidence": "High", "evidence": "t"}]})
        w.run("trace.py", "p")
        # the new app: a React Native project with the capability, its notes, strings and key map
        app = w.path("new-app", "p")
        helpers.write(app, "package.json", json.dumps({"name": "newapp", "dependencies": {"react-native": "0.81.0"}}))
        helpers.write(app, "src/features/approvals/approve/api.ts", """
            export const approve = builder.mutation({ query: body => ({ url: 'api/approval/rest/tasks/approve', method: 'POST', body }) })
            export const task = builder.query({ query: id => ({ url: `api/approval/rest/tasks/${id}` }) })
        """)
        helpers.write(app, "src/i18n/locales/en.json", json.dumps({"approvals": {"approve": "Approve", "reject": "Reject", "count": "{{count}} requests"}}))
        helpers.write(app, "src/i18n/locales/da.json", json.dumps({"approvals": {"approve": "Godkend"}}))
        helpers.write(app, "docs/fusion/i18n-map.json", json.dumps({"mgr:approve": "approvals.approve", "mgr:reject": "approvals.reject"}))
        helpers.write(app, "docs/fusion/design-placeholders.json", json.dumps(["Jane Doe"]))
        helpers.write(app, "docs/fusion/CAP-001.md", "# CAP-001\n## Files\n- `src/features/approvals/approve/api.ts`\n- `src/missing.ts`\n")
        helpers.git_init(app)
        self.app = app

    def tearDown(self):
        self.w.close()

    def record(self, unit_cases, canary_cases, journey_cases):
        w = self.w
        time.sleep(0.05)  # result files must be newer than the code
        u = junit(w.path("analysis/p/evidence/junit/CAP-001/unit.xml"), unit_cases)
        w.run("evidence.py", "suite", "p", "--capability", "CAP-001", "--name", "unit", "--command", "jest", "--junit", u)
        if canary_cases is not None:
            c = junit(w.path("analysis/p/evidence/canary/CAP-001/unit.xml"), canary_cases)
            w.run("evidence.py", "canary", "p", "--capability", "CAP-001", "--change", "threshold +1", "--junit", c)
        if journey_cases is not None:
            flow = helpers.write(self.app, ".maestro/JRN-001-approve.yaml", "appId: x\n---\n- launchApp\n")
            j = junit(w.path("analysis/p/evidence/maestro/JRN-001.xml"), journey_cases)
            w.run("evidence.py", "journey", "p", "--journey", "JRN-001", "--flow", flow, "--junit", j)

    def parity(self):
        for script in ("api_parity.py", "i18n_parity.py", "design_text.py"):
            self.w.run(script, "p", check=False)

    def verdict(self):
        out = self.w.run("fusion_proof.py", "p", check=False)
        return self.w.json("analysis", "p", "VERIFICATION.json")["capabilities"]["CAP-001"], out

    def test_parity_checks(self):
        self.parity()
        api = self.w.json("analysis", "p", "evidence", "api-parity.json")["capabilities"]["CAP-001"]
        self.assertEqual(api["verdict"], "pass", api)
        i18n = self.w.json("analysis", "p", "evidence", "i18n-parity.json")["capabilities"]["CAP-001"]
        self.assertEqual(i18n["required"], ["da", "en"], "the locales the legacy app ships")
        self.assertEqual(i18n["verdict"], "fail")
        self.assertEqual(i18n["missingLocale"], [{"key": "approvals.reject", "missing": ["da"]}])
        dt = self.w.json("analysis", "p", "evidence", "design-text.json")["capabilities"]["CAP-001"]
        screen = dt["screens"][0]
        self.assertEqual(screen["matched"], 3, "Approve, Reject and the '{{count}} requests' template")
        self.assertIn("12:30", screen["leftOut"])
        self.assertIn("Jane Doe", screen["leftOut"], "listed in design-placeholders.json")
        self.assertEqual(dt["verdict"], "pass")

    def test_verdicts(self):
        # all evidence good except strings (approvals.reject has no da) -> NOT PROVEN because i18n parity fails
        self.record([("CAP-001 approvals", "RULE-001 reject needs a comment", "passed")],
                    [("CAP-001 approvals", "RULE-001 reject needs a comment", "failed")],
                    [("JRN-001", "JRN-001-approve", "passed")])
        self.parity()
        v, _ = self.verdict()
        self.assertEqual(v["checks"]["Built"]["status"], "pass")
        self.assertEqual(v["checks"]["Tests ran"]["status"], "pass")
        self.assertEqual(v["checks"]["Rules traced"]["status"], "pass")
        self.assertEqual(v["checks"]["Journeys"]["status"], "pass")
        self.assertEqual(v["checks"]["Canary"]["status"], "pass")
        self.assertEqual(v["checks"]["Legacy untouched"]["status"], "pass")
        self.assertEqual(v["verdict"], "NOT PROVEN")
        self.assertEqual(v["checks"]["Strings"]["status"], "fail")
        # translate the missing key: every check passes -> PROVEN
        helpers.write(self.app, "src/i18n/locales/da.json", json.dumps({"approvals": {"approve": "Godkend", "reject": "Afvis"}}))
        self.parity()
        v, out = self.verdict()
        self.assertEqual(v["verdict"], "PROVEN", v)
        self.assertEqual(out.returncode, 0)

    def test_gaps_and_failures(self):
        prog = self.w.json("analysis", "p", "program.json")
        prog["locales"] = ["en"]
        self.w.put_json("analysis/p/program.json", prog)
        # no canary, no journey, the rule named only by a skipped test -> PARTLY PROVEN
        self.record([("CAP-001 approvals", "renders", "passed"), ("x", "RULE-001 pending", "skipped")], None, None)
        self.parity()
        v, out = self.verdict()
        self.assertEqual(v["verdict"], "PARTLY PROVEN", v)
        self.assertIn("named, not run: RULE-001", v["checks"]["Rules traced"]["detail"])
        self.assertEqual(v["checks"]["Canary"]["status"], "gap")
        self.assertEqual(out.returncode, 1)
        # a canary that nothing caught is a failure
        self.record([("CAP-001 approvals", "RULE-001 ok", "passed")], [("CAP-001 approvals", "RULE-001 ok", "passed")],
                    [("JRN-001", "flow", "passed")])
        v, _ = self.verdict()
        self.assertEqual(v["checks"]["Canary"]["status"], "fail")
        self.assertEqual(v["verdict"], "NOT PROVEN")
        # a change in a legacy app is caught
        with open(os.path.join(self.w.rn, "package.json"), "a", encoding="utf-8") as fh:
            fh.write("\n")
        v, _ = self.verdict()
        self.assertEqual(v["checks"]["Legacy untouched"]["status"], "fail")
        subprocess.run(["git", "-C", self.w.rn, "checkout", "--", "package.json"], check=True)

    def test_api_difference_needs_a_person(self):
        with open(os.path.join(self.app, "src/features/approvals/approve/api.ts"), "w", encoding="utf-8") as fh:
            fh.write("export const approve = builder.mutation({ query: b => ({ url: 'api/approval/rest/tasks/approve', method: 'POST' }) })\n")
        self.w.run("api_parity.py", "p", check=False)
        api = self.w.json("analysis", "p", "evidence", "api-parity.json")["capabilities"]["CAP-001"]
        self.assertEqual(api["verdict"], "fail")
        self.assertEqual(api["missing"], ["GET /approval/rest/tasks/{}"])
        self.w.run("decisions.py", "add", "p", "--about", "CAP-001:GET /approval/rest/tasks/{}", "--kind", "api", "--choice", "replaced",
                   "--note", "the list endpoint returns the task inline")
        self.w.run("api_parity.py", "p")
        api = self.w.json("analysis", "p", "evidence", "api-parity.json")["capabilities"]["CAP-001"]
        self.assertEqual(api["verdict"], "pass")
        self.assertEqual(api["approved"][0]["decision"], "replaced")

    def test_har_mode(self):
        def har(entries):
            return {"log": {"entries": [{"request": {"method": m, "url": u, "queryString": [{"name": q} for q in qs],
                                                     "postData": {"text": json.dumps(b)} if b else {}}} for m, u, qs, b in entries]}}
        a = self.w.put_json("a.har", har([("GET", "https://x.net/api/tasks/1?x=1", ["x"], None), ("POST", "https://x.net/api/tasks/1/approve", [], {"comment": "c"})]))
        b = self.w.put_json("b.har", har([("GET", "https://y.net/v2/api/tasks/2?x=2", ["x"], None), ("POST", "https://y.net/v2/api/tasks/2/approve", [], {"note": "c"})]))
        out = subprocess.run(["python3", os.path.join(helpers.SCRIPTS, "api_parity.py"), "har", a, b, "--out", self.w.path("har.json")],
                             capture_output=True, text=True)
        self.assertEqual(out.returncode, 1)
        res = self.w.json("har.json")
        self.assertEqual(res["missing"], [])
        self.assertEqual(len(res["shapeDiffers"]), 1, "the body key changed from comment to note")


if __name__ == "__main__":
    unittest.main()
