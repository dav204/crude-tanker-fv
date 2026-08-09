# BRUT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $6.41
- **Model fair value:** $9.31
- **Analyst target:** $7.13

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 1,851.9 |
| + Cash & equivalents | 66.0 |
| + Working capital (net) | 0.0 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 1,373.1 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **544.8** |
| Diluted shares | 61,923,808 |
| **NAV / share** | **$8.80** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 147,500 | 0.141 | 0.000 | 0.000 |
| Q2 | 183,500 | 183,500 | 0.193 | 0.000 | 0.000 |
| Q3 | 165,500 | 165,500 | 0.394 | 0.000 | 0.000 |
| Q4 | 123,500 | 123,500 | 0.273 | 0.000 | 0.000 |
| Q5 | 111,500 | 111,500 | 0.387 | 0.000 | 0.000 |
| Q6 | 135,500 | 135,500 | 0.675 | 0.000 | 0.000 |
| Q7 | 147,500 | 147,500 | 0.744 | 0.000 | 0.000 |
| Q8 | 105,500 | 105,500 | 0.783 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 13.29 | 10.51 |
| **DivStrip implied price** | | | | | **$10.51** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.79×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $8.80 (NAV) + 0.30 × $10.51 (strip) = **$9.31**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 20.93 | 225% |
| Balance-sheet net | -14.78 | -159% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 3.15 | 34% |
| **Blend FV** | **9.31** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $9.38 |
| 95% | $9.39 |
| 100% | $9.39 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$8.80** ≥ price **$6.41** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 40,000 | 0.00× |
| 12-month FFA | 155,000 | 0.00× |
| Current spot | 285,500 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $3.35 | $6.18 | $9.00 | $11.83 | $14.65 |
| **-15%** | $3.51 | $6.33 | $9.16 | $11.98 | $14.81 |
| **+0%** | $3.66 | $6.49 | $9.31 | $12.14 | $14.96 |
| **+15%** | $3.82 | $6.64 | $9.47 | $12.29 | $15.12 |
| **+30%** | $3.97 | $6.80 | $9.62 | $12.45 | $15.27 |

_Current price $6.41. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$9.31** is +45.3% vs the current price ($6.41) and +30.6% vs the analyst target ($7.13). NAV alone covers the price (NAV/sh $8.80 ≥ $6.41); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
