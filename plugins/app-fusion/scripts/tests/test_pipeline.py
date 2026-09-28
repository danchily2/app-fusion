import json
import os
import re
import unittest

from helpers import Workspace

KEY = "A" * 22


def map_result():
    return {
        "domains": [{"name": "Approvals", "description": "d"}],
        "capabilities": [
            {"name": "Approve an absence request", "domain": "Approvals", "description": "d", "fusion": "shared-diverged",
             "implementations": {"mgr": {"screens": ["ApprovalDetailScreen"], "endpoints": ["POST /approval/rest/tasks/approve"],
                                         "strings": ["approve"], "evidence": "src/services/api.ts:3"},
                                 "emp": {"endpoints": ["GET /employee/api/v1/expense/claims"], "evidence": "x:1"},
                                 "ghost-app": {"evidence": "dropped"}},
             "divergence": ["mgr asks for a comment"]},
            {"name": "See payslips", "domain": "Pay", "description": "d", "fusion": "unique",
             "implementations": {"emp": {"screens": ["PayslipsFeature"], "strings": ["payslip.title"], "evidence": "y:1"}}},
        ],
        "journeys": [{"name": "Manager approves", "persona": "manager",
                      "steps": [{"label": "approve", "capabilities": ["Approve an absence request", "Unknown one"]}]}],
        "platformItems": [{"area": "extensions", "name": "Share extension", "apps": {"emp": "Share/Info.plist"}, "recommendation": "decide"}],
    }


