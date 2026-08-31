# CMDB — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $20.52
- **Model fair value:** $21.48
- **Analyst target:** $27.98

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 215.6 |
| Fleet value — Pana | 149.6 |
| Fleet value — Supra-Ultra | 323.3 |
| + Cash & equivalents | 234.8 |
| + Working capital (net) | 29.6 |
| − Total debt | 137.9 |
| − Lease liabilities | 34.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **780.6** |
| Diluted shares | 24,241,646 |
| **NAV / share** | **$32.20** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Supra-Ultra, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,450 | 19,450 | 1.465 | 0.000 | 0.000 |
| Q2 | 20,275 | 20,275 | 1.564 | 0.000 | 0.000 |
| Q3 | 15,150 | 15,150 | 0.851 | 0.000 | 0.000 |
| Q4 | 15,884 | 15,884 | 1.019 | 0.000 | 0.000 |
| Q5 | 15,883 | 15,883 | 1.019 | 0.000 | 0.000 |
| Q6 | 15,883 | 15,883 | 1.019 | 0.000 | 0.000 |
| Q7 | 15,583 | 15,583 | 0.980 | 0.000 | 0.000 |
| Q8 | 15,283 | 15,283 | 0.943 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 25.14 | 19.88 |
| **DivStrip implied price** | | | | | **$19.88** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$17,690/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$17,713/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $17,713 / 10-yr mean $13,930 = **1.42×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $22.54 (NAV) + 0.40 × $19.88 (strip) = **$21.48**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 17.04 | 79% |
| Balance-sheet net | 2.28 | 11% |
| §15 governance haircut | -5.80 | -27% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 7.95 | 37% |
| **Blend FV** | **21.48** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $22.46 |
| 95% | $22.64 |
| 100% | $22.70 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.76× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **18,156** | — |
| 10-year mean | 16,532 | 1.10× |
| 12-month FFA | 23,942 | 0.76× |
| Current spot | 27,242 | 0.67× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (47% of fleet value) | 13,414 | 0.96× |
| Cape (31% of fleet value) | 27,638 | 1.17× |
| Pana (22% of fleet value) | 14,738 | 1.24× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $16.87 | $18.58 | $20.29 | $22.00 | $23.70 |
| **-15%** | $17.47 | $19.18 | $20.88 | $22.59 | $24.30 |
| **+0%** | $18.06 | $19.77 | $21.48 | $23.18 | $24.89 |
| **+15%** | $18.66 | $20.36 | $22.07 | $23.78 | $25.49 |
| **+30%** | $19.25 | $20.96 | $22.66 | $24.37 | $26.08 |

_Current price $20.52. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$21.48** is +4.7% vs the current price ($20.52) and -23.2% vs the analyst target ($27.98). The current price implies the fleet earning a value-weighted blended **$18,156/day** (0.76× the current forward) — 1.1× the value-weighted 10-yr mean ($16,532, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.1M (+19%) / 10yr $28.9M (+20%) [n=14], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
