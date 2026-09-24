# Producer cut — 2026-09-24 (owner: "yes to both, do the cut now")

**Supersedes the freeze's "keep all automation until the pilot review" stance.** The owner's goal is a lean
governor plus scout, not a full producer running beside it. This record amends `producer_freeze_2026-09-24.md`
(left byte-identical because it is sha256-pinned evidence) and `producer_freeze_amendment_ten_2026-09-24.md`.

## Before the cut
The fork executor's 2026-09-24 dry-FFA promote (9/23 print, `9cc10a4a`) had halted on two brittle tests. The tests were fixed in `5a047ecd` (full suite 1030 passed). The regen outputs were landed as `1bf6c39b` (landing gates a–e all pass). **This is the last curve update**: dry-bulk and tanker curves freeze at these values.

## What keeps running (the retained set)

| job | why |
|---|---|
| `edgar-poll` (launchd, hourly) + `crude-fv-filings-triage` (task, daily) | filing events for held names SB, CCEC, SBLK, TEN: the falsifier feed |
| `price-refresh` (launchd, nightly) + `sentinel` (launchd, daily: price-leg regen, auto-land, publication) + `delivery-worker` (launchd, 5-min) | valuations re-priced daily on frozen curves, so the governor's seam contract (≤72h) holds; email delivery for the governor |
| governor `portfolio-weekly-monitor` (Fri) and `portfolio-quarterly-review-kickoff` | the owner's one weekly email, plus the quarterly review |

## What is switched off (all reversible, no code deleted)

| job | mechanism | reverse with |
|---|---|---|
| `crude-fv-fork-executor` | scheduled task disabled | re-enable task |
| `crude-fv-results-shadow-build` | scheduled task disabled | re-enable task |
| `crude-fv-weekly-news-pull` | scheduled task disabled | re-enable task |
| `crude-fv-mb-weekly-harvest` | scheduled task disabled | re-enable task |
| `crude-fv-trigger-check-draft` | scheduled task disabled (reverses freeze amendment 1). TEN's war/de-escalation review trigger is now watched by the governor's Friday news sweep | re-enable task |
| `rocketchat-ingest`, `news-pull`, `harvester` (launchd) | `launchctl bootout` + `launchctl disable`; committed plists moved to `scripts/retired/` and marked `plist_committed: false` in `launchagents_reconciliation_2026-07-03.md`, so the sentinel doesn't expect their heartbeats | move the plists back, flip the flags, `launchctl enable` + `bootstrap` |

**Consequences, stated:**
- The dry-bulk FFA curve and the tanker curves stop updating. SB, SBLK, TEN and CCEC fair values move only with price from here, and become **dated stamps**.
- Their maintenance runs on filings, the falsifier events and the governor's weekly news sweep. That is the Phase 4 end-state, reached early.
- The sentinel will still list stale-input lines (Rocket.Chat, harvester, MB) **in its digest**. These are digest-only, not pages; retiring those checks is follow-up hygiene.

## VIE subscription: terms supplied by the owner, 2026-09-24
From the owner's account page (Value Investor's Edge, Full): **annual plan started 2026-03-09 ($652.16); paid $6,531.41 on 2026-04-09; next payment $6,531.41 on 2027-04-09.** The page states: "If you cancel, your credit card will not be charged in the future."
- The repo's assumed renewal of 2027-03-09 was wrong; the real renewal is **2027-04-09**.
- After this cut **no producer job reads VIE data**. Cancelling is the owner's action in the account.
- Whether access continues to 2027-04-09 after cancelling is not stated on the page. Check the confirmation screen; the archived VIE material already on disk is kept either way.
