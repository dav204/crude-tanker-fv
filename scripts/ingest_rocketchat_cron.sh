#!/bin/zsh
# Wrapper for the daily Rocket.Chat ingest (Pareto PDFs + FFA screenshots +
# Baltic-indexes time-series). Invoked by launchd via
# ~/Library/LaunchAgents/com.crude-tanker-fv.rocketchat-ingest.plist.
#
# Secrets live in ~/.config/crude-tanker-fv.env (chmod 600), expected to set:
#   export ROCKETCHAT_USER_ID=...
#   export ROCKETCHAT_TOKEN=...

set -eu

PROJECT="${HOME}/Projects/crude-tanker-fv"
SECRETS="${HOME}/.config/crude-tanker-fv.env"

if [[ -f "$SECRETS" ]]; then
  # shellcheck disable=SC1090
  source "$SECRETS"
fi

cd "$PROJECT"
export PYTHONPATH=src

# Daily Rocket.Chat ingest (Pareto PDFs + FFA screenshots + Baltic indexes).
# Tolerate a non-fatal ingest hiccup (e.g. a transient TLS read) so the scan
# below still runs over whatever dailies did land.
ingest_rc=0
./.venv/bin/python -m crude_tanker_fv.ingest_rocketchat "$@" || ingest_rc=$?

# Incremental S&P print scan over the freshly-ingested dailies — local-only,
# cursor-based. Surfaces prints same-day instead of waiting for the Saturday
# news-pull cron (added 2026-06-21; closes the up-to-a-week scan lag the Jun-20
# run exposed). The linked-report harvest + manifest stay weekly in
# news_pull_cron.sh.
./.venv/bin/python -m crude_tanker_fv.sp_scan

exit "$ingest_rc"
