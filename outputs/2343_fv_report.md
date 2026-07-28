# 2343 — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $0.42
- **Model fair value:** $0.39
- **Analyst target:** $0.44

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Handy-Bulk | 1,140.2 |
| Fleet value — Supra-Ultra | 1,118.4 |
| Fleet value — Cape | 23.0 |
| + Cash & equivalents | 270.6 |
| + Working capital (net) | 26.4 |
| − Total debt | 136.5 |
| − Lease liabilities | 93.9 |
| − Newbuild commitments | 284.9 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,063.2** |
| Diluted shares | 5,165,247,803 |
| **NAV / share** | **$0.40** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Handy-Bulk, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 17,190 | 17,190 | 0.022 | 0.022 | 0.021 |
| Q2 | 16,600 | 16,600 | 0.021 | 0.021 | 0.020 |
| Q3 | 13,570 | 13,570 | 0.014 | 0.014 | 0.013 |
| Q4 | 13,030 | 13,030 | 0.013 | 0.013 | 0.012 |
| Q5 | 12,490 | 12,490 | 0.012 | 0.012 | 0.011 |
| Q6 | 11,950 | 11,950 | 0.011 | 0.011 | 0.009 |
| Q7 | 11,680 | 11,680 | 0.010 | 0.010 | 0.009 |
| Q8 | 11,410 | 11,410 | 0.010 | 0.010 | 0.008 |
| Σ discounted DPS | | | | | 0.10 |
| Terminal value (NAV, q9) | | | | 0.34 | 0.27 |
| **DivStrip implied price** | | | | | **$0.37** |

_FFA spot is the Handy-Bulk forward curve that drives the strip cash flows; its 12-month average is **$15,098/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$14,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $14,500 / 10-yr mean $12,850 = **1.24×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $0.40 (NAV) + 0.40 × $0.37 (strip) = **$0.39**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 0.27 | 68% |
| Balance-sheet net | -0.03 | -7% |
| Discounted DPS (strip, 8-10q) | 0.04 | 11% |
| Discounted terminal (aged NAV) | 0.11 | 28% |
| **Blend FV** | **0.39** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.72 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $0.39 |
| 95% | $0.39 |
| 100% | $0.39 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.41× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **22,622** | — |
| 10-year mean | 13,488 | 1.68× |
| 12-month FFA | 16,098 | 1.41× |
| Current spot | 18,118 | 1.25× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Handy-Bulk (50% of fleet value) | 21,216 | 1.65× |
| Supra-Ultra (49% of fleet value) | 23,574 | 1.69× |
| Cape (1% of fleet value) | 46,015 | 1.95× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $0.29 | $0.33 | $0.36 | $0.40 | $0.44 |
| **-15%** | $0.30 | $0.34 | $0.38 | $0.41 | $0.45 |
| **+0%** | $0.31 | $0.35 | $0.39 | $0.43 | $0.47 |
| **+15%** | $0.32 | $0.36 | $0.40 | $0.44 | $0.48 |
| **+30%** | $0.34 | $0.37 | $0.41 | $0.45 | $0.49 |

_Current price $0.42. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$0.39** is -7.8% vs the current price ($0.42) and -12.4% vs the analyst target ($0.44). The current price implies the fleet earning a value-weighted blended **$22,622/day** (1.41× the current forward) — 1.7× the value-weighted 10-yr mean ($13,488, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
