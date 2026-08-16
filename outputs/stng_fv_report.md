# STNG — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $79.41
- **Model fair value:** $72.23
- **Analyst target:** $94.00

## Data validation warnings

- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 1,566.5 |
| Fleet value — MR | 1,247.0 |
| Fleet value — Handymax | 244.8 |
| + Cash & equivalents | 1,838.8 |
| + Working capital (net) | 153.2 |
| − Total debt | 855.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 644.3 |
| + Newbuild advances | 90.2 |
| **= NAV total** | **3,817.2** |
| Diluted shares | 50,081,352 |
| **NAV / share** | **$76.22** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LR2, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 59,900 | 48,714 | 2.535 | 0.450 | 0.438 |
| Q2 | 59,900 | 48,714 | 2.535 | 0.450 | 0.427 |
| Q3 | 51,450 | 43,644 | 2.304 | 0.450 | 0.416 |
| Q4 | 51,450 | 43,644 | 2.304 | 0.450 | 0.405 |
| Q5 | 38,000 | 35,574 | 1.624 | 0.450 | 0.395 |
| Q6 | 38,000 | 35,574 | 1.624 | 0.450 | 0.385 |
| Q7 | 38,000 | 35,574 | 1.624 | 0.450 | 0.375 |
| Q8 | 38,000 | 35,574 | 1.624 | 0.450 | 0.365 |
| Σ discounted DPS | | | | | 3.21 |
| Terminal value (NAV, q9) | | | | 75.53 | 59.72 |
| **DivStrip implied price** | | | | | **$62.93** |

_FFA spot is the LR2 forward curve that drives the strip cash flows; its 12-month average is **$55,675/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$51,450/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $51,450 / 10-yr mean $27,600 = **1.80×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $76.22 (NAV) + 0.30 × $62.93 (strip) = **$72.23**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 42.75 | 59% |
| Balance-sheet net | 10.61 | 15% |
| Discounted DPS (strip, 8-10q) | 0.96 | 1% |
| Discounted terminal (aged NAV) | 17.92 | 25% |
| **Blend FV** | **72.23** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.95 = **98%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $72.66 |
| 95% | $72.74 |
| 100% | $72.76 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.15× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **90,377** | — |
| 10-year mean | 21,942 | 4.12× |
| 12-month FFA | 42,117 | 2.15× |
| Current spot | 53,987 | 1.67× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| LR2 (51% of fleet value) | 119,470 | 4.33× |
| MR (41% of fleet value) | 62,820 | 3.93× |
| Handymax (8% of fleet value) | 44,580 | 2.79× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $59.54 | $64.94 | $70.35 | $75.76 | $81.17 |
| **-15%** | $60.47 | $65.88 | $71.29 | $76.70 | $82.11 |
| **+0%** | $61.41 | $66.82 | $72.23 | $77.64 | $83.05 |
| **+15%** | $62.35 | $67.76 | $73.17 | $78.58 | $83.99 |
| **+30%** | $63.29 | $68.70 | $74.11 | $79.52 | $84.93 |

_Current price $79.41. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$72.23** is -9.0% vs the current price ($79.41) and -23.2% vs the analyst target ($94.00). The current price implies the fleet earning a value-weighted blended **$90,377/day** (2.15× the current forward) — 4.1× the value-weighted 10-yr mean ($21,942, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
