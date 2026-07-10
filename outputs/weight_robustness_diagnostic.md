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
| TNK | ⚑ driven | BUY under Set A; HOLD under Set B/Set C/Set E; TRIM/SHORT under Set D |
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
| DHT | -21.2% (TRIM/SHORT) | -32.3% (TRIM/SHORT) | -28.6% (TRIM/SHORT) | -37.0% (TRIM/SHORT) | -33.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| ECO | -38.6% (TRIM/SHORT) | -50.1% (TRIM/SHORT) | -46.3% (TRIM/SHORT) | -55.0% (TRIM/SHORT) | -50.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| FRO | -37.3% (TRIM/SHORT) | -49.6% (TRIM/SHORT) | -45.5% (TRIM/SHORT) | -54.8% (TRIM/SHORT) | -50.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| INSW | -36.2% (TRIM/SHORT) | -41.9% (TRIM/SHORT) | -40.0% (TRIM/SHORT) | -44.2% (TRIM/SHORT) | -42.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TNK | +5.6% (BUY) | -2.0% (HOLD) | +0.5% (HOLD) | -5.2% (TRIM/SHORT) | -2.4% (HOLD) | ⚑ driven | BUY under Set A; HOLD under Set B/Set C/Set E; TRIM/SHORT under Set D |
| NAT | -54.0% (TRIM/SHORT) | -61.5% (TRIM/SHORT) | -59.0% (TRIM/SHORT) | -64.5% (TRIM/SHORT) | -61.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TEN | +47.5% (BUY) | +33.8% (BUY) | +38.4% (BUY) | +28.3% (BUY) | +33.2% (BUY) | ✓ robust | position BUY across all 5 weight sets |
| CMBT | -5.2% (TRIM/SHORT) | -10.3% (TRIM/SHORT) | -8.6% (TRIM/SHORT) | -12.5% (TRIM/SHORT) | -10.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| BRUT | +9.6% (BUY) | -41.7% (TRIM/SHORT) | -24.7% (TRIM/SHORT) | -63.9% (TRIM/SHORT) | -44.9% (TRIM/SHORT) | ⚑ driven | BUY under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | +0.6% (HOLD) | -21.7% (TRIM/SHORT) | -14.3% (TRIM/SHORT) | -31.1% (TRIM/SHORT) | -22.9% (TRIM/SHORT) | ⚑ driven | HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

## Per-name detail

### DHT — price $16.93, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $13.34 | -21.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $11.46 | -32.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $12.08 | -28.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $10.66 | -37.0% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $11.35 | -33.0% | TRIM/SHORT |

### ECO — price $52.23, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $32.09 | -38.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $26.06 | -50.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $28.07 | -46.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $23.52 | -55.0% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $25.73 | -50.7% | TRIM/SHORT |

### FRO — price $36.56, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $22.91 | -37.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $18.43 | -49.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $19.92 | -45.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $16.53 | -54.8% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $18.17 | -50.3% | TRIM/SHORT |

### INSW — price $82.98, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $52.93 | -36.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $48.23 | -41.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $49.79 | -40.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $46.29 | -44.2% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $48.00 | -42.2% | TRIM/SHORT |

### TNK — price $69.27, target $75.00

**Classification:** WEIGHT-DRIVEN. BUY under Set A; HOLD under Set B/Set C/Set E; TRIM/SHORT under Set D.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $73.18 | +5.6% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $67.88 | -2.0% | HOLD |
| Crude Set C (bullish, extended Phase 1) | $69.65 | +0.5% | HOLD |
| Crude Set D (bearish, deep normalization) | $65.69 | -5.2% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $67.61 | -2.4% | HOLD |

### NAT — price $5.90, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $2.72 | -54.0% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.27 | -61.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.42 | -59.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.09 | -64.5% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $2.25 | -61.8% | TRIM/SHORT |

### TEN — price $38.22, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $56.36 | +47.5% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $51.15 | +33.8% | BUY |
| Crude Set C (bullish, extended Phase 1) | $52.90 | +38.4% | BUY |
| Crude Set D (bearish, deep normalization) | $49.05 | +28.3% | BUY |
| Crude Set E (current locked, Jul-2 vintage) | $50.92 | +33.2% | BUY |

### CMBT — price $14.93, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $14.15 | -5.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.39 | -10.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.64 | -8.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.07 | -12.5% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $13.35 | -10.6% | TRIM/SHORT |

### BRUT — price $5.66, target $7.13

**Classification:** WEIGHT-DRIVEN. BUY under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $6.20 | +9.6% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $3.30 | -41.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.26 | -24.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.04 | -63.9% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $3.12 | -44.9% | TRIM/SHORT |

### CAPT — price $13.06, target $18.90

**Classification:** WEIGHT-DRIVEN. HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (Jun-9 war tilt, history bracket) | $13.14 | +0.6% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $10.23 | -21.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $11.19 | -14.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $9.00 | -31.1% | TRIM/SHORT |
| Crude Set E (current locked, Jul-2 vintage) | $10.07 | -22.9% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
