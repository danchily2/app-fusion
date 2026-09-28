#!/usr/bin/env bash
set -euo pipefail
CASE="$(cd "$(dirname "$0")" && pwd)"
bash "$CASE/../_fixtures/make-apps.sh"
S="$CASE/../../scripts"
python3 "$S/workspace.py" init work --source mgr=./src-mgr --source emp=./src-emp >/dev/null
printf '# work: intent\n\nGoal: build the new app.\n' > analysis/work/INTENT.md
printf '# work: preflight\n\n## Answers\n\nOpen items.\n' > analysis/work/PREFLIGHT.md
python3 "$S/inventory.py" work --all >/dev/null
printf '# work: assessment\n' > analysis/work/ASSESSMENT.md
