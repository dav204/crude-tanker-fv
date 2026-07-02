# GNK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $24.66
- **Model fair value:** $23.99
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
| Q1 | 31,200 | 31,465 | 1.198 | 1.198 | 1.167 |
| Q2 | 31,450 | 31,702 | 1.170 | 1.170 | 1.111 |
| Q3 | 28,500 | 28,900 | 0.997 | 0.997 | 0.922 |
| Q4 | 27,000 | 27,475 | 0.928 | 0.928 | 0.836 |
| Q5 | 25,500 | 26,050 | 0.863 | 0.863 | 0.758 |
| Q6 | 25,000 | 25,575 | 0.838 | 0.838 | 0.717 |
| Q7 | 24,500 | 25,100 | 0.813 | 0.813 | 0.677 |
| Q8 | 24,000 | 24,625 | 0.790 | 0.790 | 0.641 |
| Σ discounted DPS | | | | | 6.83 |
| Terminal value (NAV, q9) | | | | 20.82 | 16.46 |
| **DivStrip implied price** | | | | | **$23.29** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$29,538/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$27,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $27,000 / 10-yr mean $23,650 = **1.14×** → **mid-cycle**
- Weights: w_nav = 0.50, w_earn = 0.50

## Blended fair value

0.50 × $24.69 (NAV) + 0.50 × $23.29 (strip) = **$23.99**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $23.91 |
| 95% | $23.97 |
| 100% | $23.99 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.14× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **28,077** | — |
| 10-year mean | 20,033 | 1.40× |
| 12-month FFA | 24,651 | 1.14× |
| Current spot | 31,116 | 0.90× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (63% of fleet value) | 33,643 | 1.42× |
| Supra-Ultra (37% of fleet value) | 18,686 | 1.34× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.36 | $19.95 | $22.54 | $25.13 | $27.72 |
| **-15%** | $18.09 | $20.68 | $23.26 | $25.85 | $28.44 |
| **+0%** | $18.81 | $21.40 | $23.99 | $26.58 | $29.17 |
| **+15%** | $19.53 | $22.12 | $24.71 | $27.30 | $29.89 |
| **+30%** | $20.26 | $22.85 | $25.44 | $28.03 | $30.62 |

_Current price $24.66. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$23.99** is -2.7% vs the current price ($24.66) and -3.3% vs the analyst target ($24.80). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$28,077/day** (1.14× the current forward) — 1.4× the value-weighted 10-yr mean ($20,033, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
