#!/usr/bin/env python3
"""Are every legacy string of a capability and every required locale present in the new app?

    python3 i18n_parity.py <program> [--capability CAP-NNN ...] [--locales en,da,...] [--workspace DIR]

For each built capability (one with porting notes) the legacy keys come from capabilities.json (implementations.
<app>.strings). A key is mapped through new-app/<program>/docs/fusion/i18n-map.json when that file names it
({"<app>:<legacyKey>": "<newKey>", ...}, or {"ios": "<key>", "android": "<key>"} for a native pair); otherwise the new
app must hold the same key. The mapped key must exist in the new app's catalog (i18n JSON, String Catalog, .strings
or strings.xml) in every required locale, in each half of a native pair. Locales are compared by what users read
('nb-NO', 'nb' and 'no' are one; zh-Hans and zh-Hant, pt-BR and pt are two); Base and Android's default folder count
as the catalog's source language (English unless it says otherwise). Required locales are --locales, else
program.json's `locales`, else every locale any legacy app of the capability ships.

A key the new app drops needs a person's decision: kind `strings`, choice `drop`, about "<app>:<key>" or
"CAP-NNN:<app>:<key>". A null in the key map without that decision is a missing key. When the map lists no key for a
capability, its legacy files are searched for catalog keys: finding some is a gap (the map missed them), finding
none is n/a. Writes analysis/<program>/evidence/i18n-parity.json. Exit 0 when nothing fails. Standard library only.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import newapp, parity  # noqa: E402
from fusionlib.common import check_name, die, legacy_dir, load_json, read_text, workspace  # noqa: E402
from fusionlib.strings import base_locale, source_language  # noqa: E402

LITERAL = re.compile(r"(['\"`])((?:\\.|(?!\1)[^\\\n])+)\1|R\.string\.([A-Za-z0-9_]+)|@string/([A-Za-z0-9_]+)")
MAP = "docs/fusion/i18n-map.json"


def used_keys(ws, app, files, keys):
    """Catalog keys that appear as literals in the given legacy files."""
    found = []
    for rel in files:
        text = read_text(os.path.join(legacy_dir(ws, app), rel))
        if not text:
            continue
        for m in LITERAL.finditer(text):
            k = m.group(2) or m.group(3) or m.group(4)
            if k in keys and k not in found:
                found.append(k)
    return found


def run(ws, program, only=None, locales=None):
    pdir, caps, prog, decisions = parity.load_context(ws, program)
    if not caps:
        die(f"analysis/{program}/capabilities.json not found")
    key_map = load_json(os.path.join(newapp.root(ws, program), MAP)) or {}
    halves = newapp.halves(ws, program)
    cats = {half: newapp.catalog(ws, program, half or None) for _, half in halves}
    legacy = {}
    for app in prog.get("apps", []):
        s = load_json(os.path.join(pdir, "apps", app["name"], "strings.json")) or {}
        src = source_language(s)
        legacy[app["name"]] = {"locales": {src if base_locale(l) in ("base", "default") else base_locale(l) for l in s.get("locales") or []},
                               "keys": set((s.get("keys") or {}).keys())}
    results = {}
    for c, exists in parity.targets(ws, program, caps, only):
        cid = c["id"]
        if not exists:
            results[cid] = {"verdict": "gap", "reason": "no porting notes: the capability is not built yet"}
            continue
        impls = c.get("implementations") or {}
        if locales:
            required = {base_locale(l) for l in locales}
        elif prog.get("locales"):
            required = {base_locale(l) for l in prog["locales"]}
        else:
            required = set().union(*[legacy.get(app, {}).get("locales", set()) for app in impls]) if impls else set()
        required -= {"base", "default", ""}
        missing_keys, missing_locale, dropped, used = [], [], [], []
        ok = total = 0
        for app, impl in impls.items():
            for key in impl.get("strings") or []:
                total += 1
                raw = key_map.get(f"{app}:{key}", key_map.get(key, key))
                if raw is None or (isinstance(raw, dict) and "dropped" in raw):
                    did = parity.decision_for(decisions, "strings", {f"{app}:{key}", f"{cid}:{app}:{key}"}, {"drop"})
                    if did:
                        dropped.append({"legacy": f"{app}:{key}", "decision": did})
                        used.append(did)
                    else:
                        missing_keys.append({"legacy": f"{app}:{key}", "new": None,
                                             "why": "dropped in the key map without a person's decision (kind strings, choice drop)"})
                    continue
                for platform, half in halves:
                    mapped = raw.get(platform or "", raw.get("default")) if isinstance(raw, dict) else raw
                    where = f" ({platform})" if platform else ""
                    cat = cats[half]
                    have_keys = cat.get("keys") or {}
                    if not mapped or mapped not in have_keys:
                        missing_keys.append({"legacy": f"{app}:{key}", "new": mapped, "why": f"not in the new catalog{where}"})
                        continue
                    have = {base_locale(l) for l in have_keys[mapped]}
                    if have & {"base", "default"}:
                        have.add(source_language(cat))
                    lacking = sorted(l for l in required if l not in have)
                    if lacking:
                        missing_locale.append({"key": mapped + where, "missing": lacking})
                    else:
                        ok += 1
        files = [MAP] + [f for cat in cats.values() for f in cat.get("files") or []]
        stamp = parity.stamp(ws, program, cid, files, decisions, used)
        if total == 0:
            seen = []
            for app, impl in impls.items():
                seen += [f"{app}:{k}" for k in used_keys(ws, app, parity.cited_files(impl), legacy.get(app, {}).get("keys", set()))]
            if seen:
                verdict, reason = "gap", (f"the map lists no string key, but the capability's legacy files use {len(seen)} catalog "
                                          f"key(s) ({', '.join(seen[:5])}{' …' if len(seen) > 5 else ''}): add them to the map")
            else:
                verdict, reason = "n/a", "no string key in the map, and none found in the capability's legacy files"
        elif missing_keys or missing_locale:
            verdict, reason = "fail", f"{len(missing_keys)} key(s) missing, {len(missing_locale)} key(s) lacking a locale"
        else:
            verdict, reason = "pass", (f"{ok} key check(s) passed in {len(required)} locale(s) across {len(halves)} catalog(s), "
                                       f"{len(dropped)} dropped by decision")
        results[cid] = {"verdict": verdict, "reason": reason, "required": sorted(required), "keys": total, "present": ok,
                        "missingKeys": missing_keys, "missingLocale": missing_locale, "dropped": dropped, **stamp}
    path, counts = parity.write_result(
        ws, program, "i18n-parity.json",
        "each legacy key of the capability, mapped through docs/fusion/i18n-map.json or kept as is, exists in the new "
        "catalog in every required locale (compared by language); a dropped key needs a person's decision", results,
        {"catalogs": {h or "app": cats[h].get("format") for _, h in halves}})
    print(f"i18n parity: {', '.join(f'{v} {k}' for k, v in sorted(counts.items())) or 'nothing built yet'} -> {os.path.relpath(path, ws)}")
    return 1 if counts.get("fail") else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("--capability", action="append")
    ap.add_argument("--locales")
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    locales = [x.strip() for x in args.locales.split(",")] if args.locales else None
    sys.exit(run(ws, args.program, set(args.capability or []), locales))


if __name__ == "__main__":
    main()
