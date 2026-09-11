# Pipeline Delta Report

- **This run:** 2026-09-11T14:04:43+00:00
- **Previous run:** 2026-09-10T19:14:49+00:00

## Headline changes (material moves)

- **CAPT:** position TRIM/SHORT (overvalued) → HOLD (fairly valued)
- **GSL:** position HOLD (fairly valued) → TRIM/SHORT (overvalued)

## §17 read-flip strobe — tape vs the flip boundary

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (fair/rich) | $23.35 | $24.33 | parity · fair\|rich | -4.01% | -3.47% (@ $23.48) | clear of the deadband |
| GNK | flips (cheap/fair) | $26.75 | $25.87 | parity · cheap\|fair | +3.39% | -0.28% (@ $25.80) | clear of the deadband |
| SBLK | flips (cheap/fair) | $30.74 | $33.22 | parity · cheap\|fair | -7.45% | -8.48% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/earnings_calendar.yaml` (modified)
- `inputs/fleet_manifests/bwlp.yaml` (modified)
- `inputs/forks.yaml` (modified)
- `inputs/market_data/prices_daily.yaml` (modified)
- `inputs/notify.yaml` (modified)
- `inputs/reweight_triggers.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $21.43 (+0.23) | $15.26 (no change) | $16.32 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +16.2pp (+0.7pp) |
| ECO | $72.92 (+1.25) | $39.87 (no change) | $42.22 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +12.5pp (+0.9pp) |
| FRO | $48.40 (+1.19) | $26.71 (no change) | $28.79 (no change) | $26.04 (no change) | TRIM/SHORT (overvalued) | +19.5pp (+1.3pp) |
| INSW | $102.14 (-2.48) | $37.95 (no change) | $59.91 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +26.4pp (-1.2pp) |
| TNK | $98.25 (+1.94) | $84.12 (no change) | $83.24 (no change) | $84.60 (no change) | TRIM/SHORT (overvalued) | +20.4pp (+1.5pp) |
| NAT | $7.21 (-0.06) | $2.95 (no change) | $2.97 (no change) | $2.76 (no change) | TRIM/SHORT (overvalued) | +68.1pp (-0.2pp) |
| FLNG | $31.61 (+0.47) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -15.5pp (+1.2pp) |
| CCEC | $22.52 (-0.08) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -2.8pp (-0.3pp) |
| STNG | $84.51 (+1.45) | $72.66 (no change) | $75.97 (no change) | $76.22 (no change) | TRIM/SHORT (overvalued) | +42.9pp (+1.4pp) |
| HAFN | $9.36 (+0.20) | $4.92 (no change) | $5.47 (no change) | $4.64 (no change) | TRIM/SHORT (overvalued) | +43.7pp (+1.0pp) |
| TRMD | $34.60 (-0.86) | $32.62 (no change) | $35.14 (no change) | $32.30 (no change) | HOLD (fairly valued) | +14.0pp (-2.1pp) |
| ASC | $18.46 (+0.23) | $17.26 (no change) | $16.28 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +33.3pp (+1.0pp) |
| TEN | $44.71 (+0.39) | $59.49 (no change) | $61.80 (no change) | $88.16 (no change) | BUY (undervalued) | +29.0pp (+1.1pp) |
| CMDB | $23.35 (-0.13) | $21.83 (no change) | $19.52 (no change) | $32.60 (no change) | TRIM/SHORT (overvalued) | -11.2pp (-0.5pp) |
| SBLK | $30.74 (-0.42) | $32.67 (no change) | $28.59 (no change) | $33.27 (no change) | TRIM/SHORT (overvalued) | +1.3pp (-1.1pp) |
| GNK | $26.75 (-0.39) | $25.41 (no change) | $21.48 (no change) | $25.37 (no change) | TRIM/SHORT (overvalued) | +8.0pp (-1.1pp) |
| CAPT ⚑ | $18.41 (-0.70) | $17.09 (no change) | $17.77 (no change) | $17.32 (no change) | HOLD (fairly valued) ⟵ | +41.7pp (-3.2pp) |
| MPCC | $2.94 (no change) | $2.33 (no change) | $2.16 (no change) | $2.15 (no change) | TRIM/SHORT (overvalued) | +17.9pp (no change) |
| GSL ⚑ | $45.54 (+0.52) | $44.17 (no change) | $42.94 (no change) | $41.37 (no change) | TRIM/SHORT (overvalued) ⟵ | +33.0pp (+0.8pp) |
| BRUT | $5.03 (-0.04) | $4.71 (no change) | $5.35 (no change) | $4.92 (no change) | BUY (undervalued) | -0.8pp (-0.8pp) |
| CMBT | $19.38 (+0.03) | $15.87 (no change) | $13.54 (no change) | $16.46 (no change) | TRIM/SHORT (overvalued) | +25.1pp (+0.1pp) |
| SB | $8.38 (+0.02) | $10.42 (no change) | $9.07 (no change) | $10.72 (no change) | BUY (undervalued) | -31.7pp (+0.3pp) |
| LPG | $54.41 (+0.78) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +23.9pp (+0.8pp) |
| BWLP | $24.89 (+0.74) | $15.48 (no change) | $14.52 (no change) | $15.83 (no change) | TRIM/SHORT (overvalued) | +12.6pp (+1.6pp) |
| 2343 | $0.55 (+0.01) | $0.41 (no change) | $0.38 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +4.8pp (+0.8pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._