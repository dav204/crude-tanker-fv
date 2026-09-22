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
./.venv/bin/python -m crude_tanker_fv.operations worker
CRON_OUTCOME=ok
