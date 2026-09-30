#!/usr/bin/env python3
"""PreToolUse guard: the legacy apps are never edited, the judge's inputs are written only by the scripts, and a
person's decisions and sign-offs are recorded only with that person's yes.

Reads the hook input (JSON on stdin), from Claude Code or from Devin, which names its tools differently. It finds the
fusion workspace(s) from the project folder, the shell's folder, the path a file tool writes and the paths a shell
command names, walking up and one level down, so it works when the agent was started above or inside the workspace.
Outside every workspace with analysis/*/program.json it does nothing. Inside one:
  - a file write (Claude Code's Edit, Write, MultiEdit, NotebookEdit; Devin's edit, write, notebook_edit and every file
    an apply_patch adds, updates, deletes or moves to) whose path resolves under legacy/<app>, or under the real
    directory a legacy link points to, is denied; paths are compared without regard to case on macOS and Windows;
  - the shell is Claude Code's Bash, Devin's exec (in its workdir) and the text Devin's write_to_process types;
  - a write to what the proof reads is denied, by a file tool or from the shell: analysis/<program>/program.json,
    DECISIONS.*, SIGNOFF.json, VERIFICATION.*, capabilities.json, capability_index.json, rules.json,
    traceability.json, platform.json, design/placeholders.json and everything under evidence/ except screenshots and
    logs (evidence/shots, evidence/logs), the folders that hold them (analysis/<program>, evidence/, design/) and any
    folder above them (rm -rf . at the workspace root). The scripts that own them write them: test results come
    only from `evidence.py run` and `canary.py run`;
  - the shell is read the way a shell reads it: operators (; && || | &) and new lines split the command, shell
    keywords (do, then, if ...) are stepped over, `cd` and `pushd` move the folder for what follows, every redirect
    form (> >> >| 2> &> ...) names a target, `sh -c`, `bash -lc` and `eval` are read inside, a script a shell or an
    interpreter runs is read when it is a file outside this plugin, a script piped into a shell is "unsure",
    heredocs and inline code (python -c, python -, node -e ...) are scanned for the paths they open and whether they
    write or spawn a process, `xargs` takes the paths of the command before the pipe, `find -exec` is read for the
    command it runs, and `dd of=`, `curl -o`, `tar -C`, `sed -i`, `perl -pi`, package managers, build tools,
    formatters with --fix or --write, and git (with -C, --git-dir, --work-tree) name their targets;
  - a shell command that records a person's decision or sign-off (decisions.py add|add-json, signoff.py
    brief|proof|visual, workspace.py intent, figma_index.py placeholders, also as `python -m <module>` or code that
    imports one) is sent to the person to approve, so a model can never answer for them or exempt its own work;
  - a git command that can rewrite the judge's inputs, run in the repository that holds the analysis folder
    (checkout/restore of them, stash, reset, clean, switch, pull, merge, rebase ...), is sent to the person; the same
    commands in another repository (the new app) pass;
  - a shell command that writes into a legacy path is sent to the person to approve: redirects, file writers, build
    tools and package managers run inside it, formatters, patch, inline code writing relative paths there;
  - a write whose target the guard cannot resolve (a variable, a substitution, a brace expansion, a cd into an
    unknown folder, a script piped into a shell) is sent to the person when the command also names a judged file, a
    legacy path or the analysis folder: unsure is asked, never silently allowed. Reads (cat, jq, grep, git
    status/log/diff, copies out of legacy, zipping analysis into /tmp) pass silently.
Set the plugin option guard=false (or APP_FUSION_GUARD=false where plugin options do not exist) to turn it off.
Standard library only.
"""

import glob
import json
import os
import re
import shlex
import sys

WRITE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit", "edit", "write", "notebook_edit"}  # Claude Code, Devin
PATCH_TOOLS = {"apply_patch"}
SHELL_TOOLS = {"Bash", "exec", "write_to_process"}
PATCH_FILE = re.compile(r"^\*\*\* (?:(?:Add|Update|Delete) File|Move to): (.+?)\s*$", re.M)
WRITE_VERBS = {"rm", "rmdir", "mv", "cp", "tee", "touch", "truncate", "chmod", "chown", "ln", "mkdir", "install", "rsync",
               "unzip", "patch", "dd", "shred", "tar", "curl", "wget", "zip", "gunzip", "gzip", "ditto", "xattr", "bzip2", "xz"}
DEST_LAST = {"cp", "rsync", "install", "ln", "ditto"}
RECURSIVE = {"rm", "rmdir", "mv", "cp", "rsync", "install", "ln", "ditto", "tar", "unzip", "dd", "find", "chmod", "chown"}
SHELLS = {"sh", "bash", "zsh", "dash", "ksh", "fish"}
SHELL_C = re.compile(r"^-[A-Za-z]*c[A-Za-z]*$")
SHELL_KEYWORDS = {"do", "then", "else", "elif", "if", "while", "until", "!", "time", "coproc", "function", "["}
WRAPPERS = {"sudo", "doas", "env", "command", "nohup", "time", "nice", "exec", "caffeinate", "stdbuf", "builtin"}
INTERPRETERS = {"python", "python2", "python3", "node", "nodejs", "perl", "ruby", "osascript", "deno", "bun"}
INLINE_FLAGS = {"-c", "-e", "-E", "--eval", "-p", "--print"}
GIT_WRITES = {"commit", "checkout", "reset", "clean", "stash", "apply", "am", "merge", "rebase", "pull", "restore", "switch",
              "rm", "mv", "add", "cherry-pick", "revert", "tag", "branch", "worktree", "gc", "prune", "fetch", "init", "push",
              "update-ref", "symbolic-ref", "filter-branch", "submodule", "lfs", "notes", "replace", "sparse-checkout",
              "checkout-index", "read-tree", "write-tree", "update-index", "pack-refs", "reflog", "bisect", "remote", "config"}
