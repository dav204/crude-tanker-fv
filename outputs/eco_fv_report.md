# ECO — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $61.86
- **Model fair value:** $42.03
- **Analyst target:** $45.00

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

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
| Q1 | 147,500 | 140,737 | 3.623 | 3.080 | 3.001 |
| Q2 | 183,500 | 172,417 | 4.604 | 3.913 | 3.714 |
| Q3 | 165,500 | 156,577 | 4.154 | 3.531 | 3.265 |
| Q4 | 123,500 | 119,617 | 2.917 | 2.479 | 2.233 |
| Q5 | 111,500 | 109,057 | 2.552 | 2.169 | 1.904 |
| Q6 | 135,500 | 130,177 | 3.350 | 2.848 | 2.435 |
| Q7 | 147,500 | 140,737 | 3.623 | 3.080 | 2.566 |
| Q8 | 105,500 | 103,777 | 2.375 | 2.019 | 1.638 |
| Σ discounted DPS | | | | | 20.76 |
| Terminal value (NAV, q9) | | | | 34.27 | 27.10 |
| **DivStrip implied price** | | | | | **$47.85** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.50×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $39.54 (NAV) + 0.30 × $47.85 (strip) = **$42.03**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 35.13 | 84% |
| Balance-sheet net | -7.45 | -18% |
| Discounted DPS (strip, 8-10q) | 6.23 | 15% |
| Discounted terminal (aged NAV) | 8.13 | 19% |
| **Blend FV** | **42.03** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.57 = **87%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $41.99 |
| 95% | $42.12 |
| 100% | $42.16 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.33× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **401,319** | — |
| 10-year mean | 33,933 | 11.83× |
| 12-month FFA | 120,339 | 3.33× |
| Current spot | 205,928 | 1.95× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (50% of fleet value) | 516,910 | 12.92× |
| Suezmax (50% of fleet value) | 283,467 | 10.22× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $30.52 | $35.00 | $39.48 | $43.97 | $48.45 |
| **-15%** | $31.80 | $36.28 | $40.76 | $45.24 | $49.72 |
| **+0%** | $33.07 | $37.55 | $42.03 | $46.51 | $51.00 |
| **+15%** | $34.34 | $38.82 | $43.31 | $47.79 | $52.27 |
| **+30%** | $35.62 | $40.10 | $44.58 | $49.06 | $53.54 |

_Current price $61.86. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$42.03** is -32.1% vs the current price ($61.86) and -6.6% vs the analyst target ($45.00). The current price implies the fleet earning a value-weighted blended **$401,319/day** (3.33× the current forward) — 11.8× the value-weighted 10-yr mean ($33,933, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
