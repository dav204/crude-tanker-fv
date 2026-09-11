# OPERATING.md — how this project runs, and where you come in

Written 2026-09-11 after the owner asked "what is the surface for engaging with this project".
One page. What runs by itself, what an agent does on a schedule, what only you do, and the one
surface you watch. Times are given in UTC with the machine-local (Pacific) launchd hour beside
them; the desktop app shows its own task times in your display zone.

## The one surface: your inbox

You read email. Nothing else is required.

| Email | When | What it means | What you do |
|---|---|---|---|
| `[crude-fv] daily digest` | every day after the sentinel run (15:15 UTC / 08:15 machine-local) | status, sent on OK days too; its absence is the tell | nothing |
| `[crude-fv] PAGE: n flag(s)` | only when YOUR action is needed | each line carries `ACTION: OWNER …` saying what to do | do the named action, or nothing if it says "(optional)" |
| weekly report | Saturdays (catches up on Monday if the Mac slept) | the week's surface changes, band hits, fork docket | read it |
| healthchecks.io alert | when the sentinel did not ping for a day | the automation itself is down | open a chat in this repo and say "sentinel did not ping" |

A page never asks for agent-class work. Filings triage, earnings-date sweeps, unreadable-filing
recovery and watchlist pair rebases ride the digest and the agent tasks below; the routing table
is `inputs/notify.yaml` and `tests/test_notify.py` reds the build if a page-class tag has no
owner action text.

Most pages are of the form "object within three business days or it runs" (`FORK-EXECUTABLE`,
policy `inputs/forks.yaml`). Silence executes the recommendation. To object, open a chat in this
repo and say so in one line.

## Layer 1 — runs by itself (launchd on this Mac; no app, no agent, no LLM)

| Job | Cadence | Does |
|---|---|---|
| `edgar-poll` | hourly at :20 | stages new EDGAR / MFN / Oslo / HKEX arrivals into `inputs/filings/` + the manifest |
| `rocketchat-ingest` | 14:00 UTC (07:00 local) | pulls the broker-chat feed into the archive |
| `sentinel` | 15:15 UTC (08:15 local) | all checks → weekly report if owed → **auto-land** explained drift (`promote land`) → **auto-push** → digest email + any page + healthchecks ping |
| `price-refresh` | 01:30 UTC (18:30 local) | writes the day's price vintage; the next sentinel lands it as its own commit |
| `news-pull` | Sat 15:00 UTC (08:00 local) | the scanner half of the weekly news sweep |
| `harvester` | Sat 16:00 UTC (09:00 local) | the vendored `shipping_harvester` S&P scan into the print queue |

The scripts are `scripts/*_cron.sh`; secrets come from `~/.config/crude-tanker-fv.env`. These run
whether or not the desktop app is open, as long as the Mac is awake.

## Layer 2 — agent tasks (Claude scheduled tasks; run only while the desktop app is open)

Each task starts cold from this repo's CLAUDE.md and its own SKILL.md. If the app was closed when
one was due, it runs at the next launch. Producer side:

| Task | Cadence | Does |
|---|---|---|
| `crude-fv-filings-triage` | daily, after the sentinel | dispositions every arrival in the 48h window (record-only / calendar / print / refresh-trigger / unreadable), appends `decisions/filings_triage_log.md`, acks the ledger so it stops flagging; pages you only for an `owner` disposition |
| `crude-fv-mb-weekly-harvest` | Saturday morning | the four MB Shipbrokers weeklies from Gmail into `inputs/research_mb/` |
| `crude-fv-weekly-news-pull` | Saturday morning | the web-reading half of the news sweep into a dated digest |
| drill one-shots | as scheduled | arm / restore the healthchecks ping-gap drill (marker file) |

Governor side (repo `../portfolio-governance`):

| Task | Cadence | Does |
|---|---|---|
| `portfolio-weekly-monitor` | Friday after the US close | reads the live book and the producer's `outputs/book_scorecard.json`; flags any tripwire, tier or label change; writes `monitor/log.md`; never trades |
| `portfolio-quarterly-review-kickoff` | 26th of Mar / Jun / Sep / Dec | prepares the review pack; you decide |

## The seam: producer → governor is a file, not a conversation

The sentinel lands and pushes `outputs/book_scorecard.json` (schema major version 2) every day.
The governor's Friday monitor reads it and flags a tier or position-label change on any holding.
Nothing about your positions is decided in this repo; nothing about valuation is decided in that one.

## Layer 3 — you (the only things that are yours)

- **Rule on a page.** Open a chat in the repo the page names and say one line.
- **Object to a fork, or don't.** Silence after three business days executes the recommendation.
- **Submit orders.** Claude drafts IBKR order instructions in the governor repo; you click submit.
- **Decide at the quarterly review.** The kickoff pack is analysis; the decisions are yours.
- **Permissions.** Only you edit `.claude/settings.json`. Today the ask-tier files are the
  watchlist, transactions and the FFA curve, plus `git push` from a chat (the cron pushes on its
  own). An unattended agent stalls on an ask-tier action, so a promotion that touches those files
  happens in a chat with you present, or you loosen the rule per file class.
- **Re-authenticate** a surface when a `REAUTH-NEEDED` page names one.

## What still needs the hand crank (honest list, 2026-09-11)

- A balance-sheet build when a results filing lands (TEN Q2 is waiting on its 6-K).
- Packet refreshes that end in a watchlist / transactions / FFA edit.
- The baseline ratify (`scripts/ratify_baseline.sh`) — human-committed by design.
- Order submission, and anything that changes account settings at the broker.

## Where to open a chat

- Producer questions, rulings, sheet builds: a session **inside** `~/Projects/crude-tanker-fv`.
- Brokerage, orders, reviews: a session **inside** `~/Projects/portfolio-governance`.
- Never a session in `~/Projects` itself: it loads neither repo's CLAUDE.md and neither
  permission file, so it has no operating rules and the IBKR connector is neither allowed nor
  denied by design. The two repos meet through git and the scorecard, not a shared chat.
- Compaction inside a session does not require a new one; start fresh at a clean boundary if you
  like, in the repo for the work.

## The page vocabulary (what a page can ask of you)

| Tag | Your action |
|---|---|
| `SURFACE-INCOHERENT` | a guard contradicted the published surface; the agent halted — read the named check and rule |
| `FILING-OVERDUE` | the issuer has not filed past its window — chase, or hold the name on its prior sheet |
| `TRIGGER-DUE` | an observable you registered is due — record its outcome, or say "agent" |
| `FORK-EXECUTABLE` | optional: object today, else the recommendation runs |
| `DIRTY-TOO-LONG` | the tree has been mid-surgery for days — finish, stash, or say "discard" |
| `REAUTH-NEEDED` | re-authenticate the named surface |
| `FETCH-FAILED` (in reporting season, two runs) | check the network or the credentials file |

Everything else in an email is information.
