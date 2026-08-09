# CMDB — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $17.80
- **Model fair value:** $21.13
- **Analyst target:** $27.98

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 215.6 |
| Fleet value — Pana | 147.9 |
| Fleet value — Supra-Ultra | 323.3 |
| + Cash & equivalents | 234.8 |
| + Working capital (net) | 29.6 |
| − Total debt | 137.9 |
| − Lease liabilities | 34.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **779.0** |
| Diluted shares | 24,241,646 |
| **NAV / share** | **$32.13** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Supra-Ultra, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,200 | 19,200 | 1.393 | 0.000 | 0.000 |
| Q2 | 19,158 | 19,158 | 1.352 | 0.000 | 0.000 |
| Q3 | 15,075 | 15,075 | 0.754 | 0.000 | 0.000 |
| Q4 | 14,475 | 14,475 | 0.862 | 0.000 | 0.000 |
| Q5 | 13,875 | 13,875 | 0.827 | 0.000 | 0.000 |
| Q6 | 13,275 | 13,275 | 0.792 | 0.000 | 0.000 |
| Q7 | 12,975 | 12,975 | 0.753 | 0.000 | 0.000 |
| Q8 | 12,675 | 12,675 | 0.716 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 24.12 | 19.07 |
| **DivStrip implied price** | | | | | **$19.07** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$16,977/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$16,750/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $16,750 / 10-yr mean $13,930 = **1.32×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $22.49 (NAV) + 0.40 × $19.07 (strip) = **$21.13**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 17.00 | 80% |
| Balance-sheet net | 2.28 | 11% |
| §15 governance haircut | -5.78 | -27% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 7.63 | 36% |
| **Blend FV** | **21.13** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $21.96 |
| 95% | $22.11 |
| 100% | $22.17 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.09× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **1,982** | — |
| 10-year mean | 16,544 | 0.12× |
| 12-month FFA | 22,439 | 0.09× |
| Current spot | 25,625 | 0.08× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (47% of fleet value) | 1,500 | 0.11× |
| Cape (31% of fleet value) | 2,940 | 0.12× |
| Pana (22% of fleet value) | 1,640 | 0.14× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $16.62 | $18.33 | $20.03 | $21.73 | $23.44 |
| **-15%** | $17.17 | $18.87 | $20.58 | $22.28 | $23.99 |
| **+0%** | $17.72 | $19.42 | $21.13 | $22.83 | $24.53 |
| **+15%** | $18.26 | $19.97 | $21.67 | $23.38 | $25.08 |
| **+30%** | $18.81 | $20.52 | $22.22 | $23.92 | $25.63 |

_Current price $17.80. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$21.13** is +18.7% vs the current price ($17.80) and -24.5% vs the analyst target ($27.98). The current price implies the fleet earning a value-weighted blended **$1,982/day** (0.09× the current forward) — 0.1× the value-weighted 10-yr mean ($16,544, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
