#!/usr/bin/env python3
"""Split the source apps into shards for the capability-map and rule-extraction fan-outs.

    python3 shard.py <program> [--app APP] [--pattern GLOB] [--max-lines N] [--workspace DIR]

A shard is one area of one app that an agent can read in full: a React Native screen area (src/screens/<area>),
a logic folder (services, epics, reducers, utils, hooks), a Swift package (Modules/<X>, EmployeeServices/<X>) or app
target folder, an Android module or feature package. Areas over --max-lines (default 9000 non-blank lines) are
split by sub-folder; areas under 300 lines are merged into one shard per app. Each shard carries hints from the
inventory (the routes, endpoints and events whose file is inside it), so an agent starts from facts.

Writes analysis/<program>/shards.json: {"version": 1, "shards": [{id, app, stack, kind, name, files, loc, hints}]}.
Standard library only.
"""

import argparse
import fnmatch
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib.common import (SOURCE_EXT, check_name, die, is_test_path, load_json, load_program, program_dir,  # noqa: E402
                              read_text, walk, workspace, write_json)

LOGIC_DIRS = {"services", "api", "epics", "sagas", "reducers", "slices", "store", "state", "selectors", "hooks", "utils",
              "helpers", "lib", "models", "domain", "configs", "config", "contexts", "providers", "actions", "gql",
              "graphql", "types", "consts", "constants", "navigation", "components"}
SKIP_TOP = {"ios", "android", "node_modules", "Pods", "fastlane", "scripts", "ci", "docs", "assets", "resources",
            "Resources", "__mocks__", "__test_utils", "e2e", "tools", ".maestro", "patches", "vendor", "commit-hooks"}
UI_DIRS = {"components", "ui", "views", "widgets", "design-system", "designSystem"}


def _files(root):
    out = {}
    for rel, full in walk(root, SOURCE_EXT, include_tests=False):
        top = rel.split("/")[0]
        if top in SKIP_TOP or top.startswith("."):
            continue
        text = read_text(full)
        if text is None:
            continue
        out[rel] = sum(1 for line in text.splitlines() if line.strip())
    return out


def _area_rn(rel):
    parts = rel.split("/")
    base = parts[1:] if parts[0] in ("src", "app") and len(parts) > 2 else parts
    if base[0] in ("screens", "features", "modules", "pages") and len(base) > 2:
        return "screens", f"{base[0]}/{base[1]}", "/".join(parts[: len(parts) - len(base) + 2])
    if base[0] in UI_DIRS and len(base) > 1:
        return "ui", base[0], "/".join(parts[: len(parts) - len(base) + 1])
    if base[0] in LOGIC_DIRS and len(base) > 1:
        return "logic", base[0], "/".join(parts[: len(parts) - len(base) + 1])
    return "logic", base[0] if len(base) > 1 else "root", "/".join(parts[: len(parts) - len(base) + 1]) if len(base) > 1 else ""


def _area_ios(rel):
    parts = rel.split("/")
    # Swift packages: <Group>/<Package>/Sources/...  or  <Package>/Sources/...
    if "Sources" in parts:
        i = parts.index("Sources")
        pkg = parts[i - 1] if i >= 1 else parts[0]
        prefix = "/".join(parts[:i])
        kind = "logic" if pkg.endswith(("Interface", "Core", "API", "Database", "Resources", "Utils")) else "screens"
        return kind, pkg, prefix
    if len(parts) > 2:
        return "screens", f"{parts[0]}/{parts[1]}", f"{parts[0]}/{parts[1]}"
    return "logic", parts[0] if len(parts) > 1 else "root", parts[0] if len(parts) > 1 else ""


def _area_android(rel):
    parts = rel.split("/")
    if "java" in parts or "kotlin" in parts:
        i = parts.index("java") if "java" in parts else parts.index("kotlin")
        module = parts[0] if parts[0] != "src" else "app"
        pkg = parts[i + 1: -1]
        feature = next((p for p in reversed(pkg) if p not in ("ui", "data", "domain", "di", "presentation", "screen", "screens")), module)
        prefix = "/".join(parts[: i + 1 + len(pkg)])
        return ("screens" if any(p in ("ui", "presentation", "screen", "screens", "feature") for p in pkg) else "logic"), \
            f"{module}/{feature}", prefix
    return "logic", parts[0], parts[0]


def build(ws, program, app_filter=None, pattern=None, max_lines=9000):
    prog = load_program(ws, program)
    shards = []
    for app in prog.get("apps", []):
        name = app["name"]
        if app_filter and name != app_filter:
            continue
        root = os.path.join(ws, app.get("path") or f"legacy/{name}")
        if not os.path.isdir(root):
            die(f"{os.path.relpath(root, ws)} does not exist")
        stack = app.get("stack")
        files = _files(root)
        if pattern:
            files = {f: n for f, n in files.items() if fnmatch.fnmatch(f, pattern) or fnmatch.fnmatch(f, pattern.rstrip("/") + "/*")}
        area_of = {"react-native": _area_rn, "ios-native": _area_ios, "android-native": _area_android}.get(stack, _area_rn)
        groups = {}
        path_kind = {}
        for rel, loc in files.items():
            kind, area, prefix = area_of(rel)
            g = groups.setdefault(area, {"prefix": prefix, "files": {}})
            g["files"][rel] = loc
            path_kind[rel] = kind
        inv = load_json(os.path.join(program_dir(ws, program), "apps", name, "inventory.json")) or {}
        parts = []
        for area, g in sorted(groups.items()):
            parts += _split(area, g, max_lines)
        for part_name, part_files in _pack(parts, max_lines):
            shard = _shard(name, stack, part_name, part_files, inv)
            kinds = [path_kind[f] for f in part_files]
            majority = max(set(kinds), key=kinds.count)
            shard["kind"] = "screens" if shard["hints"].get("routes") or shard["hints"].get("screens") else (
                "ui" if majority == "ui" else ("logic" if majority != "screens" else "screens"))
            shards.append(shard)
    return shards


