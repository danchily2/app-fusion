#!/usr/bin/env python3
"""PreToolUse guard: the legacy apps are never edited, the judge's inputs are written only by the scripts, and a
person's decisions and sign-offs are recorded only with that person's yes.

Reads the hook input (JSON on stdin). Outside a workspace with analysis/*/program.json it does nothing. Inside one:
  - a file write (Edit, Write, MultiEdit, NotebookEdit) whose path resolves under legacy/<app>, or under the real
    directory a legacy link points to, is denied;
  - a write to what the proof reads is denied, by a file tool or from the shell (a redirect, cp/mv/tee/sed -i, or
    inline python -c / node -e code naming it): analysis/<program>/program.json, DECISIONS.*, SIGNOFF.json,
    VERIFICATION.*, capabilities.json, capability_index.json, rules.json, traceability.json, platform.json,
    design/placeholders.json and everything under evidence/. The scripts that own them write them;
  - a shell command that records a person's decision or sign-off (decisions.py add|add-json, signoff.py
    brief|proof|visual, workspace.py intent) or which design texts are sample data (figma_index.py placeholders) is
    sent to the person to approve, so a model can never answer for them or exempt its own work;
  - a shell command that writes into a legacy path (a redirect whose target is there, rm/mv/cp/tee/touch/sed -i/...
    with an argument there, a git or package-manager write run against it) is sent to the person to approve.
Anything the guard cannot parse is allowed through to the normal permission rules, never silently blocked.
Set the plugin option guard=false to turn it off. Standard library only.
"""

import json
import os
import re
import shlex
import sys

WRITE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
WRITE_VERBS = {"rm", "rmdir", "mv", "cp", "tee", "touch", "truncate", "chmod", "chown", "ln", "mkdir", "install", "rsync",
               "unzip", "patch", "dd", "shred"}
GIT_WRITES = {"commit", "checkout", "reset", "clean", "stash", "apply", "am", "merge", "rebase", "pull", "restore", "switch",
              "rm", "mv", "add", "cherry-pick", "revert", "tag", "branch", "worktree", "gc", "prune", "fetch", "init"}
PKG_WRITES = re.compile(r"\b(?:npm|yarn|pnpm|bun)\s+(?:install|i|add|remove|ci|update|upgrade)\b|\bpod\s+(?:install|update|deintegrate)\b|"
                        r"\bbundle\s+(?:install|update)\b|\bswift\s+package\s+(?:update|resolve|reset)\b|\bgradlew?\s+\S*clean\b|"
                        r"\bnpx\s+react-native\s+(?:upgrade|link)\b|\bfastlane\b")


JUDGED = re.compile(r"^(?:program\.json|DECISIONS\.(?:json|md)|SIGNOFF\.json|VERIFICATION\.(?:json|md)|capabilities\.json|"
                    r"capability_index\.json|rules\.json|traceability\.json|platform\.json|design/placeholders\.json|evidence/.+)$")
# a person's answers and signatures: the subcommand may come anywhere after the script name
RECORDS = re.compile(r"\bdecisions\.py\b[^|;&]*\s(?:add|add-json)\b|\bsignoff\.py\b[^|;&]*\s(?:brief|proof|visual)\b|"
                     r"\bfigma_index\.py\b[^|;&]*\splaceholders\b|\bworkspace\.py\b[^|;&]*\sintent\b")
INLINE_CODE = re.compile(r"\b(?:python3?|node|perl|ruby)\s+-(?:c|e)\b")


def judged_file(ws, path):
    """The path of a judge's input relative to analysis/<program>/ when `path` is one, else None."""
    analysis = os.path.realpath(os.path.join(ws, "analysis"))
    if not path.startswith(analysis + os.sep):
        return None
    parts = os.path.relpath(path, analysis).split(os.sep)
    if len(parts) < 2 or not os.path.isfile(os.path.join(analysis, parts[0], "program.json")):
        return None
    rel = "/".join(parts[1:])
    return rel if JUDGED.match(rel) else None


