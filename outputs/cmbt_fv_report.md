# CMBT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $15.78
- **Model fair value:** $15.25
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 624.4 |
| Fleet value — Suezmax | 1,266.2 |
| Fleet value — Cape | 4,746.2 |
| Fleet value — Pana | 980.4 |
| Fleet value — Ctr-Large | 257.2 |
| + Cash & equivalents | 202.9 |
| + Working capital (net) | 912.1 |
| − Total debt | 5,238.2 |
| − Lease liabilities | 6.2 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 759.8 |
| **= NAV total** | **4,604.9** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$15.87** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 35,400 | 35,400 | 1.040 | 0.520 | 0.507 |
| Q2 | 35,200 | 35,200 | 1.157 | 0.579 | 0.549 |
| Q3 | 30,100 | 30,100 | 0.965 | 0.482 | 0.446 |
| Q4 | 29,100 | 29,100 | 0.765 | 0.383 | 0.345 |
| Q5 | 28,100 | 28,100 | 0.685 | 0.342 | 0.301 |
| Q6 | 27,100 | 27,100 | 0.770 | 0.385 | 0.329 |
| Q7 | 26,600 | 26,600 | 0.785 | 0.392 | 0.327 |
| Q8 | 26,100 | 26,100 | 0.598 | 0.299 | 0.242 |
| Σ discounted DPS | | | | | 3.05 |
| Terminal value (NAV, q9) | | | | 13.59 | 10.75 |
| **DivStrip implied price** | | | | | **$13.79** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,450/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.73×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $15.87 (NAV) + 0.30 × $13.79 (strip) = **$15.25**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.00 | 125% |
| Balance-sheet net | -7.89 | -52% |
| Discounted DPS (strip, 8-10q) | 0.91 | 6% |
| Discounted terminal (aged NAV) | 3.22 | 21% |
| **Blend FV** | **15.25** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.78 = **93%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.31 |
| 95% | $15.35 |
| 100% | $15.36 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.18× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **58,887** | — |
| 10-year mean | 24,709 | 2.38× |
| 12-month FFA | 49,752 | 1.18× |
| Current spot | 65,275 | 0.90× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 38,408 | 1.62× |
| Suezmax (16% of fleet value) | 100,605 | 3.63× |
| Pana (12% of fleet value) | 21,467 | 1.80× |
| VLCC (8% of fleet value) | 183,457 | 4.59× |
| Ctr-Large (3% of fleet value) | 71,607 | 1.75× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $9.56 | $11.97 | $14.38 | $16.78 | $19.19 |
| **-15%** | $9.99 | $12.40 | $14.81 | $17.22 | $19.63 |
| **+0%** | $10.43 | $12.84 | $15.25 | $17.66 | $20.07 |
| **+15%** | $10.86 | $13.27 | $15.68 | $18.09 | $20.50 |
| **+30%** | $11.30 | $13.71 | $16.12 | $18.53 | $20.94 |

_Current price $15.78. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.25** is -3.4% vs the current price ($15.78) and -8.1% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$58,887/day** (1.18× the current forward) — 2.4× the value-weighted 10-yr mean ($24,709, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
