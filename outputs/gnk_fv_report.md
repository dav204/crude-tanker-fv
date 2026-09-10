# GNK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $27.14
- **Model fair value:** $25.41
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
| Q1 | 45,125 | 44,694 | 1.763 | 1.763 | 1.718 |
| Q2 | 44,125 | 43,744 | 1.751 | 1.751 | 1.662 |
| Q3 | 29,925 | 30,254 | 1.094 | 1.094 | 1.012 |
| Q4 | 34,292 | 34,402 | 1.268 | 1.268 | 1.143 |
| Q5 | 34,292 | 34,402 | 1.268 | 1.268 | 1.113 |
| Q6 | 34,291 | 34,401 | 1.268 | 1.268 | 1.085 |
| Q7 | 33,791 | 33,926 | 1.242 | 1.242 | 1.035 |
| Q8 | 33,291 | 33,451 | 1.216 | 1.216 | 0.987 |
| Σ discounted DPS | | | | | 9.75 |
| Terminal value (NAV, q9) | | | | 19.86 | 15.71 |
| **DivStrip implied price** | | | | | **$25.46** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$38,367/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$37,025/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $37,025 / 10-yr mean $23,650 = **1.48×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $25.37 (NAV) + 0.40 × $25.46 (strip) = **$25.41**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.30 | 76% |
| Balance-sheet net | -4.08 | -16% |
| Discounted DPS (strip, 8-10q) | 3.90 | 15% |
| Discounted terminal (aged NAV) | 6.28 | 25% |
| **Blend FV** | **25.41** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.62 = **85%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $25.32 |
| 95% | $25.38 |
| 100% | $25.41 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.34× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **41,661** | — |
| 10-year mean | 20,134 | 2.07× |
| 12-month FFA | 31,071 | 1.34× |
| Current spot | 34,360 | 1.21× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (64% of fleet value) | 51,443 | 2.18× |
| Supra-Ultra (36% of fleet value) | 24,400 | 1.75× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.34 | $21.11 | $23.88 | $26.66 | $29.43 |
| **-15%** | $19.10 | $21.87 | $24.65 | $27.42 | $30.19 |
| **+0%** | $19.86 | $22.64 | $25.41 | $28.18 | $30.95 |
| **+15%** | $20.62 | $23.40 | $26.17 | $28.94 | $31.72 |
| **+30%** | $21.39 | $24.16 | $26.93 | $29.71 | $32.48 |

_Current price $27.14. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$25.41** is -6.4% vs the current price ($27.14) and -6.6% vs the analyst target ($27.20). The current price implies the fleet earning a value-weighted blended **$41,661/day** (1.34× the current forward) — 2.1× the value-weighted 10-yr mean ($20,134, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
