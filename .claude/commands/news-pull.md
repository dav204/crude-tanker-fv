---
description: Weekly agent web-sweep of all watchlist names → dated review digest (prints, stance changes, deals, policy moves)
argument-hint: [TICKER,TICKER … — optional subset; default all watchlist names]
---

Run the agent-judgment half of the weekly news pull. The mechanical half
(Rocket.Chat ingest → `sp_scan` → `--links` → `fetch_links` → manifest)
runs Saturdays via `scripts/news_pull_cron.sh`; this command is the
web-side sweep that the scanners can't do.

**Hard constraint (vetting amendment 1): never write a pipeline-loaded
YAML.** This command writes exactly one file — the digest. Promotion of
anything it finds (prints, prices, policy changes) is human-only.

## 1. Build the name sets

- **All names:** tickers from `inputs/watchlist.yaml` (or the subset in
  `$ARGUMENTS` if given).
- **APPROX set:** read `APPROX_PNAV_TICKERS` from
  `src/crude_tanker_fv/reconcile.py` — do NOT hardcode; the set grows.
- **Live-event names:** detect from `decisions/<ticker>_log.md` files —
  scan for open items with future dates or unresolved triggers (tender
  deadlines, pending vessel-sale closings, announced-not-closed deals,
  revisit-on-X conditions). Not hardcoded; events resolve and new ones
  appear.

Weight the sweep effort toward APPROX + live-event names — they have no
Pareto coverage (or a pinned price) doing the work for them. Covered
names get a lighter pass.

## 2. Sweep (web search per name)

Hunt, per name, for items since the last digest (check
`outputs/news_digest_*.md` for the previous run date; default lookback
14 days on the first run):

- **Disclosed S&P prints** — vessel sales/purchases with named vessel and
  price (press releases, 6-K/10-Q mentions, trade press: TradeWinds,
  Splash, gCaptain, Lloyd's List).
- **Dividend / capital-allocation policy changes** — payout ratio moves,
  buyback authorizations, special dividends.
- **Broker stance / TP changes** — any house, not just Pareto.
- **Newbuild orders** — yard, class, count, delivery window, price if
  disclosed.
- **Deal milestones** — tender results, merger votes, closing
  announcements, extensions.
- **For APPROX names only:** a fresher market price than the watchlist
  `as_of`.
- **STANDING (added 2026-07-02, reviewer condition): war-risk insurance
  premia for Gulf/Hormuz voyages** — current level + direction (Lloyd's
  List, TradeWinds, insurer statements). Leading indicator for the §13.3
  reweight triggers (`inputs/reweight_triggers.yaml`,
  `crude_transit_normalization`); the level has been UNCONFIRMED since
  2026-07-02. Also check each dated trigger in that file whose `due` falls
  before the next Saturday and note the observable's state in the digest.

## 3. Write the digest — `outputs/news_digest_YYYY-MM-DD.md`

Sections, in order. Keep it signal-dense; a name with nothing goes in
No-action as one line, not a paragraph.

1. **Promotable candidates** (S&P prints). Each entry MUST carry
   (vetting amendment 4): vessel name, class, price, **built-year/age**,
   and an explicit **en-bloc / per-vessel-split** field. En-bloc with no
   disclosed per-vessel split = `documented-not-promoted` per the
   no-back-solve rule — record it, flag it, do not stage it for a
   transactions YAML.
2. **Stance changes** — house, date, old → new, TP.
3. **Live deals** — status per live-event name; flag anything that
   resolves the event (e.g. a tender deadline passing).
4. **Stale prices** — APPROX names are permanently stale-priced by
   construction (vetting amendment 3): list one standing known-stale
   line for the set, and add a per-name entry ONLY when the sweep found
   a fresher price (quote it with source + timestamp so the owner can
   update `watchlist.yaml`).
5. **No action** — one line per swept name with nothing material.

End the digest with the standing reminder:

> **If any print above is promoted** to a `transactions/<class>.yaml`:
> re-run the pipeline, read `outputs/transaction_anchor_comparison.md`,
> and annotate the decision log of every name whose txn-anchored EV
> moved >2pp or whose position band flipped (CLAUDE.md drift-gate rule).

## 4. Report back

Summarize to the user: counts per section, anything urgent (live-deal
resolution, fresher APPROX price, promotable print), and the digest path.
Do not promote, do not edit YAMLs, do not update decision logs — those
are the owner's follow-ups from the digest.
