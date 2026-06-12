# TNK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $72.50
- **Model fair value:** $73.92
- **Analyst target:** $75.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 721.7 |
| Fleet value — Aframax | 794.9 |
| Fleet value — VLCC | 73.3 |
| + Cash & equivalents | 996.2 |
| + Working capital (net) | 97.3 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,683.3** |
| Diluted shares | 34,643,858 |
| **NAV / share** | **$77.45** |
| NAV / share (ex yard discount) | $78.80 |
| Yard-discount impact / share | $-1.35 |

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
| Terminal value (NAV, q9) | | | | 69.94 | 55.30 |
| **DivStrip implied price** | | | | | **$65.69** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **2.15×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $77.45 (NAV) + 0.30 × $65.69 (strip) = **$73.92**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $79.61 |
| 95% | $81.15 |
| 100% | $81.67 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.47× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **39,706** | — |
| 10-year mean | 28,238 | 1.41× |
| 12-month FFA | 84,351 | 0.47× |
| Current spot | 74,328 | 0.53× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Aframax (50% of fleet value) | 36,363 | 1.32× |
| Suezmax (45% of fleet value) | 40,011 | 1.44× |
| VLCC (5% of fleet value) | 72,962 | 1.82× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $64.87 | $68.99 | $73.12 | $77.24 | $81.36 |
| **-15%** | $65.28 | $69.40 | $73.52 | $77.64 | $81.77 |
| **+0%** | $65.68 | $69.80 | $73.92 | $78.05 | $82.17 |
| **+15%** | $66.08 | $70.21 | $74.33 | $78.45 | $82.57 |
| **+30%** | $66.49 | $70.61 | $74.73 | $78.85 | $82.98 |

_Current price $72.50. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$73.92** is +2.0% vs the current price ($72.50) and -1.4% vs the analyst target ($75.00). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$39,706/day** (0.47× the current forward) — 1.4× the value-weighted 10-yr mean ($28,238, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $30.2M (-8%) / 10yr $22.1M (-12%) [n=20], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
