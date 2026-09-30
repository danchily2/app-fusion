#!/usr/bin/env python3
"""PreToolUse guard: the legacy apps are never edited, the judge's inputs are written only by the scripts, and a
person's decisions and sign-offs are recorded only with that person's yes.

Reads the hook input (JSON on stdin). It finds the fusion workspace(s) from the project folder, the shell's folder,
the path a file tool writes and the paths a shell command names, walking up and one level down, so it works when
Claude was started above or inside the workspace. Outside every workspace with analysis/*/program.json it does
nothing. Inside one:
  - a file write (Edit, Write, MultiEdit, NotebookEdit) whose path resolves under legacy/<app>, or under the real
    directory a legacy link points to, is denied; paths are compared without regard to case on macOS and Windows;
  - a write to what the proof reads is denied, by a file tool or from the shell: analysis/<program>/program.json,
    DECISIONS.*, SIGNOFF.json, VERIFICATION.*, capabilities.json, capability_index.json, rules.json,
    traceability.json, platform.json, design/placeholders.json and everything under evidence/ except screenshots and
    logs (evidence/shots, evidence/logs), and the folders that hold them (analysis/<program>, evidence/, design/).
    The scripts that own them write them: test results come only from `evidence.py run` and `canary.py run`;
  - the shell is read the way a shell reads it: operators (; && || | &) split the command, `cd` moves the folder
    for what follows, every redirect form (> >> >| 2> &> ...) names a target, `sh -c`, `bash -c` and `eval` are read
    inside, heredocs and inline code (python -c, python -, node -e ...) are scanned for the paths they open and
    whether they write, `xargs` takes the paths of the command before the pipe, and `dd of=`, `curl -o`, `tar -C`,
    `find -delete`, `sed -i`, `perl -pi`, package managers and git write commands name their targets;
  - a shell command that records a person's decision or sign-off (decisions.py add|add-json, signoff.py
    brief|proof|visual, workspace.py intent, figma_index.py placeholders, also as `python -m <module>` or code that
    imports one) is sent to the person to approve, so a model can never answer for them or exempt its own work;
  - a git command in the workspace that can rewrite the judge's inputs (checkout/restore of them, stash, reset,
    clean, switch, pull, merge, rebase ...) is sent to the person to approve;
  - a shell command that writes into a legacy path is sent to the person to approve;
  - a write whose target the guard cannot resolve (a variable, a substitution, a brace expansion) is sent to the
    person when the command also names a judged file, a legacy path or the analysis folder: unsure is asked, never
    silently allowed. Reads (cat, jq, grep, git status/log/diff, copies out of legacy) pass silently.
Set the plugin option guard=false to turn it off. Standard library only.
"""

import glob
import json
import os
import re
import shlex
import sys

WRITE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
WRITE_VERBS = {"rm", "rmdir", "mv", "cp", "tee", "touch", "truncate", "chmod", "chown", "ln", "mkdir", "install", "rsync",
               "unzip", "patch", "dd", "shred", "tar", "curl", "wget", "zip", "gunzip", "gzip"}
DEST_LAST = {"cp", "rsync", "install", "ln"}
SHELLS = {"sh", "bash", "zsh", "dash", "ksh", "fish"}
WRAPPERS = {"sudo", "doas", "env", "command", "nohup", "time", "nice", "exec", "caffeinate", "stdbuf", "builtin"}
INTERPRETERS = {"python", "python2", "python3", "node", "nodejs", "perl", "ruby", "osascript", "deno", "bun"}
INLINE_FLAGS = {"-c", "-e", "-E", "--eval", "-p", "--print"}
GIT_WRITES = {"commit", "checkout", "reset", "clean", "stash", "apply", "am", "merge", "rebase", "pull", "restore", "switch",
              "rm", "mv", "add", "cherry-pick", "revert", "tag", "branch", "worktree", "gc", "prune", "fetch", "init", "push"}
GIT_READ_FORMS = {"branch": {"--show-current", "--list", "-l", "-a", "-r", "-v", "-vv", "--contains", "--merged", "--no-merged",
                             "--points-at", "--format"},
                  "tag": {"-l", "--list", "-n", "--contains", "--points-at", "--format"}, "stash": {"list", "show"},
                  "worktree": {"list"}, "fetch": {"--dry-run"}, "remote": {"-v", "show", "get-url"}}
