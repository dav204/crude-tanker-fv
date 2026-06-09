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
PYTHONPATH=src ./.venv/bin/python -m crude_tanker_fv.ingest_rocketchat "$@"
