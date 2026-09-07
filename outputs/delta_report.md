# Pipeline Delta Report

- **This run:** 2026-09-07T20:16:43+00:00
- **Previous run:** 2026-09-07T20:11:53+00:00

## Headline changes (material moves)

- **CMDB:** position BUY (undervalued) → TRIM/SHORT (overvalued); broker spread +28.9pp

## §17 read-flip strobe — tape vs the flip boundary

> ⚡ **STROBE ZONE — 1 name(s) inside the ±2.0% deadband at the tape: CMDB (-1.55%).** The governed `read_flag` holds its state on the watchlist vintage, but at today's close the read sits close enough to its settling boundary that the next vintage rebase could restate it — and `read_flag` caps position size. This is the hazard the deadband exists for: surfaced, not acted on.

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (cheap/fair) | $23.95 | $24.33 | parity · fair\|rich | **-1.55%** | +6.96% (@ $17.25) | ⚡ inside ±2.0% deadband |
| GNK | flips (cheap/fair) | $27.65 | $28.40 | hist · fair\|rich | -2.63% | -0.29% (@ $25.80) | clear of the deadband |
| SBLK | flips (cheap/fair) | $32.42 | $33.22 | parity · cheap\|fair | -2.40% | -8.48% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/notify.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $20.87 (no change) | $15.32 (no change) | $15.97 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +14.2pp (no change) |
| ECO | $71.43 (no change) | $39.73 (no change) | $41.71 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +11.4pp (no change) |
| FRO | $46.12 (no change) | $26.58 (no change) | $28.29 (no change) | $26.04 (no change) | TRIM/SHORT (overvalued) | +16.9pp (no change) |
| INSW | $104.50 (no change) | $37.59 (no change) | $59.59 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +27.5pp (no change) |
| TNK | $93.37 (no change) | $83.23 (no change) | $83.93 (no change) | $84.60 (no change) | TRIM/SHORT (overvalued) | +16.9pp (no change) |
| NAT | $7.25 (no change) | $2.89 (no change) | $3.00 (no change) | $2.76 (no change) | TRIM/SHORT (overvalued) | +69.4pp (no change) |
| FLNG | $31.51 (no change) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -15.7pp (no change) |
| CCEC | $22.65 (no change) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -2.2pp (no change) |
| STNG | $82.35 (no change) | $72.23 (no change) | $76.73 (no change) | $76.22 (no change) | TRIM/SHORT (overvalued) | +41.3pp (no change) |
| HAFN | $9.22 (no change) | $4.83 (no change) | $5.59 (no change) | $4.64 (no change) | TRIM/SHORT (overvalued) | +43.9pp (no change) |
| TRMD | $35.18 (no change) | $32.14 (no change) | $35.79 (no change) | $32.30 (no change) | HOLD (fairly valued) | +15.7pp (no change) |
| ASC | $18.17 (no change) | $17.22 (no change) | $16.38 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +32.3pp (no change) |
| TEN | $43.74 (no change) | $59.21 (no change) | $62.66 (no change) | $88.16 (no change) | BUY (undervalued) | +58.1pp (no change) |
| CMDB ⚑ | $23.95 (+6.70) | $21.83 (no change) | $19.52 (no change) | $32.60 (no change) | TRIM/SHORT (overvalued) ⟵ | +13.8pp (+28.9pp) |
| SBLK | $32.42 (no change) | $32.67 (no change) | $28.59 (no change) | $33.27 (no change) | TRIM/SHORT (overvalued) | +5.7pp (no change) |
| GNK | $27.65 (no change) | $25.41 (no change) | $21.48 (no change) | $25.37 (no change) | TRIM/SHORT (overvalued) | +10.4pp (no change) |
| CAPT | $18.51 (no change) | $16.95 (no change) | $17.56 (no change) | $17.32 (no change) | TRIM/SHORT (overvalued) | +41.9pp (no change) |
| MPCC | $2.90 (no change) | $2.29 (no change) | $2.15 (no change) | $2.10 (no change) | TRIM/SHORT (overvalued) | +18.6pp (no change) |
| GSL | $46.40 (no change) | $44.02 (no change) | $42.88 (no change) | $41.20 (no change) | TRIM/SHORT (overvalued) | +34.7pp (no change) |
| BRUT | $5.03 (no change) | $4.70 (no change) | $5.12 (no change) | $4.92 (no change) | HOLD (fairly valued) | -0.7pp (no change) |
| CMBT | $19.49 (no change) | $15.94 (no change) | $13.65 (no change) | $16.54 (no change) | TRIM/SHORT (overvalued) | +25.1pp (no change) |
| SB | $9.17 (no change) | $10.42 (no change) | $9.07 (no change) | $10.72 (no change) | HOLD (fairly valued) | -22.9pp (no change) |
| LPG | $55.20 (no change) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +24.7pp (no change) |
| BWLP | $23.69 (no change) | $15.48 (no change) | $14.52 (no change) | $15.83 (no change) | TRIM/SHORT (overvalued) | +9.9pp (no change) |
| 2343 | $0.54 (no change) | $0.41 (no change) | $0.38 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +4.0pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._