# git commands that can rewrite files of the workspace (the judge's inputs live there, and people commit them)
GIT_REWRITES = {"checkout", "restore", "reset", "stash", "clean", "switch", "pull", "merge", "rebase", "revert", "cherry-pick", "am", "apply"}
PKG_WRITES = re.compile(r"\b(?:npm|yarn|pnpm|bun)\b[^|;&]*?\b(?:install|i|add|remove|ci|update|upgrade)\b|\bpod\b[^|;&]*?\b(?:install|update|deintegrate)\b|"
                        r"\bbundle\s+(?:install|update)\b|\bswift\s+package\s+(?:update|resolve|reset)\b|\bgradlew?\b[^|;&]*?\bclean\b|"
                        r"\bnpx\s+react-native\s+(?:upgrade|link)\b|\bfastlane\b")
PKG_DIR_OPTS = {"--prefix", "--cwd", "-C", "--project-directory", "-p", "--project-dir", "--dir"}

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
CODE_WRITES = re.compile(r"""open\s*\([^)]*['"](?:[wax]|r\+|[wa]b|[wa]\+)['"]|write_text|write_bytes|writeFile|appendFile|createWriteStream|"""
                         r"""\.write\s*\(|json\.dump\s*\(|os\.(?:remove|unlink|rename|replace|rmdir|makedirs|mkdir|truncate|chmod)|shutil\.|"""
                         r"""\bunlink(?:Sync)?\s*\(|\brename(?:Sync)?\s*\(|\brmSync|\bmkdirSync|\bcopyFile|\.unlink\(\)|\.touch\(\)|\.rename\(|"""
                         r""">\s*[\w./$]|\bFile\.(?:write|delete|open)|\bFileUtils|\bIO\.write""")
PATHISH = re.compile(r"(?:~|\$\w+|\$\(pwd\)|\.{1,2})?/?(?:[\w.$@{}-]+/)*(?:analysis|legacy|ANALYSIS|LEGACY|Analysis|Legacy)/[\w./${}@-]*|/[\w./${}@-]{2,}")
REDIRECT = re.compile(r"^(?:\d*>>?\|?|&>>?|\d*<>)$")
DUP = re.compile(r"^(?:\d*>&|\d*<&|>&\d*|<&\d*)$")
OPERATORS = {";", ";;", "&&", "||", "|", "|&", "&", "(", ")", "{", "}", "\n"}
CASE_FOLD = sys.platform in ("darwin", "win32")
MAX_DEPTH = 3
MAX_GLOB = 200


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

    def in_workspace(self, path):
        return any(under(path, ws) for _, ws in self.analysis)

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
    """(arguments, redirect targets, heredoc?): redirect operators and their targets taken out of the argument list."""
    args, targets, heredoc = [], [], False
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
        if t == "<" and i + 1 < len(argv):  # input redirect: a read
            i += 2
            continue
        if re.match(r"^\d+$", t) and i + 1 < len(argv) and (REDIRECT.match(argv[i + 1]) or DUP.match(argv[i + 1])):
            i += 1  # the fd number before an operator
            continue
        args.append(t)
        i += 1
    return args, targets, heredoc


def strip_wrappers(argv):
    while argv:
        head = os.path.basename(argv[0])
        if re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", argv[0]):
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


def classify_write(prot, path, what, f, legacy_word="would write into"):
    """A write to a resolved path: deny for a judged file or folder, ask for a legacy app."""
    j = prot.judged(path)
    if j:
        f.add("deny", f"{what} {j[1]}, " + ("an input of the proof, written only by its script" if j[0] == "file" else
                                            "a folder that holds the proof's inputs"))
        return True
    app = prot.legacy_app(path)
    if app:
        f.add("ask", f"{what} legacy/{app}: the legacy apps are read-only for this work")
        return True
    return False


def scan_code(code, cwd, prot, f, label):
    """Inline code or a heredoc body: the paths it names, and whether it writes."""
    writes = bool(CODE_WRITES.search(code))
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
                hits = classify_write(prot, p, f"{label} writes", f) or hits
    for module, subs in RECORDS.items():
        if re.search(rf"\b{module}\b", code) and (re.search(r"\bmain\s*\(|sys\.argv|__main__|import|require\(", code)
                                                    and any(re.search(rf"\b{re.escape(s)}\b", code) for s in subs)):
            f.add("ask", f"{label} runs {module}.py's recording of a person's answer")
    return hits


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


