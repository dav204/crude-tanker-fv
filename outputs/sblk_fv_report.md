# SBLK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $28.90
- **Model fair value:** $29.66
- **Analyst target:** $34.50

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,594.7 |
| Fleet value — Pana | 1,420.2 |
| Fleet value — Supra-Ultra | 1,433.2 |
| + Cash & equivalents | 397.0 |
| + Working capital (net) | 44.6 |
| − Total debt | 946.3 |
| − Lease liabilities | 149.8 |
| − Newbuild commitments | 195.6 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,598.0** |
| Diluted shares | 117,431,435 |
| **NAV / share** | **$30.64** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 34,900 | 34,900 | 1.615 | 1.534 | 1.495 |
| Q2 | 35,725 | 35,725 | 1.604 | 1.524 | 1.446 |
| Q3 | 30,675 | 30,675 | 1.263 | 1.200 | 1.109 |
| Q4 | 29,675 | 29,675 | 1.188 | 1.129 | 1.017 |
| Q5 | 28,675 | 28,675 | 1.113 | 1.057 | 0.928 |
| Q6 | 27,675 | 27,675 | 1.038 | 0.986 | 0.843 |
| Q7 | 27,175 | 27,175 | 0.997 | 0.947 | 0.789 |
| Q8 | 26,675 | 26,675 | 0.959 | 0.911 | 0.740 |
| Σ discounted DPS | | | | | 8.37 |
| Terminal value (NAV, q9) | | | | 25.07 | 19.83 |
| **DivStrip implied price** | | | | | **$28.19** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,744/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.48×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $30.64 (NAV) + 0.40 × $28.19 (strip) = **$29.66**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 22.73 | 77% |
| Balance-sheet net | -4.34 | -15% |
| Discounted DPS (strip, 8-10q) | 3.35 | 11% |
| Discounted terminal (aged NAV) | 7.93 | 27% |
| **Blend FV** | **29.66** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.70 = **88%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $29.60 |
| 95% | $29.66 |
| 100% | $29.68 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.87× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **19,951** | — |
| 10-year mean | 16,767 | 1.19× |
| 12-month FFA | 22,915 | 0.87× |
| Current spot | 25,136 | 0.79× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 28,508 | 1.21× |
| Supra-Ultra (32% of fleet value) | 14,605 | 1.05× |
| Pana (32% of fleet value) | 15,737 | 1.32× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $21.34 | $24.62 | $27.90 | $31.18 | $34.45 |
| **-15%** | $22.22 | $25.50 | $28.78 | $32.06 | $35.34 |
| **+0%** | $23.10 | $26.38 | $29.66 | $32.94 | $36.22 |
| **+15%** | $23.98 | $27.26 | $30.54 | $33.82 | $37.10 |
| **+30%** | $24.87 | $28.15 | $31.43 | $34.70 | $37.98 |

_Current price $28.90. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$29.66** is +2.6% vs the current price ($28.90) and -14.0% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$19,951/day** (0.87× the current forward) — 1.2× the value-weighted 10-yr mean ($16,767, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
