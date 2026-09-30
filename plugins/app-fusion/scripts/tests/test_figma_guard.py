import json
import os
import subprocess
import sys
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer

import helpers
from helpers import Workspace

KEY = "C" * 22
PAGE_LIST = "No nodeId was provided.\n\nTop-level pages of the document:\n- 1:1: App screens\n- 2:1: -> Archive\n"
METADATA = """<canvas id="1:1" name="App screens" x="0" y="0" width="0" height="0">
  <section id="5:1" name="Approvals &amp; flow" x="0" y="0" width="2000" height="1000">
    <frame id="5:2" name="Approvals / List" x="0" y="0" width="390" height="844">
      <text id="5:3" name="Approvals" x="0" y="0" width="10" height="10" />
      <instance id="5:4" name="Button/Primary" x="0" y="0" width="10" height="10"><text id="5:5" name="Approve all" x="0" y="0" width="1" height="1"/></instance>
    </frame>
    <frame id="5:6" name="Approvals / Empty state" x="0" y="0" width="390" height="844" />
  </section>
  <frame id="5:7" name="Icons" x="0" y="0" width="120" height="120" />
</canvas>IMPORTANT: After you call this tool, you MUST call get_design_context"""


class FigmaIndex(unittest.TestCase):
    def setUp(self):
        self.w = Workspace(git=False).init()
        self.w.run("workspace.py", "init", "p", "--figma", f"https://www.figma.com/design/{KEY}/New-App?node-id=1-2")

    def tearDown(self):
        self.w.close()

    def test_pages_scope_build_plan_budget(self):
        w = self.w
        prog = w.json("analysis", "p", "program.json")
        self.assertEqual(prog["figma"][0]["fileKey"], KEY)
        pages_path = w.run("figma_index.py", "path", "p", KEY, "pages", "pages").stdout.strip()
        with open(w.path(pages_path), "w") as fh:
            fh.write(PAGE_LIST)
        w.run("figma_index.py", "pages", "p", KEY, w.path(pages_path), "--name", "New App")
        self.assertIn("-> Archive", w.run("figma_index.py", "plan", "p").stdout + json.dumps(w.json("analysis", "p", "design", "design.json")))
        w.run("figma_index.py", "scope", "p", KEY, "--pages", "1:1")
        plan = json.loads(w.run("figma_index.py", "plan", "p", "--json").stdout)
        self.assertEqual(plan["next"][0]["call"], "get_metadata")
        meta_path = w.run("figma_index.py", "path", "p", KEY, "1:1", "metadata").stdout.strip()
        with open(w.path(meta_path), "w") as fh:
            fh.write(METADATA)
        w.run("figma_index.py", "build", "p")
        d = w.json("analysis", "p", "design", "design.json")
        kinds = {s["name"]: s["kind"] for s in d["screens"]}
        self.assertEqual(kinds["Approvals / List"], "screen")
        self.assertEqual(kinds["Approvals / Empty state"], "state")
        self.assertEqual(kinds["Icons"], "component")
        lst = next(s for s in d["screens"] if s["name"] == "Approvals / List")
        self.assertEqual(lst["texts"], ["Approvals", "Approve all"])
        self.assertEqual(lst["section"], "Approvals & flow", "XML entities are unescaped")
        plan = json.loads(w.run("figma_index.py", "plan", "p", "--json").stdout)
        self.assertEqual([s["call"] for s in plan["next"]].count("get_screenshot"), 2, "screens and states, not components")
        # a cached screenshot is not planned again
        shot = w.run("figma_index.py", "path", "p", KEY, "5:2", "shot").stdout.strip()
        with open(w.path(shot), "wb") as fh:
            fh.write(b"\x89PNG")
        w.run("figma_index.py", "build", "p")
        plan = json.loads(w.run("figma_index.py", "plan", "p", "--json").stdout)
        self.assertEqual([s["call"] for s in plan["next"]].count("get_screenshot"), 1)
        b1 = json.loads(w.run("figma_index.py", "budget", "p", "--spend", "3").stdout)
        self.assertEqual(b1["spentToday"], 3)
        w.run("render.py", "design", "p")
        self.assertIn("Approvals / List", w.text("analysis", "p", "DESIGN_INVENTORY.md"))
        # path traversal in ids is refused
        self.assertNotEqual(w.run("figma_index.py", "path", "p", KEY, "../../x", "metadata", check=False).returncode, 0)
        self.assertNotEqual(w.run("figma_index.py", "path", "p", "short", "1:1", "metadata", check=False).returncode, 0)


