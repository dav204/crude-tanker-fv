# Crude Weight-Robustness Diagnostic

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Crude Set A weights. Surfaces which crude tanker calls survive defensible reweighting (call is **weight-robust**) vs which depend on a specific weight prior (**weight-driven**).

**Driver:** Catlin / VIE analysis (2026-05-25) plus the June 1 macro briefing suggest current Set A weights may put too much weight on "deep normalisation" relative to "slow normalisation with extended Phase 1." Sets B/C/D bracket the normalisation-speed axis.

**Naming namespace:** the labels below are CRUDE-sector weight families. The LNG sector uses its own "Set B" / "Set B-revised" naming (METHODOLOGY §11.3). Cross-sector conflation would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| DHT | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| ECO | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| FRO | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| INSW | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TNK | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| NAT | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TEN | ✓ robust | position BUY across all 8 weight sets |
| CMBT | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| BRUT | ⚑ driven | BUY under Set A'''/Set A''/Set A'; HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | ⚑ driven | HOLD under Set A'''/Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

## Weight sets compared

| Scenario | Set A''' | Set A'' | Set A' | Set A | Set B | Set C | Set D | Set E |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| escalation | 0.28 | 0.25 | 0.25 | 0.25 | 0.10 | 0.15 | 0.05 | 0.10 |
| pre_mou_baseline | 0.59 | 0.62 | 0.57 | 0.45 | 0.25 | 0.30 | 0.10 | 0.20 |
| mou_base | 0.00 | 0.00 | 0.05 | 0.18 | 0.45 | 0.40 | 0.55 | 0.45 |
| mou_bear | 0.13 | 0.13 | 0.13 | 0.12 | 0.20 | 0.15 | 0.30 | 0.25 |

Set B (Catlin-leaning) shifts 10pp from `mou_base` and 5pp from `mou_bear` into `pre_mou_baseline` — i.e. Phase 1 extends, Phase 2 normalisation arrives later. Set C is more bullish (15pp into Phase 1). Set D is more bearish (15pp deeper into MoU phase).

## Summary — per-name robustness

| Ticker | Set A''' EV | Set A'' EV | Set A' EV | Set A EV | Set B EV | Set C EV | Set D EV | Set E EV | Robustness | Notes |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| DHT | -22.2% (TRIM/SHORT) | -23.1% (TRIM/SHORT) | -23.5% (TRIM/SHORT) | -24.3% (TRIM/SHORT) | -32.2% (TRIM/SHORT) | -29.5% (TRIM/SHORT) | -36.1% (TRIM/SHORT) | -33.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| ECO | -43.3% (TRIM/SHORT) | -44.1% (TRIM/SHORT) | -44.5% (TRIM/SHORT) | -45.3% (TRIM/SHORT) | -52.5% (TRIM/SHORT) | -50.0% (TRIM/SHORT) | -56.0% (TRIM/SHORT) | -53.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| FRO | -38.2% (TRIM/SHORT) | -39.2% (TRIM/SHORT) | -39.6% (TRIM/SHORT) | -40.5% (TRIM/SHORT) | -48.8% (TRIM/SHORT) | -46.0% (TRIM/SHORT) | -52.8% (TRIM/SHORT) | -49.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| INSW | -39.4% (TRIM/SHORT) | -39.9% (TRIM/SHORT) | -40.1% (TRIM/SHORT) | -40.6% (TRIM/SHORT) | -45.0% (TRIM/SHORT) | -43.5% (TRIM/SHORT) | -47.1% (TRIM/SHORT) | -45.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TNK | -7.3% (TRIM/SHORT) | -7.9% (TRIM/SHORT) | -8.2% (TRIM/SHORT) | -8.9% (TRIM/SHORT) | -14.6% (TRIM/SHORT) | -12.6% (TRIM/SHORT) | -17.5% (TRIM/SHORT) | -15.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| NAT | -57.6% (TRIM/SHORT) | -58.2% (TRIM/SHORT) | -58.4% (TRIM/SHORT) | -59.1% (TRIM/SHORT) | -64.6% (TRIM/SHORT) | -62.7% (TRIM/SHORT) | -67.3% (TRIM/SHORT) | -65.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TEN | +45.1% (BUY) | +44.1% (BUY) | +43.5% (BUY) | +42.1% (BUY) | +32.0% (BUY) | +35.5% (BUY) | +26.8% (BUY) | +30.8% (BUY) | ✓ robust | position BUY across all 8 weight sets |
| CMBT | -43.4% (TRIM/SHORT) | -43.9% (TRIM/SHORT) | -44.0% (TRIM/SHORT) | -44.5% (TRIM/SHORT) | -48.2% (TRIM/SHORT) | -46.9% (TRIM/SHORT) | -50.1% (TRIM/SHORT) | -48.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| BRUT | +8.4% (BUY) | +6.2% (BUY) | +5.1% (BUY) | +2.5% (HOLD) | -18.5% (TRIM/SHORT) | -11.3% (TRIM/SHORT) | -29.0% (TRIM/SHORT) | -20.7% (TRIM/SHORT) | ⚑ driven | BUY under Set A'''/Set A''/Set A'; HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | +0.7% (HOLD) | -0.8% (HOLD) | -1.7% (HOLD) | -3.5% (HOLD) | -18.1% (TRIM/SHORT) | -13.2% (TRIM/SHORT) | -25.7% (TRIM/SHORT) | -19.8% (TRIM/SHORT) | ⚑ driven | HOLD under Set A'''/Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

