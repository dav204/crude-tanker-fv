#!/bin/sh
set -eu
PROJECT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT"
export PYTHONPATH=src
command="${1:-}"
[ $# -gt 0 ] && shift
case "$command" in
  refresh) exec ./.venv/bin/python -m crude_tanker_fv.refresh "$@" ;;
  shadow) exec /bin/bash scripts/shadow_regen.sh "$@" ;;
  sentinel) exec ./.venv/bin/python -m crude_tanker_fv.sentinel "$@" ;;
  mb) exec ./.venv/bin/python scripts/mb_harvest.py "$@" ;;
  *) echo 'usage: routine_task.sh refresh|shadow|sentinel|mb' >&2; exit 2 ;;
esac