GIT_READ_FORMS = {"branch": {"--show-current", "--list", "-l", "-a", "-r", "-v", "-vv", "--contains", "--merged", "--no-merged",
                             "--points-at", "--format"},
                  "tag": {"-l", "--list", "-n", "--contains", "--points-at", "--format"}, "stash": {"list", "show"},
                  "worktree": {"list"}, "fetch": {"--dry-run"}, "remote": {"-v", "show", "get-url"},
                  "submodule": {"status", "summary", "foreach"}, "lfs": {"ls-files", "status", "env", "version", "logs"},
                  "reflog": {"show"}, "notes": {"list", "show"}, "sparse-checkout": {"list"}, "bisect": {"log", "visualize", "view"},
                  "config": {"--get", "--list", "-l", "--get-all", "--get-regexp", "--show-origin", "--show-scope"}}
GIT_READ_WHEN_BARE = {"branch", "tag", "worktree", "remote", "reflog", "config", "lfs"}
# git commands that can rewrite files of the repository they run in (the judge's inputs live in the workspace repo)
GIT_REWRITES = {"checkout", "restore", "reset", "stash", "clean", "switch", "pull", "merge", "rebase", "revert", "cherry-pick", "am", "apply",
                "filter-branch", "read-tree", "checkout-index"}
GIT_WHOLE_TREE = {"stash", "reset", "clean", "switch", "pull", "merge", "rebase", "revert", "cherry-pick", "am", "apply", "filter-branch",
                  "read-tree", "checkout-index"}
PKG_VERBS = {"npm", "yarn", "pnpm", "bun"}
PKG_READS = {"ls", "list", "view", "info", "why", "outdated", "-v", "--version", "help", "--help", "-h", "test", "t", "jest", "audit",
             "explain", "licenses", "bin", "root", "prefix", "start", "config", "cache"}
PKG_RUN_READS = {"test", "lint", "typecheck", "tsc", "check", "start", "storybook"}
PKG_DIR_OPTS = {"--prefix", "--cwd", "-C", "--project-directory", "-p", "--project-dir", "--dir", "--filter"}
# build tools and formatters that write into the folder they run in: None = always, a set = when one of these appears
BUILD_WRITES = {"gradlew": None, "gradle": None, "carthage": None, "tuist": None, "make": None, "cmake": None, "fastlane": None,
                "swiftformat": None, "black": None, "isort": None, "patch": None,
                "swift": {"build", "test", "package", "run"}, "flutter": {"pub", "build", "test", "clean", "create", "gen-l10n", "run"},
                "dart": {"pub", "run", "compile", "format"}, "pod": {"install", "update", "deintegrate", "repo"},
                "bundle": {"install", "update", "exec"}, "swiftlint": {"--fix", "autocorrect"}, "eslint": {"--fix"},
                "prettier": {"--write", "-w"}, "rubocop": {"-a", "-A", "--autocorrect", "--auto-correct"}, "gofmt": {"-w"},
                "ktlint": {"-F", "--format"}, "biome": {"--write", "--fix"}}
XCODEBUILD_READS = {"-list", "-showsdks", "-version", "-showBuildSettings", "-showdestinations", "-usage", "-help"}

JUDGED = re.compile(r"^(?:program\.json|DECISIONS\.(?:json|md)|SIGNOFF\.json|VERIFICATION\.(?:json|md)|capabilities\.json|"
                    r"capability_index\.json|rules\.json|traceability\.json|platform\.json|design/placeholders\.json|evidence/.+)$")
# screenshots and logs are written by simulators, Maestro and tee from the shell; everything else under evidence/ by the scripts
RUN_OUTPUT = re.compile(r"^evidence/(?:shots|logs)(?:/.+)?$")
JUDGED_DIRS = re.compile(r"^(?:evidence(?:/(?!shots|logs).*)?|design)$")
JUDGED_WORDS = re.compile(r"program\.json|DECISIONS\.(?:json|md)|SIGNOFF\.json|VERIFICATION\.(?:json|md)|capabilities\.json|"
                          r"capability_index\.json|rules\.json|traceability\.json|platform\.json|placeholders\.json|test-runs\.json|"
                          r"\bevidence/|\banalysis/", re.I)
RECORDS = {"decisions": {"add", "add-json"}, "signoff": {"brief", "proof", "visual"}, "workspace": {"intent"},
           "figma_index": {"placeholders"}}
# code that writes files, or that spawns a process which may: a read (open(path), json.load, print) never matches
CODE_WRITES = re.compile(r"""open\s*\([^)]*['"](?:[wax]|r\+|[wa]b|[wa]\+)['"]|os\.open\s*\(|write_text|write_bytes|writeFile|appendFile|"""
                         r"""createWriteStream|os\.(?:remove|unlink|rename|replace|rmdir|makedirs|mkdir|truncate|"""
                         r"""chmod|link|symlink|system|popen)|shutil\.|subprocess|child_process|execSync|spawnSync|\bspawn\s*\(|"""
                         r"""\bunlink(?:Sync)?\s*\(|\brename(?:Sync)?\s*\(|\brmSync|\bmkdirSync|\bcopyFile|\bcpSync|\bwriteSync|"""
                         r"""\bopenSync|\btruncateSync|fs\.promises\.(?:write|unlink|rename|rm|mkdir|copy)|\.unlink\(\)|\.touch\(\)|"""
                         r""">\s*[\w./$]|\bFile\.(?:write|delete|open)|\bFileUtils|\bIO\.write""")
