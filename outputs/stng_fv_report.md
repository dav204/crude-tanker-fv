# STNG — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $76.08
- **Model fair value:** $73.34
- **Analyst target:** $94.00

## Data validation warnings

- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 1,576.7 |
| Fleet value — MR | 1,247.0 |
| Fleet value — Handymax | 244.8 |
| + Cash & equivalents | 1,838.8 |
| + Working capital (net) | 153.2 |
| − Total debt | 855.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 644.3 |
| + Newbuild advances | 90.2 |
| **= NAV total** | **3,827.3** |
| Diluted shares | 50,081,352 |
| **NAV / share** | **$76.42** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LR2, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 57,774 | 2.537 | 0.450 | 0.438 |
| Q2 | 88,000 | 65,574 | 3.542 | 0.450 | 0.427 |
| Q3 | 82,000 | 61,974 | 3.217 | 0.450 | 0.416 |
| Q4 | 64,000 | 51,174 | 1.996 | 0.450 | 0.405 |
| Q5 | 59,000 | 48,174 | 1.779 | 0.450 | 0.395 |
| Q6 | 70,000 | 54,774 | 2.485 | 0.450 | 0.385 |
| Q7 | 74,000 | 57,174 | 2.838 | 0.450 | 0.375 |
| Q8 | 56,000 | 46,374 | 1.699 | 0.450 | 0.365 |
| Σ discounted DPS | | | | | 3.21 |
| Terminal value (NAV, q9) | | | | 79.58 | 62.93 |
| **DivStrip implied price** | | | | | **$66.13** |

_FFA spot is the LR2 forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **1.72×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $76.42 (NAV) + 0.30 × $66.13 (strip) = **$73.34**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 42.89 | 58% |
| Balance-sheet net | 10.61 | 14% |
| Discounted DPS (strip, 8-10q) | 0.96 | 1% |
| Discounted terminal (aged NAV) | 18.88 | 26% |
| **Blend FV** | **73.34** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.95 = **99%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $73.85 |
| 95% | $73.95 |
| 100% | $73.98 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.38× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **71,456** | — |
| 10-year mean | 21,961 | 3.25× |
| 12-month FFA | 51,727 | 1.38× |
| Current spot | 39,094 | 1.83× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| LR2 (51% of fleet value) | 106,715 | 3.87× |
| MR (41% of fleet value) | 34,190 | 2.14× |
| Handymax (8% of fleet value) | 34,190 | 2.14× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $60.33 | $65.75 | $71.18 | $76.60 | $82.03 |
| **-15%** | $61.40 | $66.83 | $72.26 | $77.68 | $83.11 |
| **+0%** | $62.48 | $67.91 | $73.34 | $78.76 | $84.19 |
| **+15%** | $63.56 | $68.99 | $74.41 | $79.84 | $85.27 |
| **+30%** | $64.64 | $70.07 | $75.49 | $80.92 | $86.35 |

_Current price $76.08. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$73.34** is -3.6% vs the current price ($76.08) and -22.0% vs the analyst target ($94.00). The current price implies the fleet earning a value-weighted blended **$71,456/day** (1.38× the current forward) — 3.3× the value-weighted 10-yr mean ($21,961, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
