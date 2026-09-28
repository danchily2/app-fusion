#!/usr/bin/env python3
"""Are every legacy string of a capability and every required locale present in the new app?

    python3 i18n_parity.py <program> [--capability CAP-NNN ...] [--locales en,da,...] [--workspace DIR]

For each built capability (one with porting notes) the legacy keys come from capabilities.json (implementations.
<app>.strings). A key is mapped through new-app/<program>/docs/fusion/i18n-map.json when that file names it
({"<app>:<legacyKey>": "<newKey>", ...}); otherwise the new app must hold the same key. The mapped key must exist
in the new app's catalog (i18n JSON, String Catalog, .strings or strings.xml) in every required locale. Locales are
compared by language ('nb-NO', 'nb' and 'no' are one language). Required locales are --locales, else program.json's
`locales`, else every locale any legacy app of the capability ships.

A key a person decided to drop is listed in i18n-map.json with the value null. Writes
analysis/<program>/evidence/i18n-parity.json. Exit 0 all pass, 1 any gap. Standard library only.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import newapp  # noqa: E402
from fusionlib.common import check_name, die, load_json, now_iso, program_dir, workspace, write_json  # noqa: E402
from fusionlib.strings import base_locale  # noqa: E402


def run(ws, program, only=None, locales=None):
    pdir = program_dir(ws, program)
    caps = load_json(os.path.join(pdir, "capabilities.json"))
    if not caps:
        die(f"analysis/{program}/capabilities.json not found")
    prog = load_json(os.path.join(pdir, "program.json")) or {}
    key_map = load_json(os.path.join(newapp.root(ws, program), "docs", "fusion", "i18n-map.json")) or {}
    catalog = newapp.catalog(ws, program)
    new_keys = {k: {base_locale(l) for l in v} for k, v in (catalog.get("keys") or {}).items()}
    new_locales = {base_locale(l) for l in catalog.get("locales") or []}
    legacy_locales = {}
    for app in prog.get("apps", []):
        s = load_json(os.path.join(pdir, "apps", app["name"], "strings.json")) or {}
        legacy_locales[app["name"]] = {base_locale(l) for l in s.get("locales") or []}
    results = {}
    for c in caps.get("capabilities", []):
        cid = c["id"]
        if only and cid not in only:
            continue
        if not os.path.isfile(newapp.notes_path(ws, program, cid)):
            if only:
                results[cid] = {"verdict": "gap", "reason": "no porting notes: the capability is not built yet"}
            continue
        if locales:
            required = {base_locale(l) for l in locales}
        elif prog.get("locales"):
            required = {base_locale(l) for l in prog["locales"]}
        else:
            required = set()
            for app in c.get("implementations") or {}:
                required |= legacy_locales.get(app, set())
        required.discard("default")
        missing_keys, missing_locale, dropped, ok = [], [], [], 0
        total = 0
        for app, impl in (c.get("implementations") or {}).items():
            for key in impl.get("strings") or []:
                total += 1
                if f"{app}:{key}" in key_map:
                    mapped = key_map[f"{app}:{key}"]
                elif key in key_map:
                    mapped = key_map[key]
                else:
                    mapped = key
                if mapped is None:
                    dropped.append(f"{app}:{key}")
                    continue
                if mapped not in new_keys:
                    missing_keys.append({"legacy": f"{app}:{key}", "new": mapped})
                    continue
                have = set(new_keys[mapped])
                if "default" in have:  # Android's values/ folder holds the source language, taken as English
                    have.add("en")
                lacking = sorted(l for l in required if l not in have)
                if lacking:
                    missing_locale.append({"key": mapped, "missing": lacking})
                else:
                    ok += 1
        absent_locales = sorted(l for l in required if l not in new_locales)
        if total == 0:
            verdict, reason = "n/a", "the capability's legacy screens use no string key the map recorded"
        elif missing_keys or missing_locale:
            verdict, reason = "fail", f"{len(missing_keys)} key(s) missing, {len(missing_locale)} key(s) lacking a locale"
        else:
            verdict, reason = "pass", f"{ok} key(s) present in {len(required)} locale(s), {len(dropped)} dropped by decision"
        results[cid] = {"verdict": verdict, "reason": reason, "required": sorted(required), "absentLocales": absent_locales,
                        "keys": total, "present": ok, "missingKeys": missing_keys, "missingLocale": missing_locale,
                        "dropped": dropped}
    out = {"program": program, "version": 1, "generated": now_iso(), "catalog": catalog.get("format"),
           "rule": "each legacy key of the capability, mapped through docs/fusion/i18n-map.json or kept as is, exists in the new catalog in every required locale (compared by language)",
           "capabilities": results}
    path = os.path.join(pdir, "evidence", "i18n-parity.json")
    write_json(path, out)
    counts = {}
    for r in results.values():
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
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
