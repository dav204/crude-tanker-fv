# TNK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $71.91
- **Model fair value:** $79.61
- **Analyst target:** $75.00

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 731.7 |
| Fleet value — Aframax | 795.6 |
| Fleet value — VLCC | 72.1 |
| + Cash & equivalents | 996.2 |
| + Working capital (net) | 97.3 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,692.8** |
| Diluted shares | 34,643,858 |
| **NAV / share** | **$77.73** |
| NAV / share (ex yard discount) | $79.08 |
| Yard-discount impact / share | $-1.36 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Aframax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 68,400 | 5.086 | 1.521 | 1.482 |
| Q2 | 88,000 | 78,540 | 6.123 | 1.781 | 1.690 |
| Q3 | 82,000 | 73,860 | 5.671 | 1.668 | 1.542 |
| Q4 | 64,000 | 59,820 | 4.247 | 1.312 | 1.182 |
| Q5 | 59,000 | 55,920 | 3.832 | 1.208 | 1.060 |
| Q6 | 70,000 | 64,500 | 4.782 | 1.445 | 1.236 |
| Q7 | 74,000 | 67,620 | 5.051 | 1.513 | 1.260 |
| Q8 | 56,000 | 53,580 | 3.613 | 1.153 | 0.936 |
| Σ discounted DPS | | | | | 10.39 |
| Terminal value (NAV, q9) | | | | 93.10 | 73.61 |
| **DivStrip implied price** | | | | | **$84.00** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $36,483 = **1.90×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $77.73 (NAV) + 0.30 × $84.00 (strip) = **$79.61**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 32.32 | 41% |
| Balance-sheet net | 22.09 | 28% |
| Discounted DPS (strip, 8-10q) | 3.12 | 4% |
| Discounted terminal (aged NAV) | 22.08 | 28% |
| **Blend FV** | **79.61** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.88 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $80.28 |
| 95% | $80.46 |
| 100% | $80.52 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.22× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **18,151** | — |
| 10-year mean | 32,645 | 0.56× |
| 12-month FFA | 84,302 | 0.22× |
| Current spot | 91,059 | 0.20× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Aframax (50% of fleet value) | 16,633 | 0.46× |
| Suezmax (46% of fleet value) | 18,302 | 0.66× |
| VLCC (5% of fleet value) | 33,374 | 0.83× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $68.56 | $72.61 | $76.67 | $80.72 | $84.78 |
| **-15%** | $70.03 | $74.08 | $78.14 | $82.19 | $86.25 |
| **+0%** | $71.50 | $75.56 | $79.61 | $83.67 | $87.72 |
| **+15%** | $72.97 | $77.03 | $81.08 | $85.14 | $89.19 |
| **+30%** | $74.44 | $78.50 | $82.56 | $86.61 | $90.67 |

_Current price $71.91. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$79.61** is +10.7% vs the current price ($71.91) and +6.1% vs the analyst target ($75.00). The current price implies the fleet earning a value-weighted blended **$18,151/day** (0.22× the current forward) — 0.6× the value-weighted 10-yr mean ($32,645, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
