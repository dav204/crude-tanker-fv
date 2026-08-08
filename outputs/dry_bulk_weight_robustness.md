# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| GNK | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
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
| SBLK | -1.0% (HOLD) | +2.8% (HOLD) | -5.1% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| GNK | -4.9% (HOLD) | -1.1% (HOLD) | -9.2% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| CMDB | +16.8% (BUY) | +20.2% (BUY) | +13.0% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| SB | +24.6% (BUY) | +29.8% (BUY) | +19.0% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| 2343 | -19.9% (TRIM/SHORT) | -18.0% (TRIM/SHORT) | -21.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Per-name detail

### SBLK — price $28.90, target $34.50

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $28.62 | -1.0% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $29.71 | +2.8% | HOLD |
| Bulk Set C (China-property-drag bracket) | $27.44 | -5.1% | TRIM/SHORT |

### GNK — price $25.33, target $24.80

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $24.08 | -4.9% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $25.04 | -1.1% | HOLD |
| Bulk Set C (China-property-drag bracket) | $23.00 | -9.2% | TRIM/SHORT |

### CMDB — price $17.80, target $27.98

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.79 | +16.8% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $21.40 | +20.2% | BUY |
| Bulk Set C (China-property-drag bracket) | $20.11 | +13.0% | BUY |

### SB — price $7.60, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.47 | +24.6% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.87 | +29.8% | BUY |
| Bulk Set C (China-property-drag bracket) | $9.05 | +19.0% | BUY |

### 2343 — price $0.48, target $0.44

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.39 | -19.9% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.40 | -18.0% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $0.38 | -21.9% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.
