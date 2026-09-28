#!/bin/sh
# App Fusion legacy guard. Cheap no-op outside a fusion workspace; python3 does the real check.
dir="${CLAUDE_PROJECT_DIR:-$PWD}"
[ -d "$dir/analysis" ] || exit 0
command -v python3 >/dev/null 2>&1 || exit 0
exec python3 "$CLAUDE_PLUGIN_ROOT/scripts/guard.py"
