# ECO — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $61.86
- **Model fair value:** $40.24
- **Analyst target:** $45.00

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 915.4 |
| Fleet value — Suezmax | 970.2 |
| + Cash & equivalents | 247.8 |
| + Working capital (net) | 138.4 |
| − Total debt | 722.5 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 79.4 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,470.0** |
| Diluted shares | 39,044,655 |
| **NAV / share** | **$37.65** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 81,500 | 81,500 | 3.623 | 3.080 | 3.001 |
| Q2 | 99,000 | 99,000 | 4.604 | 3.913 | 3.714 |
| Q3 | 92,000 | 92,000 | 4.154 | 3.531 | 3.265 |
| Q4 | 67,500 | 67,500 | 2.917 | 2.479 | 2.233 |
| Q5 | 60,000 | 60,000 | 2.552 | 2.169 | 1.904 |
| Q6 | 78,000 | 78,000 | 3.350 | 2.848 | 2.435 |
| Q7 | 81,500 | 81,500 | 3.623 | 3.080 | 2.566 |
| Q8 | 56,500 | 56,500 | 2.375 | 2.019 | 1.638 |
| Σ discounted DPS | | | | | 20.76 |
| Terminal value (NAV, q9) | | | | 32.30 | 25.54 |
| **DivStrip implied price** | | | | | **$46.29** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.49×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $37.65 (NAV) + 0.30 × $46.29 (strip) = **$40.24**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 33.81 | 84% |
| Balance-sheet net | -7.45 | -19% |
| Discounted DPS (strip, 8-10q) | 6.23 | 15% |
| Discounted terminal (aged NAV) | 7.66 | 19% |
| **Blend FV** | **40.24** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.55 = **87%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $40.20 |
| 95% | $40.33 |
| 100% | $40.37 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.55× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **421,886** | — |
| 10-year mean | 33,696 | 12.52× |
| 12-month FFA | 118,984 | 3.55× |
| Current spot | 202,817 | 2.08× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (51% of fleet value) | 301,389 | 10.86× |
| VLCC (49% of fleet value) | 549,591 | 13.74× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $29.09 | $33.39 | $37.69 | $42.00 | $46.30 |
| **-15%** | $30.36 | $34.67 | $38.97 | $43.27 | $47.57 |
| **+0%** | $31.64 | $35.94 | $40.24 | $44.54 | $48.85 |
| **+15%** | $32.91 | $37.21 | $41.52 | $45.82 | $50.12 |
| **+30%** | $34.18 | $38.49 | $42.79 | $47.09 | $51.39 |

_Current price $61.86. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$40.24** is -34.9% vs the current price ($61.86) and -10.6% vs the analyst target ($45.00). The current price implies the fleet earning a value-weighted blended **$421,886/day** (3.55× the current forward) — 12.5× the value-weighted 10-yr mean ($33,696, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
