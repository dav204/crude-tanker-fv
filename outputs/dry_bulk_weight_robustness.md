# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ✓ robust | position HOLD across all 3 weight sets |
| GNK | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | ✓ robust | position BUY across all 3 weight sets |
| SB | ✓ robust | position BUY across all 3 weight sets |
| 2343 | ✓ robust | position TRIM/SHORT across all 3 weight sets |

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
| SBLK | +0.2% (HOLD) | +4.0% (HOLD) | -4.0% (HOLD) | ✓ robust | position HOLD across all 3 weight sets |
| GNK | -11.6% (TRIM/SHORT) | -8.1% (TRIM/SHORT) | -15.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | +8.6% (BUY) | +11.9% (BUY) | +5.1% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| SB | +22.9% (BUY) | +28.2% (BUY) | +17.1% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| 2343 | -9.0% (TRIM/SHORT) | -6.9% (TRIM/SHORT) | -11.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Per-name detail

### SBLK — price $28.14, target $34.50

**Classification:** WEIGHT-ROBUST. position HOLD across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $28.19 | +0.2% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $29.26 | +4.0% | HOLD |
| Bulk Set C (China-property-drag bracket) | $27.01 | -4.0% | HOLD |

### GNK — price $26.77, target $24.80

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $23.66 | -11.6% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $24.61 | -8.1% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $22.60 | -15.6% | TRIM/SHORT |

### CMDB — price $18.84, target $27.98

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.47 | +8.6% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $21.07 | +11.9% | BUY |
| Bulk Set C (China-property-drag bracket) | $19.80 | +5.1% | BUY |

### SB — price $7.67, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.42 | +22.9% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.83 | +28.2% | BUY |
| Bulk Set C (China-property-drag bracket) | $8.99 | +17.1% | BUY |

### 2343 — price $0.42, target $0.44

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.38 | -9.0% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.39 | -6.9% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $0.37 | -11.3% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.