# test runners write their results into run folders from the shell (jest, swift test, maestro, tee, cp of Gradle XML):
# those stay writable from Bash; the file tools still cannot write them, so no result is typed by hand
RUN_OUTPUT = re.compile(r"^evidence/(?:(?:junit|maestro|canary)/.+/run-\d+(?:/.+)?|shots(?:/.+)?|logs(?:/.+)?)$")


def check_bash_judged(command, cwd, ws):
    """A judged file the command would write: a redirect into it, a write verb naming it, or inline code (python -c,
    node -e ...) that names it. Reads (cat, jq, grep) pass, and so do test results written into a run folder."""
    def judged(path):
        rel = judged_file(ws, resolve(path, cwd))
        return rel if rel and not RUN_OUTPUT.match(rel) else None

    try:
        tokens = shlex.split(command, posix=True)
    except ValueError:
        tokens = command.split()
    for m in re.finditer(r"(?<![0-9&<>])>>?\s*(\"[^\"]+\"|'[^']+'|[^\s;&|()]+)", command):
        rel = judged(m.group(1).strip("\"'"))
        if rel:
            return rel
    if INLINE_CODE.search(command):
        # inline code names paths inside its own string: look for them in the command text
        inline = [judged(m) for m in re.findall(r"[\w./~-]*analysis/[\w-]+/[\w./-]+", command)]
        if any(inline):
            return next(n for n in inline if n)
    named = [judged(t) for t in tokens if "/" in t or t.endswith(".json") or t.endswith(".md")]
    named = [n for n in named if n]
    if not named:
        return None
    for i, t in enumerate(tokens):
        verb = os.path.basename(t)
        if verb in WRITE_VERBS or (verb == "sed" and any(a.startswith("-i") for a in tokens[i + 1:i + 4])):
            rest = [a for a in tokens[i + 1:] if not a.startswith("-")]
            rest = rest[: next((k for k, a in enumerate(rest) if a in ("&&", "||", ";", "|")), len(rest))]
            targets = rest[-1:] if verb in ("cp", "rsync", "install", "ln") else rest
            hit = [judged(a) for a in targets]
            if any(hit):
                return next(h for h in hit if h)
    return None


def decide(decision, reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": decision,
                                             "permissionDecisionReason": reason}}))
    sys.exit(0)


