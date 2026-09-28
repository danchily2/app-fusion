#!/usr/bin/env bash
set -euo pipefail
CASE="$(cd "$(dirname "$0")" && pwd)"
bash "$CASE/../_fixtures/make-apps.sh"
python3 "$CASE/../../scripts/workspace.py" init work --source mgr=./src-mgr --source emp=./src-emp >/dev/null
