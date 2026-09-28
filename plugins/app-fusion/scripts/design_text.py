#!/usr/bin/env python3
"""Does each designed screen's text exist in the new app's strings?

    python3 design_text.py <program> [--capability CAP-NNN ...] [--threshold 0.9] [--workspace DIR]

For every built capability with design screens (traceability.json), the texts of each linked screen (design.json:
the characters from a cached design context or the REST path, else text-layer names from metadata) are compared with
the values of the new app's string catalog, all locales. Placeholder texts are left out and listed: digits-only,
dates, times, amounts, e-mail addresses, lorem ipsum, single characters, and the sample data listed in
analysis/<program>/design/placeholders.json (written in the design step, never by the build). A text matches when it
equals a catalog value after normalizing case, whitespace and edge punctuation, or fits a catalog template whose
fixed words ({{count}}, {name}, %@, %d, %1$s ... are the variable parts) hold at least two letters and match whole
words.

A screen passes when at least the threshold (default 90%) of its texts match, and a screen with no text captured is
a gap. A capability passes when all its screens do. With no design screen, the result follows its status: n/a when
the program has no Figma file (no design by intent), when a person decided `gap: carry-as-is`, or when it is
dropped; otherwise a gap. This checks copy, not layout: look and feel is signed by a person from the side-by-side
screenshots. Writes analysis/<program>/evidence/design-text.json. Exit 0 when nothing fails. Standard library only.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fusionlib import newapp, parity  # noqa: E402
from fusionlib.common import check_name, die, load_json, workspace  # noqa: E402

PLACEHOLDER = re.compile(
    r"^\s*(?:[\d\s.,:/+\-%€$£¥]+|\d{1,2}[:.]\d{2}(?:\s?[ap]m)?|[\w.+-]+@[\w-]+\.[\w.]+|lorem ipsum.*|.|\W+|"
    r"(?:mon|tue|wed|thu|fri|sat|sun)[a-z]*,?\s*\d.*|\d+\s*(?:kr|nok|sek|dkk|eur|usd|h|min|days?|hours?)\.?)\s*$", re.I)
TEMPLATE = re.compile(r"\{\{[^}]*\}\}|\{[A-Za-z0-9_]*\}|%(?:\d+\$)?[@sdifu]|%\.\d+f|\$\{[^}]*\}|<\d+>|<[a-z]+>|</[a-z]+>")
EDGE = " .,:;!?…'\"“”‘’()[]-–—"


def norm(text):
    s = re.sub(r"\s+", " ", str(text or "").strip().casefold())
    return s.strip(EDGE)


def template_regex(value):
    """A regex for a catalog value with variable parts, or None when its fixed words are too short to mean anything
    ('%d d' would match any text)."""
    parts = TEMPLATE.split(str(value or ""))
    if len(parts) == 1:
        return None
    fixed = [re.sub(r"\s+", " ", p.casefold()) for p in parts]
    if sum(len(re.findall(r"[^\W\d_]", p)) for p in fixed) < 2:
        return None
    fixed[0], fixed[-1] = fixed[0].lstrip(EDGE), fixed[-1].rstrip(EDGE)
    # the spaces around a variable part stay in the pattern, so fixed words match whole words: 'hi {name}' needs
    # 'hi ' and a word after it, and never matches 'history'
    body = r"(?:\S.*?)".join(re.escape(p) for p in fixed)
    return re.compile("^" + body + "$")


def placeholders(pdir):
    """{screen id or '*': {normalized text}} from design/placeholders.json: ["text", ...] or [{text, screen?, why?}]."""
    out = {}
    for item in load_json(os.path.join(pdir, "design", "placeholders.json")) or []:
        text, screen = (item, "*") if isinstance(item, str) else (item.get("text"), item.get("screen") or "*")
        if text:
            out.setdefault(screen, set()).add(norm(text))
    return out


def run(ws, program, only=None, threshold=0.9):
    pdir, caps, prog, decisions = parity.load_context(ws, program)
    if not caps:
        die(f"analysis/{program}/capabilities.json not found")
    trace = load_json(os.path.join(pdir, "traceability.json")) or {}
    design = load_json(os.path.join(pdir, "design", "design.json")) or {}
    no_design = not prog.get("figma")
    extra = placeholders(pdir)
    screens = {s["id"]: s for s in design.get("screens", [])}
    cat = newapp.catalog(ws, program)
    values, templates = set(), []
    # every locale, not only the source one: design copy may be written in the product's main language
    for loc_values in list((cat.get("allValues") or {}).values()) or [cat.get("values") or {}]:
        for v in loc_values.values():
            n = norm(v)
            if n:
                values.add(n)
            t = template_regex(v)
            if t:
                templates.append(t)
    inputs = (cat.get("files") or [])
    design_files = [os.path.join(pdir, "design", "design.json"), os.path.join(pdir, "design", "placeholders.json"),
                    os.path.join(pdir, "traceability.json")]
    results = {}
    for c, exists in parity.targets(ws, program, caps, only):
        cid = c["id"]
        if not exists:
            results[cid] = {"verdict": "gap", "reason": "no porting notes: the capability is not built yet"}
            continue
        info = (trace.get("capabilities") or {}).get(cid) or {}
        stamp = parity.stamp(ws, program, cid, inputs, decisions, [])
        stamp["inputs"].update({os.path.relpath(p, ws): h for p, h in
                                ((p, parity.proofkit.sha256_file(p)) for p in design_files if os.path.isfile(p))})
        if no_design:
            results[cid] = {"verdict": "n/a", "reason": "no design by intent: program.json names no Figma file", "screens": [], **stamp}
            continue
        if not trace or not design:
            results[cid] = {"verdict": "gap", "reason": f"the design is not inventoried and traced yet: run /app-fusion:fuse-design {program}",
                            "screens": [], **stamp}
            continue
        if not info.get("screens"):
            status = info.get("status") or "untraced"
            if status in ("design-exempt", "dropped"):
                results[cid] = {"verdict": "n/a", "reason": f"no design screen ({status}, decided by a person)", "screens": [], **stamp}
            else:
                results[cid] = {"verdict": "gap", "reason": f"no design screen ({status}): a person decides in fuse-review "
                                                            "whether it is designed, carried as it is, or dropped", "screens": [], **stamp}
            continue
        rows, failing, empty = [], 0, 0
        for sid in info["screens"]:
            s = screens.get(sid) or {}
            skip = extra.get("*", set()) | extra.get(sid, set())
            counted, left_out, matched, unmatched = [], [], [], []
            for t in [t for t in s.get("texts") or [] if t]:
                n = norm(t)
                if not n or PLACEHOLDER.match(t) or n in skip:
                    left_out.append(t)
                    continue
                counted.append(t)
                if n in values or any(tp.match(n) for tp in templates):
                    matched.append(t)
                else:
                    unmatched.append(t)
            if not counted:
                empty += 1
                rows.append({"screen": sid, "name": s.get("name"), "texts": 0, "matched": 0, "score": None, "pass": None,
                             "unmatched": [], "leftOut": left_out[:50], "textsFrom": s.get("textsFrom"),
                             "note": "no text captured for this screen: fetch its design context, or check the frame"})
                continue
            score = len(matched) / len(counted)
            ok = score >= threshold
            failing += 0 if ok else 1
            rows.append({"screen": sid, "name": s.get("name"), "texts": len(counted), "matched": len(matched),
                         "score": round(score, 3), "pass": ok, "unmatched": unmatched[:50], "leftOut": left_out[:50],
                         "textsFrom": s.get("textsFrom")})
        judged = len(rows) - empty
        if failing:
            verdict = "fail"
        elif empty:
            verdict = "gap"
        else:
            verdict = "pass"
        reason = f"{judged - failing} of {judged} screen(s) at or above {int(threshold * 100)}%" + \
                 (f"; {empty} screen(s) with no text captured" if empty else "")
        results[cid] = {"verdict": verdict, "reason": reason, "screens": rows, **stamp}
    path, counts = parity.write_result(
        ws, program, "design-text.json",
        "texts of each linked screen, placeholders left out, found among the new app's catalog values after normalizing "
        "case, whitespace and edge punctuation, or fitting a catalog template with at least two fixed letters",
        results, {"threshold": threshold})
    print(f"design text: {', '.join(f'{v} {k}' for k, v in sorted(counts.items())) or 'nothing built yet'} -> {os.path.relpath(path, ws)}")
    return 1 if counts.get("fail") else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("--capability", action="append")
    ap.add_argument("--threshold", type=float, default=0.9)
    ap.add_argument("--workspace")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    if not 0 < args.threshold <= 1:
        die("--threshold must be between 0 and 1")
    sys.exit(run(ws, args.program, set(args.capability or []), args.threshold))


if __name__ == "__main__":
    main()
