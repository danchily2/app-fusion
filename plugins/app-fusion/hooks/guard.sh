#!/bin/sh
# App Fusion legacy guard. Cheap checks here; python3 does the real work when a fusion workspace may be involved:
# analysis/ in the project folder or any folder above it, in a folder one level below it, or a legacy/ or analysis/
# path named in the tool call (Claude may have been started above or inside the workspace).
dir="${CLAUDE_PROJECT_DIR:-$PWD}"
command -v python3 >/dev/null 2>&1 || exit 0
input=$(cat)
run=0
d="$dir"
while [ -n "$d" ]; do
  if [ -d "$d/analysis" ]; then run=1; break; fi
  p=$(dirname "$d")
  [ "$p" = "$d" ] && break
  d="$p"
done
if [ "$run" = 0 ]; then
  for c in "$dir"/*/; do
    if [ -d "${c}analysis" ]; then run=1; break; fi
  done
fi
if [ "$run" = 0 ]; then
  case "$input" in
    *[Ll][Ee][Gg][Aa][Cc][Yy]/*|*[Aa][Nn][Aa][Ll][Yy][Ss][Ii][Ss]/*) run=1 ;;
  esac
fi
[ "$run" = 1 ] || exit 0
printf '%s' "$input" | python3 "$CLAUDE_PLUGIN_ROOT/scripts/guard.py"
