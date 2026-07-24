# GNK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $25.26
- **Model fair value:** $24.71
- **Analyst target:** $24.80

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 868.3 |
| Fleet value — Supra-Ultra | 527.5 |
| + Cash & equivalents | 54.8 |
| + Working capital (net) | 16.8 |
| − Total debt | 330.0 |
| − Lease liabilities | 5.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,131.8** |
| Diluted shares | 44,411,222 |
| **NAV / share** | **$25.48** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 34,900 | 34,980 | 1.333 | 1.333 | 1.299 |
| Q2 | 35,725 | 35,764 | 1.347 | 1.347 | 1.279 |
| Q3 | 30,675 | 30,966 | 1.082 | 1.082 | 1.001 |
| Q4 | 29,675 | 30,016 | 1.031 | 1.031 | 0.929 |
| Q5 | 28,675 | 29,066 | 0.981 | 0.981 | 0.861 |
| Q6 | 27,675 | 28,116 | 0.930 | 0.930 | 0.795 |
| Q7 | 27,175 | 27,641 | 0.904 | 0.904 | 0.753 |
| Q8 | 26,675 | 27,166 | 0.879 | 0.879 | 0.713 |
| Σ discounted DPS | | | | | 7.63 |
| Terminal value (NAV, q9) | | | | 20.12 | 15.91 |
| **DivStrip implied price** | | | | | **$23.54** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,744/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.44×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $25.48 (NAV) + 0.40 × $23.54 (strip) = **$24.71**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 18.86 | 76% |
| Balance-sheet net | -3.57 | -14% |
| Discounted DPS (strip, 8-10q) | 3.05 | 12% |
| Discounted terminal (aged NAV) | 6.36 | 26% |
| **Blend FV** | **24.71** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.68 = **87%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $24.63 |
| 95% | $24.69 |
| 100% | $24.71 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.13× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **30,248** | — |
| 10-year mean | 19,977 | 1.51× |
| 12-month FFA | 26,709 | 1.13× |
| Current spot | 29,232 | 1.03× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (62% of fleet value) | 37,083 | 1.57× |
| Supra-Ultra (38% of fleet value) | 18,998 | 1.36× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.03 | $20.74 | $23.45 | $26.16 | $28.87 |
| **-15%** | $18.66 | $21.37 | $24.08 | $26.79 | $29.50 |
| **+0%** | $19.29 | $22.00 | $24.71 | $27.42 | $30.13 |
| **+15%** | $19.91 | $22.62 | $25.33 | $28.04 | $30.75 |
| **+30%** | $20.54 | $23.25 | $25.96 | $28.67 | $31.38 |

_Current price $25.26. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$24.71** is -2.2% vs the current price ($25.26) and -0.4% vs the analyst target ($24.80). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$30,248/day** (1.13× the current forward) — 1.5× the value-weighted 10-yr mean ($19,977, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