def _split(area, group, max_lines):
    """Cut an area into shards of at most max_lines: by sub-folder, then by file order; small parts are packed
    together so no shard is a fragment of a few hundred lines."""
    files = group["files"]
    if sum(files.values()) <= max_lines:
        return [(area, files)]
    prefix = group.get("prefix") or ""
    subs = {}
    for rel, loc in files.items():
        rest = rel[len(prefix):].lstrip("/") if prefix and rel.startswith(prefix) else rel
        head = rest.split("/")[0] if "/" in rest else "(top)"
        subs.setdefault(head, {})[rel] = loc
    if len(subs) == 1:
        chunk, out, n = {}, [], 1
        for rel, loc in sorted(files.items()):
            if chunk and sum(chunk.values()) + loc > max_lines:
                out.append((f"{area}#{n}", chunk))
                chunk, n = {}, n + 1
            chunk[rel] = loc
        if n > 1 and sum(chunk.values()) < max_lines // 6:
            prev_name, prev = out.pop()
            prev.update(chunk)
            out.append((prev_name, prev))
        else:
            out.append((f"{area}#{n}" if n > 1 else area, chunk))
        return out
    parts = []
    for head, sub in sorted(subs.items()):
        sub_prefix = f"{prefix}/{head}" if prefix else head
        parts += _split(f"{area}/{head}", {"prefix": sub_prefix, "files": sub}, max_lines)
    packed, names, current = [], [], {}
    for name, part in parts:
        size = sum(part.values())
        if size >= max_lines // 3:
            packed.append((name, part))
            continue
        if current and sum(current.values()) + size > max_lines:
            packed.append((_pack_name(area, names), current))
            names, current = [], {}
        names.append(name)
        current.update(part)
    if current:
        packed.append((_pack_name(area, names), current))
    return packed


def _pack(parts, max_lines):
    """Pack consecutive small parts (under a third of max_lines) into shared shards, in name order, so related areas
    such as Calendar, CalendarFeature and CalendarInterface land together."""
    out, names, current = [], [], {}
    for name, files in sorted(parts, key=lambda p: p[0].lower()):
        size = sum(files.values())
        if size >= max_lines // 3:
            out.append((name, files))
            continue
        if current and sum(current.values()) + size > max_lines:
            out.append((_pack_name("", names), current))
            names, current = [], {}
        names.append(name)
        current.update(files)
    if current:
        out.append((_pack_name("", names), current))
    return out


def _pack_name(area, names):
    if len(names) == 1:
        return names[0]
    tail = lambda n: n[len(area) + 1:] if area and n.startswith(area + "/") else n
    joined = f"[{tail(names[0])}..{tail(names[-1])}]"
    return f"{area}/{joined}" if area else joined


def _shard(app, stack, area, files, inv):
    fileset = set(files)

    def inside(entries, key="file"):
        return [e for e in entries or [] if (e.get(key) or "").split(":")[0] in fileset]

    hints = {
        "routes": sorted({r.get("name") for r in inv.get("routes", []) if (r.get("componentFile") in fileset
                          or (r.get("file") or "").split(":")[0] in fileset) and r.get("name")})[:80],
        "screens": sorted({s.get("name") for s in inside(inv.get("screens"), "file") if s.get("name")})[:80],
        "endpoints": sorted({f"{e.get('method') or '?'} {e['path']}" for e in inside(inv.get("endpoints"))})[:80],
        "events": sorted({e.get("name") for e in inside(inv.get("events")) if e.get("name")})[:120],
        "storage": sorted({f"{s.get('kind')}:{s.get('key')}" for s in inside(inv.get("storage"))})[:40],
    }
    return {"id": f"{app}:{area}", "app": app, "stack": stack, "kind": None, "name": area,
            "files": sorted(files), "loc": sum(files.values()), "hints": {k: v for k, v in hints.items() if v}}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("--app")
    ap.add_argument("--pattern")
    ap.add_argument("--max-lines", type=int, default=9000)
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    if args.app:
        check_name(args.app, "app")
    shards = build(ws, args.program, args.app, args.pattern, args.max_lines)
    out = os.path.join(program_dir(ws, args.program), "shards.json")
    write_json(out, {"version": 1, "program": args.program, "maxLines": args.max_lines, "shards": shards})
    by_app = {}
    for s in shards:
        by_app.setdefault(s["app"], []).append(s)
    for app, items in by_app.items():
        kinds = {k: sum(1 for s in items if s["kind"] == k) for k in ("screens", "ui", "logic")}
        print(f"{app}: {len(items)} shards ({kinds['screens']} screen areas, {kinds['ui']} UI, {kinds['logic']} logic), "
              f"{sum(s['loc'] for s in items)} lines, largest {max(s['loc'] for s in items)}")
    if not shards:
        print("0 shards: the pattern matched nothing, or no source files were found")
        sys.exit(1)
    print(f"wrote analysis/{args.program}/shards.json ({len(shards)} shards)")


if __name__ == "__main__":
    main()
