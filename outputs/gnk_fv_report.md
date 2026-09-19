# GNK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $27.96
- **Model fair value:** $25.19
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
| Q1 | 50,000 | 49,325 | 1.957 | 1.957 | 1.906 |
| Q2 | 46,375 | 45,881 | 1.848 | 1.848 | 1.754 |
| Q3 | 31,925 | 32,154 | 1.188 | 1.188 | 1.099 |
| Q4 | 34,425 | 34,529 | 1.280 | 1.280 | 1.153 |
| Q5 | 34,425 | 34,529 | 1.280 | 1.280 | 1.123 |
| Q6 | 34,425 | 34,529 | 1.280 | 1.280 | 1.094 |
| Q7 | 33,925 | 34,054 | 1.254 | 1.254 | 1.045 |
| Q8 | 33,425 | 33,579 | 1.228 | 1.228 | 0.997 |
| Σ discounted DPS | | | | | 10.17 |
| Terminal value (NAV, q9) | | | | 18.46 | 14.60 |
| **DivStrip implied price** | | | | | **$24.77** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$40,681/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$39,150/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $39,150 / 10-yr mean $23,650 = **1.55×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $25.37 (NAV) + 0.30 × $24.77 (strip) = **$25.19**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 22.52 | 89% |
| Balance-sheet net | -4.75 | -19% |
| Discounted DPS (strip, 8-10q) | 3.05 | 12% |
| Discounted terminal (aged NAV) | 4.38 | 17% |
| **Blend FV** | **25.19** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.59 = **88%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $25.12 |
| 95% | $25.17 |
| 100% | $25.19 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.70× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **55,727** | — |
| 10-year mean | 20,134 | 2.77× |
| 12-month FFA | 32,717 | 1.70× |
| Current spot | 42,601 | 1.31× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (64% of fleet value) | 69,294 | 2.93× |
| Supra-Ultra (36% of fleet value) | 31,788 | 2.28× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.31 | $21.16 | $24.01 | $26.86 | $29.71 |
| **-15%** | $18.90 | $21.75 | $24.60 | $27.45 | $30.30 |
| **+0%** | $19.49 | $22.34 | $25.19 | $28.04 | $30.89 |
| **+15%** | $20.08 | $22.93 | $25.78 | $28.63 | $31.48 |
| **+30%** | $20.67 | $23.52 | $26.37 | $29.22 | $32.07 |

_Current price $27.96. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$25.19** is -9.9% vs the current price ($27.96) and -7.4% vs the analyst target ($27.20). The current price implies the fleet earning a value-weighted blended **$55,727/day** (1.70× the current forward) — 2.8× the value-weighted 10-yr mean ($20,134, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
