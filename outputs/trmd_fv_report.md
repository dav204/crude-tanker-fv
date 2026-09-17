# TRMD — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $36.59
- **Model fair value:** $32.62
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
| Q1 | 29,600 | 29,600 | 2.864 | 2.148 | 2.092 |
| Q2 | 29,600 | 29,600 | 2.864 | 2.148 | 2.039 |
| Q3 | 30,000 | 30,000 | 2.210 | 1.658 | 1.533 |
| Q4 | 30,000 | 30,000 | 2.210 | 1.658 | 1.493 |
| Q5 | 25,250 | 25,250 | 1.491 | 1.118 | 0.981 |
| Q6 | 25,250 | 25,250 | 1.491 | 1.118 | 0.956 |
| Q7 | 25,250 | 25,250 | 1.491 | 1.118 | 0.932 |
| Q8 | 25,250 | 25,250 | 1.491 | 1.118 | 0.908 |
| Σ discounted DPS | | | | | 10.93 |
| Terminal value (NAV, q9) | | | | 28.38 | 22.44 |
| **DivStrip implied price** | | | | | **$33.38** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$29,800/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$30,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $30,000 / 10-yr mean $16,000 = **1.94×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $32.30 (NAV) + 0.30 × $33.38 (strip) = **$32.62**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 26.65 | 82% |
| Balance-sheet net | -4.04 | -12% |
| Discounted DPS (strip, 8-10q) | 3.28 | 10% |
| Discounted terminal (aged NAV) | 6.73 | 21% |
| **Blend FV** | **32.62** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.67 = **90%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $32.65 |
| 95% | $32.74 |
| 100% | $32.76 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.61× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **73,723** | — |
| 10-year mean | 20,829 | 3.54× |
| 12-month FFA | 45,911 | 1.61× |
| Current spot | 43,475 | 1.70× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (58% of fleet value) | 47,852 | 2.99× |
| LR2 (33% of fleet value) | 109,996 | 3.99× |
| LR1 (8% of fleet value) | 109,996 | 3.99× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $23.90 | $27.28 | $30.66 | $34.04 | $37.42 |
| **-15%** | $24.88 | $28.26 | $31.64 | $35.02 | $38.40 |
| **+0%** | $25.87 | $29.25 | $32.62 | $36.00 | $39.38 |
| **+15%** | $26.85 | $30.23 | $33.61 | $36.99 | $40.37 |
| **+30%** | $27.83 | $31.21 | $34.59 | $37.97 | $41.35 |

_Current price $36.59. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$32.62** is -10.8% vs the current price ($36.59) and +30.5% vs the analyst target ($25.00). The current price implies the fleet earning a value-weighted blended **$73,723/day** (1.61× the current forward) — 3.5× the value-weighted 10-yr mean ($20,829, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
