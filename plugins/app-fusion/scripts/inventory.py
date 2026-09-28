#!/usr/bin/env python3
"""Deterministic inventory of one source app (or all of them).

    python3 inventory.py <program> <app> [--workspace DIR]
    python3 inventory.py <program> --all [--workspace DIR]

Reads analysis/<program>/program.json for the app's path and stack, scans legacy/<app> read-only, and writes
analysis/<program>/apps/<app>/inventory.json, strings.json and INVENTORY.md. Every count is written next to the rule
that produced it. Standard library only; uses scc for lines of code when it is installed.
"""

import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import android, detect, ios, rn  # noqa: E402
from fusionlib import strings as strcat  # noqa: E402
from fusionlib.common import (PROGRAMMING, app_dir, check_name, die, git_info, load_program, loc_by_language,  # noqa: E402
                              md_table, now_iso, one_line, workspace, write_json, write_text)

EXTRACTORS = {"react-native": rn.extract, "ios-native": ios.extract, "android-native": android.extract}


def run(ws, program, app):
    prog = load_program(ws, program)
    entry = next((a for a in prog.get("apps", []) if a.get("name") == app), None)
    if entry is None:
        die(f"app {app!r} is not in analysis/{program}/program.json (apps: {', '.join(a['name'] for a in prog.get('apps', []))})")
    path = os.path.join(ws, entry.get("path") or f"legacy/{app}")
    if not os.path.isdir(path):
        die(f"{os.path.relpath(path, ws)} does not exist: link it with /app-fusion:fuse {program} --source {app}=<path>")
    stack = entry.get("stack")
    if stack not in EXTRACTORS:
        found = detect.detect(path)
        stack = found["stack"]
    if stack not in EXTRACTORS:
        die(f"{app}: stack {stack!r} has no extractor (react-native, ios-native and android-native do); "
            "the assess step reads it with an analyst agent instead", code=3)

    raw = EXTRACTORS[stack](path)
    langs, loc_rule = loc_by_language(path)
    git = git_info(path)
    catalog = raw.pop("strings")
    counts = raw.pop("counts")
    rules = raw.pop("rules")
    counts["code"] = sum(l.get("code", 0) for l in langs if l.get("name") in PROGRAMMING)
    rules["code"] = loc_rule + "; summed over programming languages only (JSON, YAML, Markdown and other data formats are listed, not counted)"

    inventory = {
        "app": app, "stack": stack, "version": 1, "generated": now_iso(),
        "commit": git.get("commit"), "branch": git.get("branch"), "shallowClone": git.get("shallow"),
        "counts": counts, "rules": rules, "languages": langs,
        "strings": strcat.summary(catalog),
    }
    for key in ("screens", "routes", "navigators", "unresolvedRoutes", "swiftuiViews", "coordinators", "endpoints",
                "webLinks", "graphql", "events", "storage", "platform", "dependencies", "localPackages", "tests", "notes"):
        if key in raw:
            inventory[key] = raw[key]
    inventory["storage"] = _dedupe_storage(inventory.get("storage", []))
    counts["storageKeys"] = len(inventory["storage"])
    rules["storageKeys"] = rules.get("storageKeys", "") + " (one row per distinct kind and key)"

    out_dir = app_dir(ws, program, app)
    write_json(os.path.join(out_dir, "inventory.json"), inventory)
    write_json(os.path.join(out_dir, "strings.json"), {
        "app": app, "version": 1, "format": catalog.get("format"), "files": catalog.get("files", []),
        "locales": catalog.get("locales", []), "source": catalog.get("source"),
        "keys": dict(sorted((catalog.get("keys") or {}).items())),
        "values": dict(sorted((catalog.get("values") or {}).items())),
    })
    write_text(os.path.join(out_dir, "INVENTORY.md"), render(inventory, entry))
    return inventory


def _dedupe_storage(rows):
    seen = collections.OrderedDict()
    for row in rows:
        key = (row.get("kind"), row.get("key"))
        if key in seen:
            seen[key]["sites"] += 1
        else:
            seen[key] = {**row, "sites": 1}
    return list(seen.values())


