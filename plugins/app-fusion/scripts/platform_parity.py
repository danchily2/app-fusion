#!/usr/bin/env python3
"""Will existing users keep what the operating system ties to the legacy apps?

    python3 platform_parity.py <program> [--workspace DIR]

An app-level check, run on the new app as it is. It compares the new app's own platform facts (read with the same
rules as the legacy inventories: Info.plist, entitlements, AndroidManifest, Gradle, and notification categories and
channels registered in code) with every platform item the new app must keep: the items `platform.json` marks
required, and the items a person decided to keep. An item a person dropped is listed and skipped; an item nobody
decided yet is a gap.

  identity       with the store listing of an existing app (program.json storeIdentity), the new app ships under that
                 app's bundle and application ids, so its users update in place
  links          every associated domain and app-link host (links in e-mails and on the web keep opening the app)
  schemes        every custom URL scheme (OAuth callbacks, other apps' links)
  push           push stays registered (aps-environment, Firebase messaging)
  categories     every notification category and channel id (the backend's pushes keep their actions and channel)
  extensions     every app extension type kept (share, notification service, widgets ...)
  sharing        kept app groups and keychain access groups (shared data and a login that survives the update)
  locales        every required locale ships
  privacy        a privacy manifest when a legacy app had one

Writes analysis/<program>/evidence/platform-parity.json with the hash of every file it read. Exit 0 when nothing
fails. Standard library only.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import newapp, proofkit  # noqa: E402
from fusionlib.common import check_name, die, load_json, now_iso, program_dir, walk, workspace, write_json  # noqa: E402
from fusionlib.strings import base_locale, source_language  # noqa: E402

PLATFORM_FILES = re.compile(r"(^|/)(Info\.plist|[^/]*-Info\.plist|[^/]*\.entitlements|AndroidManifest\.xml|build\.gradle(\.kts)?|"
                            r"app\.json|app\.config\.[jt]s|project\.pbxproj|[^/]*\.xcconfig|PrivacyInfo\.xcprivacy)$")


def host(value):
    v = str(value or "").lower().strip()
    v = re.sub(r"^(applinks|webcredentials|activitycontinuation|appclips):", "", v)
    v = re.sub(r"^https?://", "", v).split("/")[0].split("?")[0]
    return v.lstrip("*.")


def facts(p):
    p = p or {}
    return {
        "bundleIds": set(p.get("bundleIds") or []),
        "hosts": {host(d) for d in (p.get("associatedDomains") or []) + (p.get("appLinkHosts") or []) if host(d)},
        "schemes": {s.lower() for s in p.get("urlSchemes") or []},
        "push": bool(p.get("push")),
        "extensions": {x.get("type") for x in p.get("extensions") or [] if isinstance(x, dict)},
        "appGroups": set(p.get("appGroups") or []),
        "keychainGroups": set(p.get("keychainGroups") or []),
        "categories": {f"{c.get('kind')}:{c.get('id')}" for c in p.get("notificationCategories") or []},
        "privacy": bool(p.get("privacyManifest")),
    }


def main_ids(ids):
    """App ids without the extension ids nested under them (com.x.app.share sits under com.x.app)."""
    return {b for b in ids if not any(b != o and b.startswith(o + ".") for o in ids)}


def run(ws, program):
    pdir = program_dir(ws, program)
    prog = load_json(os.path.join(pdir, "program.json"))
    platform = load_json(os.path.join(pdir, "platform.json"))
    if not prog or not platform:
        die(f"analysis/{program}/program.json and platform.json are needed: run /app-fusion:fuse-map {program} first")
    decisions = (load_json(os.path.join(pdir, "DECISIONS.json")) or {}).get("decisions") or {}
    base = newapp.root(ws, program)
    if not os.path.isdir(base):
        die(f"the new app is not there yet ({os.path.relpath(base, ws)}): run /app-fusion:fuse-scaffold {program} first")
    apps = [a["name"] for a in prog.get("apps", [])]
    legacy = {a: facts(((load_json(os.path.join(pdir, "apps", a, "inventory.json")) or {}).get("platform"))) for a in apps}
    inv = newapp.inventory(ws, program)
    plat = inv.get("platform") or {}
    halves = {k: facts(v) for k, v in plat.items()} if set(plat) <= {"ios", "android"} and plat else {"app": facts(plat)}
    new = {k: set().union(*[h[k] for h in halves.values()]) if isinstance(next(iter(halves.values()))[k], set)
           else any(h[k] for h in halves.values()) for k in next(iter(halves.values()))}

    items = platform.get("items") or []

    def state(pred):
        """(item, 'check' | 'dropped' | 'undecided', DEC id) for the first platform item matching pred."""
        it = next((i for i in items if pred(i)), None)
        if not it:
            return None, "check", None
        did = next((k for k, d in decisions.items() if d.get("kind") == "platform" and d.get("about") == it["id"]), None)
        choice = (decisions.get(did) or {}).get("choice")
        if choice == "drop":
            return it, "dropped", did
        if choice == "keep" or it.get("newApp") == "required":
            return it, "check", did
        return it, "undecided", did

    rows = []

    def row(check, pred, expected, found, applies=True):
        if not applies or not expected:
            return
        it, st, did = state(pred)
        missing = sorted(expected - found) if isinstance(expected, set) else ([] if found else ["yes"])
        if st == "dropped":
            verdict, why = "n/a", f"dropped by a person ({did})"
        elif st == "undecided":
            verdict, why = "gap", f"{it['id']} {it['name']} is not decided yet (fuse-review)"
        elif missing:
            verdict, why = "fail", "missing in the new app: " + ", ".join(missing[:8]) + (" …" if len(missing) > 8 else "")
        else:
            verdict, why = "pass", "present"
        rows.append({"check": check, "item": it["id"] if it else None, "expected": sorted(expected) if isinstance(expected, set) else expected,
                     "verdict": verdict, "why": why, "decision": did})

    store = prog.get("storeIdentity")
    if store in apps:
        row("identity", lambda i: i["area"] == "identity" and "bundle" in i["name"].lower(), main_ids(legacy[store]["bundleIds"]),
            new["bundleIds"])
    elif store in (None, "", "undecided"):
        rows.append({"check": "identity", "item": None, "expected": None, "verdict": "gap", "decision": None,
                     "why": "the store listing is not decided (continuity:store-identity)"})
    else:
        rows.append({"check": "identity", "item": None, "expected": None, "verdict": "n/a", "decision": None,
                     "why": "a new store listing: existing users move to it (CONTINUITY.md says how)"})
    row("links", lambda i: i["area"] == "links" and "universal" in i["name"].lower(), set().union(*[l["hosts"] for l in legacy.values()]), new["hosts"])
    row("schemes", lambda i: i["area"] == "links" and "scheme" in i["name"].lower(), set().union(*[l["schemes"] for l in legacy.values()]), new["schemes"])
    row("push", lambda i: i["area"] == "push" and i["name"].lower().startswith("push"), any(l["push"] for l in legacy.values()), new["push"])
    row("categories", lambda i: i["area"] == "push" and "categor" in i["name"].lower(),
        set().union(*[l["categories"] for l in legacy.values()]), new["categories"])
    for kind in sorted(set().union(*[l["extensions"] for l in legacy.values()]) - {None}):
        row(f"extension:{kind}", lambda i, k=kind: i["area"] == "extensions" and i["name"].lower().endswith(f": {k}".lower()), {kind},
            new["extensions"])
    row("app groups", lambda i: i["area"] == "sharing" and "app group" in i["name"].lower(),
        set().union(*[l["appGroups"] for l in legacy.values()]), new["appGroups"])
    row("keychain groups", lambda i: i["area"] == "sharing" and "keychain" in i["name"].lower(),
        set().union(*[l["keychainGroups"] for l in legacy.values()]), new["keychainGroups"])
    row("privacy", lambda i: i["area"] == "privacy", any(l["privacy"] for l in legacy.values()), new["privacy"])
    cat = newapp.catalog(ws, program)
    have = {base_locale(l) for l in cat.get("locales") or []}
    if have & {"base", "default"}:
        have.add(source_language(cat))
    if prog.get("locales"):
        required = {base_locale(l) for l in prog["locales"]}
    else:
        required = set()
        for a in apps:
            s = load_json(os.path.join(pdir, "apps", a, "strings.json")) or {}
            required |= {source_language(s) if base_locale(l) in ("base", "default") else base_locale(l) for l in s.get("locales") or []}
    row("locales", lambda i: i["area"] == "i18n", required - {"", "base", "default"}, have)

    read = [rel for rel, _ in walk(base) if PLATFORM_FILES.search(rel)]
    for half in (plat.values() if set(plat) <= {"ios", "android"} and plat else [plat]):
        read += [c["file"].split(":")[0] for c in (half or {}).get("notificationCategories") or []]
    states = [r["verdict"] for r in rows]
    verdict = "fail" if "fail" in states else ("gap" if "gap" in states else "pass")
    out = {"program": program, "version": 2, "generated": now_iso(), "verdict": verdict,
           "rule": "every required or kept platform item of the legacy apps is present in the new app's own platform files",
           "checks": rows, "inputs": newapp.input_hashes(ws, program, read),
           "decisionsUsed": proofkit.decisions_used(decisions, [r["decision"] for r in rows if r.get("decision")])}
    path = os.path.join(pdir, "evidence", "platform-parity.json")
    write_json(path, out)
    for r in rows:
        print(f"  {r['check']:<18} {r['verdict']:<5} {r['why']}")
    print(f"platform parity: {verdict} -> {os.path.relpath(path, ws)}")
    return 1 if verdict == "fail" else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    sys.exit(run(ws, args.program))


if __name__ == "__main__":
    main()
