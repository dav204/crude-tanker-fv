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

# WEEKLY REPORT (2026-09-02) — Saturday only, on the back of the run that already has the
# env sourced and the channel proven. Deliberately NOT a new launchd job: a new plist is an
# owner install, and this needs none. The report is the owner-facing surface that replaces
# reading a 30-flag daily digest; its failure must never fail the sentinel, so it is
# non-fatal and its rc rides the note.
# Called EVERY run, not gated on the weekday: the module decides (weekly_report.is_due).
# A shell `date +%u -eq 6` test was the first cut and it failed on its first real Saturday —
# the Mac was dark 9/05-9/06, launchd coalesced the missed firings into one run on Monday
# 9/07, and the weekday test was false there, so the report skipped and could never catch up.
echo "=== [weekly-report] $(date '+%Y-%m-%d %H:%M:%S')"
report_rc=0
./.venv/bin/python -m crude_tanker_fv.weekly_report --if-due --send || report_rc=$?
[ "$report_rc" -eq 0 ] || CRON_NOTE="${CRON_NOTE:+$CRON_NOTE,}weekly_report=rc${report_rc}"
echo "=== [weekly-report] EXIT CODE $report_rc"

# Auto-land (owner's word 2026-09-10, "wire it in now"): the promoter's landing lane
# re-ratifies the drift-gate baseline ONLY when every precondition holds — 0 UNEXPLAINED,
# every moved row annotated since the last ratify, drift-only tree, no flip toward BUY, the
# committed surface current for HEAD and fresh. A quiet gate lands nothing; a FREEZE (rc 1)
# is the normal state while a move awaits its annotation and rides the ledger note. Runs
# BEFORE auto-push so the baseline commit goes out in the same morning.
echo "=== [auto-land] $(date '+%Y-%m-%d %H:%M:%S')"
land_rc=0
PYTHONPATH=src ./.venv/bin/python -m crude_tanker_fv.promote land || land_rc=$?
[ "$land_rc" -eq 0 ] || CRON_NOTE="${CRON_NOTE:+$CRON_NOTE,}auto_land=rc${land_rc}"
echo "=== [auto-land] EXIT CODE $land_rc"

# Auto-push (owner ruling 2026-09-10): push main when the tree is drift-only and the drift
# gate reads 0 UNEXPLAINED. Held states ride the ledger note; a push is never a way past a
# red gate. Runs here because launchd already has the shell, the env, and the keychain.
echo "=== [auto-push] $(date '+%Y-%m-%d %H:%M:%S')"
push_rc=0
bash scripts/auto_push.sh || push_rc=$?
[ "$push_rc" -eq 0 ] || CRON_NOTE="${CRON_NOTE:+$CRON_NOTE,}auto_push=rc${push_rc}"
echo "=== [auto-push] EXIT CODE $push_rc"

exit $rc
