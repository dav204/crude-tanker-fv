# SB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $6.31
- **Model fair value:** $9.75
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
| Q1 | 19,000 | 17,947 | 0.561 | 0.168 | 0.164 |
| Q2 | 18,125 | 17,597 | 0.554 | 0.166 | 0.158 |
| Q3 | 16,600 | 16,987 | 0.504 | 0.151 | 0.140 |
| Q4 | 16,000 | 16,747 | 0.488 | 0.146 | 0.132 |
| Q5 | 15,400 | 16,507 | 0.472 | 0.142 | 0.124 |
| Q6 | 14,800 | 16,267 | 0.457 | 0.137 | 0.117 |
| Q7 | 14,400 | 16,107 | 0.447 | 0.134 | 0.112 |
| Q8 | 14,100 | 15,987 | 0.439 | 0.132 | 0.107 |
| Σ discounted DPS | | | | | 1.05 |
| Terminal value (NAV, q9) | | | | 9.93 | 7.85 |
| **DivStrip implied price** | | | | | **$8.90** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$17,431/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$18,550/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $18,550 / 10-yr mean $11,900 = **1.53×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $10.12 (NAV) + 0.30 × $8.90 (strip) = **$9.75**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $9.81 |
| 95% | $9.83 |
| 100% | $9.84 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$10.12** ≥ price **$6.31** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 13,785 | 0.00× |
| 12-month FFA | 19,614 | 0.00× |
| Current spot | 21,258 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (59% of fleet value) | 0 | 0.00× |
| Post-Panamax (25% of fleet value) | 0 | 0.00× |
| Cape (16% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $6.55 | $8.02 | $9.50 | $10.97 | $12.44 |
| **-15%** | $6.68 | $8.15 | $9.62 | $11.10 | $12.57 |
| **+0%** | $6.81 | $8.28 | $9.75 | $11.22 | $12.70 |
| **+15%** | $6.93 | $8.41 | $9.88 | $11.35 | $12.83 |
| **+30%** | $7.06 | $8.53 | $10.01 | $11.48 | $12.95 |

_Current price $6.31. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$9.75** is +54.5% vs the current price ($6.31) and +37.3% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $10.12 ≥ $6.31); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
