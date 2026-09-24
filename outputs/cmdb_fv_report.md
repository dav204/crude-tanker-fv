# CMDB — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $22.34
- **Model fair value:** $21.92
- **Analyst target:** $27.98

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 215.6 |
| Fleet value — Pana | 152.1 |
| Fleet value — Supra-Ultra | 330.5 |
| + Cash & equivalents | 234.8 |
| + Working capital (net) | 29.6 |
| − Total debt | 137.9 |
| − Lease liabilities | 34.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **790.3** |
| Diluted shares | 24,241,646 |
| **NAV / share** | **$32.60** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Supra-Ultra, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,887 | 19,887 | 1.694 | 0.000 | 0.000 |
| Q2 | 21,033 | 21,033 | 1.710 | 0.000 | 0.000 |
| Q3 | 16,575 | 16,575 | 1.035 | 0.000 | 0.000 |
| Q4 | 16,342 | 16,342 | 1.071 | 0.000 | 0.000 |
| Q5 | 16,342 | 16,342 | 1.071 | 0.000 | 0.000 |
| Q6 | 16,341 | 16,341 | 1.071 | 0.000 | 0.000 |
| Q7 | 16,041 | 16,041 | 1.032 | 0.000 | 0.000 |
| Q8 | 15,741 | 15,741 | 0.995 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 25.06 | 19.81 |
| **DivStrip implied price** | | | | | **$19.81** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$18,459/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$18,804/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $18,804 / 10-yr mean $13,930 = **1.52×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $22.82 (NAV) + 0.30 × $19.81 (strip) = **$21.92**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 20.16 | 92% |
| Balance-sheet net | 2.66 | 12% |
| §15 governance haircut | -6.85 | -31% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 5.94 | 27% |
| **Blend FV** | **21.92** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $22.73 |
| 95% | $22.88 |
| 100% | $22.93 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.14× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **29,091** | — |
| 10-year mean | 16,489 | 1.76× |
| 12-month FFA | 25,615 | 1.14× |
| Current spot | 31,768 | 0.92× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (47% of fleet value) | 20,965 | 1.51× |
| Cape (31% of fleet value) | 45,883 | 1.94× |
| Pana (22% of fleet value) | 22,949 | 1.93× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.42 | $19.20 | $20.99 | $22.77 | $24.55 |
| **-15%** | $17.89 | $19.67 | $21.45 | $23.23 | $25.02 |
| **+0%** | $18.35 | $20.14 | $21.92 | $23.70 | $25.48 |
| **+15%** | $18.82 | $20.60 | $22.38 | $24.17 | $25.95 |
| **+30%** | $19.29 | $21.07 | $22.85 | $24.63 | $26.41 |

_Current price $22.34. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$21.92** is -1.9% vs the current price ($22.34) and -21.7% vs the analyst target ($27.98). The current price implies the fleet earning a value-weighted blended **$29,091/day** (1.14× the current forward) — 1.8× the value-weighted 10-yr mean ($16,489, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
