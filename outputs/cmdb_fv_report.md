# CMDB — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $17.80
- **Model fair value:** $20.87
- **Analyst target:** $27.98

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 214.1 |
| Fleet value — Pana | 137.7 |
| Fleet value — Supra-Ultra | 329.9 |
| + Cash & equivalents | 234.8 |
| + Working capital (net) | 29.6 |
| − Total debt | 137.9 |
| − Lease liabilities | 34.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **773.8** |
| Diluted shares | 24,241,646 |
| **NAV / share** | **$31.92** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Supra-Ultra, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,100 | 19,100 | 1.266 | 0.000 | 0.000 |
| Q2 | 18,450 | 18,450 | 1.245 | 0.000 | 0.000 |
| Q3 | 15,075 | 15,075 | 0.888 | 0.000 | 0.000 |
| Q4 | 14,475 | 14,475 | 0.815 | 0.000 | 0.000 |
| Q5 | 13,875 | 13,875 | 0.742 | 0.000 | 0.000 |
| Q6 | 13,275 | 13,275 | 0.669 | 0.000 | 0.000 |
| Q7 | 12,975 | 12,975 | 0.630 | 0.000 | 0.000 |
| Q8 | 12,675 | 12,675 | 0.593 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 23.59 | 18.65 |
| **DivStrip implied price** | | | | | **$18.65** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$16,775/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$18,800/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $18,800 / 10-yr mean $13,930 = **1.45×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $22.34 (NAV) + 0.40 × $18.65 (strip) = **$20.87**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 16.87 | 81% |
| Balance-sheet net | 2.28 | 11% |
| §15 governance haircut | -5.75 | -28% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 7.46 | 36% |
| **Blend FV** | **20.87** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $21.64 |
| 95% | $21.78 |
| 100% | $21.83 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.13× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **2,798** | — |
| 10-year mean | 16,573 | 0.17× |
| 12-month FFA | 22,053 | 0.13× |
| Current spot | 24,419 | 0.11× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (48% of fleet value) | 2,129 | 0.15× |
| Cape (31% of fleet value) | 4,155 | 0.18× |
| Pana (20% of fleet value) | 2,294 | 0.19× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $16.43 | $18.12 | $19.81 | $21.51 | $23.20 |
| **-15%** | $16.96 | $18.65 | $20.34 | $22.03 | $23.72 |
| **+0%** | $17.49 | $19.18 | $20.87 | $22.56 | $24.25 |
| **+15%** | $18.01 | $19.70 | $21.40 | $23.09 | $24.78 |
| **+30%** | $18.54 | $20.23 | $21.92 | $23.61 | $25.31 |

_Current price $17.80. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$20.87** is +17.2% vs the current price ($17.80) and -25.4% vs the analyst target ($27.98). The current price implies the fleet earning a value-weighted blended **$2,798/day** (0.13× the current forward) — 0.2× the value-weighted 10-yr mean ($16,573, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
