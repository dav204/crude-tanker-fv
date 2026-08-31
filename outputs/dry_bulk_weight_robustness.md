# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ⚑ driven | TRIM/SHORT under Set A/Set C; HOLD under Set B |
| GNK | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| SB | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
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
| SBLK | -5.7% (TRIM/SHORT) | -2.4% (HOLD) | -9.3% (TRIM/SHORT) | ⚑ driven | TRIM/SHORT under Set A/Set C; HOLD under Set B |
| GNK | -16.3% (TRIM/SHORT) | -13.0% (TRIM/SHORT) | -20.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | -4.8% (HOLD) | -2.1% (HOLD) | -7.8% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| SB | +8.4% (BUY) | +12.7% (BUY) | +3.8% (HOLD) | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
| 2343 | -29.2% (TRIM/SHORT) | -27.7% (TRIM/SHORT) | -30.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Per-name detail

### SBLK — price $30.48, target $34.50

**Classification:** WEIGHT-DRIVEN. TRIM/SHORT under Set A/Set C; HOLD under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $28.74 | -5.7% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $29.75 | -2.4% | HOLD |
| Bulk Set C (China-property-drag bracket) | $27.64 | -9.3% | TRIM/SHORT |

### GNK — price $25.88, target $27.20

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $21.66 | -16.3% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $22.52 | -13.0% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $20.69 | -20.1% | TRIM/SHORT |

### CMDB — price $20.52, target $27.98

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $19.53 | -4.8% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.08 | -2.1% | HOLD |
| Bulk Set C (China-property-drag bracket) | $18.91 | -7.8% | TRIM/SHORT |

### SB — price $8.52, target $7.10

**Classification:** WEIGHT-DRIVEN. BUY under Set A/Set B; HOLD under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.23 | +8.4% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.60 | +12.7% | BUY |
| Bulk Set C (China-property-drag bracket) | $8.85 | +3.8% | HOLD |

### 2343 — price $0.53, target $0.44

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.38 | -29.2% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.39 | -27.7% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $0.37 | -30.9% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.
