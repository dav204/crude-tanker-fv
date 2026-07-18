# GNK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $24.12
- **Model fair value:** $24.65
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
| Q1 | 35,400 | 35,455 | 1.344 | 1.344 | 1.309 |
| Q2 | 35,200 | 35,265 | 1.314 | 1.314 | 1.248 |
| Q3 | 30,100 | 30,420 | 1.061 | 1.061 | 0.982 |
| Q4 | 29,100 | 29,470 | 1.011 | 1.011 | 0.910 |
| Q5 | 28,100 | 28,520 | 0.960 | 0.960 | 0.842 |
| Q6 | 27,100 | 27,570 | 0.909 | 0.909 | 0.777 |
| Q7 | 26,600 | 27,095 | 0.883 | 0.883 | 0.736 |
| Q8 | 26,100 | 26,620 | 0.858 | 0.858 | 0.696 |
| Σ discounted DPS | | | | | 7.50 |
| Terminal value (NAV, q9) | | | | 20.12 | 15.91 |
| **DivStrip implied price** | | | | | **$23.41** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,450/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.43×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $25.48 (NAV) + 0.40 × $23.41 (strip) = **$24.65**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 18.86 | 76% |
| Balance-sheet net | -3.57 | -14% |
| Discounted DPS (strip, 8-10q) | 3.00 | 12% |
| Discounted terminal (aged NAV) | 6.36 | 26% |
| **Blend FV** | **24.65** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.68 = **87%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $24.58 |
| 95% | $24.64 |
| 100% | $24.65 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.87× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **23,026** | — |
| 10-year mean | 19,977 | 1.15× |
| 12-month FFA | 26,443 | 0.87× |
| Current spot | 29,594 | 0.78× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (62% of fleet value) | 28,257 | 1.19× |
| Supra-Ultra (38% of fleet value) | 14,417 | 1.03× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.99 | $20.70 | $23.41 | $26.12 | $28.83 |
| **-15%** | $18.61 | $21.32 | $24.03 | $26.74 | $29.45 |
| **+0%** | $19.23 | $21.94 | $24.65 | $27.36 | $30.07 |
| **+15%** | $19.85 | $22.56 | $25.27 | $27.98 | $30.69 |
| **+30%** | $20.47 | $23.18 | $25.89 | $28.60 | $31.31 |

_Current price $24.12. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$24.65** is +2.2% vs the current price ($24.12) and -0.6% vs the analyst target ($24.80). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$23,026/day** (0.87× the current forward) — 1.2× the value-weighted 10-yr mean ($19,977, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
