#!/usr/bin/env python3
"""Set up and check an App Fusion workspace.

    python3 workspace.py init <program> --source <app>=<path> [--source ...] [--product <app>=<name>] [--twin <app>=<of>]
                               [--figma <url> ...] [--target <path>] [--snapshot] [--workspace DIR]
    python3 workspace.py intent <program> [--goal build|understand] [--platforms ios,android] [--stack S] [--persona P ...]
                               [--must TEXT ...] [--store APP|new-listing|undecided|ios=APP,android=APP] [--locales en,da,...]
    python3 workspace.py check <program> [--json]          are the legacy apps linked, clean and at the recorded commit?
    python3 workspace.py guard <program>                   which permission deny rules protect the legacy code?

`init` makes legacy/<app> a symlink to each source (copying nothing), records stack, platforms, repository, branch
and commit in analysis/<program>/program.json (merging with what is there), links new-app/<program> when --target
names an existing repository, and makes sure analysis/.gitignore keeps secrets out of git. With --snapshot, legacy/<app>
is instead a local clone of the source's current commit (`git clone --local`, which only reads the source), so the
developer's own edits in their working copy never change what is analyzed or fail the legacy check. It never writes
inside a source app. `check` and `guard` only read.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import detect  # noqa: E402
from fusionlib.common import (check_name, die, git_info, load_json, program_dir, today, workspace,  # noqa: E402
                              write_json)

GITIGNORE_LINES = ["SECRETS.local.md", "*.local.patch", "**/*.token*", "**/*.har", "!**/*.sanitized.har"]
FIGMA_URL = re.compile(r"https?://(?:www\.)?figma\.com/(design|file|proto|board|make)/([0-9A-Za-z]{22,128})(?:/branch/([0-9A-Za-z]{22,128}))?(?:/([^?#]*))?")


def parse_figma(url):
    m = FIGMA_URL.match(url.strip())
    if not m:
        return None
    kind, key, branch, name = m.groups()
    node = re.search(r"[?&]node-id=([0-9]+)[-:]([0-9]+)", url)
    return {"url": url.split("?")[0], "fileKey": branch or key, "kind": kind,
            "name": (name or "").split("/")[0].replace("-", " ") or key,
            "nodeId": f"{node.group(1)}:{node.group(2)}" if node else None, "pages": []}


def _pairs(values, what):
    out = {}
    for v in values or []:
        if "=" not in v:
            die(f"--{what} expects <app>=<value>, got {v!r}")
        k, _, val = v.partition("=")
        out[check_name(k.strip(), "app")] = val.strip()
    return out


def _link(ws, link_rel, target):
    link = os.path.join(ws, link_rel)
    real = os.path.realpath(os.path.expanduser(target))
    if not os.path.isdir(real):
        die(f"{target} is not a directory")
    if real in ("/", os.path.realpath(os.path.expanduser("~"))):
        die(f"refusing to link {real}: point --source at the app's repository, not the filesystem root or your home")
    ws_real = os.path.realpath(ws)
    if ws_real == real or ws_real.startswith(real + os.sep):
        die(f"refusing to link {real}: the workspace is inside it, so its own files would count as the app's")
    if os.path.lexists(link):
        current = os.path.realpath(link)
        if current != real:
            die(f"{link_rel} already points to {current}, not {real}: change nothing and ask which one is right")
        return real, False
    os.makedirs(os.path.dirname(link), exist_ok=True)
    os.symlink(real, link, target_is_directory=True)
    return real, True


def _snapshot(ws, link_rel, target):
    """Clone the source's committed HEAD into the workspace (read-only on the source), detached at that commit."""
    real = os.path.realpath(os.path.expanduser(target))
    info = git_info(real)
    if not info.get("commit"):
        die(f"--snapshot needs a git repository: {target} is not one (link it without --snapshot)")
    dest = os.path.join(ws, link_rel)
    if os.path.lexists(dest):
        current = git_info(dest).get("commit") if not os.path.islink(dest) else None
        if os.path.islink(dest) or current is None:
            die(f"{link_rel} already exists and is not a snapshot: change nothing and ask which one is right")
        return dest, False, info
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    import subprocess
    subprocess.run(["git", "clone", "--quiet", "--local", "--no-checkout", real, dest], check=True)
    subprocess.run(["git", "-C", dest, "checkout", "--quiet", "--detach", info["commit"]], check=True)
    return dest, True, info


