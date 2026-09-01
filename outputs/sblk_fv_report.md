# SBLK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $30.48
- **Model fair value:** $32.67
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
| Q1 | 45,250 | 45,250 | 2.058 | 1.955 | 1.905 |
| Q2 | 44,475 | 44,475 | 2.128 | 2.021 | 1.919 |
| Q3 | 30,125 | 30,125 | 1.354 | 1.286 | 1.189 |
| Q4 | 34,359 | 34,359 | 1.465 | 1.392 | 1.254 |
| Q5 | 34,358 | 34,358 | 1.465 | 1.392 | 1.222 |
| Q6 | 34,358 | 34,358 | 1.465 | 1.392 | 1.190 |
| Q7 | 33,858 | 33,858 | 1.423 | 1.352 | 1.126 |
| Q8 | 33,358 | 33,358 | 1.384 | 1.315 | 1.067 |
| Σ discounted DPS | | | | | 10.87 |
| Terminal value (NAV, q9) | | | | 25.79 | 20.39 |
| **DivStrip implied price** | | | | | **$31.26** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$38,552/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$37,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $37,300 / 10-yr mean $23,650 = **1.55×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $33.27 (NAV) + 0.30 × $31.26 (strip) = **$32.67**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 27.37 | 84% |
| Balance-sheet net | -4.09 | -13% |
| Discounted DPS (strip, 8-10q) | 3.26 | 10% |
| Discounted terminal (aged NAV) | 6.12 | 19% |
| **Blend FV** | **32.67** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.65 = **90%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $32.60 |
| 95% | $32.67 |
| 100% | $32.69 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.58× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **15,280** | — |
| 10-year mean | 16,742 | 0.91× |
| 12-month FFA | 26,158 | 0.58× |
| Current spot | 28,223 | 0.54× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 22,520 | 0.95× |
| Pana (32% of fleet value) | 11,853 | 1.00× |
| Supra-Ultra (32% of fleet value) | 10,657 | 0.77× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $24.14 | $27.62 | $31.09 | $34.56 | $38.03 |
| **-15%** | $24.93 | $28.41 | $31.88 | $35.35 | $38.82 |
| **+0%** | $25.72 | $29.19 | $32.67 | $36.14 | $39.61 |
| **+15%** | $26.51 | $29.98 | $33.45 | $36.93 | $40.40 |
| **+30%** | $27.30 | $30.77 | $34.24 | $37.72 | $41.19 |

_Current price $30.48. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$32.67** is +7.2% vs the current price ($30.48) and -5.3% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$15,280/day** (0.58× the current forward) — 0.9× the value-weighted 10-yr mean ($16,742, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
