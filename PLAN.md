# PLAN.md — active plan / sprint handoff

A new agent reads CLAUDE.md, then this file, then starts. This is a
**forward-looking valuation aid** for shipping equities (independent NAV +
forward dividend strip, blended by cycle position), judged by the soundness of
its per-name reads — not by a cross-sectional backtest. Development proceeds
normally (the 2026-06-14 "development freeze" was lifted 2026-06-21).

**Current state (2026-06-22):** 20 watchlist names across 5 sectors; **286 tests
green**; `reconcile --all` 20/20 SANITY OK (0 fail, 0 drift); tree clean, pushed
to origin/main. Per-change detail is in `CHANGELOG.md`.

## Recent work (this sprint) — detail in `CHANGELOG.md`
- **Freeze lifted** (2026-06-21): reframed as a forward-looking valuation aid;
  CLAUDE.md DECISION-RECORD → project-stance note; PLAN.md de-gated.
- **Week-5 hardening shipped:** B4 (§9.9 two-regime k_broker), B5 (anchor-basis
  commensurability + MIXED-ANCHOR-BASIS flag, §10), B6 (§9.2 terminal multiple
  LOCKED 1.0×; cycle-conditional recorded as the triggered successor).
- **BRUT (Bruton Ltd) onboarded — 20th name** (pure-play VLCC newbuild vehicle,
  Oslo Growth). Surfaced + resolved the **§9.6 time-to-delivery PV discount**: a
  newbuild arriving in N years is PV-discounted (per-vessel `years_to_delivery`,
  `NEWBUILD_DELIVERY_DISCOUNT_RATE` 11%), backward-compatible (default 0). BRUT
  +116% SANITY-FAIL → +30.6% OK. **Rolled out** to CAPT/FRO/MPCC (GSL/CMDB have
  no Q1 NBs); CAPT refined to its exact Q1-release dates (NAV $15.03, now a
  documented −17.5% divergence — the tool is more conservative on NB timing than
  Pareto; SANITY OK).
- **Ingest:** daily incremental `sp_scan` wired into the RC-ingest wrapper
  (prints surface same-day). **Automation-drift policy:** `scripts/commit_drift.sh`
  (commit-only) flushes the cron drifters — tracked, not gitignored.
  **shipping_harvester** reviewed → kept a separate gitignored sibling (vendor as
  a VIE-style cross-check, NOT integrated into src/).
- **News pull** 2026-06-21 (`outputs/news_digest_2026-06-21.md`): no promotable
  prints; CAPT Jun-16 sponsor-VLCC deal logged (§15 tripwire); TEN dividend +36%
  (argues §15 down).

## Active backlog / what's next
### Near-term
- **GNK / Diana tender — RESOLVES Jun-26.** A one-time check is SCHEDULED
  (`gnk-diana-tender-jun26-check`, fires ~Jun-26 8pm ET): reads the tender
  outcome + any board decision on the non-binding $27.34 proposal and re-frames
  GNK (deal-arb → NAV-discount on a lapse; expect reversion toward ~0.70× Pareto
  NAV). Then annotate `decisions/gnk_log.md`.
- **FFA feed DORMANT since 2026-06-12** (source-side — the single poster stopped
  posting the parseable grid; NOT a pipeline fault; the staleness alarm fires
  weekly). Action is upstream: check the Rocket.Chat channel / consider an
  alternative FFA source (Baltic settlements, MB weekly). Only the ffa_vs_strip
  diagnostic is stale meanwhile — no live valuation input is affected.
- **Weekly /news-pull** — resume the Saturday cadence (Jun-21 digest done).

### Q2-refresh carry-forwards (earnings calendar + preflight §0 drive timing)
- **Early cluster Jul-28 → Aug-6:** STNG/ASC/TNK/CCEC, then ECO/GNK/GSL/CMDB/
  DHT/INSW/SBLK.
- **BRUT (H1, Aug-13):** confirm the Pareto-estimate balance sheet against the
  first issuer report; complete the §15 screen (Goodwood fee load + control —
  needs the admission prospectus); refine the NB cohorts.
- **CAPT (Q2):** verify the Jun-16 sponsor VLCC deal terms/funding (§15
  tripwire). NB cohorts now issuer-dated.
- **MPCC (Aug-26):** issuer fleet list → built years + NB delivery quarters (the
  `years_to_delivery` are deck estimates); 3 sale-print prices; NAV anchor.
- **GSL (Aug-4/6):** Series B prefs post-ATM; the Jun-26 $917M NB order's
  charterers + delivery schedule (then apply §9.6 to GSL); 20-F board rights.
- **TEN (Sep, H1):** TCM fee-load (§15 anchor); the +36% dividend argues the 30%
  haircut down; ten_log Q2 kit deltas. **CMDB:** the Astros sale price.

### Standing threads
- **§9.6 follow-ups:** cycle-conditional terminal (the B6 successor) on its
  triggers; GSL gets the time-to-delivery discount once its NB order's delivery
  schedule is disclosed (Q2).
- **MB weeklies:** container current-rate refresh (owner-gated); Pana anchor
  flagged structurally low; LNG weekly not yet delivered.
- **OWNER ACTION pending:** ratify-or-revise the A1 horizon (wired as 10 strip
  quarters = end-2028).
- **Hormuz weight-revisit trigger** — standing (trigger NOT met).
- **§5 ask-tier verification** — confirm git push / watchlist-edit / fetch_links
  / curl actually PROMPT in an interactive session.
- **Deferred by owner:** /news-pull agent-half orchestration; Task-3 weight
  adjuster; demand-destruction overlay; FFA Stage 2.

## Backtest (complete — reference, not a gate)
Crude-subsector edge backtest in `backtest/` (`REPORT.md`): no *statistically
demonstrated* cross-sectional edge on ~1.5yr of published P/NAV (small-sample,
not a refutation of the per-name work). Test 1 (engine EV% vs naive P/NAV) was
never run (data-blocked on historical point-in-time inputs). No longer gates
development.
