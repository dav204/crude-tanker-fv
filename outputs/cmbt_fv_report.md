# CMBT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $19.35
- **Model fair value:** $15.98
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
| Q1 | 45,125 | 45,125 | 1.467 | 0.734 | 0.715 |
| Q2 | 44,125 | 44,125 | 1.450 | 0.725 | 0.688 |
| Q3 | 29,925 | 29,925 | 0.814 | 0.407 | 0.376 |
| Q4 | 34,292 | 34,292 | 0.912 | 0.456 | 0.411 |
| Q5 | 34,292 | 34,292 | 0.636 | 0.318 | 0.279 |
| Q6 | 34,291 | 34,291 | 0.634 | 0.317 | 0.271 |
| Q7 | 33,791 | 33,791 | 0.617 | 0.308 | 0.257 |
| Q8 | 33,291 | 33,291 | 0.601 | 0.300 | 0.244 |
| Σ discounted DPS | | | | | 3.24 |
| Terminal value (NAV, q9) | | | | 14.47 | 11.45 |
| **DivStrip implied price** | | | | | **$14.69** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$38,367/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$37,025/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $37,025 / 10-yr mean $23,650 = **1.85×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $16.54 (NAV) + 0.30 × $14.69 (strip) = **$15.98**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.47 | 122% |
| Balance-sheet net | -7.89 | -49% |
| Discounted DPS (strip, 8-10q) | 0.97 | 6% |
| Discounted terminal (aged NAV) | 3.43 | 21% |
| **Blend FV** | **15.98** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.78 = **93%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $16.06 |
| 95% | $16.10 |
| 100% | $16.11 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.12× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **112,675** | — |
| 10-year mean | 24,601 | 4.58× |
| 12-month FFA | 53,148 | 2.12× |
| Current spot | 80,919 | 1.39× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 81,337 | 3.44× |
| Suezmax (16% of fleet value) | 203,626 | 7.34× |
| Pana (13% of fleet value) | 43,274 | 3.64× |
| VLCC (8% of fleet value) | 276,130 | 6.90× |
| Ctr-Large (3% of fleet value) | 130,115 | 3.17× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $10.14 | $12.61 | $15.08 | $17.55 | $20.03 |
| **-15%** | $10.59 | $13.06 | $15.53 | $18.01 | $20.48 |
| **+0%** | $11.04 | $13.51 | $15.98 | $18.46 | $20.93 |
| **+15%** | $11.49 | $13.96 | $16.43 | $18.91 | $21.38 |
| **+30%** | $11.94 | $14.41 | $16.89 | $19.36 | $21.83 |

_Current price $19.35. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.98** is -17.4% vs the current price ($19.35) and -3.7% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$112,675/day** (2.12× the current forward) — 4.6× the value-weighted 10-yr mean ($24,601, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
