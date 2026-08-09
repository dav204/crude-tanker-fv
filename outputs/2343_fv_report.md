# 2343 — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $0.48
- **Model fair value:** $0.40
- **Analyst target:** $0.44

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Handy-Bulk | 1,166.5 |
| Fleet value — Supra-Ultra | 1,128.7 |
| Fleet value — Cape | 22.5 |
| + Cash & equivalents | 206.5 |
| + Working capital (net) | 85.8 |
| − Total debt | 49.3 |
| − Lease liabilities | 94.0 |
| − Newbuild commitments | 344.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,122.3** |
| Diluted shares | 5,165,247,803 |
| **NAV / share** | **$0.41** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Handy-Bulk, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 17,190 | 17,190 | 0.022 | 0.022 | 0.022 |
| Q2 | 16,600 | 16,600 | 0.021 | 0.021 | 0.020 |
| Q3 | 13,570 | 13,570 | 0.015 | 0.015 | 0.014 |
| Q4 | 13,030 | 13,030 | 0.014 | 0.014 | 0.012 |
| Q5 | 12,490 | 12,490 | 0.012 | 0.012 | 0.011 |
| Q6 | 11,950 | 11,950 | 0.011 | 0.011 | 0.010 |
| Q7 | 11,680 | 11,680 | 0.011 | 0.011 | 0.009 |
| Q8 | 11,410 | 11,410 | 0.010 | 0.010 | 0.008 |
| Σ discounted DPS | | | | | 0.11 |
| Terminal value (NAV, q9) | | | | 0.35 | 0.28 |
| **DivStrip implied price** | | | | | **$0.38** |

_FFA spot is the Handy-Bulk forward curve that drives the strip cash flows; its 12-month average is **$15,098/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$14,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $14,500 / 10-yr mean $12,850 = **1.24×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $0.41 (NAV) + 0.40 × $0.38 (strip) = **$0.40**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 0.27 | 67% |
| Balance-sheet net | -0.02 | -6% |
| Discounted DPS (strip, 8-10q) | 0.04 | 11% |
| Discounted terminal (aged NAV) | 0.11 | 28% |
| **Blend FV** | **0.40** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.72 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $0.40 |
| 95% | $0.40 |
| 100% | $0.40 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.03× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **32,599** | — |
| 10-year mean | 13,481 | 2.42× |
| 12-month FFA | 16,085 | 2.03× |
| Current spot | 18,100 | 1.80× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Handy-Bulk (50% of fleet value) | 30,597 | 2.38× |
| Supra-Ultra (49% of fleet value) | 33,996 | 2.44× |
| Cape (1% of fleet value) | 66,359 | 2.81× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $0.30 | $0.34 | $0.38 | $0.41 | $0.45 |
| **-15%** | $0.31 | $0.35 | $0.39 | $0.43 | $0.47 |
| **+0%** | $0.32 | $0.36 | $0.40 | $0.44 | $0.48 |
| **+15%** | $0.33 | $0.37 | $0.41 | $0.45 | $0.49 |
| **+30%** | $0.35 | $0.39 | $0.42 | $0.46 | $0.50 |

_Current price $0.48. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$0.40** is -17.5% vs the current price ($0.48) and -9.7% vs the analyst target ($0.44). The current price implies the fleet earning a value-weighted blended **$32,599/day** (2.03× the current forward) — 2.4× the value-weighted 10-yr mean ($13,481, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
