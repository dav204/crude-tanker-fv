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

# PAUSE guard (WO1 Task 3). The dirty-tree case is NOT a skip here (WO2 0.3,
# invariant 3): the sentinel itself detects a dirty tree and runs in META-MODE
# — content checks suspended, heartbeat/digest/ping still fire, DIRTY-TOO-LONG
# pages at 36h (12h in an open earnings window). A dirty reconciliation week
# must not look like death to the dead-man.
if [ -f "$PROJECT/PAUSE" ]; then
  CRON_OUTCOME=skipped-paused
  echo "$(date -u '+%Y-%m-%dT%H:%M:%SZ') SKIPPED: paused"
  exit 0
fi

echo "=== [sentinel] $(date '+%Y-%m-%d %H:%M:%S')"
rc=0
./.venv/bin/python -m crude_tanker_fv.sentinel --log state/sentinel.log \
  --notify --ping || rc=$?
# rc mapping (2026-09-02, Stage 0): 0 quiet · 2 flags · anything else — including
# 1, python's uncaught-traceback exit — stays the default `error`. Before this,
# rc=1 read as a normal flag day: the 2026-09-01 run died on a YAML ParserError
# in inputs/archive_gaps.yaml and the heartbeat said `outcome=flags`.
case $rc in
  0) CRON_OUTCOME=ok ;;
  2) CRON_OUTCOME=flags ;;
esac
echo "=== [sentinel] EXIT CODE $rc"
exit $rc
