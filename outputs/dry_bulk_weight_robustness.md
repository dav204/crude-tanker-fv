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
| SB | ⚑ driven | HOLD under Set A/Set C; BUY under Set B |
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
| SBLK | -7.9% (TRIM/SHORT) | -4.7% (HOLD) | -11.4% (TRIM/SHORT) | ⚑ driven | TRIM/SHORT under Set A/Set C; HOLD under Set B |
| GNK | -17.5% (TRIM/SHORT) | -14.3% (TRIM/SHORT) | -21.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | -4.6% (HOLD) | -1.9% (HOLD) | -7.5% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| SB | +3.7% (HOLD) | +7.7% (BUY) | -0.6% (HOLD) | ⚑ driven | HOLD under Set A/Set C; BUY under Set B |
| 2343 | -28.7% (TRIM/SHORT) | -27.1% (TRIM/SHORT) | -30.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Per-name detail

### SBLK — price $31.05, target $34.50

**Classification:** WEIGHT-DRIVEN. TRIM/SHORT under Set A/Set C; HOLD under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $28.59 | -7.9% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $29.58 | -4.7% | HOLD |
| Bulk Set C (China-property-drag bracket) | $27.51 | -11.4% | TRIM/SHORT |

### GNK — price $26.03, target $27.20

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $21.48 | -17.5% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $22.32 | -14.3% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $20.53 | -21.1% | TRIM/SHORT |

### CMDB — price $20.45, target $27.98

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $19.52 | -4.6% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.07 | -1.9% | HOLD |
| Bulk Set C (China-property-drag bracket) | $18.91 | -7.5% | TRIM/SHORT |

### SB — price $8.75, target $7.10

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set C; BUY under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.07 | +3.7% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.43 | +7.7% | BUY |
| Bulk Set C (China-property-drag bracket) | $8.69 | -0.6% | HOLD |

### 2343 — price $0.53, target $0.44

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.38 | -28.7% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.38 | -27.1% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $0.37 | -30.3% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.
