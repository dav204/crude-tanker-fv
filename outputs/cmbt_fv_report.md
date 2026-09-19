# CMBT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $20.29
- **Model fair value:** $13.02
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $790,800/day is 19.8x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 701.3 |
| Fleet value — Suezmax | 1,247.9 |
| Fleet value — Cape | 4,933.2 |
| Fleet value — Pana | 1,045.9 |
| Fleet value — Ctr-Large | 256.5 |
| + Cash & equivalents | 159.8 |
| + Working capital (net) | 1,252.7 |
| − Total debt | 5,447.1 |
| − Lease liabilities | 5.6 |
| − Newbuild commitments | 900.8 |
| + Newbuild advances | 532.7 |
| **= NAV total** | **3,876.4** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$13.36** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 50,000 | 50,000 | 1.550 | 0.775 | 0.755 |
| Q2 | 46,375 | 46,375 | 1.472 | 0.736 | 0.699 |
| Q3 | 31,925 | 31,925 | 0.848 | 0.424 | 0.392 |
| Q4 | 34,425 | 34,425 | 0.903 | 0.452 | 0.407 |
| Q5 | 34,425 | 34,425 | 0.640 | 0.320 | 0.281 |
| Q6 | 34,425 | 34,425 | 0.638 | 0.319 | 0.273 |
| Q7 | 33,925 | 33,925 | 0.621 | 0.310 | 0.259 |
| Q8 | 33,425 | 33,425 | 0.604 | 0.302 | 0.245 |
| Σ discounted DPS | | | | | 3.31 |
| Terminal value (NAV, q9) | | | | 11.27 | 8.91 |
| **DivStrip implied price** | | | | | **$12.22** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$40,681/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$39,150/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $39,150 / 10-yr mean $23,650 = **1.90×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $13.36 (NAV) + 0.30 × $12.22 (strip) = **$13.02**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.74 | 152% |
| Balance-sheet net | -10.39 | -80% |
| Discounted DPS (strip, 8-10q) | 0.99 | 8% |
| Discounted terminal (aged NAV) | 2.67 | 21% |
| **Blend FV** | **13.02** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.73 = **92%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $13.10 |
| 95% | $13.14 |
| 100% | $13.15 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.39× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **185,771** | — |
| 10-year mean | 24,718 | 7.52× |
| 12-month FFA | 54,798 | 3.39× |
| Current spot | 125,993 | 1.47× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 137,914 | 5.83× |
| Suezmax (15% of fleet value) | 325,620 | 11.74× |
| Pana (13% of fleet value) | 67,668 | 5.69× |
| VLCC (9% of fleet value) | 441,562 | 11.04× |
| Ctr-Large (3% of fleet value) | 208,068 | 5.07× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $7.09 | $9.60 | $12.11 | $14.61 | $17.12 |
| **-15%** | $7.55 | $10.05 | $12.56 | $15.07 | $17.58 |
| **+0%** | $8.00 | $10.51 | $13.02 | $15.53 | $18.03 |
| **+15%** | $8.46 | $10.97 | $13.47 | $15.98 | $18.49 |
| **+30%** | $8.92 | $11.42 | $13.93 | $16.44 | $18.95 |

_Current price $20.29. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$13.02** is -35.8% vs the current price ($20.29) and -21.5% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$185,771/day** (3.39× the current forward) — 7.5× the value-weighted 10-yr mean ($24,718, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
