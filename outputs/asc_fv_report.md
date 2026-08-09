# ASC — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $16.71
- **Model fair value:** $17.13
- **Analyst target:** $17.95

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — MR | 572.5 |
| Fleet value — Handysize | 181.9 |
| + Cash & equivalents | 48.1 |
| + Working capital (net) | 125.8 |
| − Total debt | 33.4 |
| − Lease liabilities | 1.6 |
| − Newbuild commitments | 183.6 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **709.7** |
| Diluted shares | 40,851,870 |
| **NAV / share** | **$17.37** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 22,000 | 22,000 | 0.627 | 0.418 | 0.408 |
| Q2 | 30,000 | 30,000 | 1.046 | 0.698 | 0.662 |
| Q3 | 28,000 | 28,000 | 0.942 | 0.628 | 0.581 |
| Q4 | 19,000 | 19,000 | 0.470 | 0.314 | 0.283 |
| Q5 | 18,000 | 18,000 | 0.418 | 0.279 | 0.245 |
| Q6 | 23,000 | 23,000 | 0.680 | 0.453 | 0.388 |
| Q7 | 26,000 | 26,000 | 0.837 | 0.558 | 0.465 |
| Q8 | 18,000 | 18,000 | 0.418 | 0.279 | 0.226 |
| Σ discounted DPS | | | | | 3.26 |
| Terminal value (NAV, q9) | | | | 17.09 | 13.51 |
| **DivStrip implied price** | | | | | **$16.77** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.38×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $17.37 (NAV) + 0.40 × $16.77 (strip) = **$17.13**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 11.08 | 65% |
| Balance-sheet net | -0.66 | -4% |
| Discounted DPS (strip, 8-10q) | 1.30 | 8% |
| Discounted terminal (aged NAV) | 5.41 | 32% |
| **Blend FV** | **17.13** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.81 = **92%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $17.16 |
| 95% | $17.20 |
| 100% | $17.21 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.87× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **21,597** | — |
| 10-year mean | 16,000 | 1.35× |
| 12-month FFA | 24,750 | 0.87× |
| Current spot | 35,600 | 0.61× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (76% of fleet value) | 21,597 | 1.35× |
| Handysize (24% of fleet value) | 21,597 | 1.35× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $12.89 | $14.51 | $16.14 | $17.76 | $19.39 |
| **-15%** | $13.38 | $15.01 | $16.64 | $18.26 | $19.89 |
| **+0%** | $13.88 | $15.51 | $17.13 | $18.76 | $20.38 |
| **+15%** | $14.38 | $16.00 | $17.63 | $19.26 | $20.88 |
| **+30%** | $14.88 | $16.50 | $18.13 | $19.75 | $21.38 |

_Current price $16.71. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$17.13** is +2.5% vs the current price ($16.71) and -4.6% vs the analyst target ($17.95). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$21,597/day** (0.87× the current forward) — 1.3× the value-weighted 10-yr mean ($16,000, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
