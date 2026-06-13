# PLAN.md — single focus: DOES THE CRUDE TOOL HAVE EDGE?

> **DEVELOPMENT FROZEN (2026-06-13, owner directive).** Everything in this
> repo is on hold until the crude backtest below returns a verdict
> (edge / no edge / inconclusive). Only backtest-supporting code and
> bugfixes are in scope. See the decision record at the top of CLAUDE.md.
> All prior sprint work is parked in "FROZEN until edge verdict" below —
> parked, not deleted.

A new agent starting here reads CLAUDE.md (incl. the freeze decision
record), then this file, then works ONLY on the backtest.

## The one question

Does cheapness on P/NAV — and, if so, the tool's own EV% signal — predict
forward relative returns in the crude tanker subsector? If neither beats a
coin flip, the tool has no demonstrated picking edge and the elaborate
NAV/blend/strip machinery is not earning its keep as a stock selector.

## Pre-registered primary metric (FIXED before looking at any result)

> **Mean quarterly cross-sectional Spearman rank IC between the signal and
> the 1-quarter-forward market-neutral return across the crude names, with a
> t-stat** (t = mean_IC / (std_IC / sqrt(N_quarters)), non-overlapping
> quarterly windows; Newey-West lag-1 SE reported alongside as a
> robustness check).
>
> - Signal for Test 0 = cheapness = **−P/NAV** (lower P/NAV ⇒ higher
>   expected forward return ⇒ positive IC means cheap-on-P/NAV outperforms).
> - Signal for Test 1 = the tool's **EV%** (expected value vs price).
> - "Market-neutral return" = each name's forward return minus the
>   equal-weight average forward return of the crude names in that quarter's
>   cross-section.
> - Benchmarks the tool must beat to justify itself: (a) the naive −P/NAV
>   IC, and (b) the equal-weight-crude basket (the market-neutral baseline,
>   IC ≈ 0 by construction).
>
> Any other horizon, bucket, or sub-window is **exploratory**, labelled as
> such, and does not move the verdict.

This metric is pre-registered in `backtest/PRE_REGISTRATION.md` (committed
before results). The verdict is reported against THIS metric only.

## Honesty constraints (non-negotiable)

