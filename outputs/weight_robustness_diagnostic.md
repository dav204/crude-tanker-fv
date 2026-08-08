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
| DHT | -29.4% (TRIM/SHORT) | -30.2% (TRIM/SHORT) | -40.1% (TRIM/SHORT) | -36.8% (TRIM/SHORT) | -44.3% (TRIM/SHORT) | -40.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| ECO | -47.4% (TRIM/SHORT) | -48.1% (TRIM/SHORT) | -57.8% (TRIM/SHORT) | -54.6% (TRIM/SHORT) | -62.0% (TRIM/SHORT) | -58.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| FRO | -41.8% (TRIM/SHORT) | -42.6% (TRIM/SHORT) | -53.9% (TRIM/SHORT) | -50.1% (TRIM/SHORT) | -58.7% (TRIM/SHORT) | -54.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| INSW | -41.1% (TRIM/SHORT) | -41.4% (TRIM/SHORT) | -46.5% (TRIM/SHORT) | -44.8% (TRIM/SHORT) | -48.6% (TRIM/SHORT) | -46.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| TNK | +3.4% (HOLD) | +2.9% (HOLD) | -4.3% (HOLD) | -1.9% (HOLD) | -7.3% (TRIM/SHORT) | -4.7% (HOLD) | ⚑ driven | HOLD under Set A'/Set A/Set B/Set C/Set E; TRIM/SHORT under Set D |
| NAT | -56.8% (TRIM/SHORT) | -57.3% (TRIM/SHORT) | -64.2% (TRIM/SHORT) | -62.0% (TRIM/SHORT) | -67.1% (TRIM/SHORT) | -64.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| TEN | +45.2% (BUY) | +44.5% (BUY) | +32.2% (BUY) | +36.3% (BUY) | +27.4% (BUY) | +31.7% (BUY) | ✓ robust | position BUY across all 6 weight sets |
| CMBT | -13.4% (TRIM/SHORT) | -13.8% (TRIM/SHORT) | -18.5% (TRIM/SHORT) | -16.9% (TRIM/SHORT) | -20.5% (TRIM/SHORT) | -18.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 6 weight sets |
| BRUT | +0.7% (HOLD) | -3.1% (HOLD) | -48.5% (TRIM/SHORT) | -33.5% (TRIM/SHORT) | -68.1% (TRIM/SHORT) | -51.3% (TRIM/SHORT) | ⚑ driven | HOLD under Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | -4.0% (HOLD) | -5.7% (TRIM/SHORT) | -26.6% (TRIM/SHORT) | -19.7% (TRIM/SHORT) | -35.4% (TRIM/SHORT) | -27.8% (TRIM/SHORT) | ⚑ driven | HOLD under Set A'; TRIM/SHORT under Set A/Set B/Set C/Set D/Set E |

## Per-name detail

### DHT — price $18.76, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $13.24 | -29.4% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $13.10 | -30.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $11.24 | -40.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $11.86 | -36.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $10.45 | -44.3% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $11.13 | -40.6% | TRIM/SHORT |

### ECO — price $61.86, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $32.57 | -47.4% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $32.10 | -48.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $26.08 | -57.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $28.08 | -54.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $23.54 | -62.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $25.74 | -58.4% | TRIM/SHORT |

### FRO — price $39.74, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $23.15 | -41.8% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $22.80 | -42.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $18.33 | -53.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $19.82 | -50.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $16.43 | -58.7% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $18.07 | -54.5% | TRIM/SHORT |

### INSW — price $92.41, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $54.46 | -41.1% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $54.12 | -41.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $49.44 | -46.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $50.99 | -44.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $47.51 | -48.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $49.21 | -46.8% | TRIM/SHORT |

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
| Crude Set A' (B' reweight, production 2026-07-31) | $56.83 | +45.2% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $56.56 | +44.5% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $51.74 | +32.2% | BUY |
| Crude Set C (bullish, extended Phase 1) | $53.34 | +36.3% | BUY |
| Crude Set D (bearish, deep normalization) | $49.85 | +27.4% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $51.56 | +31.7% | BUY |

### CMBT — price $16.29, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 6 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $14.11 | -13.4% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $14.05 | -13.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.28 | -18.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.54 | -16.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.96 | -20.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.24 | -18.7% | TRIM/SHORT |

### BRUT — price $6.41, target $7.13

**Classification:** WEIGHT-DRIVEN. HOLD under Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $6.45 | +0.7% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $6.21 | -3.1% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $3.30 | -48.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.26 | -33.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.05 | -68.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $3.12 | -51.3% | TRIM/SHORT |

### CAPT — price $13.94, target $18.90

**Classification:** WEIGHT-DRIVEN. HOLD under Set A'; TRIM/SHORT under Set A/Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A' (B' reweight, production 2026-07-31) | $13.38 | -4.0% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $13.14 | -5.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $10.23 | -26.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $11.19 | -19.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $9.00 | -35.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $10.07 | -27.8% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
