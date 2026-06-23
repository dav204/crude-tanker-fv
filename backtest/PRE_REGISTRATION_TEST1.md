# Test 1 — engine EV% ex-post falsification — PRE-REGISTRATION (locked)

**Committed:** 2026-06-22, **before** any historical EV% is computed and before
the data backfill that feeds it. Git history is the proof of order: this file
lands in its own commit prior to `backtest/run_engine_test1.py` producing any
result. Nothing below is editable after results are seen — a method change is a
new, separately-dated amendment with its reason, never a quiet rewrite. (Same
discipline as `PRE_REGISTRATION.md` Test 0 / Amendments 1–3.)

This is **Test 1**: the tool's *own* signal (the engine's probability-weighted
EV%), not a proxy. Test 0 and Amendments 1–3 tested whether *cheapness*
(published P/NAV, or a P/B proxy) predicts returns; Amendment 3 was a powered
near-null on the P/B proxy. Test 1 asks the narrower, decisive question the proxy
cannot: **does the engine's market-NAV-based EV% add ex-post signal?**

## The question (one, locked)

> Within a sector, does a higher engine **EV%** (probability-weighted scenario
> fair value vs price, computed *as-of* the quarter with no look-ahead) predict
> a higher 1-quarter-forward total return, relative to sector peers?

