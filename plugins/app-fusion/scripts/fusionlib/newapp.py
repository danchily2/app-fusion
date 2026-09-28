"""The new app: where it is, which files a capability's porting notes name, its inventory and its strings."""

import os
import re

from . import android, detect, ios, rn
from . import strings as strcat
from .common import load_json, program_dir, walk

EXTRACT = {"react-native": rn.extract, "ios-native": ios.extract, "android-native": android.extract}


def root(ws, program):
    prog = load_json(os.path.join(program_dir(ws, program), "program.json")) or {}
    return os.path.join(ws, (prog.get("target") or {}).get("path") or f"new-app/{program}")


def notes_path(ws, program, cap):
    return os.path.join(root(ws, program), "docs", "fusion", f"{cap}.md")


def notes_files(ws, program, cap):
    """New-app files a capability's porting notes name in backticks (only those that exist)."""
    path = notes_path(ws, program, cap)
    if not os.path.isfile(path):
        return []
    base = root(ws, program)
    text = open(path, encoding="utf-8", errors="replace").read()
    found = []
    for m in re.finditer(r"`([^`\s]+)`", text):
        rel = m.group(1).split(":")[0].lstrip("./")
        if "/" in rel or "." in rel:
            if os.path.isfile(os.path.join(base, rel)) and rel not in found:
                found.append(rel)
    return found


def stack(ws, program):
    base = root(ws, program)
    if not os.path.isdir(base):
        return None
    found = detect.detect(base)["stack"]
    if found != "other":
        return found
    # a new app may hold both a native iOS and a native Android project side by side
    return "native" if os.path.isdir(os.path.join(base, "ios")) and os.path.isdir(os.path.join(base, "android")) else found


def inventory(ws, program):
    """Extract the new app with the same rules as the legacy apps. For a two-project native app, both halves."""
    base = root(ws, program)
    st = stack(ws, program)
    if st in EXTRACT:
        return EXTRACT[st](base)
    if st == "native":
        parts = [ios.extract(os.path.join(base, "ios")), android.extract(os.path.join(base, "android"))]
        for p, prefix in zip(parts, ("ios/", "android/")):
            for key in ("endpoints", "events", "storage", "screens"):
                for e in p.get(key, []):
                    if "file" in e:
                        e["file"] = prefix + e["file"]
        merged = {k: parts[0].get(k, []) + parts[1].get(k, []) for k in ("endpoints", "events", "storage", "screens")}
        merged["strings"] = strcat.combine(parts[0]["strings"], parts[1]["strings"])
        return merged
    return {"endpoints": [], "events": [], "storage": [], "screens": [], "strings": strcat.combine()}


def catalog(ws, program):
    """The new app's string catalog, whatever its format."""
    base = root(ws, program)
    if not os.path.isdir(base):
        return strcat.combine()
    parts = [strcat.find_i18n_json(base, include=["src", "app", "assets", "locales", "translations", "i18n", "lang", "res", "."])]
    xc = [rel for rel, _ in walk(base, {".xcstrings"})]
    lproj = [rel for rel, _ in walk(base, {".strings"}) if ".lproj/" in rel]
    values = [rel for rel, _ in walk(base, {".xml"}) if "/res/values" in f"/{rel}"]
    parts += [strcat.parse_xcstrings(base, xc), strcat.parse_lproj_strings(base, lproj), strcat.parse_android_strings(base, values)]
    return strcat.combine(*parts)