def protected_roots(ws):
    roots = {}
    analysis = os.path.join(ws, "analysis")
    if not os.path.isdir(analysis):
        return roots
    for name in os.listdir(analysis):
        prog_path = os.path.join(analysis, name, "program.json")
        if not os.path.isfile(prog_path):
            continue
        try:
            prog = json.load(open(prog_path, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for app in prog.get("apps") or []:
            link = os.path.join(ws, app.get("path") or f"legacy/{app.get('name')}")
            roots[os.path.normpath(os.path.abspath(link))] = app.get("name")
            if os.path.exists(link):
                roots[os.path.realpath(link)] = app.get("name")
            if app.get("snapshotOf"):  # a snapshot's source repository is just as read-only
                roots[os.path.realpath(app["snapshotOf"])] = app.get("name")
    legacy = os.path.join(ws, "legacy")
    if os.path.isdir(legacy):
        for entry in os.listdir(legacy):
            full = os.path.join(legacy, entry)
            roots.setdefault(os.path.normpath(full), entry)
            if os.path.exists(full):
                roots.setdefault(os.path.realpath(full), entry)
    return roots


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


def inside(path, roots):
    for root, app in roots.items():
        if path == root or path.startswith(root + os.sep):
            return app
    return None


def check_bash(command, cwd, roots):
    try:
        tokens = shlex.split(command, posix=True)
    except ValueError:
        tokens = command.split()
    mentioned = [t for t in tokens if not t.startswith("-") and inside(resolve(t, cwd), roots)]
    cd_into = [tokens[i + 1] for i, t in enumerate(tokens[:-1]) if t == "cd" and inside(resolve(tokens[i + 1], cwd), roots)]
    for m in re.finditer(r"(?<![0-9&<>])>>?\s*(\"[^\"]+\"|'[^']+'|[^\s;&|()]+)", command):
        target = m.group(1).strip("\"'")
        if target.startswith("&") or target == "/dev/null":
            continue
        base = cd_into[-1] if cd_into else cwd
        app = inside(resolve(target, resolve(base, cwd) if cd_into else cwd), roots)
        if app:
            return f"the command redirects output into legacy/{app} ({target})"
    if not mentioned and not cd_into:
        return None
    app = inside(resolve((mentioned or cd_into)[0], cwd), roots)
    for i, t in enumerate(tokens):
        verb = os.path.basename(t)
        if verb in WRITE_VERBS:
            args = [a for a in tokens[i + 1:] if a not in ("&&", "||", ";", "|")]
            args = args[: next((k for k, a in enumerate(args) if a in ("&&", "||", ";", "|")), len(args))]
            if verb in ("cp", "rsync", "install", "ln") and args:
                dest = args[-1]
                if inside(resolve(dest, cwd), roots) or (cd_into and not os.path.isabs(dest)):
                    return f"`{verb}` would write into legacy/{app}"
            elif any(inside(resolve(a, cwd), roots) for a in args if not a.startswith("-")) or (cd_into and args):
                return f"`{verb}` would change files in legacy/{app}"
        if verb == "sed" and any(a.startswith("-i") or a == "--in-place" for a in tokens[i + 1:i + 4]):
            return f"`sed -i` would edit files in legacy/{app}"
        if verb in ("perl", "ruby") and any(a.startswith("-pi") or a.startswith("-i") for a in tokens[i + 1:i + 4]):
            return f"an in-place edit would change files in legacy/{app}"
        if verb == "git":
            rest = [a for a in tokens[i + 1:] if not a.startswith("-")]
            if "-C" in tokens[i + 1:i + 3]:
                rest = rest[1:]
            if rest and rest[0] in GIT_WRITES:
                return f"`git {rest[0]}` would change the legacy/{app} repository (fetching or committing writes its refs)"
    if PKG_WRITES.search(command):
        return f"a package manager would write into legacy/{app} (node_modules, Pods, lock files)"
    return None


def main():
    if (os.environ.get("CLAUDE_PLUGIN_OPTION_GUARD") or "true").strip().lower() in ("false", "0", "off", "no"):
        return
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return
    ws = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    roots = protected_roots(ws)
    if not roots:
        return
    tool = data.get("tool_name")
    args = data.get("tool_input") or {}
    cwd = data.get("cwd") or ws
    if tool in WRITE_TOOLS:
        target = args.get("file_path") or args.get("notebook_path") or args.get("path")
        if not target:
            return
        full = resolve(target, cwd)
        app = inside(full, roots)
        if app:
            decide("deny", f"App Fusion never edits a legacy app: {target} is inside legacy/{app}. Write analysis output "
                           "under analysis/<program>/ and new code under new-app/<program>/. (To change the legacy app "
                           "on purpose, do it outside this workspace or set the plugin option guard=false.)")
        judged = judged_file(os.path.realpath(ws), full)
        if judged:
            decide("deny", f"App Fusion: {judged} is an input of the proof, written only by its script (decisions.py, "
                           "signoff.py, evidence.py, canary.py, the parity scripts, render.py, trace.py). Edit the "
                           "workflow result it is rendered from (map_result.json, rules_result.json, trace_result.json) "
                           "and render again, or run the script.")
        return
    if tool == "Bash":
        command = args.get("command") or ""
        judged = check_bash_judged(command, cwd, os.path.realpath(ws))
        if judged:
            decide("deny", f"App Fusion: {judged} is an input of the proof, written only by its script. Run the script "
                           "that owns it instead of writing it from the shell.")
        if RECORDS.search(command):
            decide("ask", "App Fusion: this records a person's decision or sign-off. Approve only if these are that "
                          "person's own answers, given in this session.")
        reason = check_bash(command, cwd, roots)
        if reason:
            decide("ask", f"App Fusion guard: {reason}. The legacy apps are read-only for this work; approve only if a "
                          "person really wants this change.")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:  # a guard bug must never block the session; the permission rules still apply
        sys.exit(0)
