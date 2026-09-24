# Pipeline Delta Report

- **This run:** 2026-09-24T15:15:22+00:00
- **Previous run:** 2026-09-23T20:07:17+00:00

## Headline changes (material moves)

- **No material changes.** All tickers within thresholds (|ΔFV%|≤10%, |Δspread|≤5pp, |ΔNAV%|≤5%) and no position flips.

## §17 read-flip strobe — tape vs the flip boundary

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (fair/rich) | $22.34 | $24.33 | parity · fair\|rich | -8.16% | -3.47% (@ $23.48) | clear of the deadband |
| GNK | flips (cheap/fair) | $26.43 | $25.87 | parity · cheap\|fair | +2.16% | -0.28% (@ $25.80) | clear of the deadband |
| SBLK | flips (cheap/fair) | $30.40 | $33.22 | parity · cheap\|fair | -8.48% | -8.48% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/forks.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $21.28 (no change) | $15.26 (no change) | $16.56 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +8.8pp (no change) |
| ECO | $77.91 (no change) | $39.87 (no change) | $44.15 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +6.7pp (no change) |
| FRO | $47.56 (no change) | $26.71 (no change) | $29.38 (no change) | $26.04 (no change) | TRIM/SHORT (overvalued) | +13.4pp (no change) |
| INSW | $102.05 (no change) | $37.95 (no change) | $61.81 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +25.1pp (no change) |
| TNK | $94.54 (no change) | $84.12 (no change) | $87.59 (no change) | $84.60 (no change) | TRIM/SHORT (overvalued) | +12.0pp (no change) |
| NAT | $7.62 (no change) | $2.95 (no change) | $3.24 (no change) | $2.76 (no change) | TRIM/SHORT (overvalued) | +62.8pp (no change) |
| FLNG | $30.97 (no change) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | HOLD (fairly valued) | -16.4pp (no change) |
| CCEC | $21.80 (no change) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -1.6pp (no change) |
| STNG | $81.20 (no change) | $72.66 (no change) | $75.97 (no change) | $76.22 (no change) | TRIM/SHORT (overvalued) | +33.6pp (no change) |
| HAFN | $9.10 (no change) | $4.92 (no change) | $5.47 (no change) | $4.64 (no change) | TRIM/SHORT (overvalued) | +34.6pp (no change) |
| TRMD | $34.42 (no change) | $32.62 (no change) | $35.14 (no change) | $32.30 (no change) | HOLD (fairly valued) | +6.0pp (no change) |
| ASC | $17.61 (no change) | $17.26 (no change) | $16.28 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +30.1pp (no change) |
| TEN | $46.97 (no change) | $62.06 (no change) | $68.15 (no change) | $91.91 (no change) | BUY (undervalued) | +22.4pp (no change) |
| CMDB | $22.34 (no change) | $21.97 (no change) | $19.30 (no change) | $32.60 (no change) | TRIM/SHORT (overvalued) | -11.1pp (no change) |
| SBLK | $30.40 (no change) | $32.81 (no change) | $28.20 (no change) | $33.27 (no change) | TRIM/SHORT (overvalued) | +0.4pp (no change) |
| GNK | $26.43 (no change) | $25.23 (no change) | $21.05 (no change) | $25.37 (no change) | TRIM/SHORT (overvalued) | +5.1pp (no change) |
| CAPT | $18.45 (no change) | $17.09 (no change) | $18.57 (no change) | $17.32 (no change) | HOLD (fairly valued) | +25.7pp (no change) |
| MPCC | $2.98 (no change) | $2.33 (no change) | $2.16 (no change) | $2.15 (no change) | TRIM/SHORT (overvalued) | +16.7pp (no change) |
| GSL | $44.55 (no change) | $44.17 (no change) | $42.94 (no change) | $41.37 (no change) | HOLD (fairly valued) | +18.5pp (no change) |
| BRUT | $5.08 (no change) | $4.71 (no change) | $5.51 (no change) | $4.92 (no change) | BUY (undervalued) | -6.7pp (no change) |
| CMBT | $19.15 (no change) | $13.04 (no change) | $10.75 (no change) | $13.36 (no change) | TRIM/SHORT (overvalued) | +33.1pp (no change) |
| SB | $8.37 (no change) | $10.42 (no change) | $9.01 (no change) | $10.72 (no change) | BUY (undervalued) | -30.4pp (no change) |
| LPG | $53.16 (no change) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +16.9pp (no change) |
| BWLP | $24.40 (no change) | $15.48 (no change) | $14.52 (no change) | $15.83 (no change) | TRIM/SHORT (overvalued) | +10.9pp (no change) |
| 2343 | $0.52 (no change) | $0.41 (no change) | $0.37 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +2.9pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._