SHELL_WRITES = re.compile(r"\b(?:rm|mv|cp|tee|dd|truncate|install|rsync|ditto|touch|mkdir|patch)\b|>\s*\S|\bsed\s+-i|\bperl\s+-p?i")
PATHISH = re.compile(r"(?:~|\$\w+|\$\(pwd\)|\.{1,2})?/?(?:[\w.$@{}-]+/)*(?:analysis|legacy|ANALYSIS|LEGACY|Analysis|Legacy)/[\w./${}@-]*|/[\w./${}@-]{2,}")
CAT_SUBST = re.compile(r"\$\(\s*cat\s+([^\s)]+)\s*\)|`\s*cat\s+([^\s`]+)\s*`")
REDIRECT = re.compile(r"^(?:\d*>>?\|?|&>>?|\d*<>)$")
DUP = re.compile(r"^(?:\d*>&|\d*<&|>&\d*|<&\d*)$")
OPERATORS = {";", ";;", "&&", "||", "|", "|&", "&", "(", ")", "{", "}", "\n"}
CASE_FOLD = sys.platform in ("darwin", "win32")
MAX_DEPTH = 3
MAX_GLOB = 200
MAX_SCRIPT = 262_144
PLUGIN_ROOT = os.path.realpath(os.environ.get("CLAUDE_PLUGIN_ROOT") or os.environ.get("DEVIN_PLUGIN_ROOT")
                               or os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def fold(path):
    return path.lower() if CASE_FOLD else path


def under(path, root):
    p, r = fold(path), fold(root)
    return p == r or p.startswith(r + os.sep)


def decide(decision, reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": decision,
                                             "permissionDecisionReason": reason}}))
    sys.exit(0)


# ---------------------------------------------------------------- paths

def resolve(path, cwd):
    """Absolute, symlink-resolved form of a path that may not exist yet (resolve the deepest existing ancestor)."""
    p = os.path.expanduser(path)
    if not os.path.isabs(p):
        p = os.path.join(cwd, p)
    p = os.path.normpath(p)
    head, tail = p, []
    while head and not os.path.exists(head):
        head, part = os.path.split(head)
        tail.insert(0, part)
        if head == os.path.dirname(head):
            break
    real = os.path.realpath(head) if head else head
    return os.path.normpath(os.path.join(real, *tail)) if tail else real


def literal(token):
    """False when the shell would still change the token: a variable, a substitution, a brace expansion."""
    return not re.search(r"\$|`|\{[^}]*\}", token)


def targets_of(token, cwd):
    """(resolved paths a token names, whether it was literal). A glob is expanded against cwd."""
    if not literal(token):
        return [], False
    if re.search(r"[*?\[]", token):
        pattern = os.path.expanduser(token)
        if not os.path.isabs(pattern):
            pattern = os.path.join(cwd, pattern)
        matches = glob.glob(pattern)[:MAX_GLOB]
        return [resolve(m, cwd) for m in matches] or [resolve(re.split(r"[*?\[]", token)[0] or ".", cwd)], True
    return [resolve(token, cwd)], True