class Pipeline(unittest.TestCase):
    def setUp(self):
        self.w = Workspace().init()

    def tearDown(self):
        self.w.close()

    def test_link_inventory_shard_platform_overlap(self):
        w = self.w
        self.assertTrue(os.path.islink(w.path("legacy", "mgr")))
        prog = w.json("analysis", "p", "program.json")
        self.assertEqual({a["name"]: a["stack"] for a in prog["apps"]}, {"mgr": "react-native", "emp": "ios-native"})
        self.assertTrue(all(a["commit"] for a in prog["apps"]))
        self.assertIn("SECRETS.local.md", w.text("analysis", ".gitignore"))
        # linking the same name to another folder is refused
        out = w.run("workspace.py", "init", "p", "--source", f"mgr={w.ios}", check=False)
        self.assertNotEqual(out.returncode, 0)
        self.assertIn("already points", out.stderr)
        # the home directory is refused
        out = w.run("workspace.py", "init", "p", "--source", "x=~", check=False)
        self.assertNotEqual(out.returncode, 0)

        w.run("inventory.py", "p", "--all")
        inv = w.json("analysis", "p", "apps", "mgr", "inventory.json")
        self.assertEqual(set(inv["counts"]) - set(inv["rules"]), set(), "every count has its rule")
        self.assertTrue(os.path.exists(w.path("analysis", "p", "apps", "emp", "INVENTORY.md")))
        strings = w.json("analysis", "p", "apps", "mgr", "strings.json")
        self.assertIn("nested.title", strings["keys"])

        w.run("shard.py", "p")
        shards = w.json("analysis", "p", "shards.json")["shards"]
        self.assertTrue(shards)
        self.assertTrue(all(s["files"] and s["kind"] for s in shards))
        self.assertTrue(any(s["hints"].get("routes") for s in shards))

        w.run("render.py", "platform", "p")
        items = w.json("analysis", "p", "platform.json")["items"]
        names = {i["name"] for i in items}
        self.assertIn("Push notifications", names)
        self.assertIn("App extension: share", names)
        first_ids = {i["name"]: i["id"] for i in items}
        w.run("render.py", "platform", "p")
        self.assertEqual({i["name"]: i["id"] for i in w.json("analysis", "p", "platform.json")["items"]}, first_ids, "PLT ids are stable")

        w.run("render.py", "overlap", "p")
        pair = w.json("analysis", "p", "overlap.json")["pairs"][0]
        self.assertEqual(pair["apps"], ["mgr", "emp"])

    def test_capabilities_rules_decisions_trace_status_report(self):
        w = self.w
        w.run("inventory.py", "p", "--all")
        w.put_json("analysis/p/map_result.json", map_result())
        w.run("render.py", "capabilities", "p")
        caps = w.json("analysis", "p", "capabilities.json")
        ids = {c["name"]: c["id"] for c in caps["capabilities"]}
        self.assertEqual(set(ids.values()), {"CAP-001", "CAP-002"})
        approve = next(c for c in caps["capabilities"] if c["id"] == ids["Approve an absence request"])
        self.assertNotIn("ghost-app", approve["implementations"], "unknown apps are dropped")
        self.assertEqual(caps["journeys"][0]["steps"][0]["capabilities"], [ids["Approve an absence request"]])

        # a re-run with a new capability first keeps the old ids and never reuses one
        mr = map_result()
        mr["capabilities"].insert(0, {"name": "Submit an expense", "domain": "Expenses", "description": "d", "fusion": "unique",
                                      "implementations": {"emp": {"evidence": "z:1"}}})
        mr["capabilities"] = [c for c in mr["capabilities"] if c["name"] != "See payslips"]
        w.put_json("analysis/p/map_result.json", mr)
        w.run("render.py", "capabilities", "p")
        caps2 = {c["name"]: c["id"] for c in w.json("analysis", "p", "capabilities.json")["capabilities"]}
        self.assertEqual(caps2["Approve an absence request"], ids["Approve an absence request"])
        self.assertEqual(caps2["Submit an expense"], "CAP-003", "a removed id (CAP-002) is never reused")

        w.put_json("analysis/p/rules_result.json", {"rules": [
            {"name": "Comment required on reject", "app": "mgr", "capability": "CAP-001", "category": "Validation", "priority": "P0",
             "source": "src/services/api.ts:3-4", "plainEnglish": "p", "given": "g", "when": "w", "then": "t", "confidence": "Medium",
             "question": "Is the comment mandatory?"},
            {"name": "Bogus capability", "app": "emp", "capability": "CAP-999", "category": "Nope", "priority": "P7",
             "source": "x:1", "plainEnglish": "p", "given": "g", "when": "w", "then": "t", "confidence": "High"},
        ], "conflicts": [{"capability": "CAP-001", "rules": [{"app": "mgr", "name": "Comment required on reject"}], "difference": "d"}]})
        w.run("render.py", "rules", "p")
        rules = w.json("analysis", "p", "rules.json")
        self.assertEqual([r["id"] for r in rules["rules"]], ["RULE-001", "RULE-002"])
        bogus = next(r for r in rules["rules"] if r["name"] == "Bogus capability")
        self.assertIsNone(bogus["capability"])
        self.assertEqual((bogus["category"], bogus["priority"]), ("Policy", "P1"))
        md = w.text("analysis", "p", "BUSINESS_RULES.md")
        self.assertEqual(len(re.findall(r"^### RULE-\d{3}: ", md, re.M)), 2)

        # decisions: invalid choices are refused; open questions list the diverged capability, the flagged P0 rule, stack and store
        out = w.run("decisions.py", "add", "p", "--about", "CAP-001", "--kind", "conflict", "--choice", "take:nobody", check=False)
        self.assertNotEqual(out.returncode, 0)
        qs = json.loads(w.run("decisions.py", "open", "p", "--json").stdout)
        kinds = {(q["kind"], q["about"]) for q in qs}
        self.assertIn(("conflict", "CAP-001"), kinds)
        self.assertIn(("rule", "RULE-001"), kinds)
        self.assertIn(("stack", "stack"), kinds)
        w.put_json("answers.json", [{"about": "CAP-001", "kind": "conflict", "choice": "take:mgr", "note": "manager flow wins"},
                                    {"about": "RULE-001", "kind": "rule", "choice": "confirmed"},
                                    {"about": "CAP-001", "kind": "conflict", "choice": "design", "note": "changed my mind"}])
        w.run("decisions.py", "add-json", "p", w.path("answers.json"))
        dec = w.json("analysis", "p", "DECISIONS.json")["decisions"]
        self.assertEqual(len(dec), 2, "a new answer about the same thing replaces the earlier one")
        self.assertEqual(dec["DEC-001"]["choice"], "design")
        self.assertEqual(dec["DEC-001"]["replaces"], "take:mgr")

        # trace: an invalid link is dropped; statuses follow the rules
        w.put_json("analysis/p/design/design.json", {"program": "p", "version": 1, "files": [], "screens": [
            {"id": f"{KEY}:1:2", "fileKey": KEY, "nodeId": "1:2", "name": "Approvals", "kind": "screen", "texts": ["Approve"]},
            {"id": f"{KEY}:1:3", "fileKey": KEY, "nodeId": "1:3", "name": "Wellbeing", "kind": "screen", "texts": []}]})
        w.put_json("analysis/p/design/trace_result.json", {"links": [
            {"screen": f"{KEY}:1:2", "capabilities": ["CAP-001"], "confidence": "High", "evidence": "title"},
            {"screen": "nope:1:1", "capabilities": ["CAP-001"], "confidence": "High", "evidence": "x"}]})
        w.run("trace.py", "p")
        t = w.json("analysis", "p", "traceability.json")
        self.assertEqual(t["capabilities"]["CAP-001"]["status"], "designed")
        self.assertEqual(t["capabilities"]["CAP-003"]["status"], "no-design")
        self.assertEqual(t["gaps"]["screensWithoutCapability"], [f"{KEY}:1:3"])
        self.assertEqual(len(t["droppedLinks"]), 1)
        w.run("decisions.py", "add", "p", "--about", "CAP-003", "--kind", "gap", "--choice", "drop")
        w.run("trace.py", "p")
        self.assertEqual(w.json("analysis", "p", "traceability.json")["capabilities"]["CAP-003"]["status"], "dropped")

        # status names the next step; the report survives hostile text
        st = json.loads(w.run("status.py", "p", "--json").stdout)
        self.assertEqual(st["next"]["command"], "/app-fusion:fuse-preflight p")
        mr = map_result()
        mr["capabilities"][1]["name"] = "</script><script>alert(1)</script>"
        w.put_json("analysis/p/map_result.json", mr)
        w.run("render.py", "capabilities", "p")
        w.run("build_report.py", "p")
        html = w.text("analysis", "p", "REPORT.html")
        self.assertEqual(html.count("</script>"), 2, "only the page's own two script blocks close")
        self.assertIn("Content-Security-Policy", html)
        data = re.search(r'<script type="application/json" id="data">(.*?)</script>', html, re.S).group(1)
        self.assertTrue(any("alert(1)" in c["name"] for c in json.loads(data)["capabilities"]["capabilities"]))


if __name__ == "__main__":
    unittest.main()
