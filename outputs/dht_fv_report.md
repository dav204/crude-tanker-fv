# DHT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $18.76
- **Model fair value:** $14.91
- **Analyst target:** $16.00

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 2,443.3 |
| + Cash & equivalents | 161.7 |
| + Working capital (net) | 137.6 |
| − Total debt | 434.8 |
| − Lease liabilities | 1.0 |
| − Newbuild commitments | 77.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,229.3** |
| Diluted shares | 161,235,573 |
| **NAV / share** | **$13.83** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 118,981 | 1.324 | 1.324 | 1.290 |
| Q2 | 183,500 | 138,781 | 1.577 | 1.577 | 1.496 |
| Q3 | 165,500 | 128,881 | 1.450 | 1.450 | 1.341 |
| Q4 | 123,500 | 105,781 | 1.156 | 1.156 | 1.042 |
| Q5 | 111,500 | 99,181 | 1.072 | 1.072 | 0.941 |
| Q6 | 135,500 | 112,381 | 1.240 | 1.240 | 1.060 |
| Q7 | 147,500 | 118,981 | 1.324 | 1.324 | 1.103 |
| Q8 | 105,500 | 95,881 | 1.030 | 1.030 | 0.836 |
| Σ discounted DPS | | | | | 9.11 |
| Terminal value (NAV, q9) | | | | 10.54 | 8.34 |
| **DivStrip implied price** | | | | | **$17.45** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.79×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $13.83 (NAV) + 0.30 × $17.45 (strip) = **$14.91**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 10.61 | 71% |
| Balance-sheet net | -0.93 | -6% |
| Discounted DPS (strip, 8-10q) | 2.73 | 18% |
| Discounted terminal (aged NAV) | 2.50 | 17% |
| **Blend FV** | **14.91** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.48 = **84%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $14.85 |
| 95% | $14.90 |
| 100% | $14.91 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.82× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **437,369** | — |
| 10-year mean | 40,000 | 10.93× |
| 12-month FFA | 155,000 | 2.82× |
| Current spot | 285,500 | 1.53× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $11.59 | $12.94 | $14.28 | $15.62 | $16.96 |
| **-15%** | $11.91 | $13.25 | $14.60 | $15.94 | $17.28 |
| **+0%** | $12.23 | $13.57 | $14.91 | $16.25 | $17.60 |
| **+15%** | $12.54 | $13.89 | $15.23 | $16.57 | $17.91 |
| **+30%** | $12.86 | $14.20 | $15.55 | $16.89 | $18.23 |

_Current price $18.76. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$14.91** is -20.5% vs the current price ($18.76) and -6.8% vs the analyst target ($16.00). The current price implies the fleet earning a value-weighted blended **$437,369/day** (2.82× the current forward) — 10.9× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
