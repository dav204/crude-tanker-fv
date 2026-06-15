# PLAN.md — current focus: CRUDE BACKTEST (edge verdict)

> **FREEZE IN EFFECT (2026-06-14).** All feature / sector / methodology work
> is frozen until the crude backtest below returns a recorded verdict on the
> one question that gates everything: **does this tool have edge?** Only the
> backtest (in `backtest/`) and bugfixes are in scope. The valuation core
> (`nav`/`blend`/`cycle`/`dividend_strip`/`scenarios`) is not to be modified.
> Decision record at the top of CLAUDE.md. Parked sprint is in the
> "FROZEN until edge verdict" section at the bottom of this file — parked,
> not deleted.

## The one question

Does *cheap-on-P/NAV* — and then the tool's *EV%* — predict forward relative
returns in the crude subsector? If neither beats noise, the tool is not a
picker and development should not resume on its current premise. The verdict
(edge / no edge / inconclusive) decides whether the freeze lifts.

## Pre-registered primary metric (LOCKED before looking at any result)

The metric is fixed in `backtest/PRE_REGISTRATION.md`, committed before any
IC is computed. In one line:

> **Mean quarterly cross-sectional Spearman IC between the signal and the
> 1-quarter-forward, equal-weight-crude-neutralized total return across the
> crude names {DHT, NAT, FRO, ECO, TNK}, with a t-stat on the time series of
> quarterly ICs.** Convention: positive IC = cheap (low P/NAV) predicts
> outperformance. Benchmarks: naive published P/NAV (Test 0) and the
> equal-weight-crude return. Non-overlapping quarters; Newey-West only where
> a window overlaps. Everything else (other horizons, per-name, sub-periods,
> the P/B proxy) is **EXPLORATORY / supporting** and labeled as such.

**Stated up front, not after:** the sample is tiny and survivor-biased
(today's crude names only; names that delisted or blew up are absent, which
flatters any value signal). Real published P/NAV exists in-repo only for
~2024-08 → 2026-06 (~7 quarters), so the primary metric's N is small and its
t-stat will likely be weak *regardless of whether edge exists*. Do not
oversell. The honest deliverable may be "inconclusive — here is exactly the
data needed to make it conclusive."

## Scope & design (cheapest test first; stop at a clear answer)

Everything lives in **`backtest/`**, separate from `src/`. We add only a
historical/vintage **loader**, a **driver** loop, and an **evaluation**
module; we call the existing pure valuation core, we do not modify it.

**Correctness property (asserted in code):** no input dated after quarter `t`
may enter the `t` computation. The signal at `t` uses only the most recent
print with `report_date ≤ asof(t)`; the forward return uses `t` and `t+1`
prices (the `t+1` price is the thing predicted, never a signal input). The
assertion fails the run if any signal row post-dates `asof(t)`.

### Test 0 — naive published P/NAV (NO engine). CHEAPEST. Do first; show result.

For DHT / NAT / FRO / ECO / TNK (defer TEN / CAPT / INSW — too short or too
complex): assemble contemporaneous published Pareto P/NAV per quarter, compute
1q-forward total return (price + dividends, Yahoo), market-neutralize against
the equal-weight crude return, and report the quarterly Spearman IC + t-stat
against the pre-registered metric.

- **Signal source:** real Pareto P/NAV from `inputs/market_data/pareto_share_prices.csv`
  (2024-08 → 2026-06). FRO is missing from that extract — recover it (bugfix
  in scope) or flag it. NAT has no real Pareto P/NAV (APPROX) — excluded from
  the real-P/NAV primary, noted.
- **Supporting (exploratory, lower-fidelity, flagged):** a price-to-book (P/B)
  proxy over a longer Yahoo-fetched window — the "depreciated-book NAV" proxy
  the brief sanctioned. Book ≠ market NAV across the cycle, so this is a
  noisier complement, not the primary.

### Test 1 — engine EV% vs naive P/NAV. ONLY if Test 0 is non-zero.

Reconstruct point-in-time `CompanyInputs` per quarter, run `value_company`
as-of each quarter, compare tool-EV% IC vs the naive-P/NAV IC. The tool must
**beat** naive P/NAV to justify itself as a picker. **Blocked on data:** only
2026-Q1 vintage inputs exist in-repo; historical balance sheets + market-data
vintages (vessel marks, FFA/spot/TC rates) would have to be supplied or
reconstructed. Do not start until Test 0 is shown and the data path is agreed.

## Data status (from the 2026-06-14 inventory)

| Need | Have in-repo | Gap |
|---|---|---|
| Published P/NAV signal | `pareto_share_prices.csv`, 2024-08→2026-06, DHT/ECO/TNK (+FRO pending extract) | No pre-2024 P/NAV anywhere; NAT never covered by Pareto |
| Prices + dividends | Single-day snapshot only | Full history fetchable via Yahoo (mechanism + allowlist exist) |
| Historical `CompanyInputs` | 2026-Q1 only | Pre-2026 balance sheets + market-data vintages absent — blocks Test 1 |

