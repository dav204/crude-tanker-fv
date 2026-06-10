# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $34.50
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $24.40 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $29.36 (-14.9% vs price)
- **Breakeven TCE (scenario-invariant):** $311,332/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $33.63 | $40.78 | $38.95–$42.88 | 7.64× | 0.70 | $57.45 | $279,618 | 0.90× |
| Pre-MoU baseline | 45% | 1.12× | $28.78 | $32.42 | $31.36–$33.61 | 4.42× | 0.70 | $40.92 | $160,565 | 0.52× |
| MoU base case | 18% | 0.75× | $15.15 | $16.10 | $15.48–$16.68 | 2.00× | 0.70 | $18.30 | $72,387 | 0.23× |
| MoU bear | 12% | 0.70× | $13.40 | $13.98 | $13.52–$14.44 | 1.54× | 0.70 | $15.33 | $55,847 | 0.18× |
| **Probability-weighted** | | | | **$29.36** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.28
- **Downside (worst scenario − price):** $-20.52
- **Expected value vs current** (weighted FV − price): $-5.14 (-14.9%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
