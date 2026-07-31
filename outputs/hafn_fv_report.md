# HAFN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $7.67
- **Model fair value:** $5.99
- **Analyst target:** $10.00

## Data validation warnings

- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 574.3 |
| Fleet value — LR1 | 848.8 |
| Fleet value — MR | 1,588.5 |
| Fleet value — Handysize | 319.7 |
| + Cash & equivalents | 146.5 |
| + Working capital (net) | 362.9 |
| − Total debt | 953.9 |
| − Lease liabilities | 71.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,815.1** |
| Diluted shares | 505,321,911 |
| **NAV / share** | **$5.57** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 22,000 | 22,000 | 0.550 | 0.440 | 0.429 |
| Q2 | 30,000 | 30,000 | 0.731 | 0.584 | 0.555 |
| Q3 | 28,000 | 28,000 | 0.669 | 0.535 | 0.495 |
| Q4 | 19,000 | 19,000 | 0.445 | 0.356 | 0.321 |
| Q5 | 18,000 | 18,000 | 0.402 | 0.321 | 0.282 |
| Q6 | 23,000 | 23,000 | 0.532 | 0.426 | 0.364 |
| Q7 | 26,000 | 26,000 | 0.594 | 0.475 | 0.396 |
| Q8 | 18,000 | 18,000 | 0.383 | 0.307 | 0.249 |
| Σ discounted DPS | | | | | 3.09 |
| Terminal value (NAV, q9) | | | | 4.89 | 3.86 |
| **DivStrip implied price** | | | | | **$6.95** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.66×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $5.57 (NAV) + 0.30 × $6.95 (strip) = **$5.99**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 4.61 | 77% |
| Balance-sheet net | -0.72 | -12% |
| Discounted DPS (strip, 8-10q) | 0.93 | 15% |
| Discounted terminal (aged NAV) | 1.16 | 19% |
| **Blend FV** | **5.99** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.56 = **87%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $5.99 |
| 95% | $6.01 |
| 100% | $6.01 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.11× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **99,382** | — |
| 10-year mean | 20,955 | 4.74× |
| 12-month FFA | 47,177 | 2.11× |
| Current spot | 27,702 | 3.59× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (48% of fleet value) | 52,138 | 3.26× |
| LR1 (25% of fleet value) | 162,733 | 5.90× |
| LR2 (17% of fleet value) | 162,733 | 5.90× |
| Handysize (10% of fleet value) | 52,138 | 3.26× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $4.37 | $4.95 | $5.53 | $6.11 | $6.69 |
| **-15%** | $4.60 | $5.18 | $5.76 | $6.34 | $6.92 |
| **+0%** | $4.82 | $5.40 | $5.99 | $6.57 | $7.15 |
| **+15%** | $5.05 | $5.63 | $6.21 | $6.80 | $7.38 |
| **+30%** | $5.28 | $5.86 | $6.44 | $7.02 | $7.60 |

_Current price $7.67. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$5.99** is -22.0% vs the current price ($7.67) and -40.1% vs the analyst target ($10.00). The current price implies the fleet earning a value-weighted blended **$99,382/day** (2.11× the current forward) — 4.7× the value-weighted 10-yr mean ($20,955, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
