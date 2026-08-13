# TRMD — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $28.97
- **Model fair value:** $29.98
- **Analyst target:** $25.00

## Data validation warnings

- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 1,355.7 |
| Fleet value — LR1 | 342.3 |
| Fleet value — MR | 2,085.3 |
| + Cash & equivalents | 196.4 |
| + Working capital (net) | 254.9 |
| − Total debt | 1,081.8 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 31.2 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,121.6** |
| Diluted shares | 103,300,000 |
| **NAV / share** | **$30.22** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 29,300 | 29,300 | 2.181 | 1.636 | 1.594 |
| Q2 | 29,300 | 29,300 | 2.181 | 1.636 | 1.553 |
| Q3 | 29,250 | 29,250 | 1.948 | 1.461 | 1.351 |
| Q4 | 29,250 | 29,250 | 1.948 | 1.461 | 1.316 |
| Q5 | 25,000 | 25,000 | 1.345 | 1.009 | 0.885 |
| Q6 | 25,000 | 25,000 | 1.345 | 1.009 | 0.863 |
| Q7 | 25,000 | 25,000 | 1.345 | 1.009 | 0.840 |
| Q8 | 25,000 | 25,000 | 1.345 | 1.009 | 0.819 |
| Σ discounted DPS | | | | | 9.22 |
| Terminal value (NAV, q9) | | | | 25.54 | 20.20 |
| **DivStrip implied price** | | | | | **$29.42** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$29,275/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$29,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $29,250 / 10-yr mean $16,000 = **1.84×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $30.22 (NAV) + 0.30 × $29.42 (strip) = **$29.98**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 25.64 | 86% |
| Balance-sheet net | -4.48 | -15% |
| Discounted DPS (strip, 8-10q) | 2.77 | 9% |
| Discounted terminal (aged NAV) | 6.06 | 20% |
| **Blend FV** | **29.98** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.69 = **91%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $30.00 |
| 95% | $30.07 |
| 100% | $30.09 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.83× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **33,992** | — |
| 10-year mean | 21,206 | 1.60× |
| 12-month FFA | 41,124 | 0.83× |
| Current spot | 44,382 | 0.77× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (55% of fleet value) | 24,198 | 1.51× |
| LR2 (36% of fleet value) | 46,020 | 1.67× |
| LR1 (9% of fleet value) | 46,020 | 1.67× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $21.75 | $24.99 | $28.23 | $31.47 | $34.72 |
| **-15%** | $22.62 | $25.87 | $29.11 | $32.35 | $35.59 |
| **+0%** | $23.50 | $26.74 | $29.98 | $33.22 | $36.46 |
| **+15%** | $24.37 | $27.61 | $30.85 | $34.09 | $37.33 |
| **+30%** | $25.24 | $28.48 | $31.72 | $34.96 | $38.20 |

_Current price $28.97. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$29.98** is +3.5% vs the current price ($28.97) and +19.9% vs the analyst target ($25.00). The current price implies the fleet earning a value-weighted blended **$33,992/day** (0.83× the current forward) — 1.6× the value-weighted 10-yr mean ($21,206, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
