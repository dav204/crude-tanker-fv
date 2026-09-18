# CMDB — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $24.01
- **Model fair value:** $21.93
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
| Q1 | 20,100 | 20,100 | 1.716 | 0.000 | 0.000 |
| Q2 | 21,366 | 21,366 | 1.732 | 0.000 | 0.000 |
| Q3 | 16,675 | 16,675 | 1.032 | 0.000 | 0.000 |
| Q4 | 16,509 | 16,509 | 1.078 | 0.000 | 0.000 |
| Q5 | 16,508 | 16,508 | 1.078 | 0.000 | 0.000 |
| Q6 | 16,508 | 16,508 | 1.078 | 0.000 | 0.000 |
| Q7 | 16,208 | 16,208 | 1.039 | 0.000 | 0.000 |
| Q8 | 15,908 | 15,908 | 1.002 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 25.11 | 19.85 |
| **DivStrip implied price** | | | | | **$19.85** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$18,662/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$19,021/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $19,021 / 10-yr mean $13,930 = **1.53×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $22.82 (NAV) + 0.30 × $19.85 (strip) = **$21.93**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 20.16 | 92% |
| Balance-sheet net | 2.66 | 12% |
| §15 governance haircut | -6.85 | -31% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 5.96 | 27% |
| **Blend FV** | **21.93** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $22.74 |
| 95% | $22.90 |
| 100% | $22.95 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.67× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **42,910** | — |
| 10-year mean | 16,489 | 2.60× |
| 12-month FFA | 25,744 | 1.67× |
| Current spot | 27,147 | 1.58× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (47% of fleet value) | 31,106 | 2.23× |
| Cape (31% of fleet value) | 67,807 | 2.87× |
| Pana (22% of fleet value) | 33,270 | 2.80× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.43 | $19.21 | $21.00 | $22.78 | $24.56 |
| **-15%** | $17.90 | $19.68 | $21.46 | $23.24 | $25.03 |
| **+0%** | $18.37 | $20.15 | $21.93 | $23.71 | $25.49 |
| **+15%** | $18.84 | $20.62 | $22.40 | $24.18 | $25.96 |
| **+30%** | $19.30 | $21.08 | $22.87 | $24.65 | $26.43 |

_Current price $24.01. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$21.93** is -8.7% vs the current price ($24.01) and -21.6% vs the analyst target ($27.98). The current price implies the fleet earning a value-weighted blended **$42,910/day** (1.67× the current forward) — 2.6× the value-weighted 10-yr mean ($16,489, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
