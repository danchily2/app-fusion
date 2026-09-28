"""Notification categories (iOS actions) and channels (Android) an app registers in code.

A push payload names its category or channel. When the new app registers neither, pushes the backend already sends
arrive without their buttons, or on Android in a default channel users may have muted. Only literal ids are read.
"""

import re

from .common import is_test_path, line_of, read_text, walk

EXTS = {".swift", ".m", ".mm", ".ts", ".tsx", ".js", ".jsx", ".kt", ".java"}
PATTERNS = [
    ("category", re.compile(r"UNNotificationCategory\s*\(\s*identifier\s*:\s*\"([^\"\\]+)\"")),
    ("category", re.compile(r"categoryWithIdentifier\s*:\s*@\"([^\"\\]+)\"")),
    ("channel", re.compile(r"NotificationChannel(?:Compat\.Builder)?\s*\(\s*\"([^\"\\]+)\"")),
]
BLOCK = re.compile(r"\b(setNotificationCategories|createChannels?|createChannelGroup)\s*\(")
BLOCK_ID = re.compile(r"\bid\s*:\s*['\"]([^'\"]+)['\"]")


def scan(root, rel_prefix=""):
    """[{kind: category|channel, id, file}] for the app under root, tests and vendored code left out."""
    out, seen = [], set()
    for rel, full in walk(root, EXTS, include_tests=False):
        if is_test_path(rel) or "/Pods/" in f"/{rel}" or "/node_modules/" in f"/{rel}":
            continue
        text = read_text(full)
        if not text or ("Notification" not in text and "Channel" not in text and "Categor" not in text):
            continue
        found = [(kind, m.group(1), m.start()) for kind, rx in PATTERNS for m in rx.finditer(text)]
        for m in BLOCK.finditer(text):
            kind = "category" if "Categor" in m.group(1) else "channel"
            window = text[m.end(): m.end() + 1500]
            depth, end = 1, len(window)
            for i, ch in enumerate(window):
                depth += {"(": 1, ")": -1}.get(ch, 0)
                if depth == 0:
                    end = i
                    break
            found += [(kind, b.group(1), m.end() + b.start()) for b in BLOCK_ID.finditer(window[:end])]
        for kind, ident, pos in found:
            if (kind, ident) not in seen:
                seen.add((kind, ident))
                out.append({"kind": kind, "id": ident, "file": f"{rel_prefix}{rel}:{line_of(text, pos)}"})
    return out
