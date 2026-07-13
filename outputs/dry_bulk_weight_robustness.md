# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
| GNK | ⚑ driven | TRIM/SHORT under Set A/Set C; HOLD under Set B |
| CMDB | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
| SB | ✓ robust | position BUY across all 3 weight sets |

## Weight sets compared

| Scenario | Set A | Set B | Set C |
|---|--:|--:|--:|
| china_acceleration | 0.20 | 0.30 | 0.12 |
| moderate_growth | 0.40 | 0.40 | 0.33 |
| china_property_drag | 0.25 | 0.18 | 0.35 |
| coordinated_slowdown | 0.15 | 0.12 | 0.20 |

## Summary — per-name robustness

| Ticker | Set A EV | Set B EV | Set C EV | Robustness | Notes |
|---|--:|--:|--:|---|---|
| SBLK | +7.0% (BUY) | +11.1% (BUY) | +2.4% (HOLD) | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
| GNK | -7.7% (TRIM/SHORT) | -3.9% (HOLD) | -11.9% (TRIM/SHORT) | ⚑ driven | TRIM/SHORT under Set A/Set C; HOLD under Set B |
| CMDB | +6.7% (BUY) | +9.9% (BUY) | +3.1% (HOLD) | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
| SB | +42.3% (BUY) | +48.5% (BUY) | +35.7% (BUY) | ✓ robust | position BUY across all 3 weight sets |

## Per-name detail

### SBLK — price $26.35, target $34.50

**Classification:** WEIGHT-DRIVEN. BUY under Set A/Set B; HOLD under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $28.19 | +7.0% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $29.28 | +11.1% | BUY |
| Bulk Set C (China-property-drag bracket) | $26.99 | +2.4% | HOLD |

### GNK — price $25.51, target $24.80

**Classification:** WEIGHT-DRIVEN. TRIM/SHORT under Set A/Set C; HOLD under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $23.56 | -7.7% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $24.52 | -3.9% | HOLD |
| Bulk Set C (China-property-drag bracket) | $22.48 | -11.9% | TRIM/SHORT |

### CMDB — price $19.07, target $27.98

**Classification:** WEIGHT-DRIVEN. BUY under Set A/Set B; HOLD under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.34 | +6.7% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.95 | +9.9% | BUY |
| Bulk Set C (China-property-drag bracket) | $19.67 | +3.1% | HOLD |

### SB — price $6.90, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.82 | +42.3% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $10.25 | +48.5% | BUY |
| Bulk Set C (China-property-drag bracket) | $9.36 | +35.7% | BUY |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.
