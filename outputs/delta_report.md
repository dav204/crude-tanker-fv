# Pipeline Delta Report

- **This run:** 2026-09-10T13:39:08+00:00
- **Previous run:** 2026-09-10T13:37:05+00:00

## Headline changes (material moves)

- **No material changes.** All tickers within thresholds (|ΔFV%|≤10%, |Δspread|≤5pp, |ΔNAV%|≤5%) and no position flips.

## §17 read-flip strobe — tape vs the flip boundary

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (cheap/fair) | $23.48 | $24.33 | parity · fair\|rich | -3.48% | +6.96% (@ $17.25) | clear of the deadband |
| GNK | flips (cheap/fair) | $27.14 | $28.40 | hist · fair\|rich | -4.43% | -0.29% (@ $25.80) | clear of the deadband |
| SBLK | flips (cheap/fair) | $31.16 | $33.22 | parity · cheap\|fair | -6.20% | -8.48% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- _(no input file changes detected — hashes match)_

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $21.20 (no change) | $15.26 (no change) | $16.12 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +15.4pp (no change) |
| ECO | $71.67 (no change) | $39.87 (no change) | $41.50 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +11.5pp (no change) |
| FRO | $47.21 (no change) | $26.71 (no change) | $28.30 (no change) | $26.04 (no change) | TRIM/SHORT (overvalued) | +18.1pp (no change) |
| INSW | $104.62 (no change) | $37.95 (no change) | $59.32 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +27.4pp (no change) |
| TNK | $96.31 (no change) | $84.12 (no change) | $82.48 (no change) | $84.60 (no change) | TRIM/SHORT (overvalued) | +18.7pp (no change) |
| NAT | $7.27 (no change) | $2.95 (no change) | $2.91 (no change) | $2.76 (no change) | TRIM/SHORT (overvalued) | +67.6pp (no change) |
| FLNG | $31.14 (no change) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -16.7pp (no change) |
| CCEC | $22.60 (no change) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -2.5pp (no change) |
| STNG | $83.06 (no change) | $72.66 (no change) | $75.97 (no change) | $76.22 (no change) | TRIM/SHORT (overvalued) | +41.5pp (no change) |
| HAFN | $9.16 (no change) | $4.92 (no change) | $5.47 (no change) | $4.64 (no change) | TRIM/SHORT (overvalued) | +42.7pp (no change) |
| TRMD | $35.46 (no change) | $32.62 (no change) | $35.14 (no change) | $32.30 (no change) | HOLD (fairly valued) | +16.1pp (no change) |
| ASC | $18.23 (no change) | $17.26 (no change) | $16.28 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +32.3pp (no change) |
| TEN | $44.32 (no change) | $59.49 (no change) | $61.17 (no change) | $88.16 (no change) | BUY (undervalued) | +58.6pp (no change) |
| CMDB | $23.48 (no change) | $21.83 (no change) | $19.52 (no change) | $32.60 (no change) | TRIM/SHORT (overvalued) | +12.3pp (no change) |
| SBLK | $31.16 (no change) | $32.67 (no change) | $28.59 (no change) | $33.27 (no change) | TRIM/SHORT (overvalued) | +2.4pp (no change) |
| GNK | $27.14 (no change) | $25.41 (no change) | $21.48 (no change) | $25.37 (no change) | TRIM/SHORT (overvalued) | +9.1pp (no change) |
| CAPT | $19.11 (no change) | $17.09 (no change) | $17.46 (no change) | $17.32 (no change) | TRIM/SHORT (overvalued) | +44.5pp (no change) |
| MPCC | $2.94 (no change) | $2.29 (no change) | $2.13 (no change) | $2.10 (no change) | TRIM/SHORT (overvalued) | +19.2pp (no change) |
| GSL | $45.02 (no change) | $44.04 (no change) | $42.82 (no change) | $41.20 (no change) | HOLD (fairly valued) | +32.5pp (no change) |
| BRUT | $5.07 (no change) | $4.71 (no change) | $5.23 (no change) | $4.92 (no change) | HOLD (fairly valued) | +0.0pp (no change) |
| CMBT | $19.35 (no change) | $15.98 (no change) | $13.58 (no change) | $16.54 (no change) | TRIM/SHORT (overvalued) | +24.6pp (no change) |
| SB | $8.36 (no change) | $10.42 (no change) | $9.07 (no change) | $10.72 (no change) | BUY (undervalued) | -32.0pp (no change) |
| LPG | $53.63 (no change) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +23.1pp (no change) |
| BWLP | $24.15 (no change) | $15.48 (no change) | $14.52 (no change) | $15.83 (no change) | TRIM/SHORT (overvalued) | +11.0pp (no change) |
| 2343 | $0.54 (no change) | $0.41 (no change) | $0.38 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +4.0pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._