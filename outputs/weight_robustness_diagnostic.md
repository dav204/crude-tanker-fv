# Crude Weight-Robustness Diagnostic

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Crude Set A weights. Surfaces which crude tanker calls survive defensible reweighting (call is **weight-robust**) vs which depend on a specific weight prior (**weight-driven**).

**Driver:** Catlin / VIE analysis (2026-05-25) plus the June 1 macro briefing suggest current Set A weights may put too much weight on "deep normalisation" relative to "slow normalisation with extended Phase 1." Sets B/C/D bracket the normalisation-speed axis.

**Naming namespace:** the labels below are CRUDE-sector weight families. The LNG sector uses its own "Set B" / "Set B-revised" naming (METHODOLOGY §11.3). Cross-sector conflation would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| DHT | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| ECO | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| FRO | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| INSW | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TNK | ⚑ driven | HOLD under Set A/Set C; TRIM/SHORT under Set B/Set D/Set E |
| NAT | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TEN | ✓ robust | position BUY across all 5 weight sets |
| CMBT | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| BRUT | ⚑ driven | BUY under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | ⚑ driven | HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

## Weight sets compared

| Scenario | Set A | Set B | Set C | Set D | Set E |
|---|--:|--:|--:|--:|--:|
| escalation | 0.25 | 0.10 | 0.15 | 0.05 | 0.10 |
| pre_mou_baseline | 0.45 | 0.25 | 0.30 | 0.10 | 0.20 |
| mou_base | 0.18 | 0.45 | 0.40 | 0.55 | 0.45 |
| mou_bear | 0.12 | 0.20 | 0.15 | 0.30 | 0.25 |

Set B (Catlin-leaning) shifts 10pp from `mou_base` and 5pp from `mou_bear` into `pre_mou_baseline` — i.e. Phase 1 extends, Phase 2 normalisation arrives later. Set C is more bullish (15pp into Phase 1). Set D is more bearish (15pp deeper into MoU phase).

## Summary — per-name robustness

| Ticker | Set A EV | Set B EV | Set C EV | Set D EV | Set E EV | Robustness | Notes |
|---|--:|--:|--:|--:|--:|---|---|
| DHT | -24.9% (TRIM/SHORT) | -35.5% (TRIM/SHORT) | -32.0% (TRIM/SHORT) | -40.0% (TRIM/SHORT) | -36.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| ECO | -41.6% (TRIM/SHORT) | -52.6% (TRIM/SHORT) | -48.9% (TRIM/SHORT) | -57.2% (TRIM/SHORT) | -53.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| FRO | -39.9% (TRIM/SHORT) | -51.7% (TRIM/SHORT) | -47.8% (TRIM/SHORT) | -56.7% (TRIM/SHORT) | -52.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| INSW | -40.2% (TRIM/SHORT) | -45.5% (TRIM/SHORT) | -43.7% (TRIM/SHORT) | -47.7% (TRIM/SHORT) | -45.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TNK | +1.0% (HOLD) | -6.3% (TRIM/SHORT) | -3.9% (HOLD) | -9.3% (TRIM/SHORT) | -6.7% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set C; TRIM/SHORT under Set B/Set D/Set E |
| NAT | -56.0% (TRIM/SHORT) | -63.1% (TRIM/SHORT) | -60.8% (TRIM/SHORT) | -66.1% (TRIM/SHORT) | -63.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TEN | +42.1% (BUY) | +29.0% (BUY) | +33.4% (BUY) | +23.7% (BUY) | +28.4% (BUY) | ✓ robust | position BUY across all 5 weight sets |
| CMBT | -9.1% (TRIM/SHORT) | -14.0% (TRIM/SHORT) | -12.4% (TRIM/SHORT) | -16.1% (TRIM/SHORT) | -14.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| BRUT | +11.2% (BUY) | -40.9% (TRIM/SHORT) | -23.6% (TRIM/SHORT) | -63.4% (TRIM/SHORT) | -44.1% (TRIM/SHORT) | ⚑ driven | BUY under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | +1.1% (HOLD) | -21.3% (TRIM/SHORT) | -13.9% (TRIM/SHORT) | -30.8% (TRIM/SHORT) | -22.6% (TRIM/SHORT) | ⚑ driven | HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

## Per-name detail

### DHT — price $17.76, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $13.34 | -24.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $11.46 | -35.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $12.08 | -32.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $10.66 | -40.0% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $11.35 | -36.1% | TRIM/SHORT |

### ECO — price $54.94, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $32.09 | -41.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $26.06 | -52.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $28.07 | -48.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $23.52 | -57.2% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $25.73 | -53.2% | TRIM/SHORT |

### FRO — price $38.13, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $22.91 | -39.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $18.43 | -51.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $19.92 | -47.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $16.53 | -56.7% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $18.17 | -52.3% | TRIM/SHORT |

### INSW — price $88.48, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $52.93 | -40.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $48.23 | -45.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $49.79 | -43.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $46.29 | -47.7% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $48.00 | -45.8% | TRIM/SHORT |

### TNK — price $72.45, target $75.00

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set C; TRIM/SHORT under Set B/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $73.18 | +1.0% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $67.88 | -6.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $69.65 | -3.9% | HOLD |
| Crude Set D (bearish, deep normalization) | $65.69 | -9.3% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $67.61 | -6.7% | TRIM/SHORT |

### NAT — price $6.17, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $2.72 | -56.0% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.27 | -63.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.42 | -60.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.09 | -66.1% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $2.25 | -63.5% | TRIM/SHORT |

### TEN — price $39.66, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $56.36 | +42.1% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $51.15 | +29.0% | BUY |
| Crude Set C (bullish, extended Phase 1) | $52.90 | +33.4% | BUY |
| Crude Set D (bearish, deep normalization) | $49.05 | +23.7% | BUY |
| Crude Set E (current locked, Jul-2 vintage) | $50.92 | +28.4% | BUY |

### CMBT — price $15.57, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $14.15 | -9.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.39 | -14.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.64 | -12.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.07 | -16.1% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $13.35 | -14.3% | TRIM/SHORT |

### BRUT — price $5.58, target $7.13

**Classification:** WEIGHT-DRIVEN. BUY under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $6.20 | +11.2% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $3.30 | -40.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.26 | -23.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.04 | -63.4% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $3.12 | -44.1% | TRIM/SHORT |

### CAPT — price $13.00, target $18.90

**Classification:** WEIGHT-DRIVEN. HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $13.14 | +1.1% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $10.23 | -21.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $11.19 | -13.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $9.00 | -30.8% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $10.07 | -22.6% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