def render(inv, entry):
    c, r = inv["counts"], inv["rules"]
    lines = [f"# Inventory: {inv['app']}", "",
             f"{entry.get('product') or inv['app']} · {inv['stack']} · commit `{(inv.get('commit') or 'unknown')[:12]}`"
             f"{' (shallow clone)' if inv.get('shallowClone') else ''} · generated {inv['generated']}", "",
             "Every number below comes from `scripts/inventory.py` and is printed with the rule that produced it. "
             "Two numbers made by different rules are different facts: quote the rule with the number.", "",
             "## Counts", "", md_table(["What", "Count", "Rule"], [[k, v, r.get(k, "")] for k, v in c.items()]), ""]
    if inv.get("languages"):
        lines += ["## Languages", "", md_table(["Language", "Files", "Code lines"],
                                               [[l["name"], l["files"], l["code"]] for l in inv["languages"][:12]]), ""]
    s = inv.get("strings") or {}
    if s.get("keys"):
        lines += ["## Strings", "", f"{s['keys']} keys in `{s['format']}` ({', '.join(s.get('files', [])[:6])}); source locale "
                  f"`{s.get('source')}`.", "",
                  md_table(["Locale", "Keys", "Missing"], [[loc, n, s["missingPerLocale"].get(loc, 0)]
                                                          for loc, n in s.get("perLocale", {}).items()]), ""]
    p = inv.get("platform") or {}
    plat_rows = []
    for key, label in (("bundleIds", "Bundle / application ids"), ("minOS", "Minimum OS"), ("push", "Push"),
                       ("urlSchemes", "URL schemes"), ("associatedDomains", "Associated domains (iOS)"),
                       ("appLinkHosts", "App link hosts (Android)"), ("linkingPrefixes", "Linking prefixes (JS)"),
                       ("appGroups", "App groups"), ("keychainGroups", "Keychain groups"),
                       ("backgroundModes", "Background modes"), ("queriesSchemes", "Queried schemes"),
                       ("atsExceptions", "ATS exceptions"), ("cleartext", "Cleartext traffic"),
                       ("privacyManifest", "Privacy manifests")):
        value = p.get(key)
        if value in (None, [], {}, False, ""):
            continue
        if isinstance(value, dict):
            value = ", ".join(f"{k} {v}" for k, v in value.items())
        elif isinstance(value, list):
            value = ", ".join(str(v) for v in value)
        plat_rows.append([label, value])
    if p.get("permissions"):
        plat_rows.append(["Permissions", ", ".join(x["key"] for x in p["permissions"])])
    if p.get("extensions"):
        plat_rows.append(["Extensions", ", ".join(f"{x['type']} ({x.get('plist', '')})" for x in p["extensions"])])
    if p.get("targets"):
        plat_rows.append(["Targets", ", ".join(f"{t['name']} ({t['kind']})" for t in p["targets"])])
    if p.get("exported"):
        plat_rows.append(["Exported components", ", ".join(f"{x['component']} {x['name']}" for x in p["exported"][:12])])
    if p.get("flags"):
        plat_rows.append(["Remote-config flags", ", ".join(f["key"] for f in p["flags"][:30])])
    if plat_rows:
        lines += ["## Platform", "", md_table(["Fact", "Value"], plat_rows), ""]

    if inv.get("screens"):
        by_area = collections.Counter(sc.get("area") or "-" for sc in inv["screens"])
        lines += ["## Screens by area", "", md_table(["Area", "Screens"], by_area.most_common(25)), ""]
    if inv.get("endpoints"):
        groups = collections.Counter("/".join(e["path"].strip("/").split("/")[:2]) for e in inv["endpoints"])
        lines += ["## Endpoints by prefix", "", md_table(["Prefix", "Call sites"], groups.most_common(25)), ""]
    if inv.get("events"):
        fam = collections.Counter(e.get("family") for e in inv["events"])
        lines += ["## Analytics events by family", "", md_table(["Family", "Entries"], fam.most_common(20)), ""]
    if inv.get("storage"):
        kinds = collections.Counter(x.get("kind") for x in inv["storage"])
        lines += ["## Storage", "", md_table(["Kind", "Distinct keys"], kinds.most_common()), ""]
    t = inv.get("tests") or {}
    lines += ["## Tests", "", f"Frameworks: {', '.join(t.get('frameworks') or []) or 'none found'}. Unit test files: "
              f"{t.get('unitTestFiles', 0)}. UI test files: {t.get('uiTestFiles', 0)}. Maestro flows: {t.get('maestroFlows', 0)}.", ""]
    native = [d for d in inv.get("dependencies", []) if d.get("native") and not d.get("dev")]
    if native:
        lines += ["## Native modules", "", ", ".join(f"`{d['name']}` {d['version']}" for d in native), ""]
    if inv.get("notes"):
        lines += ["## What this scan cannot see", ""] + [f"- {one_line(n, 400)}" for n in inv["notes"]] + [""]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("app", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    prog = load_program(ws, args.program)
    apps = [a["name"] for a in prog.get("apps", [])] if args.all else [check_name(args.app or "", "app")]
    for app in apps:
        inv = run(ws, args.program, app)
        c = inv["counts"]
        keys = [k for k in ("screens", "routes", "endpoints", "events", "stringKeys", "locales", "storageKeys", "testFiles",
                            "maestroFlows", "code") if k in c]
        print(f"{app} ({inv['stack']}): " + ", ".join(f"{k} {c[k]}" for k in keys))
        print(f"  wrote analysis/{args.program}/apps/{app}/inventory.json, strings.json, INVENTORY.md")


if __name__ == "__main__":
    main()