def _ensure_gitignore(ws):
    path = os.path.join(ws, "analysis", ".gitignore")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    existing = open(path, encoding="utf-8").read().splitlines() if os.path.exists(path) else []
    missing = [line for line in GITIGNORE_LINES if line not in existing]
    if missing:
        with open(path, "a", encoding="utf-8") as fh:
            if existing and existing[-1].strip():
                fh.write("\n")
            fh.write("\n".join(missing) + "\n")
    return missing


def cmd_init(args):
    ws = workspace(args.workspace)
    program = check_name(args.program, "program")
    sources = _pairs(args.source, "source")
    products = _pairs(args.product, "product")
    twins = _pairs(args.twin, "twin")
    path = os.path.join(program_dir(ws, program), "program.json")
    prog = load_json(path) or {
        "program": program, "version": 1, "created": today(), "goal": "build", "apps": [], "figma": [],
        "target": {"path": f"new-app/{program}", "stack": "undecided", "platforms": [], "linked": False},
        "personas": [], "locales": [], "mustStayTrue": [], "storeIdentity": "undecided",
    }
    messages = []
    for app, target in sources.items():
        if args.snapshot:
            real, created, source_info = _snapshot(ws, f"legacy/{app}", target)
        else:
            real, created = _link(ws, f"legacy/{app}", target)
        found = detect.detect(real)
        info = git_info(real)
        if args.snapshot:
            info["repo"] = source_info.get("repo") or info.get("repo")
            info["branch"] = source_info.get("branch")
        entry = next((a for a in prog["apps"] if a["name"] == app), None)
        if entry is None:
            entry = {"name": app}
            prog["apps"].append(entry)
        entry.update({
            "product": products.get(app) or entry.get("product") or app,
            "stack": found["stack"], "platforms": found["platforms"], "path": f"legacy/{app}",
            "repo": info["repo"], "branch": info["branch"], "commit": info["commit"],
            "role": "twin" if app in twins else entry.get("role", "source"),
            "twinOf": twins.get(app, entry.get("twinOf")),
            "snapshotOf": os.path.realpath(os.path.expanduser(target)) if args.snapshot else entry.get("snapshotOf"),
        })
        state = ("snapshot of" if args.snapshot else "linked") if created else ("snapshot already there" if args.snapshot else "already linked")
        clean = {True: "clean", False: "HAS LOCAL CHANGES", None: "not a git checkout"}[info["clean"]]
        messages.append(f"{app}: {state} legacy/{app} -> {real} · {found['stack']} ({', '.join(found['platforms']) or 'no platform'})"
                        f" · {info['branch'] or '-'} @ {(info['commit'] or '-')[:12]} · {clean}"
                        f"{' · shallow clone' if info.get('shallow') else ''}")
    for app, of in twins.items():
        if of not in {a["name"] for a in prog["apps"]}:
            die(f"--twin {app}={of}: {of} is not a source app of this program")
    for url in args.figma or []:
        f = parse_figma(url)
        if not f:
            die(f"{url!r} is not a figma.com design, file, proto or make URL")
        if not any(x["fileKey"] == f["fileKey"] for x in prog["figma"]):
            prog["figma"].append(f)
            messages.append(f"figma: {f['name']} ({f['fileKey']})")
    if args.target:
        real, created = _link(ws, f"new-app/{program}", args.target)
        prog["target"].update({"path": f"new-app/{program}", "linked": True})
        messages.append(f"new app: {'linked' if created else 'already linked'} new-app/{program} -> {real}")
    write_json(path, prog)
    missing = _ensure_gitignore(ws)
    if missing:
        messages.append(f"analysis/.gitignore: added {', '.join(missing)}")
    for line in messages:
        print(line)
    print(f"wrote analysis/{program}/program.json ({len(prog['apps'])} app(s), {len(prog['figma'])} Figma file(s))")


