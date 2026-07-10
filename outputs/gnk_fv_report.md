# GNK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $24.31
- **Model fair value:** $23.85
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
| Q1 | 32,500 | 32,700 | 1.233 | 1.233 | 1.201 |
| Q2 | 33,650 | 33,792 | 1.244 | 1.244 | 1.181 |
| Q3 | 29,500 | 29,850 | 1.033 | 1.033 | 0.955 |
| Q4 | 28,500 | 28,900 | 0.982 | 0.982 | 0.885 |
| Q5 | 27,500 | 27,950 | 0.931 | 0.931 | 0.817 |
| Q6 | 26,500 | 27,000 | 0.880 | 0.880 | 0.753 |
| Q7 | 26,000 | 26,525 | 0.855 | 0.855 | 0.712 |
| Q8 | 25,500 | 26,050 | 0.830 | 0.830 | 0.673 |
| Σ discounted DPS | | | | | 7.18 |
| Terminal value (NAV, q9) | | | | 19.48 | 15.40 |
| **DivStrip implied price** | | | | | **$22.58** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$31,038/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$33,100/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $33,100 / 10-yr mean $23,650 = **1.36×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $24.69 (NAV) + 0.40 × $22.58 (strip) = **$23.85**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $23.78 |
| 95% | $23.83 |
| 100% | $23.85 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.12× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **28,480** | — |
| 10-year mean | 20,033 | 1.42× |
| 12-month FFA | 25,521 | 1.12× |
| Current spot | 25,709 | 1.11× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (63% of fleet value) | 34,637 | 1.46× |
| Supra-Ultra (37% of fleet value) | 18,093 | 1.30× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.36 | $20.00 | $22.65 | $25.29 | $27.93 |
| **-15%** | $17.96 | $20.60 | $23.25 | $25.89 | $28.53 |
| **+0%** | $18.56 | $21.20 | $23.85 | $26.49 | $29.13 |
| **+15%** | $19.16 | $21.80 | $24.45 | $27.09 | $29.73 |
| **+30%** | $19.76 | $22.40 | $25.05 | $27.69 | $30.33 |

_Current price $24.31. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$23.85** is -1.9% vs the current price ($24.31) and -3.8% vs the analyst target ($24.80). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$28,480/day** (1.12× the current forward) — 1.4× the value-weighted 10-yr mean ($20,033, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
