# CMDB — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $20.52
- **Model fair value:** $21.83
- **Analyst target:** $27.98

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 215.6 |
| Fleet value — Pana | 152.1 |
| Fleet value — Supra-Ultra | 330.5 |
| + Cash & equivalents | 234.8 |
| + Working capital (net) | 29.6 |
| − Total debt | 137.9 |
| − Lease liabilities | 34.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **790.3** |
| Diluted shares | 24,241,646 |
| **NAV / share** | **$32.60** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Supra-Ultra, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,875 | 19,875 | 1.612 | 0.000 | 0.000 |
| Q2 | 20,933 | 20,933 | 1.683 | 0.000 | 0.000 |
| Q3 | 16,000 | 16,000 | 0.953 | 0.000 | 0.000 |
| Q4 | 16,167 | 16,167 | 1.056 | 0.000 | 0.000 |
| Q5 | 16,167 | 16,167 | 1.056 | 0.000 | 0.000 |
| Q6 | 16,166 | 16,166 | 1.056 | 0.000 | 0.000 |
| Q7 | 15,866 | 15,866 | 1.017 | 0.000 | 0.000 |
| Q8 | 15,566 | 15,566 | 0.980 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 25.74 | 20.35 |
| **DivStrip implied price** | | | | | **$20.35** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$18,244/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$18,467/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $18,467 / 10-yr mean $13,930 = **1.49×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $22.82 (NAV) + 0.40 × $20.35 (strip) = **$21.83**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 17.28 | 79% |
| Balance-sheet net | 2.28 | 10% |
| §15 governance haircut | -5.87 | -27% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 8.14 | 37% |
| **Blend FV** | **21.83** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $22.88 |
| 95% | $23.07 |
| 100% | $23.14 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.68× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **16,931** | — |
| 10-year mean | 16,489 | 1.03× |
| 12-month FFA | 24,961 | 0.68× |
| Current spot | 27,147 | 0.62× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (47% of fleet value) | 12,375 | 0.89× |
| Cape (31% of fleet value) | 26,150 | 1.11× |
| Pana (22% of fleet value) | 13,764 | 1.16× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.15 | $18.88 | $20.61 | $22.34 | $24.07 |
| **-15%** | $17.76 | $19.49 | $21.22 | $22.95 | $24.68 |
| **+0%** | $18.37 | $20.10 | $21.83 | $23.56 | $25.30 |
| **+15%** | $18.98 | $20.71 | $22.45 | $24.18 | $25.91 |
| **+30%** | $19.60 | $21.33 | $23.06 | $24.79 | $26.52 |

_Current price $20.52. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$21.83** is +6.4% vs the current price ($20.52) and -22.0% vs the analyst target ($27.98). The current price implies the fleet earning a value-weighted blended **$16,931/day** (0.68× the current forward) — 1.0× the value-weighted 10-yr mean ($16,489, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
