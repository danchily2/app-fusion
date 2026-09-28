"""Evidence helpers shared by the recording scripts and the proof: content hashes, the capability's files as its
porting notes name them, JUnit parsing and the ids a test name carries.

Freshness is judged by content, never by file times: a result is fresh for a capability when the capability's files
still hash to the value recorded with the result. A `git checkout`, a copy or a restore that changes a file's time but
not its bytes changes nothing here.
"""

import glob
import hashlib
import os
import re
import xml.etree.ElementTree as ET

from .common import SOURCE_EXT, is_test_path, load_json, program_dir

ID = re.compile(r"\b(CAP|RULE|JRN|DEC)[-_ ]?0*(\d{1,5})(?!\d)", re.I)
NOTE_SECTIONS = ("files", "shared files", "tests", "api")


def ids_in(text):
    """{"CAP-012", "RULE-007", ...} named in a test name, class name or suite name ("CAP012", "rule_7" count too)."""
    return {f"{m.group(1).upper()}-{int(m.group(2)):03d}" for m in ID.finditer(text or "")}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------- the new app and a capability's porting notes

def target_root(ws, program):
    prog = load_json(os.path.join(program_dir(ws, program), "program.json")) or {}
    return os.path.join(ws, (prog.get("target") or {}).get("path") or f"new-app/{program}")


def notes_path(ws, program, cap):
    return os.path.join(target_root(ws, program), "docs", "fusion", f"{cap}.md")


def _sections(text):
    """{"files": body, "shared files": body, ...} for the '## <Name>' sections of a notes file."""
    out = {}
    heads = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", text))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        out.setdefault(m.group(1).strip().lower(), text[m.end():end])
    return out


def _inside(base, rel):
    """The normalized relative path when `rel` stays inside `base` after resolving links and '..', else None."""
    rel = rel.strip()
    while rel.startswith("./"):
        rel = rel[2:]
    if not rel or os.path.isabs(rel) or rel.startswith("~"):
        return None
    full = os.path.realpath(os.path.join(base, rel))
    real_base = os.path.realpath(base)
    if not full.startswith(real_base + os.sep) or not os.path.isfile(full):
        return None
    return os.path.relpath(full, real_base)


def target_rel(ws, program, path):
    """A path given relative to the new app, to the workspace (new-app/<program>/...) or absolute, as a path relative
    to the new app when it names a file inside it; else None."""
    base = target_root(ws, program)
    real_base = os.path.realpath(base)
    if os.path.isabs(path):
        real = os.path.realpath(path)
        return _inside(base, os.path.relpath(real, real_base)) if real.startswith(real_base + os.sep) else None
    in_ws = os.path.relpath(base, ws)
    if path.startswith(in_ws + "/"):
        path = path[len(in_ws) + 1:]
    return _inside(base, path)


def notes(ws, program, cap):
    """What a capability's porting notes name, by section. Paths are relative to the new app and exist inside it.

    {"exists": bool, "files": [...], "shared": [...], "tests": [...], "api": [(path, line)], "all": [...]}
    The notes' own file and anything under docs/ never count as built code. Without '## Files' / '## Shared files' /
    '## Tests' headings, every backticked path in the notes counts as a file (older notes).
    """
    path = notes_path(ws, program, cap)
    empty = {"exists": False, "files": [], "shared": [], "tests": [], "api": [], "all": []}
    if not os.path.isfile(path):
        return empty
    base = target_root(ws, program)
    text = open(path, encoding="utf-8", errors="replace").read()
    secs = _sections(text)

    def paths(body):
        found = []
        for m in re.finditer(r"`([^`\s]+)`", body or ""):
            rel = _inside(base, m.group(1).split(":")[0])
            if rel and not rel.startswith("docs" + os.sep) and rel not in found:
                found.append(rel)
        return found

    if any(k in secs for k in ("files", "shared files", "tests")):
        files, shared, tests = paths(secs.get("files")), paths(secs.get("shared files")), paths(secs.get("tests"))
    else:
        every = paths(text)
        files = [f for f in every if not is_test_path(f)]
        shared, tests = [], [f for f in every if is_test_path(f)]
    api = []
    for m in re.finditer(r"`([^`\s]+?):(\d+)(?:-\d+)?`", secs.get("api") or ""):
        rel = _inside(base, m.group(1))
        if rel:
            api.append((rel, int(m.group(2))))
    tests = [t for t in tests if t not in files]
    shared = [s for s in shared if s not in files and s not in tests]
    return {"exists": True, "files": files, "shared": shared, "tests": tests, "api": api,
            "all": sorted(set(files) | set(shared) | set(tests) | {p for p, _ in api})}


