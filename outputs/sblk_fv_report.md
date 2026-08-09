# SBLK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $28.90
- **Model fair value:** $32.10
- **Analyst target:** $34.50

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,557.8 |
| Fleet value — Pana | 1,389.0 |
| Fleet value — Supra-Ultra | 1,391.3 |
| + Cash & equivalents | 565.3 |
| + Working capital (net) | 84.2 |
| − Total debt | 1,036.6 |
| − Lease liabilities | 142.4 |
| − Newbuild commitments | 122.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,686.6** |
| Diluted shares | 111,585,370 |
| **NAV / share** | **$33.04** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 38,800 | 38,800 | 1.810 | 1.720 | 1.675 |
| Q2 | 37,250 | 37,250 | 1.763 | 1.675 | 1.589 |
| Q3 | 25,875 | 25,875 | 1.127 | 1.071 | 0.990 |
| Q4 | 31,225 | 31,225 | 1.270 | 1.207 | 1.087 |
| Q5 | 31,250 | 31,250 | 1.244 | 1.182 | 1.037 |
| Q6 | 31,250 | 31,250 | 1.216 | 1.155 | 0.988 |
| Q7 | 30,750 | 30,750 | 1.174 | 1.115 | 0.929 |
| Q8 | 30,250 | 30,250 | 1.135 | 1.078 | 0.875 |
| Σ discounted DPS | | | | | 9.17 |
| Terminal value (NAV, q9) | | | | 27.21 | 21.52 |
| **DivStrip implied price** | | | | | **$30.69** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$33,288/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$31,550/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $31,550 / 10-yr mean $23,650 = **1.36×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $33.04 (NAV) + 0.40 × $30.69 (strip) = **$32.10**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 23.33 | 73% |
| Balance-sheet net | -3.50 | -11% |
| Discounted DPS (strip, 8-10q) | 3.67 | 11% |
| Discounted terminal (aged NAV) | 8.61 | 27% |
| **Blend FV** | **32.10** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.70 = **88%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $32.03 |
| 95% | $32.10 |
| 100% | $32.12 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.49× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **11,492** | — |
| 10-year mean | 16,771 | 0.69× |
| 12-month FFA | 23,344 | 0.49× |
| Current spot | 26,776 | 0.43× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 16,387 | 0.69× |
| Supra-Ultra (32% of fleet value) | 8,357 | 0.60× |
| Pana (32% of fleet value) | 9,141 | 0.77× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $23.49 | $26.85 | $30.21 | $33.57 | $36.93 |
| **-15%** | $24.43 | $27.79 | $31.15 | $34.51 | $37.87 |
| **+0%** | $25.38 | $28.74 | $32.10 | $35.46 | $38.82 |
| **+15%** | $26.32 | $29.68 | $33.04 | $36.40 | $39.76 |
| **+30%** | $27.26 | $30.63 | $33.99 | $37.35 | $40.71 |

_Current price $28.90. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$32.10** is +11.1% vs the current price ($28.90) and -7.0% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$11,492/day** (0.49× the current forward) — 0.7× the value-weighted 10-yr mean ($16,771, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