class FakeFigma(BaseHTTPRequestHandler):
    seen_tokens = []

    def log_message(self, *a):
        pass

    def do_GET(self):
        FakeFigma.seen_tokens.append((self.path.split("?")[0], self.headers.get("X-Figma-Token")))
        path = self.path.split("?")[0]
        if path == f"/v1/files/{KEY}":
            body = {"name": "New App", "document": {"children": [{"id": "1:1", "name": "App screens"}, {"id": "2:1", "name": "Archive"}]}}
        elif path == f"/v1/files/{KEY}/nodes":
            body = {"nodes": {"1:1": {"document": {"id": "1:1", "name": "App screens", "children": [
                {"id": "5:2", "type": "FRAME", "name": "Approvals / List", "absoluteBoundingBox": {"width": 390, "height": 844},
                 "children": [{"type": "TEXT", "characters": "Approve all"}, {"type": "INSTANCE", "name": "Button/Primary", "children": []}]},
                {"id": "6:1", "type": "SECTION", "name": "Flow", "children": [
                    {"id": "6:2", "type": "FRAME", "name": "Details", "absoluteBoundingBox": {"width": 390, "height": 844},
                     "children": [{"type": "TEXT", "characters": "Comment"}]}]}]}}}}
        elif path == f"/v1/images/{KEY}":
            port = self.server.server_address[1]
            body = {"images": {"5:2": f"http://127.0.0.1:{port}/img/5-2.png", "6:2": f"http://127.0.0.1:{port}/img/6-2.png"}}
        elif path.startswith("/img/"):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"\x89PNG fake")
            return
        elif path == f"/v1/files/{KEY}/variables/local":
            body = {"meta": {"variableCollections": {"c1": {"defaultModeId": "m1"}}, "variables": {
                "v1": {"name": "g-surface/primary", "variableCollectionId": "c1", "valuesByMode": {"m1": {"r": 1, "g": 1, "b": 1, "a": 1}}},
                "v2": {"name": "g-text/body", "variableCollectionId": "c1", "valuesByMode": {"m1": {"type": "VARIABLE_ALIAS", "id": "v1"}}}}}}
        else:
            self.send_response(404)
            self.end_headers()
            return
        data = json.dumps(body).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data)


class FigmaRest(unittest.TestCase):
    def test_snapshot_against_a_fake_api(self):
        server = HTTPServer(("127.0.0.1", 0), FakeFigma)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        w = Workspace(git=False).init()
        try:
            env = {"FIGMA_TOKEN": "figd_secret_value", "FIGMA_API_BASE": f"http://127.0.0.1:{server.server_address[1]}"}
            w.run("figma_rest.py", "pages", "p", KEY, env=env)
            w.run("figma_index.py", "scope", "p", KEY, "--pages", "1:1")
            w.run("figma_rest.py", "snapshot", "p", KEY, "--images", env=env)
            d = w.json("analysis", "p", "design", "design.json")
            self.assertEqual(d["source"], "rest")
            names = {s["name"]: s for s in d["screens"]}
            self.assertEqual(names["Approvals / List"]["texts"], ["Approve all"])
            self.assertEqual(names["Details"]["section"], "Flow")
            self.assertTrue(all(s["shot"] for s in d["screens"]))
            self.assertEqual(d["tokens"]["colors"].get("g-text/body"), "#FFFFFF", "aliases resolved")
            api = [t for p, t in FakeFigma.seen_tokens if p.startswith("/v1/")]
            images = [t for p, t in FakeFigma.seen_tokens if p.startswith("/img/")]
            self.assertTrue(api and all(t == "figd_secret_value" for t in api), "API calls carry the token")
            self.assertTrue(images and all(t is None for t in images), "image downloads never send the token to another host")
            for dirpath, _, files in os.walk(w.path("analysis")):
                for f in files:
                    with open(os.path.join(dirpath, f), "rb") as fh:
                        self.assertNotIn(b"figd_secret_value", fh.read(), f"the token leaked into {f}")
            out = w.run("figma_rest.py", "pages", "p", KEY, check=False, env={"FIGMA_TOKEN": ""})
            self.assertEqual(out.returncode, 4)
        finally:
            server.shutdown()
            server.server_close()
            w.close()