EV% is the engine's headline signal: `ev_pct = (probability-weighted scenario FV
− price) / price`, the number the BUY/TRIM/HOLD band keys off
(`scenarios.py`). High EV% = the engine calls the name cheap.

## Universe & period (locked)

- **Names:** the watchlist names with reconstructable point-in-time inputs —
  Sharadar SF1 balance-sheet core + cached prices + a broker-weekly vessel-mark
  vintage. The **3 Oslo-only names (CAPT, BRUT, MPCC) are excluded** (no Sharadar
  / SEC filer record — same exclusion as Amendment 3). Realized universe is
  data-determined and reported; expected ~14–17 names as vintages populate.
- **As-of dates:** calendar quarter-ends. **MVP window 2024-Q1 → present**
  (~6–9 quarter-blocks — the era the broker-weekly parsers are already tuned
  against). **Powered window 2018-Q3 → present** (~28–32 blocks — the depth the
  free broker archives reach; gated on per-era parser backfill per the data
  contract). The window actually run is reported with the result.
- A name enters a quarter's cross-section only when **all** of its as-of inputs
  are public at the quarter-end (the no-look-ahead spine below).

## Signal construction (locked)

1. **EV%_i(q)** = the engine's probability-weighted EV% for name *i* valued
   **as-of** quarter `q`: `run_scenarios_watchlist(quarter=q, asof_quarter=q,
   inputs_dir=<vintage q>)` (the Phase-3b as-of plumbing), reading that vintage's
   point-in-time inputs (DATA_CONTRACT_TEST1.md). `use_transaction_anchored`
   matches the live default (True) — historical transaction anchors apply only
   where a print is dated ≤ q.
2. **Cheap = high EV%.** Sign convention is explicit and tested: the panel passes
   `−EV%` as the cheapness key so the reused `evaluate_wide.wide_quarter_ic`
   (built for P/NAV, where *low* = cheap) ranks *high* EV% as cheap.
3. **total return_i(q→q+1)** = `adjclose_i(≤ q+1) / adjclose_i(≤ q) − 1`
   (Sharadar SEP `adjclose`, the split+dividend-adjusted total-return series, the
   same source/loaders as Amendment 3). Both endpoints must exist.

## PRIMARY metric (one, locked — same machinery as Amendments 1–3)

> Mean over usable quarters of the **sector-neutral pooled cross-sectional
> Spearman IC** between EV%-cheapness (`−EV%`) and 1-quarter-forward total
> return: within each (sector, `q`) cell of ≥2 names, average-rank by cheapness
> and by forward return, center each rank by the cell mean, pool across sectors,
> correlate the pooled centered ranks. Average that quarterly IC over
> non-overlapping quarters; t-stat on the quarterly IC series
> (`evaluate_wide.wide_quarter_ic` + `mean_t`, reused unchanged). Positive IC =
> higher engine EV% predicts peer-relative outperformance.

A quarter is usable iff **≥4 pooled names** in sector cells of ≥2 (the
`run_proxy` filter). Quarter-block bootstrap 95% CI on the mean IC: blocks of
**4** quarters, **B = 10000**, **seed = 20260622** (locked).

## Pre-registered decision rule (verdict)

The engine test is asymmetric by design — the memo
(`outputs/test1_data_feasibility_memo_2026-06-22.md`) is explicit that **the only
outcome that should impeach the tool is a gross sign inversion** (EV% is
*anti*-predictive). So:

- **FAIL (engine EV% is anti-predictive — impeaches reliance on the signal):**
  mean IC **< 0** AND **t ≤ −2.0** (equivalently, bootstrap CI entirely below 0).
- **EDGE (engine EV% adds signal):** mean IC **> 0** AND **t ≥ 2.0**.
- **INCONCLUSIVE:** otherwise. **This is the pre-stated expected MVP outcome**
  (~6 blocks is ~50–70% powered vs a moderate effect, blind to a small one);
  absence of significance at the MVP n is NOT evidence of absence. The powered
  window can additionally clear EDGE/FAIL against a *moderate* effect (IC ≈
  0.15–0.20), still blind to a small one.

## SECONDARY (pre-registered, reported, NOT the verdict)

- **Directional sign hit-rate** `p̂` — the fraction of name-quarters where
  `sign(EV% relative to sector mean)` matches `sign(relative forward return)`,
  with a quarter-block bootstrap CI. The memo's explicit fail trip: **anti-
  predictive iff `p̂ ≤ 0.40` and the CI upper bound < 0.50.** Reported alongside
  the IC as the most interpretable "is the call directionally right" read.
- **Raw whole-panel IC** (cross-sector confounded), as in the proxy tests.
- **EV% vs the naive published-P/NAV IC** (Amendment-1 machinery) where a
  contemporaneous Pareto P/NAV exists (2024-08+) — does the *engine* beat the
  *naive broker cheapness* on the same name-quarters? (The "must beat naive"
  bar; reported only on the overlapping window.)

## EXPLORATORY (researcher DoF; report, never headline)

Per-sector ICs; split-half stability; EV% magnitude vs |return| (not just sign);
the HOLD-band (|EV%|<10%) and NB-heavy name-quarters flagged separately (the
memo's staleness-sensitive subset); a held-flat-marks ablation (how much of EV%'s
movement is marks vs price). Any that look strong are hypotheses for future
pre-registration.

## No-look-ahead spine (asserted in code — the run aborts otherwise)

Every datum is stamped with the date it became **public** and every as-of run
filters to `stamp ≤ q-end`: EDGAR `acceptanceDateTime` / Sharadar `datekey` for
balance-sheet fields (reused `loaders.bvps_at`-style `filed ≤ asof` guard); the
broker-weekly issue `report_date` for vessel marks / TC / spot; the as-of
scenario doc carries only that vintage's forward-quarter curves and
`run_scenarios(asof_quarter=…)` **fails fast** if it is asked for a vintage whose
keys are absent (Phase 3b). Prices use `price_at` (`date ≤ asof`).

## Caveats locked up front

- **Underpowered MVP by construction** — ~6 blocks catches only a gross
  inversion; INCONCLUSIVE is the expected, honest MVP result. Power compounds
  forward (every new quarter adds a block) and with the pre-2024 backfill.
- **Survivorship** — today's watchlist names; delisted/distressed shipping names
  absent, biasing any positive finding upward (so a null/negative is, if
  anything, conservative).
- **Slow-rolled fleet / shipping-specific balance sheet** (DATA_CONTRACT_TEST1.md)
  perturb EV% *magnitude*, not *sign*, except for HOLD-band and NB-heavy
  name-quarters — which are flagged, not trusted, per the memo.
- **Single-vendor marks** — one broker-weekly value series per class per vintage;
  no cross-vendor mark validation. Prices single-vendor (Sharadar).
- **Historical scenario set** — the live bespoke geopolitical scenarios (MoU
  paths) are 2026-specific and are NOT back-projected; historical vintages use a
  neutral mean-reversion forward / symmetric bracket built from the vintaged
  broker-weekly TC+spot (DATA_CONTRACT_TEST1.md §"scenario forward"). This is the
  one deliberate departure of the historical engine from the live bespoke-scenario
  engine, locked here so it is not a post-hoc choice.
- **This tests the engine's signal, not its calibration to any broker** — no
  Pareto target enters EV% (verified: `consensus_pnav` is absent from the
  valuation path). The naive-P/NAV comparison is a benchmark, not a target.