def is_source(rel):
    return os.path.splitext(rel)[1].lower() in SOURCE_EXT


def code_hash(ws, program, cap, info=None):
    """One hash over every file the capability's notes name (code, shared files, tests, API call sites), by path and
    content. None when the notes name no file. The notes themselves are left out, so filling in their Canary section
    after a run does not make the run stale."""
    info = info or notes(ws, program, cap)
    if not info["all"]:
        return None
    base = target_root(ws, program)
    h = hashlib.sha256()
    for rel in info["all"]:
        h.update(rel.encode("utf-8") + b"\0" + sha256_file(os.path.join(base, rel)).encode("ascii") + b"\n")
    return h.hexdigest()


def built(ws, program):
    """The capabilities with porting notes in the new app: {CAP-NNN: path}."""
    folder = os.path.join(target_root(ws, program), "docs", "fusion")
    if not os.path.isdir(folder):
        return {}
    return {m.group(1): os.path.join(folder, name) for name in sorted(os.listdir(folder))
            for m in [re.match(r"^(CAP-\d+)\.md$", name)] if m}


def code_hashes(ws, program, caps=None):
    """{CAP: hash} for the given capabilities, or every built one."""
    caps = caps if caps is not None else list(built(ws, program))
    return {c: code_hash(ws, program, c) for c in caps}


def changed_inputs(ws, recorded):
    """The files of a {workspace path: sha256} record whose content is no longer what was recorded (or is gone)."""
    out = []
    for rel, h in (recorded or {}).items():
        full = os.path.join(ws, rel)
        if not os.path.isfile(full) or sha256_file(full) != h:
            out.append(rel)
    return out


def decisions_used(decisions, ids):
    """{DEC id: choice} for the decisions a check relied on, so the proof can tell when one changed."""
    return {d: (decisions.get(d) or {}).get("choice") for d in sorted(set(ids))}


def changed_decisions(decisions, used):
    return [d for d, choice in (used or {}).items() if (decisions.get(d) or {}).get("choice") != choice]


# ---------------------------------------------------------------- JUnit

def xml_files(paths, ws):
    """Expand files and folders into the XML files they hold (relative to the workspace)."""
    files = []
    for p in paths or []:
        full = p if os.path.isabs(p) else os.path.join(ws, p)
        if os.path.isdir(full):
            files += sorted(glob.glob(os.path.join(full, "**", "*.xml"), recursive=True))
        elif os.path.isfile(full):
            files.append(full)
    return [os.path.relpath(f, ws) for f in files]


def junit_cases(files, ws):
    """Test cases of JUnit-style XML files: [{name, classname, suite, status, file, key}]. Unparseable files are
    reported in the second value, never silently skipped."""
    cases, bad = [], []
    for rel in files or []:
        full = rel if os.path.isabs(rel) else os.path.join(ws, rel)
        try:
            root = ET.parse(full).getroot()
        except (ET.ParseError, OSError):
            bad.append(rel)
            continue
        suites = [root] if root.tag == "testsuite" else list(root.iter("testsuite")) or [root]
        seen = set()
        for suite in suites:
            for tc in suite.iter("testcase"):
                if id(tc) in seen:
                    continue
                seen.add(id(tc))
                status = "passed"
                children = {c.tag for c in tc}
                if "failure" in children or "error" in children:
                    status = "failed"
                elif "skipped" in children:
                    status = "skipped"
                attr = (tc.get("status") or tc.get("result") or "").lower()
                if attr in ("failed", "failure", "error", "errored"):
                    status = "failed"
                elif attr in ("skipped", "disabled", "pending", "notrun", "not_run"):
                    status = "skipped"
                name, cls = tc.get("name") or "", tc.get("classname") or ""
                cases.append({"name": name, "classname": cls, "suite": suite.get("name") or "", "status": status,
                              "file": os.path.relpath(full, ws), "key": f"{cls}::{name}"})
    return cases, bad


def case_ids(tc):
    return ids_in(" ".join((tc.get("name") or "", tc.get("classname") or "", tc.get("suite") or "")))
