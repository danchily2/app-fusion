#!/bin/sh
# App Fusion legacy guard. The real check is scripts/guard.py, which finds the fusion workspace(s) from the project
# folder, the shell's folder and the paths the tool call names, above and one level below, and does nothing outside
# one. It runs on every matched tool call (about 30 ms); a cheaper gate here would have to repeat that discovery, and
# an earlier one that only looked at the project folder skipped cases the script catches.
command -v python3 >/dev/null 2>&1 || exit 0
exec python3 "${CLAUDE_PLUGIN_ROOT:-${DEVIN_PLUGIN_ROOT:-$(dirname "$0")/..}}/scripts/guard.py"
