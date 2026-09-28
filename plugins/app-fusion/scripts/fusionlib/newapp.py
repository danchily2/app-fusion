"""The new app: where it is, which files a capability's porting notes name, its inventory and its strings.

A `native` target holds two projects side by side (`ios/` and `android/`). Every check that compares code runs per
half, so an iOS-only build never passes for Android: `halves()` names them, and `inventory()` and `catalog()` take
the half to read.
"""

import os

from . import android, detect, ios, proofkit, rn
from . import strings as strcat
from .common import load_json, program_dir, walk

EXTRACT = {"react-native": rn.extract, "ios-native": ios.extract, "android-native": android.extract}
CATALOG_DIRS = ["src", "app", "assets", "locales", "translations", "i18n", "lang", "res", "."]


def root(ws, program):
    return proofkit.target_root(ws, program)


def notes_path(ws, program, cap):
    return proofkit.notes_path(ws, program, cap)


def notes_files(ws, program, cap):
    """The capability's code files (its own and the shared ones it changed), relative to the new app."""
    info = proofkit.notes(ws, program, cap)
    return info["files"] + info["shared"]


def stack(ws, program):
    base = root(ws, program)
    if not os.path.isdir(base):
        return None
    found = detect.detect(base)["stack"]
    if found != "other":
        return found
    # a new app may hold both a native iOS and a native Android project side by side
    return "native" if os.path.isdir(os.path.join(base, "ios")) and os.path.isdir(os.path.join(base, "android")) else found


def halves(ws, program):
    """[(platform or None, folder relative to the new app)]: one entry, or ios/ and android/ for a native pair."""
    if stack(ws, program) == "native":
        prog = load_json(os.path.join(program_dir(ws, program), "program.json")) or {}
        wanted = (prog.get("target") or {}).get("platforms") or ["ios", "android"]
        return [(p, p) for p in ("ios", "android") if p in wanted]
    return [(None, "")]


def in_half(rel, half):
    return not half or rel == half or rel.startswith(half + "/")


def inventory(ws, program, half=None):
    """Extract the new app with the same rules as the legacy apps. For a native pair, one half (paths keep their
    'ios/' or 'android/' prefix), or both merged when no half is given."""
    base = root(ws, program)
    st = stack(ws, program)
    if st in EXTRACT:
        return EXTRACT[st](base)
    if st == "native":
        parts = []
        for name, extract in (("ios", ios.extract), ("android", android.extract)):
            if half not in (None, name) or not os.path.isdir(os.path.join(base, name)):
                continue
            p = extract(os.path.join(base, name))
            for key in ("endpoints", "events", "storage", "screens"):
                for e in p.get(key, []):
                    if "file" in e:
                        e["file"] = f"{name}/{e['file']}"
            for c in (p.get("platform") or {}).get("notificationCategories") or []:
                c["file"] = f"{name}/{c['file']}"
            p["strings"] = dict(p.get("strings") or {}, files=[f"{name}/{f}" for f in (p.get("strings") or {}).get("files", [])])
            parts.append(p)
        if len(parts) == 1:
            return parts[0]
        merged = {k: [e for p in parts for e in p.get(k, [])] for k in ("endpoints", "events", "storage", "screens")}
        merged["strings"] = strcat.combine(*[p["strings"] for p in parts])
        merged["platform"] = {"ios": parts[0].get("platform"), "android": parts[1].get("platform")}
        return merged
    return {"endpoints": [], "events": [], "storage": [], "screens": [], "strings": strcat.combine()}


def catalog(ws, program, half=None):
    """The new app's string catalog, whatever its format, for the whole app or one half. `files` are relative to the
    new app."""
    base = root(ws, program)
    folder = os.path.join(base, half) if half else base
    if not os.path.isdir(folder):
        return strcat.combine()
    parts = [strcat.find_i18n_json(folder, include=CATALOG_DIRS)]
    xc = [rel for rel, _ in walk(folder, {".xcstrings"})]
    lproj = [rel for rel, _ in walk(folder, {".strings"}) if ".lproj/" in rel]
    values = [rel for rel, _ in walk(folder, {".xml"}) if "/res/values" in f"/{rel}"]
    parts += [strcat.parse_xcstrings(folder, xc), strcat.parse_lproj_strings(folder, lproj), strcat.parse_android_strings(folder, values)]
    cat = strcat.combine(*parts)
    if half:
        cat = dict(cat, files=[f"{half}/{f}" for f in cat.get("files") or []])
    return cat


def input_hashes(ws, program, rels):
    """{path relative to the workspace: sha256} for files given relative to the new app (what a check read)."""
    base = root(ws, program)
    out = {}
    for rel in sorted(set(rels)):
        full = os.path.join(base, rel)
        if os.path.isfile(full):
            out[os.path.relpath(full, ws)] = proofkit.sha256_file(full)
    return out