def cmd_intent(args):
    """Record the machine-readable part of the front door's answers in program.json (INTENT.md keeps the words)."""
    ws = workspace(args.workspace)
    path = os.path.join(program_dir(ws, args.program), "program.json")
    prog = load_json(path)
    if not prog:
        die(f"analysis/{args.program}/program.json not found: run `workspace.py init` first")
    stacks = {"react-native", "native", "swiftui", "compose", "flutter", "kmp", "undecided"}
    if args.goal:
        if args.goal not in ("build", "understand"):
            die("--goal is build or understand")
        prog["goal"] = args.goal
    if args.platforms:
        plats = [p.strip() for p in args.platforms.split(",") if p.strip()]
        if not set(plats) <= {"ios", "android"}:
            die("--platforms is ios, android or ios,android")
        prog["target"]["platforms"] = plats
    if args.stack:
        if args.stack not in stacks:
            die(f"--stack is one of {', '.join(sorted(stacks))}")
        prog["target"]["stack"] = args.stack
    if args.persona:
        prog["personas"] = [p.strip() for p in args.persona if p.strip()]
    if args.must:
        prog["mustStayTrue"] = [m.strip() for m in args.must if m.strip()]
    if args.store:
        names = {a["name"] for a in prog.get("apps", [])}
        allowed = names | {"new-listing", "undecided"}
        if "=" in args.store:  # one listing per platform: ios=me-ios,android=vmm
            mapping = {}
            for part in args.store.split(","):
                plat, _, choice = part.partition("=")
                plat, choice = plat.strip(), choice.strip()
                if plat not in ("ios", "android") or choice not in allowed:
                    die(f"--store {args.store!r}: each part is ios=<listing> or android=<listing>, a listing being an app "
                        f"name ({', '.join(sorted(names))}), new-listing or undecided")
                mapping[plat] = choice
            prog["storeIdentity"] = mapping
        elif args.store not in allowed:
            die(f"--store is an app name ({', '.join(sorted(names))}), new-listing, undecided, or one per platform "
                "(ios=<listing>,android=<listing>)")
        else:
            prog["storeIdentity"] = args.store
    if args.locales is not None:
        prog["locales"] = [l.strip() for l in args.locales.split(",") if l.strip()]
    write_json(path, prog)
    print(f"analysis/{args.program}/program.json: goal {prog['goal']}, platforms {','.join(prog['target'].get('platforms') or []) or '-'}, "
          f"stack {prog['target'].get('stack')}, personas {', '.join(prog.get('personas') or []) or '-'}, store {prog.get('storeIdentity')}, "
          f"locales {', '.join(prog.get('locales') or []) or 'from the apps'}")


def legacy_state(ws, prog):
    rows = []
    for a in prog.get("apps", []):
        link = os.path.join(ws, a.get("path") or f"legacy/{a['name']}")
        exists = os.path.isdir(link)
        info = git_info(link) if exists else {}
        rows.append({
            "app": a["name"], "path": a.get("path"), "exists": exists, "realPath": os.path.realpath(link) if exists else None,
            "recordedCommit": a.get("commit"), "commit": info.get("commit"), "clean": info.get("clean"),
            "atRecordedCommit": bool(a.get("commit")) and info.get("commit") == a.get("commit"),
        })
    return rows


def cmd_check(args):
    ws = workspace(args.workspace)
    prog = load_json(os.path.join(program_dir(ws, args.program), "program.json"))
    if not prog:
        die(f"analysis/{args.program}/program.json not found: run /app-fusion:fuse {args.program} first")
    rows = legacy_state(ws, prog)
    if args.json:
        print(json.dumps(rows, indent=2))
    else:
        for r in rows:
            if not r["exists"]:
                print(f"{r['app']}: MISSING ({r['path']} does not resolve)")
                continue
            parts = ["clean" if r["clean"] else ("HAS LOCAL CHANGES" if r["clean"] is False else "not a git checkout")]
            if r["recordedCommit"]:
                parts.append("at the recorded commit" if r["atRecordedCommit"] else
                             f"MOVED from {r['recordedCommit'][:12]} to {(r['commit'] or '?')[:12]}")
            print(f"{r['app']}: {r['realPath']} · " + " · ".join(parts))
    bad = [r for r in rows if not r["exists"] or r["clean"] is False]
    sys.exit(1 if bad else 0)


