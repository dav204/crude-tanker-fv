# SBLK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $31.17
- **Model fair value:** $32.78
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
| Q1 | 51,100 | 51,100 | 2.203 | 2.093 | 2.039 |
| Q2 | 45,375 | 45,375 | 2.142 | 2.035 | 1.931 |
| Q3 | 30,975 | 30,975 | 1.396 | 1.326 | 1.226 |
| Q4 | 34,842 | 34,842 | 1.507 | 1.432 | 1.290 |
| Q5 | 34,842 | 34,842 | 1.507 | 1.432 | 1.257 |
| Q6 | 34,841 | 34,841 | 1.507 | 1.432 | 1.224 |
| Q7 | 34,341 | 34,341 | 1.465 | 1.391 | 1.159 |
| Q8 | 33,841 | 33,841 | 1.426 | 1.355 | 1.100 |
| Σ discounted DPS | | | | | 11.23 |
| Terminal value (NAV, q9) | | | | 25.81 | 20.41 |
| **DivStrip implied price** | | | | | **$31.63** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$40,573/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$38,175/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $38,175 / 10-yr mean $23,650 = **1.56×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $33.27 (NAV) + 0.30 × $31.63 (strip) = **$32.78**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 27.37 | 84% |
| Balance-sheet net | -4.09 | -12% |
| Discounted DPS (strip, 8-10q) | 3.37 | 10% |
| Discounted terminal (aged NAV) | 6.12 | 19% |
| **Blend FV** | **32.78** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.65 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $32.71 |
| 95% | $32.78 |
| 100% | $32.80 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.70× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **18,888** | — |
| 10-year mean | 16,742 | 1.13× |
| 12-month FFA | 26,960 | 0.70× |
| Current spot | 28,223 | 0.67× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 28,425 | 1.20× |
| Pana (32% of fleet value) | 14,337 | 1.20× |
| Supra-Ultra (32% of fleet value) | 12,837 | 0.92× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $24.22 | $27.69 | $31.17 | $34.64 | $38.11 |
| **-15%** | $25.03 | $28.50 | $31.97 | $35.44 | $38.92 |
| **+0%** | $25.83 | $29.30 | $32.78 | $36.25 | $39.72 |
| **+15%** | $26.64 | $30.11 | $33.58 | $37.06 | $40.53 |
| **+30%** | $27.44 | $30.92 | $34.39 | $37.86 | $41.33 |

_Current price $31.17. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$32.78** is +5.2% vs the current price ($31.17) and -5.0% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$18,888/day** (0.70× the current forward) — 1.1× the value-weighted 10-yr mean ($16,742, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