- The sample is tiny and **survivor-biased** (today's crude names only) —
  say so in the report; do not oversell a point estimate.
- Non-overlapping windows OR Newey-West SEs for any overlapping construction.
- **Do NOT invent data.** Where clean historical P/NAV is missing, use a
  transparent proxy (depreciated-book NAV / archived analyst NAV), FLAG it,
  and list exactly what the owner must supply — never fabricate inputs.

## The backtest — cheapest test first, stop at a clear answer

All code under `backtest/`. Must not modify `src/` valuation core
(nav/blend/cycle/dividend_strip/scenarios). Adds only: a historical/vintage
loader, a driver loop, an evaluation module. Assertion-enforced no-look-ahead.

### Test 0 — no engine (DO FIRST, report before going further)
Long-listed crude names with real price history: **DHT, NAT, FRO, ECO, TNK**
(defer TEN/CAPT/INSW — too short or too complex). Assemble contemporaneous
published P/NAV per quarter over ~2018–2025, compute forward total returns
from prices + dividends, market-neutralize by subtracting the equal-weight
crude return, report the Spearman IC of −P/NAV-rank vs 1q-forward relative
return with a t-stat. This tests whether cheap-on-P/NAV predicts anything in
crude at all — the precondition for the tool having edge.

### Test 1 — engine (ONLY if Test 0 IC is non-zero)
Reconstruct point-in-time `CompanyInputs` for those names, run
`value_company` as-of each quarter, compare the tool's **EV% IC** vs the
naive P/NAV IC. The tool must beat naive P/NAV to justify itself as a picker.

## Deliverable

One backtest report (`outputs/backtest_test0_report.md`) stating a verdict —
**edge / no edge / inconclusive** — against the pre-registered metric and the
naive-P/NAV and equal-weight-crude benchmarks. That verdict decides whether
development resumes.

## Status (live)

- Freeze made real in repo (this file + CLAUDE.md decision record). ✅
- `backtest/` scaffolding (vintage loader + driver + evaluation +
  no-look-ahead assertion) — see `backtest/`.
- Test 0 run on available on-disk data; verdict + data-needs in
  `outputs/backtest_test0_report.md` and `backtest/README.md`.
- Test 1 — GATED (designed, not run): see the verdict before lifting the gate.

---

# FROZEN until edge verdict (parked — do NOT start)

The Week 5 plan and all standing development threads are suspended here.
Resume ONLY after the owner lifts the freeze on the strength of the verdict.
Nothing below is deleted; it is the queue to pick back up.

## Week 5 work (was in-flight) — PARKED

- **B4 — §9.9 mark-driven classification restated** (half session): restate
  the §6/§9.9 mark-driven taxonomy against post-2026-06-09 txn-anchored
  k_broker semantics; language/thresholds/§6 wording only; re-pin affected
  locked tests.
- **B5 — anchor-basis commensurability** (one session): `anchor_basis`
  column in the cycle-anchor YAMLs; MIXED-ANCHOR-BASIS flag where a
  cross-sector pairing mixes FY-avg / archive-median / TC-anchored bases;
  §10 non-composability paragraph; tests for the flag.
- **B6 — §9.2 terminal value** [DECIDE-WITH-OWNER, memo only]: one-page
  options memo (1.0× / 0.9× / 1.1× / cycle-conditional terminal NAV);
  evidence = `outputs/terminal_value_sensitivity.md` + containers 10q
  horizon; implement only if the owner's decision changes the convention.
- **The event window** (calendar-driven): weekly `/news-pull` digests;
  GNK AGM Jun-18 morning-after read (pre-planned in gnk_log); GNK tender
  deadline Jun-26 re-anchor + deal-arb framing comes off; FFA-OCR
  diagnostic go/no-go owner review of the 16 flagged queue days.
- **Small carry items**: §5 ask-tier verification in an INTERACTIVE session
  (autonomous sessions auto-approve ask-class); `fetch_links` argparse fix
  (silently ignores unknown flags).

## Q2-refresh carry-forwards — PARKED (reports land regardless of freeze)

These are data-refresh obligations, not feature work; when reports land,
update inputs and reconcile, but do NOT extend methodology while frozen.

- **MPCC (reports 2026-08-26)**: replace cohort built-year + NB-delivery
  ESTIMATES with the issuer fleet list; watch for per-vessel sale prints.
- **GSL (Aug-04/06 expected)**: Series B preferred count post-ATM; the
  Jun-26 $917M NB order's charter attachments (dimension-6 tripwire);
  20-F Item 6 board-rights.
- **TEN (September, H1 reporter)**: TCM fee-load (§15 calibration anchor);
  apply ten_log Q2-vintage kit deltas at this refresh, not before.
- **CMDB**: the Astros sale price (clean age-8 Ultramax print if per-vessel).

## Standing threads — PARKED

- **MB Shipbrokers weeklies** — subscription pending first delivery; Dan
  will say when they land. Container anchor vintage frozen at 2026-04-01
  until then; the three non-container weeklies are fresh cross-checks for
  existing sectors when they arrive.
- **Brokerage MCP** — CLOSED 2026-06-12 (DENY rules on the synced server id;
  PERMISSIONS_PROPOSAL.md §6.4). Tripwire: a claude.ai disconnect/reconnect
  can change the UUID and stale the deny — re-check in a fresh session.
- **OWNER ACTION pending**: ratify-or-revise the A1 horizon interpretation
  (wired as 10 strip quarters = end-2028; the brief said "~12q from report
  date").
- **Hormuz weight revisit trigger** — standing; preempts everything if
  physical-transit confirmation lands.
- **Deferred by owner**: /news-pull agent-half orchestration; Task-3 weight
  adjuster; demand-destruction overlay; FFA Stage 2.

## Definition of done — the freeze lifts when

The backtest report states a verdict against the pre-registered metric, the
owner reads it, and the owner explicitly decides whether development resumes.
No parked item restarts before that decision.
