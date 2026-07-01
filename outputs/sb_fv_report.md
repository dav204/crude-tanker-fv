# SB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $6.31
- **Model fair value:** $9.87
- **Analyst target:** $7.10

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Pana | 985.1 |
| Fleet value — Post-Panamax | 422.1 |
| Fleet value — Cape | 268.8 |
| + Cash & equivalents | 171.8 |
| + Working capital (net) | 53.8 |
| − Total debt | 544.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 227.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,030.0** |
| Diluted shares | 101,826,580 |
| **NAV / share** | **$10.12** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Pana, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 20,775 | 18,657 | 0.581 | 0.174 | 0.170 |
| Q2 | 19,500 | 18,147 | 0.562 | 0.169 | 0.160 |
| Q3 | 17,000 | 17,147 | 0.504 | 0.151 | 0.140 |
| Q4 | 16,500 | 16,947 | 0.487 | 0.146 | 0.132 |
| Q5 | 15,800 | 16,667 | 0.467 | 0.140 | 0.123 |
| Q6 | 15,400 | 16,507 | 0.457 | 0.137 | 0.117 |
| Q7 | 14,800 | 16,267 | 0.444 | 0.133 | 0.111 |
| Q8 | 14,500 | 16,147 | 0.437 | 0.131 | 0.106 |
| Σ discounted DPS | | | | | 1.06 |
| Terminal value (NAV, q9) | | | | 10.69 | 8.45 |
| **DivStrip implied price** | | | | | **$9.51** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$18,444/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$17,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $17,500 / 10-yr mean $11,900 = **1.42×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $10.12 (NAV) + 0.40 × $9.51 (strip) = **$9.87**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $9.96 |
| 95% | $9.98 |
| 100% | $9.99 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$10.12** ≥ price **$6.31** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 13,785 | 0.00× |
| 12-month FFA | 20,223 | 0.00× |
| Current spot | 23,307 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (59% of fleet value) | 0 | 0.00× |
| Post-Panamax (25% of fleet value) | 0 | 0.00× |
| Cape (16% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $6.65 | $8.09 | $9.53 | $10.97 | $12.41 |
| **-15%** | $6.82 | $8.26 | $9.70 | $11.14 | $12.58 |
| **+0%** | $7.00 | $8.43 | $9.87 | $11.31 | $12.75 |
| **+15%** | $7.17 | $8.61 | $10.05 | $11.48 | $12.92 |
| **+30%** | $7.34 | $8.78 | $10.22 | $11.66 | $13.09 |

_Current price $6.31. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$9.87** is +56.5% vs the current price ($6.31) and +39.1% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $10.12 ≥ $6.31); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
