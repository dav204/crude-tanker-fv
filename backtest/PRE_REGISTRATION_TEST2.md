# Test 2 — engine EV% time-series reversion to fair value — PRE-REGISTRATION

**Date:** 2026-06-23. Companion to `PRE_REGISTRATION_TEST1.md`. Test 1 graded the
**cross-sectional** question (does cheap-to-fair-value rank a name *above its sector
peers*) and returned a powered-ish null (IC ≈ 0). Test 2 grades the question the
tool is actually built for: **does a name being cheap to its own blended NAV +
dividend-strip fair value predict the name's *own* forward return** — i.e. does the
price revert toward the engine's fair value over time.

EV% is the engine's headline signal: `ev_pct = (probability-weighted scenario FV −
price)/price`, FV = NAV (per-vessel age-curve marks) + forward dividend strip,
blended by cycle (`scenarios.py`). High EV% = the engine calls the name cheap.

## Status of the in-sample evidence (DISCLOSED — this is why Test 2 exists)

This is **NOT a clean pre-registration of an unseen estimand.** An exploratory pass
(`backtest/run_engine_timeseries.py`, 2026-06-23, the 23-quarter 2019Q3–2026Q1 panel
from Test 1) already produced:

- **per-name within-name reversion IC +0.234**, quarter-block 95% CI [+0.015, +0.413],
  t +2.30, p(IC≤0)=0.018 — **nominally significant, positive in 12/12 names**;
- cross-sectional (quarter-de-meaned) IC **+0.008** — no name-selection beyond the cycle;
- cycle-timing IC (quarter-mean EV% vs quarter-mean fwd return) **+0.191** (n=23).

So Test 2 is **exploratory-confirmatory**: the point estimate was seen. What is
pre-registered below is the **CONFIRMATION on data not used to find it** — the only
thing that turns "+0.234 in-sample" into a verdict. The in-sample numbers are
reported as a hypothesis, not a result.

## The locked question

> Within-name, does a higher engine EV% (cheaper vs its own NAV+strip FV, as-of the
> quarter, no look-ahead) predict a higher own 1-quarter-forward total return —
> i.e. does the discount to fair value close?

## PRIMARY metric (locked)

> The **average within-name Spearman IC** between EV%(i,q) and own 1q-forward total
> return r(i,q→q+1), over names with ≥10 quarters. Significance: **quarter-block
> bootstrap** (resample the calendar quarters with replacement — the independent
> unit — recompute per-name ICs on the resample, average; B=10000, seed=20260624).
> Report the mean, the 2.5/97.5 percentile CI, and p(IC≤0).

The cross-sectional (quarter-de-meaned) IC and the cycle-timing IC are reported as
**SECONDARY** decompositions (they isolate, respectively, name-selection-beyond-cycle
and aggregate cycle-timing).

## Confirmation data (the pre-registered, not-yet-used part)

The verdict is taken on data the exploratory pass did NOT use:

1. **Out-of-sample forward quarters.** *(DROPPED as a recurring duty 2026-09-02, owner
   ruling F15 — nobody owned the per-quarter re-run; re-run only if a multi-cycle feed is
   acquired, item 2.)* Re-run each new quarter as it closes
   (2026Q2 onward). Pre-registered stopping rule: evaluate at **+8 new quarters**
   (≈ end-2028) or earlier if a paid multi-cycle feed lands.
2. **Multi-cycle history, if acquired.** A paid vessel-value feed (Clarksons SIN /
   VesselsValue) back to ~2008 would supply 2–3 *independent* cycles → the only way
   to a genuinely powered verdict now. If acquired, run Test 2 on the pre-2019
   cycles as the out-of-sample set.

## Pre-registered decision rule (verdict on the CONFIRMATION set)

- **EDGE (reversion-to-fair-value is real):** primary IC **> 0** AND the
  quarter-block 95% CI **entirely above 0** on the confirmation set.
- **FAIL (the signal was in-sample noise / anti-predictive):** primary IC **≤ 0**
  on the confirmation set (the in-sample +0.234 did not replicate).
- **INCONCLUSIVE:** otherwise (positive but CI still spans 0) — keep accruing.

## Caveats locked up front

- **One cycle.** The 2019–2026 panel is effectively a single autocorrelated cycle;
  the in-sample quarter-block bootstrap is therefore *optimistic* (it cannot sample
  "a different cycle"). No re-sampling or finer (monthly) slicing of 2019–2026 adds
  independent information — true power is a function of the number of **cycles**,
  obtainable only by waiting (compounding quarters) or buying multi-cycle history.
- **Cycle, not selection.** The signal is sector/cycle reversion ridden by correlated
  names (12/12 positive ≠ 12 independent edges); the de-meaned IC ≈ 0 confirms no
  cross-sectional name-selection. Test 2 is a **timing** claim for long single-name /
  sector positions, not a stock-ranking claim (that is Test 1, a null).
- **Same data-construction caveats as Test 1** (single-vendor marks, slow-rolled
  fleet/BS, neutral synthetic scenario forward, tanker+dry universe, survivorship).
- **Monthly frequency is deliberately NOT used:** with quarterly broker marks, the
  FV only updates quarterly, so monthly EV% variation is dominated by raw price
  bounce, not the engine's fair value — it would inflate N without testing the tool.
