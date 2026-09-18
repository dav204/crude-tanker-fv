# Pipeline Delta Report

- **This run:** 2026-09-18T16:51:48+00:00
- **Previous run:** 2026-09-17T18:57:17+00:00

## Headline changes (material moves)

- **TRMD:** position HOLD (fairly valued) → TRIM/SHORT (overvalued)
- **SB:** position BUY (undervalued) → HOLD (fairly valued)

## §17 read-flip strobe — tape vs the flip boundary

> ⚡ **STROBE ZONE — 2 name(s) inside the ±2.0% deadband at the tape: CMDB (-1.30%), GNK (-1.05%).** The governed `read_flag` holds its state on the watchlist vintage, but at today's close the read sits close enough to its settling boundary that the next vintage rebase could restate it — and `read_flag` caps position size. This is the hazard the deadband exists for: surfaced, not acted on.

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (fair/rich) | $24.01 | $24.33 | parity · fair\|rich | **-1.30%** | -3.47% (@ $23.48) | ⚡ inside ±2.0% deadband |
| GNK | flips (cheap/fair) | $28.10 | $28.40 | hist · fair\|rich | **-1.05%** | -0.28% (@ $25.80) | ⚡ inside ±2.0% deadband |
| SBLK | flips (cheap/fair) | $32.06 | $33.22 | parity · cheap\|fair | -3.48% | -8.48% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/agent_duties.yaml` (modified)
- `inputs/forks.yaml` (modified)
- `inputs/market_data/ffa_forward_curve.yaml` (modified)
- `inputs/market_data/prices_daily.yaml` (modified)
- `inputs/market_data/twelve_month_tc.yaml` (modified)
- `inputs/notify.yaml` (modified)
- `inputs/reweight_triggers.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $23.09 (+0.20) | $15.26 (no change) | $16.32 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +20.8pp (+0.5pp) |
| ECO | $84.61 (-1.05) | $39.87 (no change) | $42.22 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +19.2pp (-0.6pp) |
| FRO | $50.96 (-2.97) | $26.71 (no change) | $28.79 (no change) | $26.04 (no change) | TRIM/SHORT (overvalued) | +21.9pp (-2.6pp) |
| INSW | $111.21 (+0.60) | $37.95 (no change) | $59.91 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +30.4pp (+0.2pp) |
| TNK | $100.54 (-1.05) | $84.12 (no change) | $83.24 (no change) | $84.60 (no change) | TRIM/SHORT (overvalued) | +22.0pp (-0.8pp) |
| NAT | $8.16 (+0.07) | $2.95 (no change) | $2.97 (no change) | $2.76 (no change) | TRIM/SHORT (overvalued) | +71.9pp (+0.3pp) |
| FLNG | $32.51 (+0.31) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -13.2pp (+0.8pp) |
| CCEC | $22.34 (+0.34) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -3.7pp (+1.7pp) |
| STNG | $87.66 (+1.04) | $72.66 (no change) | $75.97 (no change) | $76.22 (no change) | TRIM/SHORT (overvalued) | +45.9pp (+1.0pp) |
| HAFN | $9.79 (+0.08) | $4.92 (no change) | $5.47 (no change) | $4.64 (no change) | TRIM/SHORT (overvalued) | +45.7pp (+0.4pp) |
| TRMD ⚑ | $37.38 (+0.79) | $32.62 (no change) | $35.14 (no change) | $32.30 (no change) | TRIM/SHORT (overvalued) ⟵ | +20.3pp (+1.7pp) |
| ASC | $18.97 (-0.24) | $17.26 (no change) | $16.28 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +35.5pp (-1.0pp) |
| TEN | $52.55 (+0.27) | $59.49 (no change) | $61.80 (no change) | $88.16 (no change) | BUY (undervalued) | +47.3pp (+0.6pp) |
| CMDB | $24.01 (+0.32) | $21.93 (+0.6%) | $19.37 (-1.0%) | $32.60 (no change) | TRIM/SHORT (overvalued) | -9.0pp (+1.1pp) |
| SBLK | $32.06 (+0.72) | $32.75 (+0.4%) | $28.34 (-1.3%) | $33.27 (no change) | TRIM/SHORT (overvalued) | +4.8pp (+1.9pp) |
| GNK | $28.10 (+0.56) | $25.19 (-0.8%) | $21.14 (-1.7%) | $25.37 (no change) | TRIM/SHORT (overvalued) | +11.4pp (+1.3pp) |
| CAPT | $19.75 (-0.06) | $17.09 (no change) | $17.77 (no change) | $17.32 (no change) | TRIM/SHORT (overvalued) | +47.6pp (-0.2pp) |
| MPCC | $3.00 (-0.04) | $2.33 (no change) | $2.16 (no change) | $2.15 (no change) | TRIM/SHORT (overvalued) | +19.1pp (-0.7pp) |
| GSL | $46.13 (+0.57) | $44.17 (no change) | $42.94 (no change) | $41.37 (no change) | TRIM/SHORT (overvalued) | +33.9pp (+0.8pp) |
| BRUT | $5.24 (-0.04) | $4.71 (no change) | $5.35 (no change) | $4.92 (no change) | HOLD (fairly valued) | +3.0pp (-0.6pp) |
| CMBT | $20.15 (-0.34) | $13.02 (+0.5%) | $10.50 (-2.1%) | $13.36 (no change) | TRIM/SHORT (overvalued) | +39.6pp (-1.4pp) |
| SB ⚑ | $8.91 (+0.15) | $10.41 (no change) | $9.08 (-1.5%) | $10.72 (no change) | HOLD (fairly valued) ⟵ | -25.6pp (+2.0pp) |
| LPG | $57.67 (-0.56) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +27.0pp (-0.5pp) |
| BWLP | $25.55 (-0.26) | $15.48 (no change) | $14.52 (no change) | $15.83 (no change) | TRIM/SHORT (overvalued) | +13.9pp (-0.6pp) |
| 2343 | $0.53 (-0.01) | $0.41 (no change) | $0.37 (-2.6%) | $0.41 (no change) | TRIM/SHORT (overvalued) | +2.5pp (-0.8pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._