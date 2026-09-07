# Crude Weight-Robustness Diagnostic

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Crude Set A weights. Surfaces which crude tanker calls survive defensible reweighting (call is **weight-robust**) vs which depend on a specific weight prior (**weight-driven**).

**Driver:** Catlin / VIE analysis (2026-05-25) plus the June 1 macro briefing suggest current Set A weights may put too much weight on "deep normalisation" relative to "slow normalisation with extended Phase 1." Sets B/C/D bracket the normalisation-speed axis.

**Naming namespace:** the labels below are CRUDE-sector weight families. The LNG sector uses its own "Set B" / "Set B-revised" naming (METHODOLOGY §11.3). Cross-sector conflation would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| DHT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| ECO | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| FRO | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| INSW | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TNK | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| NAT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TEN | ✓ robust | position BUY across all 7 weight sets |
| CMBT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| BRUT | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | ✓ robust | position TRIM/SHORT across all 7 weight sets |

## Weight sets compared

| Scenario | Set A'' | Set A' | Set A | Set B | Set C | Set D | Set E |
|---|--:|--:|--:|--:|--:|--:|--:|
| escalation | 0.25 | 0.25 | 0.25 | 0.10 | 0.15 | 0.05 | 0.10 |
| pre_mou_baseline | 0.62 | 0.57 | 0.45 | 0.25 | 0.30 | 0.10 | 0.20 |
| mou_base | 0.00 | 0.05 | 0.18 | 0.45 | 0.40 | 0.55 | 0.45 |
| mou_bear | 0.13 | 0.13 | 0.12 | 0.20 | 0.15 | 0.30 | 0.25 |

Set B (Catlin-leaning) shifts 10pp from `mou_base` and 5pp from `mou_bear` into `pre_mou_baseline` — i.e. Phase 1 extends, Phase 2 normalisation arrives later. Set C is more bullish (15pp into Phase 1). Set D is more bearish (15pp deeper into MoU phase).

## Summary — per-name robustness

| Ticker | Set A'' EV | Set A' EV | Set A EV | Set B EV | Set C EV | Set D EV | Set E EV | Robustness | Notes |
|---|--:|--:|--:|--:|--:|--:|--:|---|---|
| DHT | -23.5% (TRIM/SHORT) | -23.9% (TRIM/SHORT) | -24.9% (TRIM/SHORT) | -33.4% (TRIM/SHORT) | -30.6% (TRIM/SHORT) | -37.3% (TRIM/SHORT) | -34.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| ECO | -41.6% (TRIM/SHORT) | -42.0% (TRIM/SHORT) | -42.8% (TRIM/SHORT) | -50.9% (TRIM/SHORT) | -48.2% (TRIM/SHORT) | -54.5% (TRIM/SHORT) | -51.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| FRO | -38.7% (TRIM/SHORT) | -39.1% (TRIM/SHORT) | -40.1% (TRIM/SHORT) | -48.9% (TRIM/SHORT) | -46.0% (TRIM/SHORT) | -53.0% (TRIM/SHORT) | -49.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| INSW | -43.0% (TRIM/SHORT) | -43.2% (TRIM/SHORT) | -43.6% (TRIM/SHORT) | -47.9% (TRIM/SHORT) | -46.4% (TRIM/SHORT) | -49.8% (TRIM/SHORT) | -48.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TNK | -10.1% (TRIM/SHORT) | -10.3% (TRIM/SHORT) | -10.8% (TRIM/SHORT) | -16.4% (TRIM/SHORT) | -14.5% (TRIM/SHORT) | -18.8% (TRIM/SHORT) | -16.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| NAT | -58.7% (TRIM/SHORT) | -58.9% (TRIM/SHORT) | -59.5% (TRIM/SHORT) | -65.1% (TRIM/SHORT) | -63.2% (TRIM/SHORT) | -67.5% (TRIM/SHORT) | -65.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TEN | +43.3% (BUY) | +42.8% (BUY) | +41.9% (BUY) | +32.0% (BUY) | +35.2% (BUY) | +27.6% (BUY) | +31.3% (BUY) | ✓ robust | position BUY across all 7 weight sets |
| CMBT | -30.0% (TRIM/SHORT) | -30.1% (TRIM/SHORT) | -30.5% (TRIM/SHORT) | -34.2% (TRIM/SHORT) | -33.0% (TRIM/SHORT) | -35.9% (TRIM/SHORT) | -34.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| BRUT | +1.9% (HOLD) | +0.7% (HOLD) | -2.1% (HOLD) | -24.5% (TRIM/SHORT) | -17.1% (TRIM/SHORT) | -35.1% (TRIM/SHORT) | -26.5% (TRIM/SHORT) | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | -5.1% (TRIM/SHORT) | -5.9% (TRIM/SHORT) | -7.8% (TRIM/SHORT) | -22.7% (TRIM/SHORT) | -17.8% (TRIM/SHORT) | -29.9% (TRIM/SHORT) | -24.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |

## Per-name detail

### DHT — price $20.87, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $15.97 | -23.5% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $15.88 | -23.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.67 | -24.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.91 | -33.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.49 | -30.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.08 | -37.3% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.76 | -34.1% | TRIM/SHORT |

### ECO — price $71.43, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $41.71 | -41.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $41.44 | -42.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $40.83 | -42.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $35.10 | -50.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $37.00 | -48.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $32.49 | -54.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $34.66 | -51.5% | TRIM/SHORT |

### FRO — price $46.12, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $28.29 | -38.7% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $28.09 | -39.1% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $27.63 | -40.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $23.57 | -48.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $24.92 | -46.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $21.68 | -53.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $23.23 | -49.6% | TRIM/SHORT |

### INSW — price $104.50, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $59.59 | -43.0% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $59.39 | -43.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $58.96 | -43.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $54.49 | -47.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $55.97 | -46.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $52.51 | -49.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $54.18 | -48.2% | TRIM/SHORT |

### TNK — price $93.37, target $75.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $83.93 | -10.1% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $83.72 | -10.3% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $83.25 | -10.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $78.07 | -16.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $79.79 | -14.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $75.77 | -18.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $77.71 | -16.8% | TRIM/SHORT |

### NAT — price $7.25, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $3.00 | -58.7% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $2.98 | -58.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $2.94 | -59.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.53 | -65.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.67 | -63.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.35 | -67.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.51 | -65.4% | TRIM/SHORT |

### TEN — price $43.74, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $62.66 | +43.3% | BUY |
| Crude Set A' (B' reweight, history bracket) | $62.47 | +42.8% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $62.05 | +41.9% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $57.72 | +32.0% | BUY |
| Crude Set C (bullish, extended Phase 1) | $59.15 | +35.2% | BUY |
| Crude Set D (bearish, deep normalization) | $55.81 | +27.6% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $57.42 | +31.3% | BUY |

### CMBT — price $19.49, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $13.65 | -30.0% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $13.62 | -30.1% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $13.54 | -30.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $12.82 | -34.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.06 | -33.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.49 | -35.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $12.76 | -34.5% | TRIM/SHORT |

### BRUT — price $5.03, target $4.56

**Classification:** WEIGHT-DRIVEN. HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $5.12 | +1.9% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $5.06 | +0.7% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $4.92 | -2.1% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $3.80 | -24.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.17 | -17.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $3.26 | -35.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $3.70 | -26.5% | TRIM/SHORT |

### CAPT — price $18.51, target $18.90

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $17.56 | -5.1% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $17.41 | -5.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $17.07 | -7.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.30 | -22.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $15.22 | -17.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.98 | -29.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $14.05 | -24.1% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
