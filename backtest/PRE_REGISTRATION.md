# Crude backtest — PRE-REGISTRATION (locked before any result is computed)

**Committed:** 2026-06-14, before running `evaluate`. Git history is the proof
of order: this file lands in its own commit prior to any IC/return computation.
Nothing below is to be edited after results are seen — if the method has to
change, that is a new, separately-dated amendment with the reason, not a quiet
rewrite.

## The question

Does *cheap-on-P/NAV* predict forward relative returns within the crude
subsector? This is the precondition for the FV tool to be a stock-picker. If a
real, contemporaneous, published P/NAV does not rank forward winners, no amount
of NAV-engine sophistication can — so we test the cheap signal first (Test 0),
and only test the engine (Test 1) if Test 0 is non-zero.

## Universe & period

Names: **DHT, NAT, FRO, ECO, TNK** (the long-listed crude names with real price
history). TEN / CAPT / INSW deferred (too short or too complex). Period: the
window for which a **real published P/NAV** exists in-repo — the Pareto Shipping
Daily extract, **2024-08-22 → 2026-06-09** (~7 calendar quarters). There is NO
published P/NAV in-repo before 2024-08; the brief's 2018–2025 span is not
attainable from repo data (see REPORT data-ask).

## PRIMARY metric (one, locked)

> **Mean quarterly cross-sectional Spearman rank IC between the signal at
> quarter-end `t` and the 1-quarter-forward, equal-weight-crude-neutralized
> total return, averaged over quarters, with a t-stat on the time series of
> quarterly ICs.**

Exact construction:

1. **as-of dates** = calendar quarter-ends (Mar-31 / Jun-30 / Sep-30 / Dec-31).
2. **signal_i(t)** = the most recent Pareto published P/NAV for name *i* with
   `report_date ≤ asof(t)`, **only if** that print is within **45 calendar
   days** before `asof(t)` (staleness guard — this correctly drops a name once
   its feed stops, e.g. ECO after 2025-04; a stale P/NAV is not a
   contemporaneous signal). Otherwise the name-quarter is missing.
3. **total return_i(t→t+1)** = `adjclose_i(last trading day ≤ asof(t+1)) /
   adjclose_i(last trading day ≤ asof(t)) − 1`, using Yahoo adjusted close
   (adjusted close embeds dividends + splits → it is a total-return series).
   Both endpoints must exist or the name-quarter is dropped.
4. **relative return** = `return_i(t→t+1) − mean_j return_j(t→t+1)` over the
   names present at `t` (this is the equal-weight-crude neutralization the brief
   specifies).
