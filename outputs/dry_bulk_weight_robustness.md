# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ✓ robust | position BUY across all 3 weight sets |
| GNK | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| CMDB | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
| SB | ✓ robust | position BUY across all 3 weight sets |
| 2343 | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |

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
| SBLK | +11.2% (BUY) | +15.5% (BUY) | +6.5% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| GNK | -4.0% (HOLD) | -0.1% (HOLD) | -8.4% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| CMDB | +6.8% (BUY) | +10.0% (BUY) | +3.3% (HOLD) | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
| SB | +40.2% (BUY) | +46.3% (BUY) | +33.7% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| 2343 | -4.6% (HOLD) | -2.4% (HOLD) | -6.9% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |

## Per-name detail

### SBLK — price $24.90, target $34.50

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $27.69 | +11.2% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $28.75 | +15.5% | BUY |
| Bulk Set C (China-property-drag bracket) | $26.53 | +6.5% | BUY |

### GNK — price $24.12, target $24.80

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $23.15 | -4.0% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $24.09 | -0.1% | HOLD |
| Bulk Set C (China-property-drag bracket) | $22.11 | -8.4% | TRIM/SHORT |

### CMDB — price $18.81, target $27.98

**Classification:** WEIGHT-DRIVEN. BUY under Set A/Set B; HOLD under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.10 | +6.8% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.70 | +10.0% | BUY |
| Bulk Set C (China-property-drag bracket) | $19.44 | +3.3% | HOLD |

### SB — price $6.82, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.56 | +40.2% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.98 | +46.3% | BUY |
| Bulk Set C (China-property-drag bracket) | $9.12 | +33.7% | BUY |

### 2343 — price $0.40, target $0.44

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.38 | -4.6% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.39 | -2.4% | HOLD |
| Bulk Set C (China-property-drag bracket) | $0.37 | -6.9% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.
