# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $34.70
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $24.22 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $18.17 (-47.6% vs price)
- **Breakeven TCE (scenario-invariant):** $320,754/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $33.41 | $40.26 | $38.35–$42.46 | 7.64× | 0.70 | $56.24 | $279,339 | 0.87× |
| Pre-MoU baseline | 20% | 0.82× | $17.61 | $18.70 | $18.00–$19.43 | 2.46× | 0.70 | $21.23 | $89,343 | 0.28× |
| MoU base case | 45% | 0.75× | $15.02 | $15.62 | $14.97–$16.22 | 2.00× | 0.70 | $17.01 | $72,327 | 0.23× |
| MoU bear | 25% | 0.70× | $13.28 | $13.52 | $13.04–$14.00 | 1.54× | 0.70 | $14.07 | $55,801 | 0.17× |
| **Probability-weighted** | | | | **$18.17** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.56
- **Downside (worst scenario − price):** $-21.18
- **Expected value vs current** (weighted FV − price): $-16.53 (-47.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
