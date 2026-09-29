import json
import unittest

import helpers
from helpers import Workspace

KEY = "C" * 22


def cap(name, fusion="unique", domain="Approvals", **impls):
    return {"name": name, "domain": domain, "description": "d", "fusion": fusion,
            "implementations": impls or {"mgr": {"files": [f"src/{name.replace(' ', '')}.ts"], "evidence": "src/x.ts:1"}}}


def rule(name, app="mgr", capability="CAP-001", priority="P1", **extra):
    return dict({"name": name, "app": app, "capability": capability, "category": "Validation", "priority": priority,
                 "source": f"src/{name.replace(' ', '')}.ts:1-2", "plainEnglish": "p", "given": "g", "when": "w", "then": "t",
                 "confidence": "High"}, **extra)


class Decisions(unittest.TestCase):
    def setUp(self):
        self.w = Workspace().init()
        self.w.run("inventory.py", "p", "--all")

    def tearDown(self):
        self.w.close()

    def render_map(self, caps, journeys=None):
        self.w.put_json("analysis/p/map_result.json", {"capabilities": caps, "journeys": journeys or []})
        return self.w.run("render.py", "capabilities", "p")

    def ids(self):
        return {c["name"]: c["id"] for c in self.w.json("analysis", "p", "capabilities.json")["capabilities"]}

    def open(self):
        return json.loads(self.w.run("decisions.py", "open", "p", "--json").stdout)

    def test_every_question_has_its_own_answer(self):
        mgr = {"files": ["src/a.ts"], "evidence": "src/a.ts:1"}
        emp = {"files": ["A.swift"], "evidence": "A.swift:1"}
        self.render_map([cap("Approve a request", "shared-diverged", mgr=mgr, emp=emp)])
        self.w.put_json("analysis/p/rules_result.json", {"rules": [rule("Comment on reject"), rule("No comment", app="emp")],
                                                         "conflicts": [{"capability": "CAP-001", "rules": [{"app": "mgr", "name": "Comment on reject"},
                                                                                                          {"app": "emp", "name": "No comment"}],
                                                                        "difference": "one asks for a comment"}]})
        self.w.run("render.py", "rules", "p")
        rid = {r["name"]: r["id"] for r in self.w.json("analysis", "p", "rules.json")["rules"]}
        about = f"CAP-001:{'+'.join(sorted(rid.values()))}"
        qs = {(q["kind"], q["about"]) for q in self.open()}
        self.assertIn(("conflict", "CAP-001"), qs)
        self.assertIn(("conflict", about), qs, "a rule conflict inside a capability is its own question")
        self.w.run("decisions.py", "add", "p", "--about", "CAP-001", "--kind", "conflict", "--choice", "take:mgr")
        self.w.run("decisions.py", "add", "p", "--about", about, "--kind", "conflict", "--choice", "take:emp")
        dec = self.w.json("analysis", "p", "DECISIONS.json")["decisions"]
        self.assertEqual([(d["about"], d["choice"]) for d in dec.values()], [("CAP-001", "take:mgr"), (about, "take:emp")])
        bad = self.w.run("decisions.py", "add", "p", "--about", "CAP-001", "--kind", "rule", "--choice", "wrong", check=False)
        self.assertNotEqual(bad.returncode, 0, "a rule verdict must be about a RULE id")

    def test_designed_features_keep_their_screens_and_ask_for_scope(self):
        self.render_map([cap("Approve a request")])
        self.w.put_json("analysis/p/design/design.json", {"program": "p", "version": 1, "files": [], "screens": [
            {"id": f"{KEY}:1:2", "fileKey": KEY, "nodeId": "1:2", "name": "Wellbeing check-in", "kind": "screen", "texts": ["How are you?"]}]})
        self.w.put_json("analysis/p/design/new_capabilities.json", [{"name": "Check in on wellbeing", "domain": "Wellbeing",
                                                                     "description": "d", "screens": [f"{KEY}:1:2"]}])
        self.w.run("render.py", "capabilities", "p")
        new = next(c for c in self.w.json("analysis", "p", "capabilities.json")["capabilities"] if c["fusion"] == "new")
        self.assertEqual(new["designScreens"], [f"{KEY}:1:2"])
        self.w.run("trace.py", "p")
        t = self.w.json("analysis", "p", "traceability.json")
        self.assertEqual(t["capabilities"][new["id"]]["screens"], [f"{KEY}:1:2"])
        self.assertEqual(t["gaps"]["screensWithoutCapability"], [])
        scope = [q for q in self.open() if q["kind"] == "scope"]
        self.assertEqual([(q["about"], q["priority"]) for q in scope], [(new["id"], 1)], "a person decides whether it is in scope")

    def test_ids_follow_the_evidence_and_retired_ids_are_reported(self):
        self.render_map([cap("Approve a request", mgr={"files": ["src/approve.ts"], "screens": ["ApproveScreen"], "evidence": "src/approve.ts:1"}),
                         cap("See payslips", mgr={"files": ["src/payslips.ts"], "evidence": "src/payslips.ts:1"})])
        self.assertEqual(self.ids(), {"Approve a request": "CAP-001", "See payslips": "CAP-002"})
        self.w.run("decisions.py", "add", "p", "--about", "CAP-002", "--kind", "gap", "--choice", "carry-as-is")
        # a re-run renames the first capability and loses the second: the first keeps its id by its evidence
        out = self.render_map([cap("Approve or reject a request", mgr={"files": ["src/approve.ts"], "screens": ["ApproveScreen"],
                                                                      "evidence": "src/approve.ts:9"}),
                               cap("View pay documents", mgr={"files": ["src/pay-docs.ts"], "evidence": "src/pay-docs.ts:1"})])
        self.assertEqual(self.ids()["Approve or reject a request"], "CAP-001")
        self.assertEqual(self.ids()["View pay documents"], "CAP-003")
        self.assertIn("CAP-002", out.stdout)
        caps = self.w.json("analysis", "p", "capabilities.json")
        self.assertEqual([r["id"] for r in caps["retired"]], ["CAP-002"])
        self.assertIn("DEC-001 (gap)", caps["retired"][0]["referencedBy"])
        # a person says which new capability the old id is: it moves over, and nothing is retired
        self.w.put_json("analysis/p/map_aliases.json", {"CAP-002": "View pay documents"})
        self.w.run("render.py", "capabilities", "p")
        self.assertEqual(self.ids()["View pay documents"], "CAP-002")
        self.assertEqual(self.w.json("analysis", "p", "capabilities.json")["retired"], [])

    def test_retired_ids_a_person_let_go_and_reworded_rules(self):
        self.render_map([cap("Approve a request", mgr={"files": ["src/approve.ts"], "evidence": "src/approve.ts:1"}),
                         cap("Old export", mgr={"files": ["src/export.ts"], "evidence": "src/export.ts:1"})])
        self.w.run("decisions.py", "add", "p", "--about", "CAP-002", "--kind", "gap", "--choice", "drop")
        self.render_map([cap("Approve a request", mgr={"files": ["src/approve.ts"], "evidence": "src/approve.ts:1"})])
        self.assertEqual(self.w.json("analysis", "p", "capabilities.json")["retired"], [], "the person's own drop keeps nothing alive")
        # a reworded rule keeps its id by its citation, so the decision about it stays attached
        self.w.put_json("analysis/p/rules_result.json", {"rules": [rule("Comment needed to reject", source="src/approve.ts:10-20")]})
        self.w.run("render.py", "rules", "p")
        rid = self.w.json("analysis", "p", "rules.json")["rules"][0]["id"]
        self.w.run("decisions.py", "add", "p", "--about", rid, "--kind", "rule", "--choice", "wrong", "--note", "fixed on purpose")
        self.w.put_json("analysis/p/rules_result.json", {"rules": [rule("A reject needs a comment", source="src/approve.ts:11-20")]})
        self.w.run("render.py", "rules", "p")
        rules = self.w.json("analysis", "p", "rules.json")
        self.assertEqual(rules["rules"][0]["id"], rid)
        self.assertEqual(rules["retired"], [])
        # a rule that is really gone, with a decision about it, is reported until a person lets it go
        self.w.put_json("analysis/p/rules_result.json", {"rules": [rule("Something else", source="src/other.ts:1-2")]})
        out = self.w.run("render.py", "rules", "p")
        self.assertIn(rid, out.stdout)
        self.assertEqual([r["id"] for r in self.w.json("analysis", "p", "rules.json")["retired"]], [rid])
        self.w.put_json("analysis/p/rules_aliases.json", {rid: None})
        self.w.run("render.py", "rules", "p")
        self.assertEqual(self.w.json("analysis", "p", "rules.json")["retired"], [])

    def test_a_conflict_whose_rule_names_do_not_resolve_is_still_asked(self):
        self.render_map([cap("Approve a request")])
        self.w.put_json("analysis/p/rules_result.json", {"rules": [rule("Comment required on reject"), rule("No comment", app="emp")],
                                                         "conflicts": [{"capability": "CAP-001", "difference": "one asks for a comment",
                                                                        "rules": [{"app": "mgr", "name": "Comment required on a reject"},
                                                                                  {"app": "emp", "name": "Totally unrelated wording"}]}]})
        self.w.run("render.py", "rules", "p")
        conf = self.w.json("analysis", "p", "rules.json")["conflicts"][0]
        self.assertEqual(len(conf["rules"]), 1, "the paraphrased mgr name resolves, the other does not")
        self.assertTrue(conf["key"].startswith("CAP-001:conflict-"))
        qs = {(q["kind"], q["about"]) for q in self.open()}
        self.assertIn(("conflict", conf["key"]), qs)
        self.w.run("decisions.py", "add", "p", "--about", conf["key"], "--kind", "conflict", "--choice", "take:mgr")

    def test_two_conflicts_on_the_same_rules_are_two_questions(self):
        self.render_map([cap("See a day")])
        self.w.put_json("analysis/p/rules_result.json", {"rules": [rule("Tags pending only"), rule("Tags every status", app="emp")],
                                                         "conflicts": [{"capability": "CAP-001", "difference": "which statuses get a tag",
                                                                        "rules": [{"app": "mgr", "name": "Tags pending only"}, {"app": "emp", "name": "Tags every status"}]},
                                                                       {"capability": "CAP-001", "difference": "the colour of the pending tag",
                                                                        "rules": [{"app": "mgr", "name": "Tags pending only"}, {"app": "emp", "name": "Tags every status"}]}]})
        self.w.run("render.py", "rules", "p")
        keys = [c["key"] for c in self.w.json("analysis", "p", "rules.json")["conflicts"]]
        self.assertEqual(len(set(keys)), 2, keys)
        asked = [q["about"] for q in self.open() if q["kind"] == "conflict" and q["about"].startswith("CAP-001:")]
        self.assertEqual(sorted(asked), sorted(keys))
        for key, app in zip(keys, ("emp", "mgr")):
            self.w.run("decisions.py", "add", "p", "--about", key, "--kind", "conflict", "--choice", f"take:{app}")
        self.assertEqual([q for q in self.open() if q["kind"] == "conflict" and q["about"].startswith("CAP-001:")], [])

    def test_native_api_questions_use_keys_a_person_can_answer(self):
        self.render_map([cap("Approve a request")])
        self.w.put_json("analysis/p/evidence/api-parity.json", {"capabilities": {"CAP-001": {"missing": ["GET /x/{} (android)", "GET /x/{} (ios)"]}}})
        api = [q for q in self.open() if q["kind"] == "api"]
        self.assertEqual([q["about"] for q in api], ["CAP-001:GET /x/{}"])
        self.w.run("decisions.py", "add", "p", "--about", "CAP-001:GET /x/{}", "--kind", "api", "--choice", "dropped")
        self.assertEqual([q for q in self.open() if q["kind"] == "api"], [])

    def test_rules_no_referee_checked_or_no_capability_owns(self):
        self.render_map([cap("Approve a request")])
        self.w.put_json("analysis/p/rules_result.json", {
            "rules": [rule("Orphan limit", capability=None, priority="P0"), rule("Toast", suspectedDefect="shows twice")],
            "unverified": [rule("Unchecked rounding", why="no referee verdict")]})
        self.w.run("render.py", "rules", "p")
        rules = {r["name"]: r for r in self.w.json("analysis", "p", "rules.json")["rules"]}
        self.assertEqual(rules["Unchecked rounding"]["confidence"], "Low", "kept, never silently lost")
        self.assertIn("No referee could check", rules["Unchecked rounding"]["question"])
        qs = {(q["kind"], q["about"]): q for q in self.open()}
        orphan = rules["Orphan limit"]["id"]
        self.assertEqual(qs[("attach", orphan)]["priority"], 2)
        self.assertEqual(qs[("rule", rules["Toast"]["id"])]["priority"], 3, "a P1 defect is asked when its capability is built")
        self.w.run("decisions.py", "add", "p", "--about", orphan, "--kind", "attach", "--choice", "CAP-001")
        self.w.run("render.py", "rules", "p")
        self.assertEqual({r["name"]: r["capability"] for r in self.w.json("analysis", "p", "rules.json")["rules"]}["Orphan limit"], "CAP-001")

    def test_platform_items_that_existing_users_depend_on_block(self):
        self.render_map([cap("Approve a request")])
        self.w.run("render.py", "platform", "p")
        items = {i["name"]: i for i in self.w.json("analysis", "p", "platform.json")["items"]}
        self.assertIn("App extension: share", items)
        qs = {q["about"]: q["priority"] for q in self.open() if q["kind"] == "platform"}
        self.assertEqual(qs[items["App extension: share"]["id"]], 2)
        self.assertEqual(qs[items["App groups"]["id"]], 2)
        self.assertEqual(qs[items["Permission: NSCameraUsageDescription"]["id"]], 4)


