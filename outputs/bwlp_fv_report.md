# BWLP — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $21.60
- **Model fair value:** $15.43
- **Analyst target:** $17.52

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLGC | 3,046.4 |
| + Cash & equivalents | 273.1 |
| + Working capital (net) | 176.6 |
| − Total debt | 763.9 |
| − Lease liabilities | 133.9 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,399.2** |
| Diluted shares | 151,814,600 |
| **NAV / share** | **$15.80** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLGC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 62,000 | 62,000 | 1.024 | 0.768 | 0.748 |
| Q2 | 55,000 | 55,000 | 0.864 | 0.648 | 0.615 |
| Q3 | 48,000 | 48,000 | 0.704 | 0.528 | 0.488 |
| Q4 | 45,000 | 45,000 | 0.636 | 0.477 | 0.430 |
| Q5 | 43,000 | 43,000 | 0.590 | 0.443 | 0.388 |
| Q6 | 42,000 | 42,000 | 0.567 | 0.425 | 0.364 |
| Q7 | 41,000 | 41,000 | 0.544 | 0.408 | 0.340 |
| Q8 | 40,000 | 40,000 | 0.521 | 0.391 | 0.317 |
| Σ discounted DPS | | | | | 3.69 |
| Terminal value (NAV, q9) | | | | 13.76 | 10.88 |
| **DivStrip implied price** | | | | | **$14.57** |

_FFA spot is the VLGC forward curve that drives the strip cash flows; its 12-month average is **$52,500/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$63,615/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $63,615 / 10-yr mean $40,000 = **1.59×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $15.80 (NAV) + 0.30 × $14.57 (strip) = **$15.43**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 14.05 | 91% |
| Balance-sheet net | -2.98 | -19% |
| Discounted DPS (strip, 8-10q) | 1.11 | 7% |
| Discounted terminal (aged NAV) | 3.26 | 21% |
| **Blend FV** | **15.43** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.75 = **92%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.44 |
| 95% | $15.47 |
| 100% | $15.48 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.75× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **196,627** | — |
| 10-year mean | 40,000 | 4.92× |
| 12-month FFA | 52,500 | 3.75× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $11.16 | $12.96 | $14.76 | $16.56 | $18.36 |
| **-15%** | $11.50 | $13.30 | $15.10 | $16.90 | $18.70 |
| **+0%** | $11.83 | $13.63 | $15.43 | $17.23 | $19.03 |
| **+15%** | $12.17 | $13.97 | $15.77 | $17.57 | $19.37 |
| **+30%** | $12.51 | $14.31 | $16.11 | $17.91 | $19.71 |

_Current price $21.60. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.43** is -28.6% vs the current price ($21.60) and -11.9% vs the analyst target ($17.52). The current price implies the fleet earning a value-weighted blended **$196,627/day** (3.75× the current forward) — 4.9× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
