# DHT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $17.89
- **Model fair value:** $14.68
- **Analyst target:** $16.00

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 2,511.1 |
| + Cash & equivalents | 126.2 |
| + Working capital (net) | 134.1 |
| − Total debt | 505.3 |
| − Lease liabilities | 1.0 |
| − Newbuild commitments | 77.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,187.6** |
| Diluted shares | 161,041,637 |
| **NAV / share** | **$13.58** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 118,981 | 1.326 | 1.326 | 1.292 |
| Q2 | 183,500 | 138,781 | 1.579 | 1.579 | 1.498 |
| Q3 | 165,500 | 128,881 | 1.452 | 1.452 | 1.343 |
| Q4 | 123,500 | 105,781 | 1.157 | 1.157 | 1.043 |
| Q5 | 111,500 | 99,181 | 1.073 | 1.073 | 0.942 |
| Q6 | 135,500 | 112,381 | 1.242 | 1.242 | 1.062 |
| Q7 | 147,500 | 118,981 | 1.326 | 1.326 | 1.105 |
| Q8 | 105,500 | 95,881 | 1.031 | 1.031 | 0.837 |
| Σ discounted DPS | | | | | 9.12 |
| Terminal value (NAV, q9) | | | | 10.28 | 8.13 |
| **DivStrip implied price** | | | | | **$17.25** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.79×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $13.58 (NAV) + 0.30 × $17.25 (strip) = **$14.68**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 10.91 | 74% |
| Balance-sheet net | -1.41 | -10% |
| Discounted DPS (strip, 8-10q) | 2.74 | 19% |
| Discounted terminal (aged NAV) | 2.44 | 17% |
| **Blend FV** | **14.68** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.47 = **84%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $14.62 |
| 95% | $14.67 |
| 100% | $14.68 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.52× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **389,978** | — |
| 10-year mean | 40,000 | 9.75× |
| 12-month FFA | 155,000 | 2.52× |
| Current spot | 285,500 | 1.37× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $11.28 | $12.67 | $14.05 | $15.43 | $16.82 |
| **-15%** | $11.60 | $12.98 | $14.37 | $15.75 | $17.13 |
| **+0%** | $11.92 | $13.30 | $14.68 | $16.07 | $17.45 |
| **+15%** | $12.24 | $13.62 | $15.00 | $16.38 | $17.77 |
| **+30%** | $12.55 | $13.94 | $15.32 | $16.70 | $18.08 |

_Current price $17.89. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$14.68** is -17.9% vs the current price ($17.89) and -8.2% vs the analyst target ($16.00). The current price implies the fleet earning a value-weighted blended **$389,978/day** (2.52× the current forward) — 9.7× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
