# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $13.68
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $15.49 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $10.07 (-26.4% vs price)
- **Breakeven TCE (scenario-invariant):** $6,063/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $22.51 | $24.41 | $23.64–$25.30 | 7.00× | 0.70 | $28.86 | $246,237 | 40.61× |
| Pre-MoU baseline | 20% | 0.82× | $10.40 | $10.39 | $10.10–$10.69 | 2.32× | 0.70 | $10.35 | $81,123 | 13.38× |
| MoU base case | 45% | 0.75× | $8.51 | $8.33 | $8.08–$8.57 | 1.90× | 0.70 | $7.89 | $66,142 | 10.91× |
| MoU bear | 25% | 0.71× | $7.25 | $7.20 | $6.94–$7.47 | 1.50× | 0.60 | $7.14 | $51,975 | 8.57× |
| **Probability-weighted** | | | | **$10.07** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+10.73
- **Downside (worst scenario − price):** $-6.48
- **Expected value vs current** (weighted FV − price): $-3.61 (-26.4%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
