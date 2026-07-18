# CMBT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $14.96
- **Model fair value:** $15.48
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 621.3 |
| Fleet value — Suezmax | 1,282.2 |
| Fleet value — Cape | 4,807.5 |
| Fleet value — Pana | 979.2 |
| Fleet value — Ctr-Large | 257.2 |
| + Cash & equivalents | 202.9 |
| + Working capital (net) | 912.1 |
| − Total debt | 5,238.2 |
| − Lease liabilities | 6.2 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 759.8 |
| **= NAV total** | **4,677.9** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$16.12** |

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
| Terminal value (NAV, q9) | | | | 13.84 | 10.95 |
| **DivStrip implied price** | | | | | **$13.99** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,450/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.73×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $16.12 (NAV) + 0.30 × $13.99 (strip) = **$15.48**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.17 | 124% |
| Balance-sheet net | -7.89 | -51% |
| Discounted DPS (strip, 8-10q) | 0.91 | 6% |
| Discounted terminal (aged NAV) | 3.28 | 21% |
| **Blend FV** | **15.48** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.78 = **93%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.55 |
| 95% | $15.58 |
| 100% | $15.59 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.82× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **40,715** | — |
| 10-year mean | 24,703 | 1.65× |
| 12-month FFA | 49,654 | 0.82× |
| Current spot | 68,735 | 0.59× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 26,608 | 1.13× |
| Suezmax (16% of fleet value) | 69,699 | 2.51× |
| Pana (12% of fleet value) | 14,872 | 1.25× |
| VLCC (8% of fleet value) | 127,098 | 3.18× |
| Ctr-Large (3% of fleet value) | 49,609 | 1.21× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $9.75 | $12.18 | $14.61 | $17.04 | $19.48 |
| **-15%** | $10.18 | $12.61 | $15.05 | $17.48 | $19.91 |
| **+0%** | $10.62 | $13.05 | $15.48 | $17.92 | $20.35 |
| **+15%** | $11.05 | $13.49 | $15.92 | $18.35 | $20.78 |
| **+30%** | $11.49 | $13.92 | $16.35 | $18.79 | $21.22 |

_Current price $14.96. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.48** is +3.5% vs the current price ($14.96) and -6.7% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$40,715/day** (0.82× the current forward) — 1.6× the value-weighted 10-yr mean ($24,703, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
