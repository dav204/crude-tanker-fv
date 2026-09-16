# SBLK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $30.79
- **Model fair value:** $32.62
- **Analyst target:** $34.50

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,557.8 |
| Fleet value — Pana | 1,414.3 |
| Fleet value — Supra-Ultra | 1,391.6 |
| + Cash & equivalents | 565.3 |
| + Working capital (net) | 84.2 |
| − Total debt | 1,036.6 |
| − Lease liabilities | 142.4 |
| − Newbuild commitments | 122.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,712.2** |
| Diluted shares | 111,585,370 |
| **NAV / share** | **$33.27** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 48,500 | 48,500 | 2.106 | 2.001 | 1.950 |
| Q2 | 43,666 | 43,666 | 2.036 | 1.934 | 1.835 |
| Q3 | 29,875 | 29,875 | 1.332 | 1.265 | 1.170 |
| Q4 | 33,509 | 33,509 | 1.443 | 1.371 | 1.235 |
| Q5 | 33,508 | 33,508 | 1.443 | 1.371 | 1.203 |
| Q6 | 33,508 | 33,508 | 1.443 | 1.371 | 1.172 |
| Q7 | 33,008 | 33,008 | 1.401 | 1.331 | 1.109 |
| Q8 | 32,508 | 32,508 | 1.362 | 1.294 | 1.051 |
| Σ discounted DPS | | | | | 10.73 |
| Terminal value (NAV, q9) | | | | 25.78 | 20.38 |
| **DivStrip implied price** | | | | | **$31.11** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$38,888/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$36,771/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $36,771 / 10-yr mean $23,650 = **1.51×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $33.27 (NAV) + 0.30 × $31.11 (strip) = **$32.62**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 27.37 | 84% |
| Balance-sheet net | -4.09 | -13% |
| Discounted DPS (strip, 8-10q) | 3.22 | 10% |
| Discounted terminal (aged NAV) | 6.12 | 19% |
| **Blend FV** | **32.62** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.66 = **90%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $32.56 |
| 95% | $32.62 |
| 100% | $32.64 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.65× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **16,893** | — |
| 10-year mean | 16,742 | 1.01× |
| 12-month FFA | 26,038 | 0.65× |
| Current spot | 28,223 | 0.60× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 25,230 | 1.07× |
| Pana (32% of fleet value) | 12,743 | 1.07× |
| Supra-Ultra (32% of fleet value) | 11,778 | 0.85× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $24.11 | $27.58 | $31.06 | $34.53 | $38.00 |
| **-15%** | $24.89 | $28.37 | $31.84 | $35.31 | $38.78 |
| **+0%** | $25.68 | $29.15 | $32.62 | $36.09 | $39.57 |
| **+15%** | $26.46 | $29.93 | $33.40 | $36.87 | $40.35 |
| **+30%** | $27.24 | $30.71 | $34.18 | $37.66 | $41.13 |

_Current price $30.79. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$32.62** is +5.9% vs the current price ($30.79) and -5.4% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$16,893/day** (0.65× the current forward) — 1.0× the value-weighted 10-yr mean ($16,742, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
