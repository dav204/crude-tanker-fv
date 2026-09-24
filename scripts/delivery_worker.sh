#!/bin/sh
set -eu
PROJECT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT"
export PYTHONPATH=src
JOB=delivery-worker
. "$PROJECT/scripts/cron_lib.sh"
if [ -f PAUSE ] || [ -f state/operations/disabled ]; then
  CRON_OUTCOME=skipped-paused
  exit 0
fi
trial_rc=0
./.venv/bin/python -m crude_tanker_fv.vie_trial run --if-due || trial_rc=$?
./.venv/bin/python -m crude_tanker_fv.operations worker
if [ "$trial_rc" -ne 0 ]; then
  CRON_NOTE="VIE shadow execution failed; see state/vie_exit/latest.json"
  exit "$trial_rc"
fi
CRON_OUTCOME=ok
