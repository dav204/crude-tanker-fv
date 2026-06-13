# Crude edge backtest — Test 0 report

**Verdict: INCONCLUSIVE — the available data cannot power the pre-registered test.** This is NOT a no-edge finding; it is a data-insufficiency finding. See 'Why inconclusive' and 'Data needed'.

Pre-registered metric (fixed before results, `backtest/PRE_REGISTRATION.md`): mean quarterly cross-sectional Spearman IC of the signal (Test 0: −P/NAV) vs 1q-forward market-neutral return, with a t-stat over non-overlapping quarters.

## Data coverage actually on disk

Only historical (date, ticker, price, P/NAV) series available: `inputs/market_data/pareto_share_prices.csv`, weekly Pareto prints, **2024-08-22 → 2026-06-08** (~22 months — not the 2018–2025 scope). Network is blocked (Yahoo/stooq 403), so no external price/dividend history could be fetched.

| Name | Pareto ticker | rows | rows w/ P/NAV | P/NAV span |
|---|---|---:|---:|---|
| DHT  | DHT | 224 | 224 | 2024-08-22 → 2026-06-05 |
| NAT  | NAT | 18 | 0 | — (no P/NAV) |
| FRO absent | FRO | 0 | 0 | — (no P/NAV) |
| ECO  | ECO | 130 | 130 | 2024-08-22 → 2025-04-07 |
| TNK  | TNK | 204 | 204 | 2024-08-22 → 2026-06-05 |
| INSW  | INSW | 130 | 130 | 2024-08-22 → 2025-04-07 |

Net: of the five long-listed crude names, only **DHT** is continuous over the full window. **TNK** has a ~4-month hole in the extract (no rows mid-May → mid-Sep 2025), so two quarters below collapse to a single name. **ECO** stops at 2025-04-07; **NAT** has rows but no P/NAV (the known APPROX gap); **FRO is absent from the extract**. So the realizable crude cross-section is 2–3 names early and 1–2 names later — never enough for a non-degenerate rank IC.

## Primary result (5-name window, exploratory point estimate)

- Non-overlapping quarters with a usable cross-section: **N = 4**
- Mean quarterly IC (−P/NAV vs 1q-fwd market-neutral return): **-0.375**
- Std of quarterly IC: 0.946
- t-stat: **-0.79**  (0.05 two-sided bar, df=3: |t| ≥ 3.18)
- Newey-West (lag 1) SE: 0.256 → NW t: -1.47
- Distinguishable from zero at 0.05? **no**

Per-quarter (cross-section size in parens):

| Signal date | → forward | names (n) | IC |
|---|---|---|---:|
| 2024-09-30 | 2024-12-31 | DHT, ECO, TNK (3) | -0.50 |
| 2024-12-31 | 2025-03-31 | DHT, ECO, TNK (3) | -1.00 |
| 2025-03-31 | 2025-06-30 | DHT (1) | n/a |
| 2025-06-30 | 2025-09-30 | DHT (1) | n/a |
| 2025-09-30 | 2025-12-31 | DHT, TNK (2) | 1.00 |
| 2025-12-31 | 2026-03-31 | DHT, TNK (2) | -1.00 |
| 2026-03-31 | 2026-06-30 |  (0) | n/a |

Pairwise sign-agreement on the 2-name quarters (did the cheaper name beat the other?): **1/2**. A coin-flip test, powerless at this N.

## Exploratory: +INSW to thicken the early cross-section

- N = 4, mean IC = -0.437, t = -0.91. Exploratory only (INSW deferred by the owner; adds depth only Aug-2024→Apr-2025). Does not move the verdict.

## Why inconclusive (decided by the pre-registered verdict rule)

1. **Wrong period.** Signal series starts 2024-08; the test wanted ~2018–2025. ~22 months ⇒ at most ~7 non-overlapping quarters.
2. **Cross-section too thin.** Full-window crude P/NAV exists for only 2 names (DHT, TNK). At n=2 the cross-sectional Spearman IC is mechanically ±1 (degenerate); at n=3 it is in {−1,−0.5,+0.5,+1}. The point estimate above is dominated by this degeneracy.
3. **No total return.** Returns are price-only; crude dividends are large and cross-sectionally uneven, a material omission for the neutralized return.
4. **Underpowered t.** With N≈6 quarters, |t| must exceed ~2.57 (df=5) for p<0.05 — not reachable from this signal/cross-section.

Per the pre-registered rule, a tiny degenerate sample is **reported as exploratory and called INCONCLUSIVE**, not edge or no-edge. Test 1 (engine) is **GATED** behind a non-zero, trustworthy Test 0 IC and is therefore NOT run (it also cannot run here: no numpy/pandas/scipy and no `.venv` in this container).

## Data the owner must supply to make Test 0 conclusive

Do not fabricate any of this — these are the inputs to obtain:

1. **Historical quarterly P/NAV, 2018–2025, for DHT, NAT, FRO, ECO, TNK** — archived broker NAV prints (Pareto/Clarksons/Fearnley) or VIE archived analyst NAVs. This is the binding gap. FRO is missing entirely from the current extract; NAT needs a real P/NAV source (Pareto doesn't publish one).
2. **Total-return history** for those names 2018–2025 — adjusted close OR (price + dividend-per-share with ex-dates). Needed to replace the price-only proxy.
3. (For Test 1) **Point-in-time fundamentals** per name per quarter — fleet/balance-sheet/dividend-policy vintages — to reconstruct `CompanyInputs` as-of each quarter. Only 2026-Q1 exists on disk today.

**Transparent proxy if 1–2 are hard:** a depreciated-book NAV per share rebuilt from each name's historical 20-F/10-K (book equity ÷ shares) as a stand-in P/NAV denominator — clearly flagged as a proxy, not a broker mark. That requires historical financials, which are also not on disk. Both routes need the owner to supply source data.

## Reproduce

`PYTHONPATH=. python3 -m backtest.run_test0` (pure stdlib; no deps). No-look-ahead is assertion-enforced in `vintage_loader.as_of_panel`.
