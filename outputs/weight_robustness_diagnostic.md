# Crude Weight-Robustness Diagnostic

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Crude Set A weights. Surfaces which crude tanker calls survive defensible reweighting (call is **weight-robust**) vs which depend on a specific weight prior (**weight-driven**).

**Driver:** Catlin / VIE analysis (2026-05-25) plus the June 1 macro briefing suggest current Set A weights may put too much weight on "deep normalisation" relative to "slow normalisation with extended Phase 1." Sets B/C/D bracket the normalisation-speed axis.

**Naming namespace:** the labels below are CRUDE-sector weight families. The LNG sector uses its own "Set B" / "Set B-revised" naming (METHODOLOGY §11.3). Cross-sector conflation would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| DHT | ⚑ driven | HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| ECO | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| FRO | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| INSW | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TNK | ⚑ driven | BUY under Set A/Set B/Set C/Set E; HOLD under Set D |
| NAT | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TEN | ✓ robust | position BUY across all 5 weight sets |
| CMBT | ⚑ driven | BUY under Set A; HOLD under Set B/Set C/Set D/Set E |
| BRUT | ⚑ driven | BUY under Set A/Set B/Set C; TRIM/SHORT under Set D; HOLD under Set E |
| CAPT | ⚑ driven | BUY under Set A/Set C; HOLD under Set B; TRIM/SHORT under Set D/Set E |

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
| DHT | -4.6% (HOLD) | -22.5% (TRIM/SHORT) | -17.1% (TRIM/SHORT) | -32.3% (TRIM/SHORT) | -24.8% (TRIM/SHORT) | ⚑ driven | HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| ECO | -19.9% (TRIM/SHORT) | -39.0% (TRIM/SHORT) | -33.2% (TRIM/SHORT) | -49.4% (TRIM/SHORT) | -41.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| FRO | -16.9% (TRIM/SHORT) | -37.4% (TRIM/SHORT) | -31.2% (TRIM/SHORT) | -48.6% (TRIM/SHORT) | -40.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| INSW | -22.6% (TRIM/SHORT) | -32.1% (TRIM/SHORT) | -29.2% (TRIM/SHORT) | -37.1% (TRIM/SHORT) | -33.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TNK | +23.7% (BUY) | +11.0% (BUY) | +14.9% (BUY) | +4.3% (HOLD) | +9.5% (BUY) | ⚑ driven | BUY under Set A/Set B/Set C/Set E; HOLD under Set D |
| NAT | -40.1% (TRIM/SHORT) | -53.0% (TRIM/SHORT) | -49.1% (TRIM/SHORT) | -59.9% (TRIM/SHORT) | -54.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 5 weight sets |
| TEN | +81.9% (BUY) | +58.7% (BUY) | +65.8% (BUY) | +46.4% (BUY) | +56.0% (BUY) | ✓ robust | position BUY across all 5 weight sets |
| CMBT | +10.7% (BUY) | +2.0% (HOLD) | +4.7% (HOLD) | -2.7% (HOLD) | +0.9% (HOLD) | ⚑ driven | BUY under Set A; HOLD under Set B/Set C/Set D/Set E |
| BRUT | +98.1% (BUY) | +7.2% (BUY) | +34.5% (BUY) | -43.1% (TRIM/SHORT) | -5.0% (HOLD) | ⚑ driven | BUY under Set A/Set B/Set C; TRIM/SHORT under Set D; HOLD under Set E |
| CAPT | +37.4% (BUY) | -0.3% (HOLD) | +11.0% (BUY) | -20.8% (TRIM/SHORT) | -5.1% (TRIM/SHORT) | ⚑ driven | BUY under Set A/Set C; HOLD under Set B; TRIM/SHORT under Set D/Set E |

## Per-name detail

### DHT — price $16.53, target $16.00

**Classification:** WEIGHT-DRIVEN. HOLD under Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked, Jun-9) | $15.77 | -4.6% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $12.81 | -22.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.70 | -17.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $11.20 | -32.3% | TRIM/SHORT |
| Crude Set E (Jul-2 post-stand-down proposal) | $12.43 | -24.8% | TRIM/SHORT |

