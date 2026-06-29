# SB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $6.39
- **Model fair value:** $9.48
- **Analyst target:** $7.10

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Pana | 640.0 |
| Fleet value — Post-Panamax | 409.7 |
| Fleet value — Cape | 268.8 |
| + Cash & equivalents | 171.8 |
| + Working capital (net) | 53.8 |
| − Total debt | 544.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 100.0 |
| **= NAV total** | **1,000.1** |
| Diluted shares | 101,826,580 |
| **NAV / share** | **$9.82** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Pana, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 20,775 | 18,678 | 0.474 | 0.142 | 0.139 |
| Q2 | 19,500 | 18,168 | 0.460 | 0.138 | 0.131 |
| Q3 | 17,000 | 17,168 | 0.411 | 0.123 | 0.114 |
| Q4 | 16,500 | 16,968 | 0.396 | 0.119 | 0.107 |
| Q5 | 15,800 | 16,688 | 0.378 | 0.113 | 0.100 |
| Q6 | 15,400 | 16,528 | 0.370 | 0.111 | 0.095 |
| Q7 | 14,800 | 16,288 | 0.359 | 0.108 | 0.090 |
| Q8 | 14,500 | 16,168 | 0.353 | 0.106 | 0.086 |
| Σ discounted DPS | | | | | 0.86 |
| Terminal value (NAV, q9) | | | | 10.25 | 8.11 |
| **DivStrip implied price** | | | | | **$8.97** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$18,444/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$17,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $17,500 / 10-yr mean $11,900 = **1.40×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $9.82 (NAV) + 0.40 × $8.97 (strip) = **$9.48**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $9.55 |
| 95% | $9.57 |
| 100% | $9.57 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$9.82** ≥ price **$6.39** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 14,296 | 0.00× |
| 12-month FFA | 20,706 | 0.00× |
| Current spot | 24,068 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (49% of fleet value) | 0 | 0.00× |
| Post-Panamax (31% of fleet value) | 0 | 0.00× |
| Cape (20% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $6.93 | $8.06 | $9.18 | $10.31 | $11.44 |
| **-15%** | $7.07 | $8.20 | $9.33 | $10.46 | $11.59 |
| **+0%** | $7.22 | $8.35 | $9.48 | $10.61 | $11.74 |
| **+15%** | $7.37 | $8.50 | $9.63 | $10.76 | $11.89 |
| **+30%** | $7.52 | $8.65 | $9.78 | $10.91 | $12.03 |

_Current price $6.39. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$9.48** is +48.4% vs the current price ($6.39) and +33.5% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $9.82 ≥ $6.39); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
