# ECO — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $65.04
- **Model fair value:** $39.73
- **Analyst target:** $45.00

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 989.2 |
| Fleet value — Suezmax | 970.2 |
| + Cash & equivalents | 247.8 |
| + Working capital (net) | 138.4 |
| − Total debt | 722.5 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 79.4 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,543.7** |
| Diluted shares | 39,044,655 |
| **NAV / share** | **$39.54** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 179,650 | 169,029 | 4.997 | 4.248 | 4.138 |
| Q2 | 179,650 | 169,029 | 4.997 | 4.248 | 4.032 |
| Q3 | 105,700 | 103,953 | 2.414 | 2.052 | 1.897 |
| Q4 | 105,700 | 103,953 | 2.414 | 2.052 | 1.848 |
| Q5 | 48,850 | 53,925 | 0.786 | 0.668 | 0.587 |
| Q6 | 48,850 | 53,925 | 0.786 | 0.668 | 0.572 |
| Q7 | 48,850 | 53,925 | 0.786 | 0.668 | 0.557 |
| Q8 | 48,850 | 53,925 | 0.786 | 0.668 | 0.542 |
| Σ discounted DPS | | | | | 14.17 |
| Terminal value (NAV, q9) | | | | 32.89 | 26.00 |
| **DivStrip implied price** | | | | | **$40.18** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$142,675/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$105,700/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $105,700 / 10-yr mean $40,000 = **2.37×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $39.54 (NAV) + 0.30 × $40.18 (strip) = **$39.73**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 35.13 | 88% |
| Balance-sheet net | -7.45 | -19% |
| Discounted DPS (strip, 8-10q) | 4.25 | 11% |
| Discounted terminal (aged NAV) | 7.80 | 20% |
| **Blend FV** | **39.73** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.65 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $39.69 |
| 95% | $39.80 |
| 100% | $39.84 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **5.09× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **589,629** | — |
| 10-year mean | 33,933 | 17.38× |
| 12-month FFA | 115,837 | 5.09× |
| Current spot | 285,242 | 2.07× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (50% of fleet value) | 726,236 | 18.16× |
| Suezmax (50% of fleet value) | 450,350 | 16.23× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $28.91 | $33.39 | $37.87 | $42.35 | $46.84 |
| **-15%** | $29.84 | $34.32 | $38.80 | $43.28 | $47.76 |
| **+0%** | $30.77 | $35.25 | $39.73 | $44.21 | $48.69 |
| **+15%** | $31.69 | $36.18 | $40.66 | $45.14 | $49.62 |
| **+30%** | $32.62 | $37.10 | $41.59 | $46.07 | $50.55 |

_Current price $65.04. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$39.73** is -38.9% vs the current price ($65.04) and -11.7% vs the analyst target ($45.00). The current price implies the fleet earning a value-weighted blended **$589,629/day** (5.09× the current forward) — 17.4× the value-weighted 10-yr mean ($33,933, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
