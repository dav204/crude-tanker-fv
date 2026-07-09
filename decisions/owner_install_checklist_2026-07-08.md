# Owner install checklist — WO2 activation (persisted from session, 2026-07-08)

**Status: OUTSTANDING.** Delivered in-session 2026-07-03; not yet executed. Until done the watch
layer is built but mute: no digests, no pages, no dead-man — and the WO2 drill (2.5) + Phase-0
acceptance demonstrations are blocked on it. Items 1–4 ≈ 20 minutes total.

## 1. Email channel (~5 min) — first

Gmail app password (https://myaccount.google.com/apppasswords, needs 2FA), then append to the
EXISTING `~/.config/crude-tanker-fv.env` (it already holds the Rocket.Chat creds):

```
export CRUDE_FV_SMTP_HOST=smtp.gmail.com
export CRUDE_FV_SMTP_PORT=587
export CRUDE_FV_SMTP_USER=dav204@gmail.com
export CRUDE_FV_SMTP_PASS=your-16-char-app-password
export CRUDE_FV_SMTP_TO=dav204@gmail.com
```

Verify:

```
chmod 600 ~/.config/crude-tanker-fv.env
cd ~/Projects/crude-tanker-fv
source ~/.config/crude-tanker-fv.env
PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.notify --doctor
PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.notify --verify-notify
```

Receipt: the test email on the phone. (App-password rationale + the dedicated-sender-account
alternative were discussed and accepted 2026-07-06.)

## 2. Dead-man switch (~5 min)

healthchecks.io, two checks, Period 1 day / Grace **30 h**, email alerts to dav204@gmail.com:
- `crude-fv-sentinel` → its ping URL appended to the env file:

```
export CRUDE_FV_HEALTHCHECK_URL=https://hc-ping.com/your-uuid-here
```

- `crude-fv-sentinel-lite` → ping URL used in step 3.

## 3. GitHub secret (~2 min)

https://github.com/dav204/crude-tanker-fv/settings/secrets/actions → new secret
`SENTINEL_LITE_HC_URL` = the second check's ping URL. (The Action's standing `sentinel` issue
listing true conditions is expected — it self-closes on quiet runs.)

## 4. Install the plists (~3 min)

Now SIX standing jobs (three already installed: price-refresh, rocketchat-ingest, news-pull).
Install the three missing + the throwaway ctxprobe harness:

```
cp ~/Projects/crude-tanker-fv/scripts/com.crude-tanker-fv.sentinel.plist ~/Library/LaunchAgents/
cp ~/Projects/crude-tanker-fv/scripts/com.crude-tanker-fv.harvester.plist ~/Library/LaunchAgents/
cp ~/Projects/crude-tanker-fv/scripts/com.crude-tanker-fv.edgar-poll.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.crude-tanker-fv.sentinel.plist
launchctl load ~/Library/LaunchAgents/com.crude-tanker-fv.harvester.plist
launchctl load ~/Library/LaunchAgents/com.crude-tanker-fv.edgar-poll.plist
cp ~/Projects/crude-tanker-fv/scripts/ctxprobe/com.crude-tanker-fv.ctxprobe.plist ~/Library/LaunchAgents/
cp ~/Projects/crude-tanker-fv/scripts/ctxprobe/com.crude-tanker-fv.ctxprobe-load.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.crude-tanker-fv.ctxprobe.plist
launchctl load ~/Library/LaunchAgents/com.crude-tanker-fv.ctxprobe-load.plist
launchctl list | grep crude-tanker
tail -2 ~/ctxprobe.log
```

Receipts: the grep shows 8 rows (6 standing + 2 ctxprobe); the tail shows a fresh probe line.
Then update the `installed:` flags in `decisions/launchagents_reconciliation_2026-07-03.md` and
work the 7-scenario ctxprobe checklist (`decisions/ctxprobe_checklist_2026-07-03.md`) over a week
— scenario 3 (fast-user-switch) gates schedule design.

## 5. On completion, tell the agent

It will then run the Phase-0 acceptance demonstrations (one forced flag per class to the phone,
the deliberate 2-day ping gap, the Action test issue), record receipts in
`decisions/wo2_acceptance_receipts.yaml`, and build the ZZDRILL drill (WO2 2.5) before the
Jul-28 earnings cluster.