class Guard(unittest.TestCase):
    def setUp(self):
        self.w = Workspace(git=False).init()

    def tearDown(self):
        self.w.close()

    def decide(self, tool, **tool_input):
        payload = json.dumps({"tool_name": tool, "tool_input": tool_input, "cwd": self.w.ws})
        out = subprocess.run([sys.executable, os.path.join(helpers.SCRIPTS, "guard.py")], input=payload, capture_output=True,
                             text=True, env={**os.environ, "CLAUDE_PROJECT_DIR": self.w.ws})
        self.assertEqual(out.returncode, 0)
        return json.loads(out.stdout)["hookSpecificOutput"]["permissionDecision"] if out.stdout.strip() else "allow"

    def test_decisions(self):
        w = self.w
        self.assertEqual(self.decide("Write", file_path="legacy/mgr/src/x.ts"), "deny")
        self.assertEqual(self.decide("Edit", file_path=os.path.join(w.ios, "Emp", "Info.plist")), "deny", "the real path too")
        self.assertEqual(self.decide("NotebookEdit", notebook_path="legacy/emp/x.ipynb"), "deny")
        self.assertEqual(self.decide("Write", file_path="analysis/p/x.md"), "allow")
        self.assertEqual(self.decide("Write", file_path="new-app/p/src/a.ts"), "allow")
        self.assertEqual(self.decide("Bash", command="grep -rn x legacy/mgr/src > /tmp/out.txt"), "allow")
        self.assertEqual(self.decide("Bash", command="git -C legacy/mgr log --oneline"), "allow")
        self.assertEqual(self.decide("Bash", command="cp legacy/mgr/package.json /tmp/p.json"), "allow")
        self.assertEqual(self.decide("Bash", command="echo x > legacy/mgr/README.md"), "ask")
        self.assertEqual(self.decide("Bash", command="cd legacy/emp && git checkout -b x"), "ask")
        self.assertEqual(self.decide("Bash", command="cd legacy/mgr && yarn install"), "ask")
        self.assertEqual(self.decide("Bash", command=f"rm -rf {w.rn}/node_modules"), "ask")
        self.assertEqual(self.decide("Bash", command="sed -i '' s/a/b/ legacy/mgr/package.json"), "ask")
        self.assertEqual(self.decide("Bash", command="cp /tmp/x legacy/mgr/x"), "ask")

    def test_the_judges_inputs_and_a_persons_records(self):
        for rel in ("DECISIONS.json", "DECISIONS.md", "SIGNOFF.json", "VERIFICATION.json", "capabilities.json", "rules.json",
                    "traceability.json", "platform.json", "design/placeholders.json", "evidence/test-runs.json",
                    "evidence/junit/CAP-001/run-1/unit.xml"):
            self.assertEqual(self.decide("Write", file_path=f"analysis/p/{rel}"), "deny", rel)
        for rel in ("map_result.json", "rules_result.json", "design/trace_result.json", "design/new_capabilities.json",
                    "VISUAL_REVIEW.md", "FUSION_BRIEF.md", "design/cache/K/1-2.metadata.xml"):
            self.assertEqual(self.decide("Write", file_path=f"analysis/p/{rel}"), "allow", rel)
        self.assertEqual(self.decide("Bash", command='python3 "/x/scripts/decisions.py" add-json p /tmp/a.json'), "ask")
        self.assertEqual(self.decide("Bash", command="python3 scripts/decisions.py add p --about CAP-001 --kind gap --choice drop"), "ask")
        self.assertEqual(self.decide("Bash", command="python3 scripts/signoff.py p brief --by Kari"), "ask")
        self.assertEqual(self.decide("Bash", command="python3 scripts/decisions.py open p --json"), "allow")
        self.assertEqual(self.decide("Bash", command="python3 scripts/signoff.py p show"), "allow")
        # the subcommand may come after other options; intent records the person's answers too
        self.assertEqual(self.decide("Bash", command="python3 scripts/signoff.py --workspace . p proof --by X --caps CAP-001"), "ask")
        self.assertEqual(self.decide("Bash", command="python3 scripts/signoff.py p --by X proof --caps CAP-001"), "ask")
        self.assertEqual(self.decide("Bash", command="python3 scripts/workspace.py intent p --platforms ios"), "ask")
        self.assertEqual(self.decide("Write", file_path="analysis/p/program.json"), "deny")
        # the shell cannot write the judge's inputs either; test results come from evidence.py run, never from a copy
        for cmd in ("echo '{}' > analysis/p/VERIFICATION.json", "cat x.json | tee analysis/p/SIGNOFF.json",
                    "cp /tmp/v.json analysis/p/evidence/test-runs.json",
                    "python3 -c \"open('analysis/p/SIGNOFF.json','w').write('{}')\"",
                    "npx jest 2>&1 | tee analysis/p/evidence/junit/verify/run-1/output.txt",
                    "cp build/test-results/TEST-a.xml analysis/p/evidence/junit/CAP-001/run-2/"):
            self.assertEqual(self.decide("Bash", command=cmd), "deny", cmd)
        for cmd in ("cat analysis/p/VERIFICATION.json", "jq . analysis/p/DECISIONS.json",
                    "python3 scripts/evidence.py run p --capability CAP-001 --name unit -- npx jest --ci",
                    "xcrun simctl io booted screenshot analysis/p/evidence/shots/CAP-001/list.png",
                    "npx jest 2>&1 | tee analysis/p/evidence/logs/jest.txt"):
            self.assertEqual(self.decide("Bash", command=cmd), "allow", cmd)
        self.assertEqual(self.decide("Write", file_path="analysis/p/evidence/logs/build.txt"), "allow", "logs and shots are not judged")

    def test_the_bypasses_the_review_found_are_closed(self):
        deny = lambda cmd: self.assertEqual(self.decide("Bash", command=cmd), "deny", cmd)
        ask = lambda cmd: self.assertEqual(self.decide("Bash", command=cmd), "ask", cmd)
        allow = lambda cmd: self.assertEqual(self.decide("Bash", command=cmd), "allow", cmd)
        # every redirect form, cd chains, wrappers, heredocs, other writers, and the folders that hold judged files
        deny("echo '{}' >| analysis/p/SIGNOFF.json")
        deny("echo x 2> analysis/p/DECISIONS.json")
        deny("echo x &> analysis/p/VERIFICATION.json")
        deny("cd analysis/p && echo '{}' > SIGNOFF.json")
        deny("cd analysis/p; echo '{}' > SIGNOFF.json")
        deny("sh -c 'cp /tmp/x analysis/p/SIGNOFF.json'")
        deny("bash -c \"echo x > analysis/p/rules.json\"")
        deny("python3 - <<'EOF'\nopen('analysis/p/SIGNOFF.json', 'w').write('{}')\nEOF")
        deny("cat > analysis/p/evidence/junit/CAP-001/run-1/unit.xml <<'EOF'\n<testsuite/>\nEOF")
        deny("rm -r analysis/p/evidence")
        deny("rm -rf analysis/p")
        deny("mv analysis/p analysis/q")
        deny("dd if=/tmp/x of=analysis/p/program.json")
        deny("curl -o analysis/p/DECISIONS.json https://example.com/x")
        deny("tar -C analysis/p -xf /tmp/x.tar")
        deny("perl -pi -e 's/a/b/' analysis/p/rules.json")
        deny("find analysis/p/evidence -name '*.xml' -delete")
        deny("sudo tee analysis/p/platform.json < /tmp/x")
        # a write whose target the guard cannot resolve, naming a judged file: asked, never silently allowed
        ask("F=analysis/p/SIGNOFF.json; echo '{}' > $F")
        ask("echo x > $(pwd)/analysis/p/DECISIONS.json")
        # git in the workspace can rewrite the judge's inputs; reading and committing cannot
        ask("git checkout -- analysis/p/DECISIONS.json")
        ask("git restore analysis/p/SIGNOFF.json")
        ask("git stash")
        ask("git reset --hard")
        allow("git status")
        allow("git add analysis/p && git commit -m x")
        allow("git log --oneline analysis/p/DECISIONS.json")
        allow("git diff analysis/p/rules.json")
        # the sign-off and decision gate
        ask("K=proof; python3 scripts/signoff.py p $K --by Dan --all-proven")
        ask("cd scripts && python3 -m decisions add p --about CAP-001 --kind gap --choice drop")
        ask("python3 -c \"import sys; sys.argv=['signoff.py','p','proof','--by','X']; import signoff; signoff.main()\"")
        # reads stay silent
        allow("python3 -c \"import json; print(json.load(open('analysis/p/DECISIONS.json')))\"")
        allow("node -e \"console.log(require('./analysis/p/rules.json').rules.length)\"")
        allow("cat analysis/p/SIGNOFF.json | jq .")
        allow("cp analysis/p/DECISIONS.json /tmp/backup.json")
        allow("ls -la analysis/p/evidence")
        allow("python3 scripts/decisions.py open p --json > /tmp/open.json")
        self.assertEqual(self.decide("Write", file_path="analysis/p/evidence/junit/CAP-001/run-1/unit.xml"), "deny")
        if sys.platform == "darwin":
            self.assertEqual(self.decide("Write", file_path="ANALYSIS/p/SIGNOFF.json"), "deny", "the file system ignores case")
            self.assertEqual(self.decide("Write", file_path="Legacy/mgr/x.ts"), "deny")
            deny("echo x > Analysis/p/DECISIONS.json")

    def test_legacy_writes_the_review_found_are_asked(self):
        ask = lambda cmd: self.assertEqual(self.decide("Bash", command=cmd), "ask", cmd)
        allow = lambda cmd: self.assertEqual(self.decide("Bash", command=cmd), "allow", cmd)
        ask("echo x >| legacy/mgr/a.ts")
        ask("python3 -c \"open('legacy/mgr/a.ts','w').write('x')\"")
        ask("node -e \"require('fs').writeFileSync('legacy/mgr/a.ts','x')\"")
        ask("cd legacy/mgr; rm package.json")
        ask("(cd legacy/mgr && echo x > a.ts)")
        ask("find legacy/mgr -name '*.ts' -delete")
        ask("ls legacy/mgr/src | xargs rm")
        ask("sh -c 'rm legacy/mgr/package.json'")
        ask("dd if=/dev/zero of=legacy/mgr/a.bin")
        ask("curl -o legacy/mgr/x.zip https://example.com/x.zip")
        ask("tar -C legacy/mgr -xf /tmp/x.tar")
        ask("git --git-dir=legacy/mgr/.git --work-tree=legacy/mgr reset --hard")
        ask("npm --prefix legacy/mgr install")
        ask("yarn --cwd legacy/mgr add x")
        ask("L=legacy/mgr; echo x > $L/a.ts")
        ask("echo x > $(pwd)/legacy/mgr/a.ts")
        ask("python3 - <<'EOF'\nopen('legacy/mgr/a.ts','w')\nEOF")
        ask("env FOO=1 cp /tmp/x legacy/mgr/x")
        # reads and writes elsewhere stay silent
        allow("git -C legacy/mgr branch --show-current")
        allow("git -C legacy/mgr tag -l")
        allow("git -C legacy/mgr stash list")
        allow("git -C legacy/mgr fetch --dry-run")
        allow("cd legacy/mgr && mkdir -p /tmp/x && rm /tmp/x/junk")
        allow("cd legacy/mgr && git log -3")
        allow("grep -rn foo legacy/mgr/src")
        allow("python3 -c \"print(open('legacy/mgr/package.json').read())\"")
        allow("cd new-app/p && yarn add left-pad")
        allow("npx jest --ci")

    def test_the_workspace_is_found_from_above_below_and_inside(self):
        w = self.w
        plugin_root = os.path.dirname(helpers.SCRIPTS)

        def run(payload, project, script="guard.py"):
            argv = [sys.executable, os.path.join(helpers.SCRIPTS, "guard.py")] if script == "guard.py" else ["sh", os.path.join(plugin_root, "hooks", "guard.sh")]
            out = subprocess.run(argv, input=json.dumps(payload), capture_output=True, text=True,
                                 env={**os.environ, "CLAUDE_PROJECT_DIR": project, "CLAUDE_PLUGIN_ROOT": plugin_root})
            self.assertEqual(out.returncode, 0, out.stderr)
            return json.loads(out.stdout)["hookSpecificOutput"]["permissionDecision"] if out.stdout.strip() else "allow"

        # Claude started one folder above the workspace
        above = {"tool_name": "Write", "tool_input": {"file_path": os.path.join(w.ws, "legacy", "mgr", "x.ts")}, "cwd": w.root}
        self.assertEqual(run(above, w.root), "deny")
        self.assertEqual(run({"tool_name": "Bash", "tool_input": {"command": f"echo x > {w.ws}/legacy/mgr/a.ts"}, "cwd": w.root}, w.root), "ask")
        self.assertEqual(run({"tool_name": "Bash", "tool_input": {"command": f"echo x > {w.ws}/analysis/p/SIGNOFF.json"}, "cwd": w.root}, w.root), "deny")
        # Claude started inside a subfolder of the workspace
        sub = os.path.join(w.ws, "new-app", "p")
        os.makedirs(sub, exist_ok=True)
        self.assertEqual(run({"tool_name": "Write", "tool_input": {"file_path": "../../legacy/mgr/x.ts"}, "cwd": sub}, sub), "deny")
        self.assertEqual(run({"tool_name": "Bash", "tool_input": {"command": "cp x ../../analysis/p/rules.json"}, "cwd": sub}, sub), "deny")
        # the shell gate runs python in those cases too, and stays out of the way elsewhere
        self.assertEqual(run(above, w.root, script="guard.sh"), "deny")
        self.assertEqual(run({"tool_name": "Write", "tool_input": {"file_path": "../../legacy/mgr/x.ts"}, "cwd": sub}, sub, script="guard.sh"), "deny")
        elsewhere = os.path.join(w.root, "elsewhere", "project")
        os.makedirs(elsewhere)
        self.assertEqual(run({"tool_name": "Bash", "tool_input": {"command": "rm -rf build"}, "cwd": elsewhere}, elsewhere, script="guard.sh"), "allow")

    def test_a_malformed_program_json_still_protects_the_legacy_links(self):
        self.w.put_json("analysis/p/program.json", {"program": "p", "apps": "not-a-list"})
        self.assertEqual(self.decide("Write", file_path="legacy/mgr/x.ts"), "deny")
        self.w.put_json("analysis/p/program.json", {"program": "p", "apps": [{"name": None, "path": 5}, "x"]})
        self.assertEqual(self.decide("Write", file_path="legacy/mgr/x.ts"), "deny")
        self.assertEqual(self.decide("Bash", command="echo x > analysis/p/DECISIONS.json"), "deny")

    def test_a_signature_needs_a_persons_name(self):
        w = self.w
        with open(w.path("analysis", "p", "FUSION_BRIEF.md"), "w", encoding="utf-8") as fh:
            fh.write("# brief\n")
        for bad in ("claude", "Claude Fable", "the assistant", "AI agent", "Dan; rm -rf x", "x", "", "gpt-5", "Copilot User"):
            out = w.run("signoff.py", "p", "brief", "--by", bad, check=False)
            self.assertNotEqual(out.returncode, 0, bad)
        w.run("signoff.py", "p", "brief", "--by", "Kari Nordmann")
        out = w.run("decisions.py", "add", "p", "--about", "CAP-001", "--kind", "gap", "--choice", "drop", "--by", "Claude", check=False)
        self.assertNotEqual(out.returncode, 0, "a decision is never recorded in a model's name")
        w.run("decisions.py", "add", "p", "--about", "CAP-001", "--kind", "gap", "--choice", "drop", "--by", "Kari Nordmann")

    def test_a_snapshots_source_is_protected_too(self):
        w = Workspace()
        try:
            w.run("workspace.py", "init", "s", "--source", f"mgr={w.rn}", "--snapshot")
            payload = json.dumps({"tool_name": "Write", "tool_input": {"file_path": os.path.join(w.rn, "src", "x.ts")}, "cwd": w.ws})
            out = subprocess.run([sys.executable, os.path.join(helpers.SCRIPTS, "guard.py")], input=payload, capture_output=True,
                                 text=True, env={**os.environ, "CLAUDE_PROJECT_DIR": w.ws})
            self.assertEqual(json.loads(out.stdout)["hookSpecificOutput"]["permissionDecision"], "deny")
        finally:
            w.close()

    def test_off_switch_and_outside_a_workspace(self):
        payload = json.dumps({"tool_name": "Write", "tool_input": {"file_path": "legacy/mgr/x"}, "cwd": self.w.ws})
        out = subprocess.run([sys.executable, os.path.join(helpers.SCRIPTS, "guard.py")], input=payload, capture_output=True, text=True,
                             env={**os.environ, "CLAUDE_PROJECT_DIR": self.w.ws, "CLAUDE_PLUGIN_OPTION_GUARD": "false"})
        self.assertEqual(out.stdout.strip(), "")
        elsewhere = os.path.join(self.w.root, "elsewhere")
        os.makedirs(elsewhere)
        payload = json.dumps({"tool_name": "Write", "tool_input": {"file_path": "legacy/mgr/x"}, "cwd": elsewhere})
        out = subprocess.run([sys.executable, os.path.join(helpers.SCRIPTS, "guard.py")], input=payload, capture_output=True, text=True,
                             env={**os.environ, "CLAUDE_PROJECT_DIR": elsewhere})
        self.assertEqual(out.stdout.strip(), "", "no workspace anywhere near: no-op")
        out = subprocess.run([sys.executable, os.path.join(helpers.SCRIPTS, "guard.py")], input="not json", capture_output=True, text=True)
        self.assertEqual((out.returncode, out.stdout.strip()), (0, ""), "garbage in: allow, never crash the session")


