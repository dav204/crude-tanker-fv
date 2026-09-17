# Pipeline Delta Report

- **This run:** 2026-09-17T15:16:05+00:00
- **Previous run:** 2026-09-16T17:07:16+00:00

## Headline changes (material moves)

- **TRMD:** position BUY (undervalued) → HOLD (fairly valued); broker spread +8.8pp
- **TEN:** broker spread +7.4pp
- **SB:** broker spread +5.9pp

## §17 read-flip strobe — tape vs the flip boundary

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (fair/rich) | $23.69 | $24.33 | parity · fair\|rich | -2.61% | -3.47% (@ $23.48) | clear of the deadband |
| GNK | flips (cheap/fair) | $27.54 | $28.40 | hist · fair\|rich | -3.02% | -0.28% (@ $25.80) | clear of the deadband |
| SBLK | flips (cheap/fair) | $31.34 | $33.22 | parity · cheap\|fair | -5.65% | -8.48% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/forks.yaml` (modified)
- `inputs/market_data/prices_daily.yaml` (modified)
- `inputs/notify.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $22.89 (+0.59) | $15.26 (no change) | $16.32 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +20.3pp (+1.6pp) |
| ECO | $85.66 (+5.46) | $39.87 (no change) | $42.22 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +19.8pp (+2.9pp) |
| FRO | $53.93 (+2.41) | $26.71 (no change) | $28.79 (no change) | $26.04 (no change) | TRIM/SHORT (overvalued) | +24.5pp (+2.0pp) |
| INSW | $110.61 (+5.22) | $37.95 (no change) | $59.91 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +30.2pp (+2.3pp) |
| TNK | $101.59 (+1.29) | $84.12 (no change) | $83.24 (no change) | $84.60 (no change) | TRIM/SHORT (overvalued) | +22.8pp (+0.9pp) |
| NAT | $8.09 (+0.34) | $2.95 (no change) | $2.97 (no change) | $2.76 (no change) | TRIM/SHORT (overvalued) | +71.6pp (+1.3pp) |
| FLNG | $32.20 (+0.75) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -14.0pp (+1.9pp) |
| CCEC | $22.00 (-0.13) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -5.4pp (-0.7pp) |
| STNG | $86.62 (+0.93) | $72.66 (no change) | $75.97 (no change) | $76.22 (no change) | TRIM/SHORT (overvalued) | +44.9pp (+0.9pp) |
| HAFN | $9.71 (+0.32) | $4.92 (no change) | $5.47 (no change) | $4.64 (no change) | TRIM/SHORT (overvalued) | +45.3pp (+1.4pp) |
| TRMD ⚑ | $36.59 (+3.63) | $32.62 (no change) | $35.14 (no change) | $32.30 (no change) | HOLD (fairly valued) ⟵ | +18.6pp (+8.8pp) |
| ASC | $19.21 (+0.59) | $17.26 (no change) | $16.28 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +36.5pp (+2.5pp) |
| TEN ⚑ | $52.28 (+3.44) | $59.49 (no change) | $61.80 (no change) | $88.16 (no change) | BUY (undervalued) | +46.7pp (+7.4pp) |
| CMDB | $23.69 (-0.41) | $21.81 (no change) | $19.56 (no change) | $32.60 (no change) | TRIM/SHORT (overvalued) | -10.1pp (-1.3pp) |
| SBLK | $31.34 (+0.55) | $32.62 (no change) | $28.71 (no change) | $33.27 (no change) | TRIM/SHORT (overvalued) | +2.9pp (+1.5pp) |
| GNK | $27.54 (+0.54) | $25.40 (no change) | $21.50 (no change) | $25.37 (no change) | TRIM/SHORT (overvalued) | +10.1pp (+1.4pp) |
| CAPT | $19.81 (+0.42) | $17.09 (no change) | $17.77 (no change) | $17.32 (no change) | TRIM/SHORT (overvalued) | +47.8pp (+1.7pp) |
| MPCC | $3.04 (+0.08) | $2.33 (no change) | $2.16 (no change) | $2.15 (no change) | TRIM/SHORT (overvalued) | +19.8pp (+1.5pp) |
| GSL | $45.56 (-0.18) | $44.17 (no change) | $42.94 (no change) | $41.37 (no change) | TRIM/SHORT (overvalued) | +33.1pp (-0.2pp) |
| BRUT | $5.28 (+0.03) | $4.71 (no change) | $5.35 (no change) | $4.92 (no change) | HOLD (fairly valued) | +3.6pp (+0.5pp) |
| CMBT | $20.49 (+1.16) | $12.95 (no change) | $10.73 (no change) | $13.36 (no change) | TRIM/SHORT (overvalued) | +41.0pp (+3.2pp) |
| SB ⚑ | $8.76 (+0.49) | $10.41 (no change) | $9.22 (no change) | $10.72 (no change) | BUY (undervalued) | -27.6pp (+5.9pp) |
| LPG | $58.23 (+3.23) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +27.5pp (+3.0pp) |
| BWLP | $25.81 (+0.65) | $15.48 (no change) | $14.52 (no change) | $15.83 (no change) | TRIM/SHORT (overvalued) | +14.5pp (+1.3pp) |
| 2343 | $0.54 (+0.01) | $0.41 (no change) | $0.38 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +3.3pp (+1.0pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._