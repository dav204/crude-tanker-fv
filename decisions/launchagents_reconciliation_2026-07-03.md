# LaunchAgents reconciliation — 2026-07-03 (WO2 pre-work 0.0)

One-time full sweep of the machine's scheduled-job state against the committed
inventory (WO2 R-1, generalizing defects D-2/D-4). The RC-ingest case proved
unknown-unknowns exist: a job can run on the machine for weeks with no committed
plist, or sit committed and never installed, and nothing notices. This record is
the baseline; `tests/test_plists.py` guards the knowns from here forward.

## Method

`launchctl list` (full, filtered by eye for non-Apple entries) +
`ls ~/Library/LaunchAgents/` + byte-diff of every installed repo plist against
its committed counterpart in `scripts/`. Swept 2026-07-03.

## Findings

| # | Finding | Class | Disposition |
|---|---------|-------|-------------|
| 1 | `com.crude-tanker-fv.price-refresh` — loaded (status 0), installed plist byte-identical to committed | clean | none |
| 2 | `com.crude-tanker-fv.news-pull` — loaded (status 0), installed plist byte-identical to committed | clean | none |
| 3 | `com.crude-tanker-fv.rocketchat-ingest` — loaded (status 0) and installed since Jun-8, **no committed plist** | **D-4 confirmed** | commit lands Phase 1.1; inventory below carries it as `plist_committed: false` until then (flipping the flag is the 1.1 commit's reminder) |
| 4 | `com.crude-tanker-fv.sentinel` — committed plist, **never installed, never ran** | **D-2 confirmed** | owner installs after the D-1 fix (commands below); Phase 0.2 gives it a heartbeat so non-running becomes detectable |
| 5 | Sentinel plist carried price-refresh's log paths (`state/price_refresh.log/.err` — two jobs interleaving one log) and price-refresh's 18:30-NYSE comment over an 08:15 schedule | **D-1 confirmed** | **fixed in this commit**; `test_plists.py` now asserts unique log paths + comment/schedule coherence repo-wide |
| 6 | Non-repo jobs present: `com.google.GoogleUpdater.wake`, `com.google.keystone.{agent,xpcservice}` (plists), `us.zoom.updater` (loaded) | benign third-party | documented here; out of scope |

No mis-pointed ProgramArguments, no orphaned repo labels, no jobs running from
stale paths.

## Inventory (machine-readable — parsed by `tests/test_plists.py`)

The committed-plist set in `scripts/` MUST equal the `plist_committed: true`
entries below; edit this block and the plist in the same commit.

```yaml
jobs:
  com.crude-tanker-fv.price-refresh:
    plist_committed: true
    installed: true          # verified 2026-07-03, byte-identical
    schedule: "daily 18:30"
    wrapper: price_refresh_cron.sh
  com.crude-tanker-fv.news-pull:
    plist_committed: true
    installed: true          # verified 2026-07-03, byte-identical
    schedule: "Sat 08:00"
    wrapper: news_pull_cron.sh
  com.crude-tanker-fv.rocketchat-ingest:
    plist_committed: true    # D-4 closed 2026-07-03 (WO2 1.1); comment added
    installed: true          # installed copy predates the comment — re-copy at next change
    schedule: "daily 07:00"
    wrapper: ingest_rocketchat_cron.sh
  com.crude-tanker-fv.sentinel:
    plist_committed: true
    installed: false         # D-2 — owner install pending (commands below)
    schedule: "daily 08:15"
    wrapper: sentinel_cron.sh
  com.crude-tanker-fv.harvester:
    plist_committed: true    # added WO2 1.3 (2026-07-03)
    installed: false         # owner install pending (same cp+load pattern)
    schedule: "Sat 09:00"
    wrapper: harvester_cron.sh
```

## Owner install step (human-only, closes D-2)

```
cp ~/Projects/crude-tanker-fv/scripts/com.crude-tanker-fv.sentinel.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.crude-tanker-fv.sentinel.plist
launchctl list | grep crude-tanker
```

Expect four `com.crude-tanker-fv.*` rows. First scheduled run is the next
08:15; `state/sentinel.log` gains one dated line per run. Verify once:
`launchctl start com.crude-tanker-fv.sentinel` then read `state/sentinel_cron.log`.
Update the `installed:` flag above (with date) after verifying.
