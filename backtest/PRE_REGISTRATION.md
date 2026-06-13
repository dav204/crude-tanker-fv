# Pre-registration — crude edge backtest

**Committed before any result was computed.** (Git history is the proof:
this file and the evaluation code land in a commit that precedes the
results commit. The metric below is fixed; the verdict is reported against
it and nothing else.)

## Primary metric (THE number the verdict is graded on)

> **Mean quarterly cross-sectional Spearman rank IC between the signal and
> the 1-quarter-forward market-neutral return across the crude names, with a
> t-stat.**
>
> - `t = mean_IC / (std_IC / sqrt(N_quarters))`, computed over
>   **non-overlapping** quarterly windows (so windows do not mechanically
>   overlap). A Newey-West lag-1 SE is reported alongside as a robustness
>   check, not as the primary.
> - **Signal, Test 0** = cheapness = **−P/NAV** (lower published P/NAV ⇒
>   higher expected forward return ⇒ a *positive* IC means cheap-on-P/NAV
>   outperforms).
> - **Signal, Test 1** = the tool's **EV%** (expected value vs price from
>   `value_company`).
> - **Forward return** = price (ideally total) return from the signal date
>   to ~1 quarter later.
> - **Market-neutral** = each name's forward return minus the equal-weight
>   average forward return of the crude names present in that quarter's
>   cross-section.

## Benchmarks the tool must beat

1. **Naive −P/NAV IC** (Test 0). If this is ~0, P/NAV cheapness has no
   demonstrated predictive content in crude — the precondition for the tool
   having edge fails, and Test 1 is not run.
2. **Equal-weight crude basket** — the market-neutral baseline (IC ≈ 0 by
   construction; the signal must do better than holding the basket).
3. **Tool EV% IC vs naive −P/NAV IC** (Test 1, gated). The engine must beat
   naive P/NAV to justify itself as a picker rather than a P/NAV restater.

## Verdict rule (decided before results)

- **EDGE**: primary mean IC has the predicted (positive) sign AND is
  statistically distinguishable from zero at the pre-set bar (two-sided
  |t| ≥ the df-appropriate 0.05 critical value) AND survives the
  Newey-West SE.
- **NO EDGE**: mean IC ≈ 0 (|t| < ~1) or wrong sign with |t| at the bar.
- **INCONCLUSIVE**: the data available cannot power the test (too few
  non-overlapping quarters, too thin a cross-section, or the signal series
  doesn't span the period). Report the point estimate as exploratory only;
  do NOT call it edge or no-edge.

## Declared limitations (stated before results, not after)

- Sample is **tiny and survivor-biased** — only today's surviving crude
  names. Any point estimate is fragile; we do not oversell it.
- Cross-sectional Spearman IC is **degenerate at small n** (n=2 ⇒ IC ∈ {−1,
  +1}; n=3 ⇒ IC ∈ {−1, −0.5, +0.5, +1}). Where the realizable cross-section
  is 2 names, the IC collapses to a pairwise sign-agreement (a coin-flip
  test) and is reported as such.
- Any horizon, bucket, or sub-window other than the primary metric above is
  **exploratory** and does not move the verdict.

## Correctness property (assertion-enforced in code)

**No input dated after quarter _t_ may enter the _t_ computation.** The
signal/valuation at _t_ is built only from observations with
`date <= cutoff(t)`; `vintage_loader.as_of_panel` asserts this and raises
`LookAheadError` otherwise. (The realized forward return is an *outcome*
measured later, not an input to the _t_ computation, so it legitimately
uses prices after _t_.)