class Status(unittest.TestCase):
    """The next command, from a program that is set up to the brief."""

    def setUp(self):
        self.w = w = Workspace().init()
        w.run("workspace.py", "intent", "p", "--stack", "react-native", "--store", "new-listing", "--platforms", "ios")
        w.run("inventory.py", "p", "--all")
        for name in ("PREFLIGHT.md", "ASSESSMENT.md", "CONTINUITY.md"):
            helpers.write(w.path("analysis", "p"), name, "x\n")
        w.put_json("analysis/p/map_result.json", {"capabilities": [cap("Approve a request"), cap("See payslips"), cap("Export")]})
        w.run("render.py", "capabilities", "p")
        w.run("render.py", "platform", "p")
        w.put_json("analysis/p/rules_result.json", {"rules": []})
        w.run("render.py", "rules", "p")
        items = w.json("analysis", "p", "platform.json")["items"]
        w.put_json("answers.json", [{"about": i["id"], "kind": "platform", "choice": "keep"} for i in items if i["newApp"] == "decide"])
        w.run("decisions.py", "add-json", "p", w.path("answers.json"))
        helpers.write(w.path("analysis", "p"), "FUSION_BRIEF.md", """
            # Brief
            #### Phase 0 — Foundation
            Command: /app-fusion:fuse-scaffold
            Exit criteria:
            - [ ] the app builds
            #### Phase 1 — Approvals
            Command: /app-fusion:fuse-build
            Capabilities: CAP-001
            #### Phase 2 — Pay
            Command: /app-fusion:fuse-build
            Capabilities: CAP-002, CAP-003
        """)

    def tearDown(self):
        self.w.close()

    def next(self):
        return json.loads(self.w.run("status.py", "p", "--json").stdout)["next"]

    def test_approval_its_scope_and_the_goal(self):
        self.assertIn("fuse-brief p approve", self.next()["command"])
        self.w.run("signoff.py", "p", "brief", "--by", "Kari Nordmann", "--covers", "Phase 0, Phase 1")
        self.assertEqual(self.next()["command"], "/app-fusion:fuse-scaffold p")
        app = self.w.path("new-app", "p")
        helpers.write(app, "docs/fusion/SCAFFOLD.md", "done\n")
        self.assertEqual(self.next()["command"], "/app-fusion:fuse-build p CAP-001")
        helpers.write(app, "src/a.ts", "export const a = 1\n")
        helpers.write(app, "docs/fusion/CAP-001.md", "## Files\n- `src/a.ts`\n")
        self.assertEqual(self.next()["command"], "/app-fusion:fuse-verify p CAP-001")
        self.w.run("fusion_proof.py", "p", "CAP-001", check=False)
        self.assertEqual(self.next()["command"], "/app-fusion:fuse-build p CAP-001", "NOT PROVEN: fix it")
        v = self.w.json("analysis", "p", "VERIFICATION.json")
        v["capabilities"]["CAP-001"]["verdict"] = "PROVEN"
        self.w.put_json("analysis/p/VERIFICATION.json", v)
        step = self.next()
        self.assertIn("fuse-brief p approve", step["command"], "Phase 2 is outside the approval")
        self.assertIn("Phase 2", step["reason"])
        # a changed brief voids the approval
        with open(self.w.path("analysis", "p", "FUSION_BRIEF.md"), "a", encoding="utf-8") as fh:
            fh.write("\nA late change.\n")
        self.assertIn("changed after it was approved", self.next()["reason"])
        self.w.run("workspace.py", "intent", "p", "--goal", "understand")
        self.w.run("signoff.py", "p", "brief", "--by", "Kari Nordmann")
        self.assertTrue(self.next()["command"].startswith("(done)"), "understanding ends with the approved brief")

    def test_accepted_partial_proof_ticked_brief_and_a_dirty_legacy_app(self):
        self.w.run("signoff.py", "p", "brief", "--by", "Kari Nordmann", "--covers", "Phase 0, Phase 1")
        app = self.w.path("new-app", "p")
        helpers.write(app, "docs/fusion/SCAFFOLD.md", "done\n")
        helpers.write(app, "src/a.ts", "export const a = 1\n")
        helpers.write(app, "docs/fusion/CAP-001.md", "## Files\n- `src/a.ts`\n")
        self.w.run("fusion_proof.py", "p", check=False)
        v = self.w.json("analysis", "p", "VERIFICATION.json")
        v["capabilities"]["CAP-001"]["verdict"] = "PARTLY PROVEN"  # say the Android journey cannot run here
        self.w.put_json("analysis/p/VERIFICATION.json", v)
        self.assertEqual(self.next()["command"], "/app-fusion:fuse-build p CAP-001")
        self.w.run("signoff.py", "p", "proof", "--by", "Kari Nordmann", "--caps", "CAP-001", "--accept", "no emulator in CI yet")
        self.assertIn("fuse-brief p approve", self.next()["command"], "a signed, accepted partial proof is settled")
        # ticking a met criterion or proposing a revision keeps the approval
        path = self.w.path("analysis", "p", "FUSION_BRIEF.md")
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text.replace("- [ ] the app builds", "- [x] the app builds\nProposed revision: split Phase 2 by domain"))
        self.assertNotIn("changed after it was approved", self.next()["reason"])
        # a legacy checkout someone changed stops everything, with a step a person can take
        with open(self.w.path("legacy", "mgr", "package.json"), "a", encoding="utf-8") as fh:
            fh.write("\n")
        step = self.next()
        self.assertIn("restore legacy/mgr", step["command"])


if __name__ == "__main__":
    unittest.main()
