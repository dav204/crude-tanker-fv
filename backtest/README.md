# backtest/ — does the crude tool have edge?

Freeze-time diagnostic. Separate from `src/`; does **not** import or modify
the valuation core (nav / blend / cycle / dividend_strip / scenarios). Pure
Python stdlib (runs in a bare container — no numpy/pandas/scipy needed).

## Verdict (Test 0)

**INCONCLUSIVE — the data on disk cannot power the pre-registered test.**
This is a *data-insufficiency* finding, **not** a no-edge finding. Full
write-up: [`outputs/backtest_test0_report.md`](../outputs/backtest_test0_report.md).

Why: the only historical P/NAV series on disk
(`inputs/market_data/pareto_share_prices.csv`) spans **2024-08 → 2026-06**
(~22 months, not the 2018–2025 scope), and within it only **DHT** is
continuous; **TNK** has a ~4-month hole, **ECO/INSW** stop at 2025-04,
**NAT** has no P/NAV, **FRO** is absent. The realizable crude cross-section
is 2–3 names early and 1–2 later — so the cross-sectional Spearman IC is
mechanically degenerate (n=2 ⇒ ±1) and the ~4-6 quarter t-stat is powerless.
The exploratory point estimate (mean IC ≈ −0.38, t ≈ −0.8) is reported but,
per the pre-registered verdict rule, does **not** establish edge or no-edge.

Test 1 (engine EV% vs naive P/NAV) is **GATED** behind a trustworthy
non-zero Test 0 and is therefore not run.

## What the owner must supply to make Test 0 conclusive

No fabrication — these are inputs to obtain (see the report for detail):

1. **Historical quarterly P/NAV, 2018–2025, for DHT, NAT, FRO, ECO, TNK** —
   archived broker NAV (Pareto/Clarksons/Fearnley) or VIE analyst NAVs. The
   binding gap. FRO missing entirely; NAT needs a real P/NAV source.
2. **Total-return history** 2018–2025 — adjusted close, or price +
   dividend-per-share with ex-dates (current returns are price-only).
3. (Test 1) **Point-in-time fundamentals** per name per quarter to rebuild
   `CompanyInputs` as-of date — only 2026-Q1 vintages exist on disk.

Transparent proxy if 1–2 are hard: depreciated-book NAV/share from
historical 20-F/10-K, flagged as a proxy — but that needs historical
financials, also not on disk.

## Layout

| File | Role |
|---|---|
| `PRE_REGISTRATION.md` | Primary metric + verdict rule, fixed before results (commit precedes results). |
| `vintage_loader.py` | Point-in-time panels; **no-look-ahead assertion** (`as_of_panel` → `LookAheadError`). |
| `returns.py` | Forward (price-only) returns + equal-weight crude market-neutralization. |
| `evaluate.py` | Spearman IC, mean-IC t-stat, Newey-West SE (pure stdlib). |
| `run_test0.py` | Driver: naive −P/NAV IC vs 1q-fwd relative return → report. |
| `run_test1.py` | GATED engine test — designed, not run. |

Tests: `tests/test_backtest_lookahead.py` (no-look-ahead + small-sample
evaluation). Note: this container has no `pytest`/`.venv`, so the suite
wasn't run here; the backtest logic was verified directly and is stdlib-only.

## Run

```
PYTHONPATH=. python3 -m backtest.run_test0      # writes outputs/backtest_test0_report.md
```

## The one enforced correctness property

**No input dated after quarter _t_ may enter the _t_ computation.**
`as_of_panel(obs, cutoff, ...)` builds the signal panel only from
observations with `obs_date <= cutoff` and asserts it, raising
`LookAheadError` on any violation. The realized forward return is an
*outcome* measured later, not an input, so it legitimately uses prices
after _t_.
