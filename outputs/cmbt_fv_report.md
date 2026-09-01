# CMBT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $18.35
- **Model fair value:** $15.94
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 635.5 |
| Fleet value — Suezmax | 1,282.2 |
| Fleet value — Cape | 4,835.6 |
| Fleet value — Pana | 1,058.2 |
| Fleet value — Ctr-Large | 257.2 |
| + Cash & equivalents | 202.9 |
| + Working capital (net) | 912.1 |
| − Total debt | 5,238.2 |
| − Lease liabilities | 6.2 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 759.8 |
| **= NAV total** | **4,799.2** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$16.54** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 45,250 | 45,250 | 1.504 | 0.752 | 0.732 |
| Q2 | 44,475 | 44,475 | 1.493 | 0.747 | 0.709 |
| Q3 | 30,125 | 30,125 | 0.740 | 0.370 | 0.342 |
| Q4 | 34,359 | 34,359 | 0.833 | 0.417 | 0.375 |
| Q5 | 34,358 | 34,358 | 0.612 | 0.306 | 0.269 |
| Q6 | 34,358 | 34,358 | 0.610 | 0.305 | 0.261 |
| Q7 | 33,858 | 33,858 | 0.593 | 0.297 | 0.247 |
| Q8 | 33,358 | 33,358 | 0.577 | 0.288 | 0.234 |
| Σ discounted DPS | | | | | 3.17 |
| Terminal value (NAV, q9) | | | | 14.39 | 11.38 |
| **DivStrip implied price** | | | | | **$14.55** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$38,552/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$37,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $37,300 / 10-yr mean $23,650 = **1.76×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $16.54 (NAV) + 0.30 × $14.55 (strip) = **$15.94**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.47 | 122% |
| Balance-sheet net | -7.89 | -49% |
| Discounted DPS (strip, 8-10q) | 0.95 | 6% |
| Discounted terminal (aged NAV) | 3.41 | 21% |
| **Blend FV** | **15.94** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.78 = **93%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $16.02 |
| 95% | $16.05 |
| 100% | $16.07 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.81× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **96,085** | — |
| 10-year mean | 24,601 | 3.91× |
| 12-month FFA | 53,019 | 1.81× |
| Current spot | 80,919 | 1.19× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 69,868 | 2.95× |
| Suezmax (16% of fleet value) | 160,343 | 5.78× |
| Pana (13% of fleet value) | 36,775 | 3.09× |
| VLCC (8% of fleet value) | 258,569 | 6.46× |
| Ctr-Large (3% of fleet value) | 111,230 | 2.71× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $10.11 | $12.58 | $15.05 | $17.53 | $20.00 |
| **-15%** | $10.55 | $13.02 | $15.50 | $17.97 | $20.44 |
| **+0%** | $11.00 | $13.47 | $15.94 | $18.41 | $20.89 |
| **+15%** | $11.44 | $13.91 | $16.39 | $18.86 | $21.33 |
| **+30%** | $11.89 | $14.36 | $16.83 | $19.30 | $21.78 |

_Current price $18.35. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.94** is -13.1% vs the current price ($18.35) and -3.9% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$96,085/day** (1.81× the current forward) — 3.9× the value-weighted 10-yr mean ($24,601, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