def _deny_rules(path):
    data = load_json(path)
    if not isinstance(data, dict):
        return []
    return [r for r in ((data.get("permissions") or {}).get("deny") or []) if isinstance(r, str)]


def cmd_guard(args):
    ws = workspace(args.workspace)
    prog = load_json(os.path.join(program_dir(ws, args.program), "program.json")) or {"apps": []}
    files = [os.path.join(ws, ".claude", "settings.json"), os.path.join(ws, ".claude", "settings.local.json"),
             os.path.join(os.environ.get("CLAUDE_CONFIG_DIR") or os.path.expanduser("~/.claude"), "settings.json")]
    rules = []
    for f in files:
        for r in _deny_rules(f):
            if r.startswith("Edit(") or r == "Edit":
                rules.append((os.path.relpath(f, ws) if f.startswith(ws) else f.replace(os.path.expanduser("~"), "~"), r, f.startswith(ws)))
    # a leading / is relative to the settings file's own folder: Edit(/legacy/**) protects this workspace only when it
    # sits in the workspace's settings, not in ~/.claude/settings.json
    covered_legacy = any(r in ("Edit", "Edit(**/legacy/**)") or (in_ws and r in ("Edit(legacy/**)", "Edit(./legacy/**)", "Edit(/legacy/**)"))
                         for _, r, in_ws in rules)
    missing_real = []
    for a in prog.get("apps", []):
        link = os.path.join(ws, a.get("path") or f"legacy/{a['name']}")
        if os.path.islink(link):
            real = os.path.realpath(link)
            if not any(r in ("Edit", f"Edit(//{real.lstrip('/')}/**)") for _, r, _ in rules):
                missing_real.append(real)
    status = "ok" if covered_legacy and not missing_real else "warn"
    print(f"status: {status}")
    for f, r, _ in rules:
        print(f"  deny {r}  ({f})")
    if status != "ok":
        deny = ["Edit(/legacy/**)"] + [f"Edit(//{p.lstrip('/')}/**)" for p in missing_real]
        print("add to the workspace's .claude/settings.json (merge into permissions.deny if it exists):")
        print(json.dumps({"permissions": {"deny": deny}}, indent=2))
    print("note: a deny rule covers Claude's file tools and the shell commands it recognizes, not a script that opens "
          "files itself; the plugin's guard hook adds a second check, and a read-only mount is the hard guarantee.")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init")
    p.add_argument("program")
    p.add_argument("--source", action="append")
    p.add_argument("--product", action="append")
    p.add_argument("--twin", action="append")
    p.add_argument("--figma", action="append")
    p.add_argument("--target")
    p.add_argument("--snapshot", action="store_true", help="clone each source's current commit instead of linking its working copy")
    p.add_argument("--workspace")
    p = sub.add_parser("intent")
    p.add_argument("program")
    p.add_argument("--goal")
    p.add_argument("--platforms")
    p.add_argument("--stack")
    p.add_argument("--persona", action="append")
    p.add_argument("--must", action="append")
    p.add_argument("--store")
    p.add_argument("--locales")
    p.add_argument("--workspace")
    p = sub.add_parser("check")
    p.add_argument("program")
    p.add_argument("--json", action="store_true")
    p.add_argument("--workspace")
    p = sub.add_parser("guard")
    p.add_argument("program")
    p.add_argument("--workspace")
    p = sub.add_parser("figma-url")
    p.add_argument("url")
    args = ap.parse_args()
    if args.cmd == "init":
        cmd_init(args)
    elif args.cmd == "intent":
        cmd_intent(args)
    elif args.cmd == "check":
        cmd_check(args)
    elif args.cmd == "guard":
        cmd_guard(args)
    elif args.cmd == "figma-url":
        parsed = parse_figma(args.url)
        if not parsed:
            die("not a Figma design URL")
        print(json.dumps(parsed, indent=2))


if __name__ == "__main__":
    main()