5. **IC(t)** = Spearman( −P/NAV_i(t), relative_i(t→t+1) ) across names present.
   Sign convention: **positive IC = cheap (low P/NAV) predicts outperformance**
   (the direction the tool's thesis requires). A quarter is used only if
   **≥ 3 names** are present (a 2-name Spearman is degenerate, ±1).
6. **Primary statistic** = `mean_t IC(t)`; **t-stat** = `mean / (sd / sqrt(Nq))`
   over the Nq usable quarters. Quarters are non-overlapping → the quarterly ICs
   are treated as independent draws; plain t-stat. (Newey-West is used only for
   the exploratory overlapping-window reads below.)

## Benchmarks (pre-specified)

- **Equal-weight crude return** — the return the neutralization removes; reported
  alongside so the signal is judged on *relative* skill, not beta.
- **Naive published P/NAV** — in Test 0 the signal under test *is* naive
  published P/NAV, so "vs naive P/NAV" is the identity; the meaningful
  comparison for Test 0 is **vs zero IC**. The "must beat naive P/NAV" bar binds
  in **Test 1** (tool EV% IC vs this same naive-P/NAV IC).

## Pre-registered decision rule (verdict)

Against the PRIMARY metric:

- **EDGE (precondition met):** mean quarterly IC **> 0** AND **t-stat ≥ 2.0**.
- **NO EDGE:** point estimate near zero or wrong-signed with a reasonably tight
  SE — operationally `mean IC ≤ 0` with `|t| < 2`, i.e. no positive relationship
  detectable and the point estimate not encouraging.
- **INCONCLUSIVE:** a positive point estimate that does not clear t ≥ 2 — i.e.
  suggestive but underpowered. **Given Nq ≈ 7, this is the most likely outcome
  even if a true edge exists**, and we will say so rather than over-claim either
  way. Absence of significance at this N is NOT evidence of absence.

The verdict on the PRIMARY decides the freeze. The secondary/exploratory reads
below inform *what to do next* (extend data, or run Test 1), not the verdict.

## SECONDARY (pre-registered, lower-fidelity, NOT the verdict)

- **P/B proxy over the longest Yahoo-fetchable window** (~2020→2025): identical
  machinery with signal = −(price / book-value-per-share). This is the
  "depreciated-book NAV" proxy the brief sanctioned. **Fidelity caveat, stated
  before seeing it:** book value (depreciated historical cost) diverges from
  market NAV precisely across the shipping cycle, so the P/B-IC may say little
  about whether *P/NAV*-cheapness predicts returns. It buys N (≈20 quarters,
  meaningful t-stat) at the cost of signal fidelity. Reported, flagged, never
  used as the primary verdict.

## EXPLORATORY (researcher degrees of freedom; report, never headline)

Monthly horizon (overlapping → Newey-West SE), per-name time-series, sub-period
splits, NAT included via its APPROX band P/NAV, and a tangible
cheap-minus-rich quarterly spread-return portfolio readout. Any of these that
looks strong is a hypothesis for future pre-registration, not a result.

## Caveats locked up front (not added after)

- **Survivorship:** the universe is *today's* crude names. Names that delisted,
  were acquired at distress, or blew up are absent. A value signal looks better
  on survivors than it was in real time — this biases any positive finding
  upward and cannot be removed with repo data.
- **Tiny N:** ~7 quarters, 3–4 names. The primary is underpowered by
  construction; the t-stat bar is honest but hard to clear.
- **No look-ahead (asserted in code):** the loader asserts every signal row
  feeding `t` has `report_date ≤ asof(t)`; the run aborts otherwise.
- **Single data vendor** for the signal (Pareto) and returns (Yahoo). No
  cross-vendor validation of either.

---

# AMENDMENT 1 — wide shipping panel (2026-06-14, after Test 0 verdict)

Test 0 returned INCONCLUSIVE because a 4-name crude cross-section is
underpowered at any feasible sample (quarterly-IC sd ≈ 0.66; detecting IC 0.05–
0.10 needs decades–centuries). Per owner decision, we widen the universe to the
full shipping P/NAV panel to obtain a **powered** read on the precondition.
This is a NEW pre-registration (different universe), committed before its
results, same discipline. It does not retroactively change Test 0.

**Universe.** All shipping names with real published Pareto P/NAV **and** a
USD listing (returns must be currency-consistent; Yahoo adjusted close, USD).
The USD restriction drops Oslo/EUR-only names (AWILCO, BWLP, DIS, ODFB, SNI,
MPCC) — flagged as a second selection filter, not silently. NAT still excluded
(prints `na`). Each name carries a curated sector label (crude / product /
dry_bulk / lng / lpg), held in code, auditable.

**Why sector-neutral.** Cross-sector P/NAV *levels* are not comparable (LNG and
tanker NAV norms differ — the methodology says so), so a raw cross-sectional
P/NAV rank would partly pick *sectors*, not names. The tool's actual job is
peer-relative (is this name cheap vs its NAV/peers). So the PRIMARY is
sector-neutralized.

**PRIMARY metric (locked).**
> Mean over quarters of the **sector-neutral pooled cross-sectional Spearman
> IC**: for quarter `t`, within each (sector,`t`) cell with ≥2 names, rank names
> by cheapness (−P/NAV) and by 1q-forward total return as fractional in-cell
> ranks; pool all such names across sectors; IC(t) = Spearman(cheap-rank,
> return-rank) across the pooled set. Average IC(t) over non-overlapping
> quarters; t-stat on the quarterly series. Positive IC = cheap predicts
> outperformance vs sector peers.

Signal construction, staleness guard (45d), and the no-look-ahead assertion are
identical to the primary above.

**Decision rule (same thresholds):** EDGE = mean IC > 0 AND t ≥ 2.0;
NO-EDGE = mean IC ≤ 0 with |t| < 2; INCONCLUSIVE otherwise. This verdict, being
adequately powered, is the one that can actually move the freeze.

**SECONDARY (reported, not the verdict):** raw whole-panel per-quarter Spearman
of −P/NAV vs (return − equal-weight-panel return) — powered but cross-sector
confounded.

**EXPLORATORY:** per-sector ICs; sector-neutral cheap-minus-rich spread;
pooled-observation IC with a quarter-block bootstrap SE.

**Caveats (additional to the base set):** survivorship now spans all of
today's shipping names (stronger survivor bias than crude alone); the USD-
listing filter is itself a selection; LNG/LPG sectors are thin (≤2 names) and
contribute little after sector-neutralization; this answers "does cheap-on-
P/NAV predict peer-relative returns in (surviving, USD-listed) shipping," which
is broader than "crude subsector" — it is a precondition read, not a
crude-specific verdict.