def repo_top(path):
    """The git repository a folder belongs to, or None."""
    d = os.path.realpath(path)
    for _ in range(64):
        if os.path.exists(os.path.join(d, ".git")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent
    return None


# ---------------------------------------------------------------- the workspace(s)

def has_program(folder):
    analysis = os.path.join(folder, "analysis")
    try:
        return os.path.isdir(analysis) and any(os.path.isfile(os.path.join(analysis, n, "program.json")) for n in os.listdir(analysis))
    except OSError:
        return False


def find_workspaces(candidates):
    """Every folder with analysis/*/program.json above a candidate path, or one level below the first two."""
    found = []

    def add(folder):
        real = os.path.realpath(folder)
        if real not in found and has_program(real):
            found.append(real)

    for c in candidates:
        if not c:
            continue
        # the path as written and the path its links point to: a legacy link's target lies outside the workspace
        for variant in dict.fromkeys([os.path.normpath(c), os.path.realpath(c)]):
            d = variant if os.path.isdir(variant) else os.path.dirname(variant)
            seen = 0
            while d and seen < 64:
                add(d)
                parent = os.path.dirname(d)
                if parent == d:
                    break
                d, seen = parent, seen + 1
    for c in [x for x in candidates[:2] if x]:
        try:
            children = sorted(os.listdir(c))[:400]
        except OSError:
            continue
        for n in children:
            child = os.path.join(c, n)
            if os.path.isdir(child):
                add(child)
    return found


class Protected:
    """The legacy roots and analysis folders of every workspace found."""

    def __init__(self, workspaces):
        self.roots = {}  # real path -> app name
        self.analysis = []  # (real analysis folder, workspace)
        for ws in workspaces:
            self._legacy(ws)
            analysis = os.path.join(ws, "analysis")
            if os.path.isdir(analysis):
                self.analysis.append((os.path.realpath(analysis), ws))

    def _legacy(self, ws):
        analysis = os.path.join(ws, "analysis")
        try:
            programs = os.listdir(analysis)
        except OSError:
            programs = []
        for name in programs:
            prog = None
            try:
                with open(os.path.join(analysis, name, "program.json"), encoding="utf-8") as fh:
                    prog = json.load(fh)
            except (OSError, ValueError):
                continue
            apps = prog.get("apps") if isinstance(prog, dict) else None
            for app in apps if isinstance(apps, list) else []:
                try:
                    if not isinstance(app, dict):
                        continue
                    app_name = str(app.get("name") or "")
                    path = app.get("path") if isinstance(app.get("path"), str) else f"legacy/{app_name}"
                    link = os.path.join(ws, path)
                    self.roots[os.path.normpath(os.path.abspath(link))] = app_name
                    if os.path.exists(link):
                        self.roots[os.path.realpath(link)] = app_name
                    if isinstance(app.get("snapshotOf"), str):  # a snapshot's source repository is just as read-only
                        self.roots[os.path.realpath(app["snapshotOf"])] = app_name
                except (TypeError, ValueError, OSError):
                    continue
        legacy = os.path.join(ws, "legacy")
        if os.path.isdir(legacy):
            for entry in os.listdir(legacy):
                full = os.path.join(legacy, entry)
                self.roots.setdefault(os.path.normpath(full), entry)
                if os.path.exists(full):
                    self.roots.setdefault(os.path.realpath(full), entry)

    def legacy_app(self, path):
        for root, app in self.roots.items():
            if under(path, root):
                return app
        return None

    def judged(self, path):
        """("file", rel) for a judge's input, ("dir", rel) for a folder that holds them, else None."""
        for analysis, _ in self.analysis:
            if fold(path) == fold(analysis):
                return ("dir", "analysis")
            if not under(path, analysis):
                continue
            parts = path[len(analysis) + 1:].split(os.sep)
            program = parts[0]
            if not os.path.isfile(os.path.join(analysis, program, "program.json")):
                # case-folded: find the program folder as it is spelled on disk
                try:
                    program = next((n for n in os.listdir(analysis) if fold(n) == fold(program)
                                    and os.path.isfile(os.path.join(analysis, n, "program.json"))), None)
                except OSError:
                    program = None
                if not program:
                    continue
            rel = "/".join(parts[1:])
            if not rel:
                return ("dir", f"analysis/{program}")
            if RUN_OUTPUT.match(rel):
                return None
            if JUDGED.match(rel):
                return ("file", rel)
            if JUDGED_DIRS.match(rel):
                return ("dir", rel)
            if CASE_FOLD:  # the same names, spelled differently
                for pattern in (JUDGED, JUDGED_DIRS):
                    if re.match(pattern.pattern, rel, re.I) and not re.match(RUN_OUTPUT.pattern, rel, re.I):
                        return ("file" if pattern is JUDGED else "dir", rel)
        return None

    def holds(self, path):
        """What a folder above the protected paths contains: ("judged", analysis) or ("legacy", app), else None."""
        for analysis, _ in self.analysis:
            if under(analysis, path) and fold(analysis) != fold(path):
                return ("judged", "analysis")
        for root, app in self.roots.items():
            if under(root, path) and fold(root) != fold(path):
                return ("legacy", app)
        return None

    def in_workspace(self, path):
        return any(under(path, ws) for _, ws in self.analysis)

    def holds_analysis_repo(self, where):
        """True when a git command in `where` runs in the repository that holds an analysis folder."""
        top = repo_top(where)
        if top is None:
            return self.in_workspace(os.path.realpath(where))
        return any(under(analysis, top) for analysis, _ in self.analysis)

    def mentions(self, text):
        """True when the text names a judged file, the analysis folder, a legacy path or a protected real path."""
        if JUDGED_WORDS.search(text) or re.search(r"legacy/", text, re.I):
            return True
        return any(fold(root) in fold(text) for root in self.roots)


# ---------------------------------------------------------------- reading a shell command

def tokenize(command):
    command = command.replace("\r\n", "\n").replace("\n", " ; ")  # a new line starts a new command, like ;
    try:
        lex = shlex.shlex(command, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        lex.commenters = ""
        return list(lex)
    except ValueError:
        return command.split()


def segments(tokens):
    """[(argv, operator before it)] split on shell operators."""
    segs, cur, op = [], [], None
    for t in tokens:
        if t in OPERATORS:
            if cur:
                segs.append((cur, op))
                cur = []
            op = t
        else:
            cur.append(t)
    if cur:
        segs.append((cur, op))
    return segs


def split_redirects(argv):
    """(arguments, output targets, input files, heredoc?): redirect operators and their targets taken out."""
    args, targets, inputs, heredoc = [], [], [], False
    i = 0
    while i < len(argv):
        t = argv[i]
        if t in ("<<", "<<-", "<<<"):
            heredoc = heredoc or t != "<<<"
            i += 2
            continue
        if DUP.match(t):
            i += 2 if t.endswith("&") else 1
            continue
        if REDIRECT.match(t) and i + 1 < len(argv):
            target = argv[i + 1]
            if not target.startswith("&") and target not in ("/dev/null", "/dev/stdout", "/dev/stderr", "/dev/tty"):
                targets.append(target)
            i += 2
            continue
        if t == "<" and i + 1 < len(argv):  # input redirect: a read, but a shell may run what it reads
            inputs.append(argv[i + 1])
            i += 2
            continue
        if re.match(r"^\d+$", t) and i + 1 < len(argv) and (REDIRECT.match(argv[i + 1]) or DUP.match(argv[i + 1])):
            i += 1  # the fd number before an operator
            continue
        args.append(t)
        i += 1
    return args, targets, inputs, heredoc


def strip_wrappers(argv):
    while argv:
        head = os.path.basename(argv[0])
        if re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", argv[0]) or head in SHELL_KEYWORDS:
            argv = argv[1:]
        elif head in WRAPPERS:
            argv = argv[1:]
            while argv and argv[0].startswith("-") and head in ("env", "sudo", "nice", "nohup", "stdbuf", "time"):
                argv = argv[1:]
        else:
            break
    return argv


class Findings:
    def __init__(self):
        self.deny, self.ask, self.unsure = [], [], []

    def add(self, kind, reason):
        getattr(self, kind).append(reason)


def classify_write(prot, path, what, f, recursive=False):
    """A write to a resolved path: deny for a judged file or folder (or a folder above them, for a recursive verb),
    ask for a legacy app (or a folder above one)."""
    j = prot.judged(path)
    if j:
        f.add("deny", f"{what} {j[1]}, " + ("an input of the proof, written only by its script" if j[0] == "file" else
                                            "a folder that holds the proof's inputs"))
        return True
    app = prot.legacy_app(path)
    if app:
        f.add("ask", f"{what} legacy/{app}: the legacy apps are read-only for this work")
        return True
    if recursive:
        held = prot.holds(path)
        if held and held[0] == "judged":
            f.add("deny", f"{what} a folder above {held[1]}, which holds the proof's inputs")
            return True
        if held:
            f.add("ask", f"{what} a folder above legacy/{held[1]}: the legacy apps are read-only for this work")
            return True
    return False


def scan_code(code, cwd, prot, f, label, shell=False):
    """Inline code, a heredoc body or a script file: the paths it names, and whether it writes or spawns."""
    writes = bool(CODE_WRITES.search(code)) or (shell and bool(SHELL_WRITES.search(code)))
    hits = False
    for m in PATHISH.finditer(code):
        frag = m.group(0).strip("'\"")
        if not frag or frag in ("/", "//"):
            continue
        paths, lit = targets_of(frag, cwd)
        if not lit:
            if writes:
                f.add("unsure", f"{label} names {frag}, which the guard cannot resolve, and writes files")
            continue
        for p in paths:
            if writes:
                hits = classify_write(prot, p, f"{label} writes", f, recursive=True) or hits
    if writes and not hits:
        # relative paths: the code writes where the shell stands
        app = prot.legacy_app(cwd)
        if app:
            f.add("ask", f"{label} writes files while the shell is in legacy/{app}")
        elif prot.judged(cwd):
            f.add("ask", f"{label} writes files while the shell is in {prot.judged(cwd)[1]}, which holds the proof's inputs")
    for module, subs in RECORDS.items():
        if re.search(rf"\b{module}\b", code) and (re.search(r"\bmain\s*\(|sys\.argv|__main__|import|require\(", code)
                                                    and any(re.search(rf"\b{re.escape(s)}\b", code) for s in subs)):
            f.add("ask", f"{label} runs {module}.py's recording of a person's answer")
    return hits


def scan_script(token, cwd, prot, f, label):
    """A script file a shell or an interpreter is about to run: read it, unless it is this plugin's own."""
    paths, lit = targets_of(token, cwd)
    if not lit:
        f.add("unsure", f"{label} runs a script whose path the guard cannot resolve")
        return
    for p in paths:
        if under(p, PLUGIN_ROOT) or not os.path.isfile(p):
            continue
        try:
            if os.path.getsize(p) > MAX_SCRIPT:
                f.add("unsure", f"{label} runs a large script the guard did not read ({os.path.basename(p)})")
                continue
            with open(p, encoding="utf-8", errors="replace") as fh:
                code = fh.read()
        except OSError:
            continue
        scan_code(code, cwd, prot, f, f"{label} (script {os.path.basename(p)})", shell=True)


def git_repo_and_sub(argv):
    """(the repository path option, the subcommand, its arguments) of a git command."""
    repo, i = None, 1
    while i < len(argv) and argv[i].startswith("-"):
        a = argv[i]
        if a in ("-C", "--git-dir", "--work-tree") and i + 1 < len(argv):
            repo, i = argv[i + 1], i + 2
        elif a.startswith("--git-dir=") or a.startswith("--work-tree="):
            repo, i = a.split("=", 1)[1], i + 1
        elif a == "-c" and i + 1 < len(argv):
            i += 2
        else:
            i += 1
    sub = argv[i] if i < len(argv) else None
    return repo, sub, argv[i + 1:] if sub else []


def git_reads(sub, rest):
    """True for the read-only forms of a git write command."""
    if sub in GIT_READ_FORMS and any(a in GIT_READ_FORMS[sub] for a in rest):
        return True
    if sub in GIT_READ_WHEN_BARE and not rest:
        return True
    if sub == "stash" and rest and rest[0] in GIT_READ_FORMS["stash"]:
        return True
    if sub == "config":  # `git config user.name` reads; a value, --unset, --add or --edit writes
        positional = [a for a in rest if not a.startswith("-")]
        return len(positional) < 2 and not any(a in ("--unset", "--unset-all", "--add", "--replace-all", "--edit", "-e", "--rename-section",
                                                     "--remove-section") for a in rest)
    return False


def tool_dir(args, cwd):
    """The folder a package manager or build tool works in: an option's value, else the shell's folder."""
    for i, a in enumerate(args[:-1]):
        if a in PKG_DIR_OPTS:
            paths, lit = targets_of(args[i + 1], cwd)
            return paths[0] if lit and paths else None
    for a in args:
        if any(a.startswith(o + "=") for o in PKG_DIR_OPTS):
            paths, lit = targets_of(a.split("=", 1)[1], cwd)
            return paths[0] if lit and paths else None
    return cwd


def build_writes(verb, args):
    """True when a package manager, build tool or formatter would write into its folder."""
    rest = args[1:]
    if verb in PKG_VERBS:
        sub = next((a for a in rest if not a.startswith("-")), None)
        if sub is None:
            return not any(a in ("-v", "--version", "-h", "--help") for a in rest)  # bare `yarn` installs
        if sub == "run":
            script = next((a for a in rest[rest.index("run") + 1:] if not a.startswith("-")), None)
            return script not in PKG_RUN_READS
        return sub not in PKG_READS
    if verb == "npx":
        tool = next((a for a in rest if not a.startswith("-")), None)
        return bool(tool) and tool in BUILD_WRITES and build_writes(tool, args[args.index(tool):])
    if verb == "xcodebuild":
        return not any(a in XCODEBUILD_READS for a in rest)
    if verb in BUILD_WRITES:
        spec = BUILD_WRITES[verb]
        return spec is None or any(a in spec for a in rest)
    return False


def check_segment(argv, op, cwd, prot, f, prev_paths, depth, raw):
    """One simple command. Returns (new cwd or None when it cannot be known, the protected paths it mentioned)."""
    args, redirects, inputs, heredoc = split_redirects(argv)
    args = strip_wrappers(args)
    verb = os.path.basename(args[0]) if args else ""
    mentioned = []
    for tgt in redirects:
        paths, lit = targets_of(tgt, cwd)
        if not lit:
            f.add("unsure", f"redirects output into {tgt}, which the guard cannot resolve")
        for p in paths:
            classify_write(prot, p, "the command redirects output into", f)
    if verb in ("cd", "pushd"):
        target = args[1] if len(args) > 1 else os.path.expanduser("~")
        if target == "-":
            return None, mentioned
        paths, lit = targets_of(target, cwd)
        return (paths[0] if lit and paths and os.path.isdir(paths[0]) else None), mentioned
    # what this segment names, for xargs and for the unsure rule
    for a in args[1:]:
        if "/" in a or a.endswith(".json") or a.endswith(".md"):
            paths, lit = targets_of(a.split("=", 1)[1] if re.match(r"^--?[\w-]+=", a) else a, cwd)
            mentioned += [p for p in paths if prot.judged(p) or prot.legacy_app(p)]
    if verb in SHELLS:
        if depth >= MAX_DEPTH:
            f.add("unsure", "nests shells deeper than the guard reads")
            return cwd, mentioned
        flag = next((a for a in args[1:4] if SHELL_C.match(a)), None)
        if flag:
            at = args.index(flag)
            inner = args[at + 1] if at + 1 < len(args) else ""
            for m in CAT_SUBST.finditer(inner):
                scan_script(m.group(1) or m.group(2), cwd, prot, f, f"`{verb} -c`")
            if not literal(inner):
                f.add("unsure", f"`{verb} -c` runs code the guard cannot read")
            check_command(inner, cwd, prot, f, depth + 1)
        else:
            script = next((a for a in args[1:] if not a.startswith("-")), None)
            if script:
                scan_script(script, cwd, prot, f, f"`{verb}`")
            if op in ("|", "|&") or "-s" in args[1:] or not script and not inputs:
                f.add("unsure", f"`{verb}` runs the commands piped into it")
            for src in inputs:
                scan_script(src, cwd, prot, f, f"`{verb}`")
        return cwd, mentioned
    if verb in ("source", "."):
        if len(args) > 1:
            scan_script(args[1], cwd, prot, f, "`source`")
        return cwd, mentioned
    if verb == "eval":
        if depth >= MAX_DEPTH:
            f.add("unsure", "nests shells deeper than the guard reads")
        else:
            inner = " ".join(args[1:])
            if not literal(inner):
                f.add("unsure", "`eval` runs code the guard cannot read")
            check_command(inner, cwd, prot, f, depth + 1)
        return cwd, mentioned
    if verb in ("perl", "ruby") and any(a.startswith("-pi") or a.startswith("-i") for a in args[1:4]):
        positional = [x for x in args[1:] if not x.startswith("-")]
        for a in positional[1:] if "-e" in args[1:4] or "-E" in args[1:4] else positional:
            paths, lit = targets_of(a, cwd)
            if not lit:
                f.add("unsure", f"an in-place edit changes {a}, which the guard cannot resolve")
            for p in paths:
                classify_write(prot, p, "an in-place edit would change", f)
        return cwd, mentioned
    if verb in INTERPRETERS or re.match(r"^python\d(\.\d+)?$", verb):
        flags = [a for a in args[1:4] if a in INLINE_FLAGS]
        stdin = "-" in args[1:3] or (heredoc and not any(not a.startswith("-") for a in args[1:2]))
        if flags or stdin or heredoc or (inputs and len(args) == 1):
            code = ""
            if flags:
                at = args.index(flags[0])
                code = " ".join(args[at + 1:])
            if heredoc or stdin:
                code += "\n" + (raw.split("\n", 1)[1] if "\n" in raw else "")
            scan_code(code, cwd, prot, f, f"inline {verb} code")
            for src in inputs:
                scan_script(src, cwd, prot, f, f"`{verb}`")
            return cwd, mentioned
        script = os.path.basename(args[1]) if len(args) > 1 else ""
        module = args[args.index("-m") + 1] if "-m" in args[:3] and args.index("-m") + 1 < len(args) else None
        name = module or re.sub(r"\.py$", "", script)
        if name in RECORDS:
            rest = args[2:] if not module else args[args.index("-m") + 2:]
            if any(r in RECORDS[name] for r in rest):
                f.add("ask", f"this records a person's decision or sign-off ({name}.py {next(r for r in rest if r in RECORDS[name])})")
            elif any(not literal(r) for r in rest):
                f.add("ask", f"this runs {name}.py with an argument the guard cannot read, so it may record a person's answer")
        elif not module and len(args) > 1 and not args[1].startswith("-"):
            scan_script(args[1], cwd, prot, f, f"`{verb}`")
        return cwd, mentioned
    if verb == "git":
        repo, sub, rest = git_repo_and_sub(args)
        if sub in GIT_WRITES and not git_reads(sub, rest):
            where = resolve(repo, cwd) if repo else cwd
            app = prot.legacy_app(where)
            if app:
                f.add("ask", f"`git {sub}` would change the legacy/{app} repository (fetching or committing writes its refs)")
            elif sub in GIT_REWRITES and prot.holds_analysis_repo(where):
                pathspecs = [a for a in rest if not a.startswith("-")]
                creates = sub == "switch" and any(a in ("-c", "-C", "--create", "--force-create") for a in rest)
                whole = not pathspecs or "." in pathspecs or (sub in GIT_WHOLE_TREE and not creates)
                named = [p for a in pathspecs for p in targets_of(a, where)[0] if prot.judged(p)]
                if named or whole:
                    f.add("ask", f"`git {sub}` in the workspace can rewrite the proof's inputs (decisions, sign-offs, evidence, "
                                 "catalogs): approve only if a person wants that")
        return cwd, mentioned
    if verb == "find":
        options_at = next((k for k, a in enumerate(args[1:]) if a.startswith("-")), len(args) - 1)
        paths = args[1:1 + options_at]
        execs = [os.path.basename(args[i + 1]) for i, a in enumerate(args[:-1]) if a in ("-exec", "-execdir", "-ok", "-okdir")]
        writing = "-delete" in args or any(e in WRITE_VERBS or e in SHELLS or e in INTERPRETERS or e in ("sed", "perl", "git", "xargs")
                                           for e in execs)
        if writing:
            for a in paths or ["."]:
                for p in targets_of(a, cwd)[0]:
                    classify_write(prot, p, "`find` would change files under", f, recursive=True)
        return cwd, mentioned
    if verb == "xargs":
        inner = strip_wrappers([a for a in args[1:] if not a.startswith("-")])
        if inner and (os.path.basename(inner[0]) in WRITE_VERBS or os.path.basename(inner[0]) in ("sed", "perl", "git")):
            for p in prev_paths:
                classify_write(prot, p, f"`xargs {os.path.basename(inner[0])}` would change", f, recursive=True)
            if not prev_paths and op in ("|", "|&"):
                f.add("unsure", f"`xargs {os.path.basename(inner[0])}` changes whatever the pipe lists")
        return cwd, mentioned
    if verb == "sed" and any(a.startswith("-i") or a.startswith("--in-place") for a in args[1:5]):
        files = [a for a in args[1:] if not a.startswith("-")]
        if not any(a in ("-e", "-f") for a in args) and files:
            files = files[1:]  # the first non-option argument is the script
        for a in files:
            paths, lit = targets_of(a, cwd)
            if not lit:
                f.add("unsure", f"`sed -i` edits {a}, which the guard cannot resolve")
            for p in paths:
                classify_write(prot, p, "`sed -i` would edit", f)
        return cwd, mentioned
    if verb in PKG_VERBS or verb == "npx" or verb == "xcodebuild" or verb in BUILD_WRITES:
        if build_writes(verb, args):
            where = tool_dir(args, cwd)
            if where is None:
                f.add("unsure", f"`{verb}` works in a folder the guard cannot resolve")
            else:
                app = prot.legacy_app(where)
                if app:
                    f.add("ask", f"`{verb}` would write into legacy/{app} (build output, dependencies, lock files or formatted sources)")
        if verb != "patch":
            return cwd, mentioned
    if verb in WRITE_VERBS:
        targets = write_targets(verb, args, cwd)
        for a in targets:
            paths, lit = targets_of(a, cwd)
            if not lit:
                f.add("unsure", f"`{verb}` writes {a}, which the guard cannot resolve")
            for p in paths:
                classify_write(prot, p, f"`{verb}` would change", f, recursive=verb in RECURSIVE)
        return cwd, mentioned
    return cwd, mentioned


def write_targets(verb, args, cwd):
    """The arguments a writing command changes."""
    rest = args[1:]
    if verb == "dd":
        return [a.split("=", 1)[1] for a in rest if a.startswith("of=")]
    if verb == "curl":
        out = [rest[i + 1] for i, a in enumerate(rest[:-1]) if a in ("-o", "--output", "--output-dir")]
        return out + (["."] if any(a in ("-O", "--remote-name") for a in rest) else [])
    if verb == "wget":
        out = [rest[i + 1] for i, a in enumerate(rest[:-1]) if a in ("-O", "-P", "--output-document", "--directory-prefix")]
        return out or ["."]
    if verb == "tar":
        flags = "".join(a for a in rest if re.match(r"^-?[a-zA-Z]+$", a))
        dirs = [rest[i + 1] for i, a in enumerate(rest[:-1]) if a in ("-C", "--directory")] + \
               [a.split("=", 1)[1] for a in rest if a.startswith("--directory=")]
        if "x" in flags or "--extract" in rest:
            return dirs or ["."]
        if any(c in flags for c in "cru") or any(a in rest for a in ("--create", "--append", "--update")):
            return [rest[i + 1] for i, a in enumerate(rest[:-1]) if a in ("-f", "--file")] + [a.split("=", 1)[1] for a in rest if a.startswith("--file=")]
        return []
    if verb == "unzip":
        return [rest[i + 1] for i, a in enumerate(rest[:-1]) if a == "-d"] or ["."]
    positional = [a for a in rest if not a.startswith("-")]
    if verb == "zip":
        return positional[:1]  # the archive; what follows is read
    if verb == "patch":
        return positional or ["."]
    if verb == "xattr":
        return positional[1:] if any(a in ("-w", "-d", "-c") for a in rest) else []
    if verb in DEST_LAST:
        return positional[-1:]
    if verb == "mv":
        return positional  # moving a protected folder away changes it too
    return positional


def check_command(command, cwd, prot, f, depth=0):
    """Every segment of a shell command, with cd tracked and pipes remembered for xargs."""
    tokens = tokenize(command)
    cur = cwd
    prev_paths = []
    for argv, op in segments(tokens):
        new_cwd, mentioned = check_segment(argv, op, cur, prot, f, prev_paths if op in ("|", "|&") else [], depth, command)
        if new_cwd is None:  # a `cd` whose target the guard cannot resolve: what follows runs somewhere unknown
            f.add("unsure", "changes into a folder the guard cannot resolve")
        else:
            cur = new_cwd
        prev_paths = mentioned


# ---------------------------------------------------------------- main

def shell_input(tool, args):
    """The shell text of a call: Bash's and exec's command, or what write_to_process types (its keys as new lines)."""
    if tool == "write_to_process":
        text = args.get("text_input") or args.get("bytes_input")
        return re.sub(r"<(?:CR|LF)>", "\n", text) if isinstance(text, str) else None
    command = args.get("command")
    return command if isinstance(command, str) else None


def main():
    guard = os.environ.get("CLAUDE_PLUGIN_OPTION_GUARD") or os.environ.get("APP_FUSION_GUARD") or "true"
    if guard.strip().lower() in ("false", "0", "off", "no"):
        return
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return
    if not isinstance(data, dict):
        return
    tool = data.get("tool_name")
    args = data.get("tool_input") if isinstance(data.get("tool_input"), dict) else {}
    project = os.environ.get("CLAUDE_PROJECT_DIR") or os.environ.get("DEVIN_PROJECT_DIR") or ""
    cwd = data.get("cwd") if isinstance(data.get("cwd"), str) and data.get("cwd") else (project or os.getcwd())
    if tool == "exec" and isinstance(args.get("workdir"), str) and args["workdir"]:
        cwd = os.path.join(cwd, os.path.expanduser(args["workdir"]))  # Devin's exec runs where workdir says
    candidates = [project or cwd, cwd]
    lexical = lambda p: os.path.normpath(os.path.join(cwd, os.path.expanduser(p)))
    targets, command = [], None
    if tool in WRITE_TOOLS:
        target = args.get("file_path") or args.get("notebook_path") or args.get("path")
        targets = [target] if isinstance(target, str) and target else []
    elif tool in PATCH_TOOLS:
        targets = PATCH_FILE.findall("\n".join(v for v in args.values() if isinstance(v, str)))
    elif tool in SHELL_TOOLS:
        command = shell_input(tool, args)
    if not targets and command is None:
        return
    candidates += [lexical(t) for t in targets]
    if command:
        for t in tokenize(command)[:60]:
            if "/" in t and literal(t) and not re.search(r"[*?\[]", t):
                candidates.append(lexical(t.split("=", 1)[1] if re.match(r"^--?[\w-]+=", t) else t))
    workspaces = find_workspaces(candidates)
    if not workspaces:
        return
    prot = Protected(workspaces)
    for target in targets:
        full = resolve(target, cwd)
        app = prot.legacy_app(full)
        if app:
            decide("deny", f"App Fusion never edits a legacy app: {target} is inside legacy/{app}. Write analysis output "
                           "under analysis/<program>/ and new code under new-app/<program>/. (To change the legacy app "
                           "on purpose, do it outside this workspace or set the plugin option guard=false, "
                           "APP_FUSION_GUARD=false outside Claude Code.)")
        j = prot.judged(full)
        if j and j[0] == "file":
            decide("deny", f"App Fusion: {j[1]} is an input of the proof, written only by its script (decisions.py, signoff.py, "
                           "evidence.py run, canary.py, the parity scripts, render.py, trace.py). Edit the workflow result it is "
                           "rendered from (map_result.json, rules_result.json, trace_result.json) and render again, or run the script.")
    if command is None:
        return
    f = Findings()
    check_command(command, cwd, prot, f)
    if f.deny:
        decide("deny", "App Fusion: " + f.deny[0] + ". Run the script that owns it instead of writing it from the shell.")
    if f.ask:
        reason = f.ask[0]
        if "records a person" in reason or "recording of a person" in reason or "may record a person" in reason:
            decide("ask", f"App Fusion: {reason}. Approve only if these are that person's own answers, given in this session.")
        decide("ask", f"App Fusion guard: {reason}. Approve only if a person really wants this change.")
    if f.unsure and prot.mentions(command):
        decide("ask", f"App Fusion guard: this command {f.unsure[0]}, and it names a legacy path or an input of the proof. "
                      "The guard cannot tell where it writes: approve only if you can.")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:  # a guard bug must never block the session; the permission rules still apply
        sys.exit(0)
