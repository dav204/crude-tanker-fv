# Crude Weight-Robustness Diagnostic

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Crude Set A weights. Surfaces which crude tanker calls survive defensible reweighting (call is **weight-robust**) vs which depend on a specific weight prior (**weight-driven**).

**Driver:** Catlin / VIE analysis (2026-05-25) plus the June 1 macro briefing suggest current Set A weights may put too much weight on "deep normalisation" relative to "slow normalisation with extended Phase 1." Sets B/C/D bracket the normalisation-speed axis.

**Naming namespace:** the labels below are CRUDE-sector weight families. The LNG sector uses its own "Set B" / "Set B-revised" naming (METHODOLOGY §11.3). Cross-sector conflation would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| DHT | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| ECO | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| FRO | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| INSW | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| TNK | ⚑ driven | HOLD under Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D |
| NAT | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| TEN | ✓ robust | position BUY across all 6 weight sets |
| CMBT | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| BRUT | ⚑ driven | HOLD under Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | ⚑ driven | HOLD under Set A'; TRIM/SHORT under Set A/Set B/Set C/Set D/Set E |

## Weight sets compared

| Scenario | Set A' | Set A | Set B | Set C | Set D | Set E |
|---|--:|--:|--:|--:|--:|--:|
| escalation | 0.25 | 0.25 | 0.10 | 0.15 | 0.05 | 0.10 |
| pre_mou_baseline | 0.57 | 0.45 | 0.25 | 0.30 | 0.10 | 0.20 |
| mou_base | 0.05 | 0.18 | 0.45 | 0.40 | 0.55 | 0.45 |
| mou_bear | 0.13 | 0.12 | 0.20 | 0.15 | 0.30 | 0.25 |

Set B (Catlin-leaning) shifts 10pp from `mou_base` and 5pp from `mou_bear` into `pre_mou_baseline` — i.e. Phase 1 extends, Phase 2 normalisation arrives later. Set C is more bullish (15pp into Phase 1). Set D is more bearish (15pp deeper into MoU phase).

## Summary — per-name robustness

| Ticker | Set A' EV | Set A EV | Set B EV | Set C EV | Set D EV | Set E EV | Robustness | Notes |
|---|--:|--:|--:|--:|--:|--:|---|---|
| DHT | -22.8% (TRIM/SHORT) | -23.6% (TRIM/SHORT) | -33.8% (TRIM/SHORT) | -30.4% (TRIM/SHORT) | -38.2% (TRIM/SHORT) | -34.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| ECO | -39.7% (TRIM/SHORT) | -40.4% (TRIM/SHORT) | -50.3% (TRIM/SHORT) | -47.0% (TRIM/SHORT) | -54.5% (TRIM/SHORT) | -50.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| FRO | -39.0% (TRIM/SHORT) | -39.9% (TRIM/SHORT) | -51.5% (TRIM/SHORT) | -47.6% (TRIM/SHORT) | -56.4% (TRIM/SHORT) | -52.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| INSW | -39.8% (TRIM/SHORT) | -40.2% (TRIM/SHORT) | -45.4% (TRIM/SHORT) | -43.7% (TRIM/SHORT) | -47.6% (TRIM/SHORT) | -45.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| TNK | +3.4% (HOLD) | +2.9% (HOLD) | -4.3% (HOLD) | -1.9% (HOLD) | -7.3% (TRIM/SHORT) | -4.7% (HOLD) | ⚑ driven | HOLD under Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D |
| NAT | -56.8% (TRIM/SHORT) | -57.3% (TRIM/SHORT) | -64.2% (TRIM/SHORT) | -62.0% (TRIM/SHORT) | -67.1% (TRIM/SHORT) | -64.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| TEN | +46.0% (BUY) | +45.3% (BUY) | +32.9% (BUY) | +37.0% (BUY) | +28.0% (BUY) | +32.4% (BUY) | ✓ robust | position BUY across all 6 weight sets |
| CMBT | -14.9% (TRIM/SHORT) | -15.3% (TRIM/SHORT) | -20.0% (TRIM/SHORT) | -18.4% (TRIM/SHORT) | -22.0% (TRIM/SHORT) | -20.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| BRUT | +1.3% (HOLD) | -2.6% (HOLD) | -48.0% (TRIM/SHORT) | -32.9% (TRIM/SHORT) | -67.6% (TRIM/SHORT) | -50.8% (TRIM/SHORT) | ⚑ driven | HOLD under Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | -3.9% (HOLD) | -5.6% (TRIM/SHORT) | -26.5% (TRIM/SHORT) | -19.6% (TRIM/SHORT) | -35.3% (TRIM/SHORT) | -27.7% (TRIM/SHORT) | ⚑ driven | HOLD under Set A'; TRIM/SHORT under Set A/Set B/Set C/Set D/Set E |

## Per-name detail

### DHT — price $18.76, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $14.48 | -22.8% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $14.33 | -23.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $12.41 | -33.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.05 | -30.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $11.60 | -38.2% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $12.30 | -34.4% | TRIM/SHORT |

### ECO — price $61.86, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $37.31 | -39.7% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $36.84 | -40.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $30.72 | -50.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $32.76 | -47.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $28.15 | -54.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $30.39 | -50.9% | TRIM/SHORT |

### FRO — price $39.74, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $24.22 | -39.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $23.86 | -39.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $19.28 | -51.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $20.81 | -47.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $17.34 | -56.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $19.02 | -52.1% | TRIM/SHORT |

### INSW — price $92.41, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $55.59 | -39.8% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $55.24 | -40.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $50.44 | -45.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $52.03 | -43.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $48.45 | -47.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $50.19 | -45.7% | TRIM/SHORT |

### TNK — price $77.25, target $75.00

**Classification:** WEIGHT-DRIVEN. HOLD under Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $79.87 | +3.4% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $79.51 | +2.9% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $73.90 | -4.3% | HOLD |
| Crude Set C (bullish, extended Phase 1) | $75.77 | -1.9% | HOLD |
| Crude Set D (bearish, deep normalization) | $71.59 | -7.3% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $73.62 | -4.7% | HOLD |

### NAT — price $6.46, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $2.79 | -56.8% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $2.76 | -57.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.31 | -64.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.46 | -62.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.13 | -67.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.29 | -64.6% | TRIM/SHORT |

### TEN — price $39.14, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $57.16 | +46.0% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $56.89 | +45.3% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $52.02 | +32.9% | BUY |
| Crude Set C (bullish, extended Phase 1) | $53.63 | +37.0% | BUY |
| Crude Set D (bearish, deep normalization) | $50.11 | +28.0% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $51.84 | +32.4% | BUY |

### CMBT — price $16.29, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $13.86 | -14.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $13.80 | -15.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.03 | -20.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.29 | -18.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.70 | -22.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $12.99 | -20.3% | TRIM/SHORT |

### BRUT — price $6.41, target $7.13

**Classification:** WEIGHT-DRIVEN. HOLD under Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $6.49 | +1.3% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $6.24 | -2.6% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $3.33 | -48.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.30 | -32.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.08 | -67.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $3.15 | -50.8% | TRIM/SHORT |

### CAPT — price $13.94, target $18.90

**Classification:** WEIGHT-DRIVEN. HOLD under Set A'; TRIM/SHORT under Set A/Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $13.39 | -3.9% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $13.16 | -5.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $10.24 | -26.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $11.20 | -19.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $9.02 | -35.3% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $10.08 | -27.7% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
