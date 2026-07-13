# SB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $6.90
- **Model fair value:** $9.78
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
| Q1 | 19,700 | 18,227 | 0.590 | 0.177 | 0.172 |
| Q2 | 19,250 | 18,047 | 0.581 | 0.174 | 0.166 |
| Q3 | 17,100 | 17,187 | 0.516 | 0.155 | 0.143 |
| Q4 | 16,500 | 16,947 | 0.500 | 0.150 | 0.135 |
| Q5 | 15,900 | 16,707 | 0.484 | 0.145 | 0.127 |
| Q6 | 15,300 | 16,467 | 0.468 | 0.141 | 0.120 |
| Q7 | 14,900 | 16,307 | 0.459 | 0.138 | 0.115 |
| Q8 | 14,600 | 16,187 | 0.451 | 0.135 | 0.110 |
| Σ discounted DPS | | | | | 1.09 |
| Terminal value (NAV, q9) | | | | 10.01 | 7.92 |
| **DivStrip implied price** | | | | | **$9.01** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$18,138/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$19,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $19,500 / 10-yr mean $11,900 = **1.62×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $10.12 (NAV) + 0.30 × $9.01 (strip) = **$9.78**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $9.85 |
| 95% | $9.87 |
| 100% | $9.87 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$10.12** ≥ price **$6.90** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 13,785 | 0.00× |
| 12-month FFA | 20,433 | 0.00× |
| Current spot | 21,258 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (59% of fleet value) | 0 | 0.00× |
| Post-Panamax (25% of fleet value) | 0 | 0.00× |
| Cape (16% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $6.57 | $8.04 | $9.52 | $10.99 | $12.46 |
| **-15%** | $6.70 | $8.18 | $9.65 | $11.12 | $12.60 |
| **+0%** | $6.84 | $8.31 | $9.78 | $11.26 | $12.73 |
| **+15%** | $6.97 | $8.44 | $9.92 | $11.39 | $12.86 |
| **+30%** | $7.10 | $8.58 | $10.05 | $11.52 | $12.99 |

_Current price $6.90. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$9.78** is +41.8% vs the current price ($6.90) and +37.8% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $10.12 ≥ $6.90); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
