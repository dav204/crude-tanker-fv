# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ⚑ driven | HOLD under Set A/Set C; BUY under Set B |
| GNK | ⚑ driven | TRIM/SHORT under Set A/Set C; HOLD under Set B |
| CMDB | ⚑ driven | HOLD under Set A/Set C; BUY under Set B |
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
| SBLK | +4.3% (HOLD) | +8.3% (BUY) | -0.1% (HOLD) | ⚑ driven | HOLD under Set A/Set C; BUY under Set B |
| GNK | -8.7% (TRIM/SHORT) | -5.0% (HOLD) | -12.8% (TRIM/SHORT) | ⚑ driven | TRIM/SHORT under Set A/Set C; HOLD under Set B |
| CMDB | +2.8% (HOLD) | +5.8% (BUY) | -0.6% (HOLD) | ⚑ driven | HOLD under Set A/Set C; BUY under Set B |
| SB | +37.4% (BUY) | +43.4% (BUY) | +31.0% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| 2343 | -3.2% (HOLD) | -1.0% (HOLD) | -5.6% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |

## Per-name detail

### SBLK — price $26.54, target $34.50

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set C; BUY under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $27.69 | +4.3% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $28.75 | +8.3% | BUY |
| Bulk Set C (China-property-drag bracket) | $26.53 | -0.1% | HOLD |

### GNK — price $25.35, target $24.80

**Classification:** WEIGHT-DRIVEN. TRIM/SHORT under Set A/Set C; HOLD under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $23.15 | -8.7% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $24.09 | -5.0% | HOLD |
| Bulk Set C (China-property-drag bracket) | $22.11 | -12.8% | TRIM/SHORT |

### CMDB — price $19.56, target $27.98

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set C; BUY under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.10 | +2.8% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.70 | +5.8% | BUY |
| Bulk Set C (China-property-drag bracket) | $19.44 | -0.6% | HOLD |

### SB — price $6.96, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.56 | +37.4% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.98 | +43.4% | BUY |
| Bulk Set C (China-property-drag bracket) | $9.12 | +31.0% | BUY |

### 2343 — price $0.39, target $0.44

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.38 | -3.2% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.39 | -1.0% | HOLD |
| Bulk Set C (China-property-drag bracket) | $0.37 | -5.6% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.
