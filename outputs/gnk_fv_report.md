# GNK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $27.96
- **Model fair value:** $25.23
- **Analyst target:** $27.20

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 915.1 |
| Fleet value — Supra-Ultra | 518.6 |
| + Cash & equivalents | 73.6 |
| + Working capital (net) | 16.8 |
| − Total debt | 330.0 |
| − Lease liabilities | 5.7 |
| − Newbuild commitments | 57.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,131.0** |
| Diluted shares | 44,572,591 |
| **NAV / share** | **$25.37** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 50,000 | 49,325 | 1.955 | 1.955 | 1.905 |
| Q2 | 46,875 | 46,356 | 1.870 | 1.870 | 1.775 |
| Q3 | 32,500 | 32,700 | 1.214 | 1.214 | 1.123 |
| Q4 | 34,667 | 34,759 | 1.296 | 1.296 | 1.168 |
| Q5 | 34,667 | 34,759 | 1.296 | 1.296 | 1.138 |
| Q6 | 34,666 | 34,758 | 1.296 | 1.296 | 1.108 |
| Q7 | 34,166 | 34,283 | 1.270 | 1.270 | 1.058 |
| Q8 | 33,666 | 33,808 | 1.244 | 1.244 | 1.010 |
| Σ discounted DPS | | | | | 10.28 |
| Terminal value (NAV, q9) | | | | 18.46 | 14.60 |
| **DivStrip implied price** | | | | | **$24.88** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$41,010/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$39,688/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $39,688 / 10-yr mean $23,650 = **1.57×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $25.37 (NAV) + 0.30 × $24.88 (strip) = **$25.23**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 22.52 | 89% |
| Balance-sheet net | -4.75 | -19% |
| Discounted DPS (strip, 8-10q) | 3.09 | 12% |
| Discounted terminal (aged NAV) | 4.38 | 17% |
| **Blend FV** | **25.23** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.59 = **88%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $25.15 |
| 95% | $25.21 |
| 100% | $25.23 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.69× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **55,689** | — |
| 10-year mean | 20,134 | 2.77× |
| 12-month FFA | 32,977 | 1.69× |
| Current spot | 42,601 | 1.31× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (64% of fleet value) | 69,256 | 2.93× |
| Supra-Ultra (36% of fleet value) | 31,748 | 2.28× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.33 | $21.18 | $24.03 | $26.89 | $29.74 |
| **-15%** | $18.93 | $21.78 | $24.63 | $27.48 | $30.33 |
| **+0%** | $19.52 | $22.37 | $25.23 | $28.08 | $30.93 |
| **+15%** | $20.12 | $22.97 | $25.82 | $28.67 | $31.52 |
| **+30%** | $20.72 | $23.57 | $26.42 | $29.27 | $32.12 |

_Current price $27.96. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$25.23** is -9.8% vs the current price ($27.96) and -7.3% vs the analyst target ($27.20). The current price implies the fleet earning a value-weighted blended **$55,689/day** (1.69× the current forward) — 2.8× the value-weighted 10-yr mean ($20,134, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
