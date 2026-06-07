# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $16.40
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $15.29 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.34 (-18.7% vs price)
- **Breakeven TCE (scenario-invariant):** $148,415/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $19.53 | $22.36 | $21.67–$23.15 | 8.44× | 0.70 | $28.97 | $337,500 | 2.27× |
| Pre-MoU baseline | 15% | 1.10× | $16.92 | $18.35 | $17.98–$18.78 | 4.53× | 0.70 | $21.71 | $181,250 | 1.22× |
| MoU base case | 50% | 0.74× | $10.94 | $11.51 | $11.27–$11.72 | 2.12× | 0.70 | $12.82 | $84,875 | 0.57× |
| MoU bear | 25% | 0.68× | $9.86 | $10.37 | $10.17–$10.58 | 1.39× | 0.60 | $11.15 | $55,500 | 0.37× |
| **Probability-weighted** | | | | **$13.34** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.96
- **Downside (worst scenario − price):** $-6.03
- **Expected value vs current** (weighted FV − price): $-3.06 (-18.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
