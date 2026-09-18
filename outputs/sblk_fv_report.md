# SBLK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $32.06
- **Model fair value:** $32.75
- **Analyst target:** $34.50

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,557.8 |
| Fleet value — Pana | 1,414.3 |
| Fleet value — Supra-Ultra | 1,391.6 |
| + Cash & equivalents | 565.3 |
| + Working capital (net) | 84.2 |
| − Total debt | 1,036.6 |
| − Lease liabilities | 142.4 |
| − Newbuild commitments | 122.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,712.2** |
| Diluted shares | 111,585,370 |
| **NAV / share** | **$33.27** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 50,000 | 50,000 | 2.163 | 2.055 | 2.002 |
| Q2 | 46,375 | 46,375 | 2.166 | 2.058 | 1.953 |
| Q3 | 31,925 | 31,925 | 1.428 | 1.356 | 1.254 |
| Q4 | 34,425 | 34,425 | 1.484 | 1.409 | 1.270 |
| Q5 | 34,425 | 34,425 | 1.483 | 1.409 | 1.237 |
| Q6 | 34,425 | 34,425 | 1.483 | 1.409 | 1.205 |
| Q7 | 33,925 | 33,925 | 1.441 | 1.369 | 1.141 |
| Q8 | 33,425 | 33,425 | 1.403 | 1.333 | 1.082 |
| Σ discounted DPS | | | | | 11.14 |
| Terminal value (NAV, q9) | | | | 25.80 | 20.40 |
| **DivStrip implied price** | | | | | **$31.55** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$40,681/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$39,150/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $39,150 / 10-yr mean $23,650 = **1.58×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $33.27 (NAV) + 0.30 × $31.55 (strip) = **$32.75**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 27.37 | 84% |
| Balance-sheet net | -4.09 | -12% |
| Discounted DPS (strip, 8-10q) | 3.34 | 10% |
| Discounted terminal (aged NAV) | 6.12 | 19% |
| **Blend FV** | **32.75** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.65 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $32.69 |
| 95% | $32.75 |
| 100% | $32.77 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.87× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **23,456** | — |
| 10-year mean | 16,742 | 1.40× |
| 12-month FFA | 26,944 | 0.87× |
| Current spot | 33,379 | 0.70× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 35,416 | 1.50× |
| Pana (32% of fleet value) | 17,377 | 1.46× |
| Supra-Ultra (32% of fleet value) | 16,247 | 1.17× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $24.20 | $27.68 | $31.15 | $34.62 | $38.09 |
| **-15%** | $25.00 | $28.48 | $31.95 | $35.42 | $38.90 |
| **+0%** | $25.81 | $29.28 | $32.75 | $36.22 | $39.70 |
| **+15%** | $26.61 | $30.08 | $33.55 | $37.03 | $40.50 |
| **+30%** | $27.41 | $30.88 | $34.35 | $37.83 | $41.30 |

_Current price $32.06. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$32.75** is +2.2% vs the current price ($32.06) and -5.1% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$23,456/day** (0.87× the current forward) — 1.4× the value-weighted 10-yr mean ($16,742, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