def check_segment(argv, op, cwd, prot, f, prev_paths, depth, raw):
    """One simple command. Returns (new cwd, the protected paths it mentioned)."""
    args, redirects, heredoc = split_redirects(argv)
    args = strip_wrappers(args)
    verb = os.path.basename(args[0]) if args else ""
    mentioned = []
    for tgt in redirects:
        paths, lit = targets_of(tgt, cwd)
        if not lit:
            f.add("unsure", f"redirects output into {tgt}, which the guard cannot resolve")
        for p in paths:
            classify_write(prot, p, "the command redirects output into", f)
    if verb == "cd":
        target = args[1] if len(args) > 1 else os.path.expanduser("~")
        paths, lit = targets_of(target, cwd)
        return (paths[0] if lit and paths else None), mentioned
    # what this segment names, for xargs and for the unsure rule
    for a in args[1:]:
        if "/" in a or a.endswith(".json") or a.endswith(".md"):
            paths, lit = targets_of(a.split("=", 1)[1] if re.match(r"^--?[\w-]+=", a) else a, cwd)
            mentioned += [p for p in paths if prot.judged(p) or prot.legacy_app(p)]
    if verb in SHELLS and depth < MAX_DEPTH:
        if "-c" in args:
            inner = args[args.index("-c") + 1] if args.index("-c") + 1 < len(args) else ""
            check_command(inner, cwd, prot, f, depth + 1)
        elif heredoc or (len(args) > 1 and args[1] == "-"):
            check_command(raw.split("\n", 1)[1] if "\n" in raw else "", cwd, prot, f, depth + 1)
        return cwd, mentioned
    if verb == "eval" and depth < MAX_DEPTH:
        check_command(" ".join(args[1:]), cwd, prot, f, depth + 1)
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
        if flags or stdin or heredoc:
            code = ""
            if flags:
                at = args.index(flags[0])
                code = " ".join(args[at + 1:])
            if heredoc or stdin:
                code += "\n" + (raw.split("\n", 1)[1] if "\n" in raw else "")
            scan_code(code, cwd, prot, f, f"inline {verb} code")
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
        return cwd, mentioned
    if verb == "git":
        repo, sub, rest = git_repo_and_sub(args)
        if sub in GIT_WRITES:
            read_form = sub in GIT_READ_FORMS and (any(a in GIT_READ_FORMS[sub] for a in rest) or (sub in ("branch", "tag", "worktree", "remote") and not rest)
                                                    or (sub == "stash" and rest and rest[0] in GIT_READ_FORMS["stash"]))
            if not read_form:
                where = resolve(repo, cwd) if repo else cwd
                app = prot.legacy_app(where)
                if app:
                    f.add("ask", f"`git {sub}` would change the legacy/{app} repository (fetching or committing writes its refs)")
                elif sub in GIT_REWRITES and prot.in_workspace(where):
                    pathspecs = [a for a in rest if not a.startswith("-")]
                    whole = not pathspecs or "." in pathspecs or sub in ("stash", "reset", "clean", "switch", "pull", "merge", "rebase",
                                                                            "revert", "cherry-pick", "am", "apply")
                    named = [p for a in pathspecs for p in targets_of(a, cwd)[0] if prot.judged(p)]
                    if named or whole:
                        f.add("ask", f"`git {sub}` in the workspace can rewrite the proof's inputs (decisions, sign-offs, evidence, "
                                     "catalogs): approve only if a person wants that")
        return cwd, mentioned
    if verb == "find":
        paths = [a for a in args[1:] if not a.startswith("-")]
        paths = paths[: next((k for k, a in enumerate(args[1:]) if a.startswith("-")), len(paths))]
        if any(a in ("-delete", "-exec", "-execdir", "-ok", "-okdir") for a in args):
            for a in paths:
                for p in targets_of(a, cwd)[0]:
                    classify_write(prot, p, "`find` would change files under", f)
        return cwd, mentioned
    if verb == "xargs":
        inner = strip_wrappers([a for a in args[1:] if not a.startswith("-")])
        if inner and (os.path.basename(inner[0]) in WRITE_VERBS or os.path.basename(inner[0]) in ("sed", "perl", "git")):
            for p in prev_paths:
                classify_write(prot, p, f"`xargs {os.path.basename(inner[0])}` would change", f)
            if not prev_paths and op in ("|", "|&"):
                f.add("unsure", f"`xargs {os.path.basename(inner[0])}` changes whatever the pipe lists")
        return cwd, mentioned
    if verb == "sed" and any(a.startswith("-i") or a == "--in-place" for a in args[1:5]):
        files = [a for a in args[1:] if not a.startswith("-")]
        if any(a in ("-e", "-f") for a in args) or not files:
            files = files
        else:
            files = files[1:]  # the first non-option argument is the script
        for a in files:
            paths, lit = targets_of(a, cwd)
            if not lit:
                f.add("unsure", f"`sed -i` edits {a}, which the guard cannot resolve")
            for p in paths:
                classify_write(prot, p, "`sed -i` would edit", f)
        return cwd, mentioned
    if verb in WRITE_VERBS:
        targets = write_targets(verb, args, cwd)
        for a in targets:
            paths, lit = targets_of(a, cwd)
            if not lit:
                f.add("unsure", f"`{verb}` writes {a}, which the guard cannot resolve")
            for p in paths:
                classify_write(prot, p, f"`{verb}` would change", f)
        return cwd, mentioned
    return cwd, mentioned


