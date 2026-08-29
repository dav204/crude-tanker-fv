# TRMD — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $32.62
- **Model fair value:** $32.14
- **Analyst target:** $25.00

## Data validation warnings

- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 1,317.4 |
| Fleet value — LR1 | 330.8 |
| Fleet value — MR | 2,311.0 |
| + Cash & equivalents | 368.2 |
| + Working capital (net) | 342.7 |
| − Total debt | 1,076.2 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 263.7 |
| + Newbuild advances | 29.3 |
| **= NAV total** | **3,359.5** |
| Diluted shares | 104,000,000 |
| **NAV / share** | **$32.30** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 29,300 | 29,300 | 2.274 | 1.705 | 1.661 |
| Q2 | 29,300 | 29,300 | 2.274 | 1.705 | 1.619 |
| Q3 | 29,250 | 29,250 | 2.042 | 1.531 | 1.416 |
| Q4 | 29,250 | 29,250 | 2.042 | 1.531 | 1.380 |
| Q5 | 25,000 | 25,000 | 1.422 | 1.066 | 0.936 |
| Q6 | 25,000 | 25,000 | 1.422 | 1.066 | 0.912 |
| Q7 | 25,000 | 25,000 | 1.422 | 1.066 | 0.888 |
| Q8 | 25,000 | 25,000 | 1.422 | 1.066 | 0.865 |
| Σ discounted DPS | | | | | 9.68 |
| Terminal value (NAV, q9) | | | | 27.93 | 22.09 |
| **DivStrip implied price** | | | | | **$31.77** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$29,275/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$29,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $29,250 / 10-yr mean $16,000 = **1.84×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $32.30 (NAV) + 0.30 × $31.77 (strip) = **$32.14**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 26.65 | 83% |
| Balance-sheet net | -4.04 | -13% |
| Discounted DPS (strip, 8-10q) | 2.90 | 9% |
| Discounted terminal (aged NAV) | 6.63 | 21% |
| **Blend FV** | **32.14** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.70 = **91%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $32.17 |
| 95% | $32.24 |
| 100% | $32.26 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.08× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **43,444** | — |
| 10-year mean | 20,829 | 2.09× |
| 12-month FFA | 40,265 | 1.08× |
| Current spot | 43,475 | 1.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (58% of fleet value) | 31,586 | 1.97× |
| LR2 (33% of fleet value) | 60,070 | 2.18× |
| LR1 (8% of fleet value) | 60,070 | 2.18× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $23.56 | $26.94 | $30.32 | $33.70 | $37.08 |
| **-15%** | $24.47 | $27.85 | $31.23 | $34.61 | $37.99 |
| **+0%** | $25.38 | $28.76 | $32.14 | $35.52 | $38.90 |
| **+15%** | $26.29 | $29.67 | $33.05 | $36.43 | $39.81 |
| **+30%** | $27.20 | $30.58 | $33.96 | $37.34 | $40.72 |

_Current price $32.62. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$32.14** is -1.5% vs the current price ($32.62) and +28.6% vs the analyst target ($25.00). The current price implies the fleet earning a value-weighted blended **$43,444/day** (1.08× the current forward) — 2.1× the value-weighted 10-yr mean ($20,829, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
