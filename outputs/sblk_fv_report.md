# SBLK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $30.48
- **Model fair value:** $32.46
- **Analyst target:** $34.50

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,557.8 |
| Fleet value — Pana | 1,399.3 |
| Fleet value — Supra-Ultra | 1,363.0 |
| + Cash & equivalents | 565.3 |
| + Working capital (net) | 84.2 |
| − Total debt | 1,036.6 |
| − Lease liabilities | 142.4 |
| − Newbuild commitments | 122.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,668.6** |
| Diluted shares | 111,585,370 |
| **NAV / share** | **$32.88** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 41,313 | 41,313 | 1.887 | 1.792 | 1.746 |
| Q2 | 42,125 | 42,125 | 1.994 | 1.895 | 1.798 |
| Q3 | 28,725 | 28,725 | 1.246 | 1.184 | 1.095 |
| Q4 | 33,625 | 33,625 | 1.428 | 1.356 | 1.222 |
| Q5 | 33,625 | 33,625 | 1.428 | 1.356 | 1.190 |
| Q6 | 33,625 | 33,625 | 1.428 | 1.356 | 1.160 |
| Q7 | 33,125 | 33,125 | 1.385 | 1.316 | 1.096 |
| Q8 | 32,625 | 32,625 | 1.347 | 1.279 | 1.038 |
| Σ discounted DPS | | | | | 10.35 |
| Terminal value (NAV, q9) | | | | 27.17 | 21.49 |
| **DivStrip implied price** | | | | | **$31.83** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$36,447/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,425/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,425 / 10-yr mean $23,650 = **1.47×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $32.88 (NAV) + 0.40 × $31.83 (strip) = **$32.46**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 23.23 | 72% |
| Balance-sheet net | -3.50 | -11% |
| Discounted DPS (strip, 8-10q) | 4.14 | 13% |
| Discounted terminal (aged NAV) | 8.59 | 26% |
| **Blend FV** | **32.46** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.67 = **87%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $32.38 |
| 95% | $32.46 |
| 100% | $32.49 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.71× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **17,725** | — |
| 10-year mean | 16,777 | 1.06× |
| 12-month FFA | 25,019 | 0.71× |
| Current spot | 28,302 | 0.63× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 25,822 | 1.09× |
| Pana (32% of fleet value) | 13,769 | 1.16× |
| Supra-Ultra (32% of fleet value) | 12,533 | 0.90× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $23.73 | $27.07 | $30.42 | $33.77 | $37.12 |
| **-15%** | $24.75 | $28.09 | $31.44 | $34.79 | $38.14 |
| **+0%** | $25.76 | $29.11 | $32.46 | $35.81 | $39.16 |
| **+15%** | $26.78 | $30.13 | $33.48 | $36.83 | $40.17 |
| **+30%** | $27.80 | $31.15 | $34.50 | $37.84 | $41.19 |

_Current price $30.48. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$32.46** is +6.5% vs the current price ($30.48) and -5.9% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$17,725/day** (0.71× the current forward) — 1.1× the value-weighted 10-yr mean ($16,777, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.1M (+19%) / 10yr $28.9M (+20%) [n=14], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
