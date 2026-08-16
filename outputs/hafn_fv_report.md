# HAFN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $7.74
- **Model fair value:** $5.71
- **Analyst target:** $10.00

## Data validation warnings

- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 571.1 |
| Fleet value — LR1 | 848.8 |
| Fleet value — MR | 1,588.5 |
| Fleet value — Handysize | 319.7 |
| + Cash & equivalents | 146.5 |
| + Working capital (net) | 362.9 |
| − Total debt | 953.9 |
| − Lease liabilities | 71.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,811.9** |
| Diluted shares | 505,321,911 |
| **NAV / share** | **$5.56** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 29,300 | 29,300 | 0.516 | 0.413 | 0.402 |
| Q2 | 29,300 | 29,300 | 0.516 | 0.413 | 0.392 |
| Q3 | 29,250 | 29,250 | 0.463 | 0.370 | 0.343 |
| Q4 | 29,250 | 29,250 | 0.463 | 0.370 | 0.334 |
| Q5 | 25,000 | 25,000 | 0.332 | 0.265 | 0.233 |
| Q6 | 25,000 | 25,000 | 0.332 | 0.265 | 0.227 |
| Q7 | 25,000 | 25,000 | 0.332 | 0.265 | 0.221 |
| Q8 | 25,000 | 25,000 | 0.332 | 0.265 | 0.215 |
| Σ discounted DPS | | | | | 2.37 |
| Terminal value (NAV, q9) | | | | 4.68 | 3.70 |
| **DivStrip implied price** | | | | | **$6.07** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$29,275/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$29,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $29,250 / 10-yr mean $16,000 = **1.79×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $5.56 (NAV) + 0.30 × $6.07 (strip) = **$5.71**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 4.61 | 81% |
| Balance-sheet net | -0.72 | -13% |
| Discounted DPS (strip, 8-10q) | 0.71 | 12% |
| Discounted terminal (aged NAV) | 1.11 | 19% |
| **Blend FV** | **5.71** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.61 = **88%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $5.71 |
| 95% | $5.73 |
| 100% | $5.74 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.61× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **103,758** | — |
| 10-year mean | 20,949 | 4.95× |
| 12-month FFA | 39,722 | 2.61× |
| Current spot | 31,000 | 3.35× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (48% of fleet value) | 76,470 | 4.78× |
| LR1 (26% of fleet value) | 145,430 | 5.27× |
| LR2 (17% of fleet value) | 145,430 | 5.27× |
| Handysize (10% of fleet value) | 54,267 | 3.39× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $4.18 | $4.76 | $5.34 | $5.92 | $6.50 |
| **-15%** | $4.37 | $4.95 | $5.53 | $6.11 | $6.69 |
| **+0%** | $4.55 | $5.13 | $5.71 | $6.30 | $6.88 |
| **+15%** | $4.74 | $5.32 | $5.90 | $6.48 | $7.06 |
| **+30%** | $4.93 | $5.51 | $6.09 | $6.67 | $7.25 |

_Current price $7.74. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$5.71** is -26.2% vs the current price ($7.74) and -42.9% vs the analyst target ($10.00). The current price implies the fleet earning a value-weighted blended **$103,758/day** (2.61× the current forward) — 5.0× the value-weighted 10-yr mean ($20,949, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
