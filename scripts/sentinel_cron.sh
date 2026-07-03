#!/bin/sh
# Daily read-only sentinel (WO1 V-2/V-3, 2026-07-02): trigger due/overdue,
# input staleness, committed-surface coherence, price basis. Exit 0 = quiet.
# Invoked by launchd via ~/Library/LaunchAgents/com.crude-tanker-fv.sentinel.plist
# (installation is human-only — see the plist in this directory). Changes
# NOTHING beyond one dated line in state/sentinel.log.

set -eu

PROJECT="${CRUDE_TANKER_FV_ROOT:-${HOME}/Projects/crude-tanker-fv}"

cd "$PROJECT"
export PYTHONPATH=src
export PYTHONUNBUFFERED=1

# Collision guard (WO1 Task 3): identical to the price cron's — automation
# never runs through live surgery.
if [ -f "$PROJECT/PAUSE" ]; then
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: paused"
  exit 0
fi
if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: dirty-tree"
  exit 0
fi

echo "=== [sentinel] $(date '+%Y-%m-%d %H:%M:%S')"
rc=0
./.venv/bin/python -m crude_tanker_fv.sentinel --log state/sentinel.log || rc=$?
echo "=== [sentinel] EXIT CODE $rc"
exit $rc
