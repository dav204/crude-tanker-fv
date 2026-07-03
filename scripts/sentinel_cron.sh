#!/bin/sh
# Daily read-only sentinel (WO1 V-2/V-3, 2026-07-02): trigger due/overdue,
# input staleness, committed-surface coherence, price basis. Exit 0 = quiet.
# Invoked by launchd via ~/Library/LaunchAgents/com.crude-tanker-fv.sentinel.plist
# (installation is human-only — see the plist in this directory). Changes
# NOTHING beyond one dated line in state/sentinel.log.

set -eu

PROJECT="${CRUDE_TANKER_FV_ROOT:-${HOME}/Projects/crude-tanker-fv}"
SECRETS="${HOME}/.config/crude-tanker-fv.env"

# SMTP creds + healthchecks ping URL (WO2 0.2) — env-only, never in the repo.
if [ -f "$SECRETS" ]; then
  # shellcheck disable=SC1090
  . "$SECRETS"
fi

cd "$PROJECT"
export PYTHONPATH=src
export PYTHONUNBUFFERED=1

JOB=sentinel
. "$(dirname "$0")/cron_lib.sh"

# Collision guard (WO1 Task 3): identical to the price cron's — automation
# never runs through live surgery.
if [ -f "$PROJECT/PAUSE" ]; then
  CRON_OUTCOME=skipped-paused
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: paused"
  exit 0
fi
if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
  CRON_OUTCOME=skipped-dirty
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: dirty-tree"
  exit 0
fi

echo "=== [sentinel] $(date '+%Y-%m-%d %H:%M:%S')"
rc=0
./.venv/bin/python -m crude_tanker_fv.sentinel --log state/sentinel.log \
  --notify --ping || rc=$?
case $rc in
  0) CRON_OUTCOME=ok ;;
  1) CRON_OUTCOME=flags ;;
esac
echo "=== [sentinel] EXIT CODE $rc"
exit $rc
