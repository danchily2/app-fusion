#!/usr/bin/env python3
"""Convert an Xcode result bundle (.xcresult) into JUnit XML the proof script can read.

    python3 xcresult_junit.py <path.xcresult | tests.json> <out.xml>

Uses `xcrun xcresulttool get test-results tests --path <bundle>` (Xcode 16 or newer) and keeps both names Xcode
records: the display name (Swift Testing's @Test("RULE-017 ...") and @Suite("CAP-012 ...")) and the node identifier
(Suite/function()). Both land in the JUnit testcase name and classname, so a CAP or RULE id in either is found.
Passed and Expected Failure are passes, Failed is a <failure>, Skipped is <skipped>. A JSON file saved from
xcresulttool can be given instead of the bundle. Standard library only; exit 1 when the bundle holds no test.
"""

import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET


def load(path):
    if path.endswith(".json"):
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    out = subprocess.run(["xcrun", "xcresulttool", "get", "test-results", "tests", "--path", path],
                         capture_output=True, text=True, timeout=300, check=False)
    if out.returncode != 0:
        sys.exit(f"xcresulttool failed ({out.returncode}): {out.stderr.strip()[:400]}")
    return json.loads(out.stdout or "{}")


def cases(node, suite_path):
    kind = node.get("nodeType")
    if kind == "Test Case":
        yield suite_path, node
        return
    if kind in ("Test Suite", "Unit test bundle", "UI test bundle", "Test Plan"):
        name = node.get("name") or ""
        next_path = suite_path + ([name] if kind in ("Test Suite", "Unit test bundle", "UI test bundle") else [])
        for child in node.get("children") or []:
            yield from cases(child, next_path)


def convert(data):
    suites = ET.Element("testsuites")
    by_suite = {}
    for top in data.get("testNodes") or []:
        for path, case in cases(top, []):
            by_suite.setdefault(".".join(path) or "tests", []).append(case)
    total = 0
    for suite_name, items in by_suite.items():
        failures = sum(1 for c in items if c.get("result") == "Failed")
        skipped = sum(1 for c in items if c.get("result") == "Skipped")
        suite = ET.SubElement(suites, "testsuite", name=suite_name, tests=str(len(items)), failures=str(failures),
                              skipped=str(skipped), errors="0",
                              time=f"{sum(c.get('durationInSeconds') or 0 for c in items):.3f}")
        for c in items:
            total += 1
            ident = c.get("nodeIdentifier") or ""
            display = c.get("name") or ident
            name = display if not ident or ident.split("/")[-1] in display else f"{display} [{ident}]"
            tc = ET.SubElement(suite, "testcase", classname=f"{suite_name} [{ident.split('/')[0]}]" if "/" in ident else suite_name,
                               name=name, time=f"{c.get('durationInSeconds') or 0:.3f}")
            result = c.get("result")
            if result == "Failed":
                messages = [ch.get("name", "") for ch in c.get("children") or [] if ch.get("nodeType") == "Failure Message"]
                failure = ET.SubElement(tc, "failure", message=(messages[0] if messages else "failed")[:500])
                failure.text = "\n".join(messages)[:4000]
            elif result == "Skipped":
                ET.SubElement(tc, "skipped")
    return suites, total


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__.split("\n\n")[1])
    data = load(sys.argv[1])
    root, total = convert(data)
    os.makedirs(os.path.dirname(os.path.abspath(sys.argv[2])), exist_ok=True)
    ET.ElementTree(root).write(sys.argv[2], encoding="utf-8", xml_declaration=True)
    print(f"{total} test case(s) -> {sys.argv[2]}")
    sys.exit(0 if total else 1)


if __name__ == "__main__":
    main()