### ECO — price $49.94, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked, Jun-9) | $40.02 | -19.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $30.46 | -39.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $33.35 | -33.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $25.28 | -49.4% | TRIM/SHORT |
| Crude Set E (Jul-2 post-stand-down proposal) | $29.25 | -41.4% | TRIM/SHORT |

### FRO — price $34.70, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked, Jun-9) | $28.82 | -16.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $21.71 | -37.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $23.86 | -31.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $17.84 | -48.6% | TRIM/SHORT |
| Crude Set E (Jul-2 post-stand-down proposal) | $20.80 | -40.1% | TRIM/SHORT |

### INSW — price $77.78, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked, Jun-9) | $60.19 | -22.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $52.84 | -32.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $55.06 | -29.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $48.91 | -37.1% | TRIM/SHORT |
| Crude Set E (Jul-2 post-stand-down proposal) | $51.94 | -33.2% | TRIM/SHORT |

### TNK — price $64.33, target $75.00

**Classification:** WEIGHT-DRIVEN. BUY under Set A/Set B/Set C/Set E; HOLD under Set D.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked, Jun-9) | $79.59 | +23.7% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $71.44 | +11.0% | BUY |
| Crude Set C (bullish, extended Phase 1) | $73.92 | +14.9% | BUY |
| Crude Set D (bearish, deep normalization) | $67.12 | +4.3% | HOLD |
| Crude Set E (Jul-2 post-stand-down proposal) | $70.46 | +9.5% | BUY |

### NAT — price $5.56, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked, Jun-9) | $3.33 | -40.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.61 | -53.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.83 | -49.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.23 | -59.9% | TRIM/SHORT |
| Crude Set E (Jul-2 post-stand-down proposal) | $2.53 | -54.6% | TRIM/SHORT |

### TEN — price $35.37, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 5 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked, Jun-9) | $64.35 | +81.9% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $56.14 | +58.7% | BUY |
| Crude Set C (bullish, extended Phase 1) | $58.64 | +65.8% | BUY |
| Crude Set D (bearish, deep normalization) | $51.80 | +46.4% | BUY |
| Crude Set E (Jul-2 post-stand-down proposal) | $55.16 | +56.0% | BUY |

### CMBT — price $14.05, target $16.59

**Classification:** WEIGHT-DRIVEN. BUY under Set A; HOLD under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked, Jun-9) | $15.56 | +10.7% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $14.34 | +2.0% | HOLD |
| Crude Set C (bullish, extended Phase 1) | $14.71 | +4.7% | HOLD |
| Crude Set D (bearish, deep normalization) | $13.67 | -2.7% | HOLD |
| Crude Set E (Jul-2 post-stand-down proposal) | $14.18 | +0.9% | HOLD |

### BRUT — price $5.17, target $7.13

**Classification:** WEIGHT-DRIVEN. BUY under Set A/Set B/Set C; TRIM/SHORT under Set D; HOLD under Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked, Jun-9) | $10.24 | +98.1% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $5.54 | +7.2% | BUY |
| Crude Set C (bullish, extended Phase 1) | $6.95 | +34.5% | BUY |
| Crude Set D (bearish, deep normalization) | $2.94 | -43.1% | TRIM/SHORT |
| Crude Set E (Jul-2 post-stand-down proposal) | $4.91 | -5.0% | HOLD |

### CAPT — price $12.49, target $18.90

**Classification:** WEIGHT-DRIVEN. BUY under Set A/Set C; HOLD under Set B; TRIM/SHORT under Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked, Jun-9) | $17.16 | +37.4% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $12.46 | -0.3% | HOLD |
| Crude Set C (bullish, extended Phase 1) | $13.87 | +11.0% | BUY |
| Crude Set D (bearish, deep normalization) | $9.89 | -20.8% | TRIM/SHORT |
| Crude Set E (Jul-2 post-stand-down proposal) | $11.85 | -5.1% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.
