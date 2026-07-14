# GNK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $25.35
- **Model fair value:** $23.98
- **Analyst target:** $24.80

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 854.2 |
| Fleet value — Supra-Ultra | 506.3 |
| + Cash & equivalents | 54.8 |
| + Working capital (net) | 16.8 |
| − Total debt | 330.0 |
| − Lease liabilities | 5.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,096.5** |
| Diluted shares | 44,411,222 |
| **NAV / share** | **$24.69** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 35,400 | 35,455 | 1.344 | 1.344 | 1.309 |
| Q2 | 35,200 | 35,265 | 1.314 | 1.314 | 1.248 |
| Q3 | 30,100 | 30,420 | 1.061 | 1.061 | 0.982 |
| Q4 | 29,100 | 29,470 | 1.011 | 1.011 | 0.910 |
| Q5 | 28,100 | 28,520 | 0.960 | 0.960 | 0.842 |
| Q6 | 27,100 | 27,570 | 0.909 | 0.909 | 0.777 |
| Q7 | 26,600 | 27,095 | 0.883 | 0.883 | 0.736 |
| Q8 | 26,100 | 26,620 | 0.858 | 0.858 | 0.696 |
| Σ discounted DPS | | | | | 7.50 |
| Terminal value (NAV, q9) | | | | 19.48 | 15.40 |
| **DivStrip implied price** | | | | | **$22.90** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,450/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.43×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $24.69 (NAV) + 0.40 × $22.90 (strip) = **$23.98**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $23.90 |
| 95% | $23.96 |
| 100% | $23.98 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.33× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **35,366** | — |
| 10-year mean | 20,033 | 1.77× |
| 12-month FFA | 26,535 | 1.33× |
| Current spot | 25,709 | 1.38× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (63% of fleet value) | 43,248 | 1.83× |
| Supra-Ultra (37% of fleet value) | 22,066 | 1.58× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.45 | $20.09 | $22.74 | $25.38 | $28.02 |
| **-15%** | $18.07 | $20.71 | $23.36 | $26.00 | $28.64 |
| **+0%** | $18.69 | $21.33 | $23.98 | $26.62 | $29.26 |
| **+15%** | $19.31 | $21.95 | $24.59 | $27.24 | $29.88 |
| **+30%** | $19.93 | $22.57 | $25.21 | $27.86 | $30.50 |

_Current price $25.35. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$23.98** is -5.4% vs the current price ($25.35) and -3.3% vs the analyst target ($24.80). The current price implies the fleet earning a value-weighted blended **$35,366/day** (1.33× the current forward) — 1.8× the value-weighted 10-yr mean ($20,033, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