def write_targets(verb, args, cwd):
    """The arguments a writing command changes."""
    rest = args[1:]
    if verb == "dd":
        return [a.split("=", 1)[1] for a in rest if a.startswith("of=")]
    if verb == "curl":
        out = [rest[i + 1] for i, a in enumerate(rest[:-1]) if a in ("-o", "--output")]
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
    if verb in ("unzip",):
        return [rest[i + 1] for i, a in enumerate(rest[:-1]) if a == "-d"] or ["."]
    positional = [a for a in rest if not a.startswith("-")]
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
    unknown_cwd = False
    for argv, op in segments(tokens):
        new_cwd, mentioned = check_segment(argv, op, cur, prot, f, prev_paths if op in ("|", "|&") else [], depth, command)
        if new_cwd is None:  # a `cd` whose target the guard cannot resolve: what follows runs somewhere unknown
            unknown_cwd = True
            f.add("unsure", "changes into a folder the guard cannot resolve")
        else:
            cur = new_cwd
        prev_paths = mentioned
    if PKG_WRITES.search(command):
        where = cur
        tokens_flat = tokenize(command)
        for i, t in enumerate(tokens_flat[:-1]):
            if t in PKG_DIR_OPTS:
                where = targets_of(tokens_flat[i + 1], cwd)[0][0] if targets_of(tokens_flat[i + 1], cwd)[0] else where
            elif any(t.startswith(o + "=") for o in PKG_DIR_OPTS):
                where = targets_of(t.split("=", 1)[1], cwd)[0][0] if targets_of(t.split("=", 1)[1], cwd)[0] else where
        app = prot.legacy_app(where)
        if app:
            f.add("ask", f"a package manager would write into legacy/{app} (node_modules, Pods, lock files)")
    return unknown_cwd


# ---------------------------------------------------------------- main

def main():
    if (os.environ.get("CLAUDE_PLUGIN_OPTION_GUARD") or "true").strip().lower() in ("false", "0", "off", "no"):
        return
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return
    if not isinstance(data, dict):
        return
    tool = data.get("tool_name")
    args = data.get("tool_input") if isinstance(data.get("tool_input"), dict) else {}
    project = os.environ.get("CLAUDE_PROJECT_DIR") or ""
    cwd = data.get("cwd") if isinstance(data.get("cwd"), str) and data.get("cwd") else (project or os.getcwd())
    candidates = [project or cwd, cwd]
    lexical = lambda p: os.path.normpath(os.path.join(cwd, os.path.expanduser(p)))
    target = None
    if tool in WRITE_TOOLS:
        target = args.get("file_path") or args.get("notebook_path") or args.get("path")
        if not isinstance(target, str) or not target:
            return
        candidates.append(lexical(target))
    command = args.get("command") if tool == "Bash" else None
    if tool == "Bash" and not isinstance(command, str):
        return
    if command:
        for t in tokenize(command)[:60]:
            if "/" in t and literal(t) and not re.search(r"[*?\[]", t):
                candidates.append(lexical(t.split("=", 1)[1] if re.match(r"^--?[\w-]+=", t) else t))
    workspaces = find_workspaces(candidates)
    if not workspaces:
        return
    prot = Protected(workspaces)
    if tool in WRITE_TOOLS:
        full = resolve(target, cwd)
        app = prot.legacy_app(full)
        if app:
            decide("deny", f"App Fusion never edits a legacy app: {target} is inside legacy/{app}. Write analysis output "
                           "under analysis/<program>/ and new code under new-app/<program>/. (To change the legacy app "
                           "on purpose, do it outside this workspace or set the plugin option guard=false.)")
        j = prot.judged(full)
        if j and j[0] == "file":
            decide("deny", f"App Fusion: {j[1]} is an input of the proof, written only by its script (decisions.py, signoff.py, "
                           "evidence.py run, canary.py, the parity scripts, render.py, trace.py). Edit the workflow result it is "
                           "rendered from (map_result.json, rules_result.json, trace_result.json) and render again, or run the script.")
        return
    if tool != "Bash":
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
