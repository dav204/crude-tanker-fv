# CMBT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $16.29
- **Model fair value:** $15.93
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 635.5 |
| Fleet value — Suezmax | 1,282.2 |
| Fleet value — Cape | 4,835.6 |
| Fleet value — Pana | 1,034.4 |
| Fleet value — Ctr-Large | 257.2 |
| + Cash & equivalents | 202.9 |
| + Working capital (net) | 912.1 |
| − Total debt | 5,238.2 |
| − Lease liabilities | 6.2 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 759.8 |
| **= NAV total** | **4,775.4** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$16.46** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 38,800 | 38,800 | 1.125 | 0.563 | 0.548 |
| Q2 | 37,250 | 37,250 | 1.215 | 0.607 | 0.576 |
| Q3 | 25,875 | 25,875 | 0.862 | 0.431 | 0.399 |
| Q4 | 31,225 | 31,225 | 0.821 | 0.410 | 0.370 |
| Q5 | 31,250 | 31,250 | 0.769 | 0.384 | 0.337 |
| Q6 | 31,250 | 31,250 | 0.883 | 0.441 | 0.377 |
| Q7 | 30,750 | 30,750 | 0.897 | 0.449 | 0.374 |
| Q8 | 30,250 | 30,250 | 0.709 | 0.355 | 0.288 |
| Σ discounted DPS | | | | | 3.27 |
| Terminal value (NAV, q9) | | | | 14.47 | 11.44 |
| **DivStrip implied price** | | | | | **$14.71** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$33,288/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$31,550/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $31,550 / 10-yr mean $23,650 = **1.62×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $16.46 (NAV) + 0.30 × $14.71 (strip) = **$15.93**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.41 | 122% |
| Balance-sheet net | -7.89 | -50% |
| Discounted DPS (strip, 8-10q) | 0.98 | 6% |
| Discounted terminal (aged NAV) | 3.43 | 22% |
| **Blend FV** | **15.93** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.78 = **93%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $16.00 |
| 95% | $16.04 |
| 100% | $16.05 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.12× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **56,053** | — |
| 10-year mean | 24,638 | 2.28× |
| 12-month FFA | 50,149 | 1.12× |
| Current spot | 71,070 | 0.79× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 37,206 | 1.57× |
| Suezmax (16% of fleet value) | 95,006 | 3.42× |
| Pana (13% of fleet value) | 20,755 | 1.74× |
| VLCC (8% of fleet value) | 173,247 | 4.33× |
| Ctr-Large (3% of fleet value) | 68,600 | 1.67× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $10.09 | $12.56 | $15.02 | $17.49 | $19.95 |
| **-15%** | $10.55 | $13.01 | $15.48 | $17.94 | $20.41 |
| **+0%** | $11.00 | $13.47 | $15.93 | $18.40 | $20.86 |
| **+15%** | $11.46 | $13.92 | $16.39 | $18.85 | $21.32 |
| **+30%** | $11.91 | $14.38 | $16.84 | $19.31 | $21.77 |

_Current price $16.29. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.93** is -2.2% vs the current price ($16.29) and -4.0% vs the analyst target ($16.59). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$56,053/day** (1.12× the current forward) — 2.3× the value-weighted 10-yr mean ($24,638, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