## Per-name detail

### DHT — price $21.28, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $16.56 | -22.2% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $16.37 | -23.1% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $16.29 | -23.5% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $16.10 | -24.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.42 | -32.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.99 | -29.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.59 | -36.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $14.25 | -33.0% | TRIM/SHORT |

### ECO — price $77.91, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $44.15 | -43.3% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $43.53 | -44.1% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $43.24 | -44.5% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $42.61 | -45.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $37.02 | -52.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $38.92 | -50.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $34.26 | -56.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $36.44 | -53.2% | TRIM/SHORT |

### FRO — price $47.56, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $29.38 | -38.2% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $28.92 | -39.2% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $28.73 | -39.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $28.30 | -40.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $24.36 | -48.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $25.70 | -46.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $22.43 | -52.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $23.97 | -49.6% | TRIM/SHORT |

### INSW — price $102.05, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $61.81 | -39.4% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $61.31 | -39.9% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $61.09 | -40.1% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $60.60 | -40.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $56.17 | -45.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $57.68 | -43.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $54.00 | -47.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $55.73 | -45.4% | TRIM/SHORT |

### TNK — price $94.54, target $75.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $87.59 | -7.3% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $87.05 | -7.9% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $86.75 | -8.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $86.09 | -8.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $80.76 | -14.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $82.58 | -12.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $78.02 | -17.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $80.14 | -15.2% | TRIM/SHORT |

### NAT — price $7.62, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $3.24 | -57.6% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $3.19 | -58.2% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $3.17 | -58.4% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $3.12 | -59.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.70 | -64.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.84 | -62.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.49 | -67.3% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.66 | -65.2% | TRIM/SHORT |

### TEN — price $46.97, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $68.15 | +45.1% | BUY |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $67.69 | +44.1% | BUY |
| Crude Set A' (B' reweight, history bracket) | $67.40 | +43.5% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $66.75 | +42.1% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $62.01 | +32.0% | BUY |
| Crude Set C (bullish, extended Phase 1) | $63.62 | +35.5% | BUY |
| Crude Set D (bearish, deep normalization) | $59.55 | +26.8% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $61.45 | +30.8% | BUY |

### CMBT — price $19.15, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $10.83 | -43.4% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $10.75 | -43.9% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $10.71 | -44.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $10.63 | -44.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $9.92 | -48.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $10.16 | -46.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $9.56 | -50.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $9.84 | -48.6% | TRIM/SHORT |

### BRUT — price $5.08, target $4.56

**Classification:** WEIGHT-DRIVEN. BUY under Set A'''/Set A''/Set A'; HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $5.51 | +8.4% | BUY |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $5.40 | +6.2% | BUY |
| Crude Set A' (B' reweight, history bracket) | $5.34 | +5.1% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $5.21 | +2.5% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $4.14 | -18.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.51 | -11.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $3.61 | -29.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $4.03 | -20.7% | TRIM/SHORT |

### CAPT — price $18.45, target $18.90

**Classification:** WEIGHT-DRIVEN. HOLD under Set A'''/Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $18.57 | +0.7% | HOLD |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $18.30 | -0.8% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $18.14 | -1.7% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $17.80 | -3.5% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $15.10 | -18.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $16.02 | -13.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.72 | -25.7% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $14.79 | -19.8% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