**What I will need the owner to supply to make the verdict conclusive** (TBD
after Test 0 result; do not fabricate): either an archived analyst-NAV / P-NAV
time series for the names back to ~2018 (exact format to be specified), or
authorization to extend the proxy. Detailed ask lands in `backtest/REPORT.md`.

## Definition of done

One report — `backtest/REPORT.md` — stating a verdict (edge / no edge /
inconclusive) against the pre-registered metric and BOTH benchmarks (naive
P/NAV and equal-weight crude), with the sample/survivorship caveats and the
exact data ask if inconclusive. Show Test 0 before any Test 1 work.

---

# FROZEN until edge verdict (parked, not deleted)

Everything below was the active Week-5 sprint at the moment of the freeze.
It resumes only if the backtest verdict says the tool has edge. Preserved
verbatim so no context is lost.

## Week 5 theme (parked): hardening + the event window

- **B4 — §9.9 mark-driven classification restated: SHIPPED 2026-06-12**
  (commit cb83315; two-regime k_broker band in METHODOLOGY §9, mechanical
  sweep relabel, fetch_links argparse fix). Done before the freeze.
- **B5 — anchor-basis commensurability (NOT STARTED):** `anchor_basis` enum
  on all cycle-anchor YAML blocks; MIXED-ANCHOR-BASIS flag in delta +
  reconcile; §10 non-composability paragraph; tests. Full design in the prior
  plan file history / the approved Session-B design.
- **B6 — §9.2 terminal-value options memo (NOT STARTED):** re-run the 19-name
  terminal sweep, write the four-option memo (1.0× / 0.9× / 1.1× /
  cycle-conditional) with an agent recommendation + empty owner DECISION
  block; record the owner pick.

## Event window (parked; dates have now passed — re-plan on resume)

- Weekly `/news-pull` digests (were scheduled Sat Jun-13 / Jun-20).
- GNK AGM Jun-18 + Diana tender deadline Jun-26 — on resume, read the
  outcomes and annotate `decisions/gnk_log.md` (deal-arb framing comes off on
  a tender lapse; EV/position reads revert to NAV-discount).
- FFA-OCR go/no-go: owner reviews the 16 flagged queue days, then record the
  diagnostic-vs-strip decision; Stage 2 (2020-2026 backfill) rides on it.

## Small carry items (parked)

- **§5 ask-tier verification, INTERACTIVE session:** confirm git push /
  watchlist-edit / fetch_links / curl actually PROMPT with a human present
  (the autonomous session could only prove deny rules enforce).

## Q2-refresh carry-forwards (parked; earnings calendar + preflight §0 drive timing)

- **MPCC (reports 2026-08-26):** replace cohort built-year ESTIMATES + NB
  delivery quarters with the issuer fleet list; clean per-vessel prices on the
  three handed-over sale prints; refresh the company-implied NAV anchor.
- **GSL (Aug-04/06):** Series B preferred count post-ATM; the Jun-26 $917M NB
  order's charter attachments; 20-F Item 6 board-rights verify.
- **TEN (September, H1 reporter):** TCM fee-load computation (§15 anchor);
  apply ten_log Q2-vintage kit deltas (Ulysses sale, Sola TS step-up, rolls).
- **CMDB:** the Astros sale price — clean age-8 Ultramax print if per-vessel.

## Standing threads (parked)

- **MB Shipbrokers weeklies — LANDED 2026-06-12.** Ingest route established
  (Gmail link harvest → `scripts/fetch_pdf.py` → `inputs/research_mb/`).
  Container current-rate refresh queued (owner-gated); crude NB anchor review;
  Pana anchor flagged structurally low; LNG weekly not yet delivered. Full
  once-over: `outputs/mb_weekly_check_2026-06-12.md`. The 7 MB Weekly-24 print
  candidates were promoted 2026-06-12 (commit d7c7a41) before the freeze.
- **Brokerage MCP — CLOSED 2026-06-12** (DENY rules on the synced server id;
  re-check the UUID in a fresh session's tool list — disconnect/reconnect can
  stale it).
- **OWNER ACTION pending:** ratify-or-revise the A1 horizon interpretation
  (wired as 10 strip quarters = end-2028; brief said "~12q from report date").
- **Hormuz weight-revisit trigger** — standing; preempts everything if
  physical-transit confirmation lands. (MB Weekly 24: draft memo + 30-day
  window, trigger NOT met.)
- **Deferred by owner:** /news-pull agent-half orchestration; Task-3 weight
  adjuster; demand-destruction overlay; FFA Stage 2.
