# LPG — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $45.76
- **Model fair value:** $33.93
- **Analyst target:** $54.00

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLGC | 1,413.0 |
| + Cash & equivalents | 342.1 |
| + Working capital (net) | 202.9 |
| − Total debt | 512.4 |
| − Lease liabilities | 138.7 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,526.9** |
| Diluted shares | 42,782,681 |
| **NAV / share** | **$35.69** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLGC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 62,000 | 62,000 | 1.447 | 0.868 | 0.846 |
| Q2 | 55,000 | 55,000 | 1.183 | 0.710 | 0.674 |
| Q3 | 48,000 | 48,000 | 0.920 | 0.552 | 0.510 |
| Q4 | 45,000 | 45,000 | 0.807 | 0.484 | 0.436 |
| Q5 | 43,000 | 43,000 | 0.732 | 0.439 | 0.385 |
| Q6 | 42,000 | 42,000 | 0.694 | 0.417 | 0.356 |
| Q7 | 41,000 | 41,000 | 0.657 | 0.394 | 0.328 |
| Q8 | 40,000 | 40,000 | 0.619 | 0.371 | 0.301 |
| Σ discounted DPS | | | | | 3.84 |
| Terminal value (NAV, q9) | | | | 32.85 | 25.98 |
| **DivStrip implied price** | | | | | **$29.82** |

_FFA spot is the VLGC forward curve that drives the strip cash flows; its 12-month average is **$52,500/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$63,615/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $63,615 / 10-yr mean $40,000 = **1.59×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $35.69 (NAV) + 0.30 × $29.82 (strip) = **$33.93**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 23.12 | 68% |
| Balance-sheet net | 1.86 | 5% |
| Discounted DPS (strip, 8-10q) | 1.15 | 3% |
| Discounted terminal (aged NAV) | 7.79 | 23% |
| **Blend FV** | **33.93** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.87 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $33.98 |
| 95% | $34.01 |
| 100% | $34.03 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **4.26× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **223,619** | — |
| 10-year mean | 40,000 | 5.59× |
| 12-month FFA | 52,500 | 4.26× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $26.92 | $29.88 | $32.84 | $35.80 | $38.76 |
| **-15%** | $27.46 | $30.42 | $33.38 | $36.34 | $39.31 |
| **+0%** | $28.01 | $30.97 | $33.93 | $36.89 | $39.85 |
| **+15%** | $28.55 | $31.51 | $34.47 | $37.43 | $40.39 |
| **+30%** | $29.10 | $32.06 | $35.02 | $37.98 | $40.94 |

_Current price $45.76. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$33.93** is -25.9% vs the current price ($45.76) and -37.2% vs the analyst target ($54.00). The current price implies the fleet earning a value-weighted blended **$223,619/day** (4.26× the current forward) — 5.6× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
