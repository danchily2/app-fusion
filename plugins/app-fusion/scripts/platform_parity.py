#!/usr/bin/env python3
"""Will existing users keep what the operating system ties to the legacy apps?

    python3 platform_parity.py <program> [--workspace DIR]

An app-level check, run on the new app as it is, for every target platform on its own (an iOS entitlement never
covers Android users). It compares the new app's own platform facts (read with the same
rules as the legacy inventories: Info.plist, entitlements, AndroidManifest, Gradle, and notification categories and
channels registered in code) with every platform item the new app must keep: the items `platform.json` marks
required, and the items a person decided to keep. An item a person dropped is listed and skipped; an item nobody
decided yet is a gap.

  identity       per platform: with the store listing of an existing app (program.json storeIdentity, one app for
                 every platform or {"ios": <app>, "android": <app>}), the new app ships under that app's bundle or
                 application id on that platform, so its users update in place
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
        "categories": set(),
        "privacy": bool(p.get("privacyManifest")),
    }


def by_platform(p, stack):
    """{"ios": facts, "android": facts} for one app. React Native apps and the new app keep each shell's facts under
    `byPlatform` (an older inventory without it counts the merged facts for both); a native pair's inventory is keyed
    by half. Notification categories are iOS's, channels Android's."""
    p = p or {}
    if set(p) and set(p) <= {"ios", "android"}:
        halves = {k: dict(v or {}) for k, v in p.items()}
        cats = [c for v in halves.values() for c in (v.get("notificationCategories") or [])]
    elif p.get("byPlatform"):
        halves = {k: dict(v or {}) for k, v in p["byPlatform"].items()}
        cats = p.get("notificationCategories") or []
    elif stack == "ios-native":
        halves, cats = {"ios": p}, p.get("notificationCategories") or []
    elif stack == "android-native":
        halves, cats = {"android": p}, p.get("notificationCategories") or []
    else:
        halves, cats = {"ios": p, "android": p}, p.get("notificationCategories") or []
    out = {k: facts(v) for k, v in halves.items()}
    for c in cats:
        plat = "ios" if c.get("kind") == "category" else "android"
        if plat in out:
            out[plat]["categories"].add(f"{c.get('kind')}:{c.get('id')}")
    # a React Native app's JavaScript linking prefixes are left out on purpose: a link opens the app only when the
    # shell registers it (entitlements, Info.plist, the manifest), so each shell is compared with its own facts
    return out


def main_ids(ids):
    """App ids without the extension ids nested under them (com.x.app.share sits under com.x.app)."""
    return {b for b in ids if not any(b != o and b.startswith(o + ".") for o in ids)}


def store_by_platform(store, platforms):
    """program.json storeIdentity as {platform: app | new-listing | undecided}: one value for every platform, or a
    mapping such as {"ios": "me-ios", "android": "vmm"}."""
    if isinstance(store, dict):
        return {p: store.get(p) or "undecided" for p in platforms}
    return {p: store or "undecided" for p in platforms}


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
    apps = {a["name"]: a for a in prog.get("apps", [])}
    platforms = (prog.get("target") or {}).get("platforms") or ["ios", "android"]
    legacy = {}
    for name, a in apps.items():
        inv = load_json(os.path.join(pdir, "apps", name, "inventory.json")) or {}
        legacy[name] = by_platform(inv.get("platform"), inv.get("stack") or a.get("stack"))
    inv = newapp.inventory(ws, program)
    plat = inv.get("platform") or {}
    new = by_platform(plat, newapp.stack(ws, program))
    empty = facts({})
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

    def row(check, pred, expected, found, decided_by=None):
        if not expected:
            return
        it, st, did = state(pred)
        if decided_by:  # the store listing decision settles the identity item
            st, did = "check", decided_by
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
                     "verdict": verdict, "why": why, "decision": did if did and str(did).startswith("DEC-") else None})

    store = store_by_platform(prog.get("storeIdentity"), platforms)
    store_dec = next((k for k, d in decisions.items() if d.get("about") == "continuity:store-identity"), None)
    for p in platforms:
        mine = new.get(p, empty)
        union = lambda key: set().union(*[legacy[a].get(p, empty)[key] for a in legacy]) if legacy else set()
        chosen = store[p]
        if chosen in apps:
            ids = main_ids(legacy[chosen].get(p, empty)["bundleIds"])
            if not ids:
                rows.append({"check": f"identity ({p})", "item": None, "expected": None, "verdict": "fail", "decision": store_dec,
                             "why": f"{chosen} has no {p} listing to update: choose another listing for {p}"})
            else:
                row(f"identity ({p})", lambda i: i["area"] == "identity" and "bundle" in i["name"].lower(), ids, mine["bundleIds"],
                    decided_by=store_dec or "program.json storeIdentity")
        elif chosen in (None, "", "undecided"):
            rows.append({"check": f"identity ({p})", "item": None, "expected": None, "verdict": "gap", "decision": None,
                         "why": f"the store listing for {p} is not decided (continuity:store-identity)"})
        else:
            rows.append({"check": f"identity ({p})", "item": None, "expected": None, "verdict": "n/a", "decision": store_dec,
                         "why": "a new store listing: existing users move to it (CONTINUITY.md says how)"})
        row(f"links ({p})", lambda i: i["area"] == "links" and "universal" in i["name"].lower(), union("hosts"), mine["hosts"])
        row(f"schemes ({p})", lambda i: i["area"] == "links" and "scheme" in i["name"].lower(), union("schemes"), mine["schemes"])
        row(f"push ({p})", lambda i: i["area"] == "push" and i["name"].lower().startswith("push"),
            any(legacy[a].get(p, empty)["push"] for a in legacy), mine["push"])
        row(f"categories ({p})", lambda i: i["area"] == "push" and "categor" in i["name"].lower(), union("categories"), mine["categories"])
        if p == "ios":
            for kind in sorted(union("extensions") - {None}):
                row(f"extension:{kind}", lambda i, k=kind: i["area"] == "extensions" and i["name"].lower().endswith(f": {k}".lower()),
                    {kind}, mine["extensions"])
            row("app groups", lambda i: i["area"] == "sharing" and "app group" in i["name"].lower(), union("appGroups"), mine["appGroups"])
            row("keychain groups", lambda i: i["area"] == "sharing" and "keychain" in i["name"].lower(), union("keychainGroups"),
                mine["keychainGroups"])
            row("privacy", lambda i: i["area"] == "privacy", any(legacy[a].get("ios", empty)["privacy"] for a in legacy), mine["privacy"])
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
    for half in (plat.values() if set(plat) and set(plat) <= {"ios", "android"} else [plat]):
        read += [c["file"].split(":")[0] for c in (half or {}).get("notificationCategories") or []]
    states = [r["verdict"] for r in rows]
    verdict = "fail" if "fail" in states else ("gap" if "gap" in states else "pass")
    out = {"program": program, "version": 2, "generated": now_iso(), "verdict": verdict, "platforms": platforms,
           "rule": "on every target platform, every required or kept platform item of the legacy apps is present in the new "
                   "app's own platform files",
           "checks": rows, "inputs": newapp.input_hashes(ws, program, read),
           "decisionsUsed": proofkit.decisions_used(decisions, [r["decision"] for r in rows if r.get("decision")])}
    path = os.path.join(pdir, "evidence", "platform-parity.json")
    write_json(path, out)
    for r in rows:
        print(f"  {r['check']:<22} {r['verdict']:<5} {r['why']}")
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
