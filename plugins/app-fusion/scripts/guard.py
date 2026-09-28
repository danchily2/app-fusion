#!/usr/bin/env python3
"""PreToolUse guard: the legacy apps are never edited.

Reads the hook input (JSON on stdin). Outside a workspace with analysis/*/program.json it does nothing. Inside one:
  - a file write (Edit, Write, MultiEdit, NotebookEdit) whose path resolves under legacy/<app>, or under the real
    directory a legacy link points to, is denied;
  - a shell command that writes into such a path (a redirect whose target is there, rm/mv/cp/tee/touch/sed -i/...
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
        app = inside(resolve(target, cwd), roots)
        if app:
            decide("deny", f"App Fusion never edits a legacy app: {target} is inside legacy/{app}. Write analysis output "
                           "under analysis/<program>/ and new code under new-app/<program>/. (To change the legacy app "
                           "on purpose, do it outside this workspace or set the plugin option guard=false.)")
        return
    if tool == "Bash":
        reason = check_bash(args.get("command") or "", cwd, roots)
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
