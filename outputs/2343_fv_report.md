# 2343 — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $0.39
- **Model fair value:** $0.38
- **Analyst target:** $0.44

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Handy-Bulk | 1,140.2 |
| Fleet value — Supra-Ultra | 1,045.9 |
| Fleet value — Cape | 22.4 |
| + Cash & equivalents | 270.6 |
| + Working capital (net) | 26.4 |
| − Total debt | 136.5 |
| − Lease liabilities | 93.9 |
| − Newbuild commitments | 284.9 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,990.1** |
| Diluted shares | 5,165,247,803 |
| **NAV / share** | **$0.39** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Handy-Bulk, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 16,920 | 16,920 | 0.021 | 0.021 | 0.021 |
| Q2 | 16,090 | 16,090 | 0.020 | 0.020 | 0.019 |
| Q3 | 13,570 | 13,570 | 0.014 | 0.014 | 0.013 |
| Q4 | 13,030 | 13,030 | 0.013 | 0.013 | 0.012 |
| Q5 | 12,490 | 12,490 | 0.012 | 0.012 | 0.011 |
| Q6 | 11,950 | 11,950 | 0.011 | 0.011 | 0.009 |
| Q7 | 11,680 | 11,680 | 0.010 | 0.010 | 0.009 |
| Q8 | 11,410 | 11,410 | 0.010 | 0.010 | 0.008 |
| Σ discounted DPS | | | | | 0.10 |
| Terminal value (NAV, q9) | | | | 0.33 | 0.26 |
| **DivStrip implied price** | | | | | **$0.36** |

_FFA spot is the Handy-Bulk forward curve that drives the strip cash flows; its 12-month average is **$14,902/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$14,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $14,500 / 10-yr mean $12,850 = **1.22×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $0.39 (NAV) + 0.40 × $0.36 (strip) = **$0.38**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 0.26 | 68% |
| Balance-sheet net | -0.03 | -7% |
| Discounted DPS (strip, 8-10q) | 0.04 | 11% |
| Discounted terminal (aged NAV) | 0.10 | 28% |
| **Blend FV** | **0.38** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.72 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $0.37 |
| 95% | $0.37 |
| 100% | $0.38 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.19× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **18,872** | — |
| 10-year mean | 13,471 | 1.40× |
| 12-month FFA | 15,864 | 1.19× |
| Current spot | 17,567 | 1.07× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Handy-Bulk (52% of fleet value) | 17,728 | 1.38× |
| Supra-Ultra (47% of fleet value) | 19,696 | 1.41× |
| Cape (1% of fleet value) | 38,603 | 1.63× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $0.28 | $0.31 | $0.35 | $0.39 | $0.43 |
| **-15%** | $0.29 | $0.33 | $0.36 | $0.40 | $0.44 |
| **+0%** | $0.30 | $0.34 | $0.38 | $0.41 | $0.45 |
| **+15%** | $0.31 | $0.35 | $0.39 | $0.42 | $0.46 |
| **+30%** | $0.32 | $0.36 | $0.40 | $0.44 | $0.47 |

_Current price $0.39. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$0.38** is -3.9% vs the current price ($0.39) and -15.3% vs the analyst target ($0.44). The current price implies the fleet earning a value-weighted blended **$18,872/day** (1.19× the current forward) — 1.4× the value-weighted 10-yr mean ($13,471, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
