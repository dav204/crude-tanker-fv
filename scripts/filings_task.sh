#!/bin/sh
set -eu
PROJECT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT"
export PYTHONPATH=src
case "${1:-}" in
  list|record) exec ./.venv/bin/python -m crude_tanker_fv.filings "$@" ;;
  *) echo 'usage: filings_task.sh list [--json] | record < dispositions.json' >&2; exit 2 ;;
esac