class XcresultJunit(unittest.TestCase):
    def test_convert_keeps_display_names_and_ids(self):
        sample = {"testNodes": [{"nodeType": "Test Plan", "name": "App", "children": [{"nodeType": "Unit test bundle", "name": "AppTests", "children": [
            {"nodeType": "Test Suite", "name": "CAP-012 mileage", "children": [
                {"nodeType": "Test Case", "name": "RULE-019 zero km is zero", "nodeIdentifier": "MileageSuite/zero()", "result": "Passed", "durationInSeconds": 0.1},
                {"nodeType": "Test Case", "name": "test_rule020()", "nodeIdentifier": "MileageSuite/test_rule020()", "result": "Failed",
                 "children": [{"nodeType": "Failure Message", "name": "x.swift:3: expected 1"}]},
                {"nodeType": "Test Case", "name": "skipped()", "nodeIdentifier": "MileageSuite/skipped()", "result": "Skipped"}]}]}]}]}
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            src = os.path.join(d, "t.json")
            with open(src, "w") as fh:
                json.dump(sample, fh)
            out = os.path.join(d, "j.xml")
            r = subprocess.run([sys.executable, os.path.join(helpers.SCRIPTS, "xcresult_junit.py"), src, out], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            from fusionlib import proofkit
            cases, _ = proofkit.junit_cases([out], d)
            by = {c["name"]: c for c in cases}
            self.assertEqual({c["status"] for c in cases}, {"passed", "failed", "skipped"})
            zero = next(c for c in cases if c["name"].startswith("RULE-019"))
            self.assertEqual(proofkit.case_ids(zero), {"RULE-019", "CAP-012"})
            self.assertIn("test_rule020()", by)


if __name__ == "__main__":
    unittest.main()
