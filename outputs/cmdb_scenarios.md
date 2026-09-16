# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $24.10
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $19.56 (-18.8% vs price)
- **Breakeven TCE (scenario-invariant):** $38,942/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.05× | $34.15 | $23.14 | $22.64–$23.65 | 1.75× | 0.70 | $21.36 | $29,156 | 0.75× |
| Moderate growth (base) | 40% | 0.92× | $30.36 | $19.86 | $19.34–$20.38 | 1.33× | 0.60 | $17.78 | $22,004 | 0.57× |
| China property drag | 25% | 0.86× | $28.56 | $18.23 | $17.65–$18.81 | 1.14× | 0.50 | $16.47 | $18,352 | 0.47× |
| Coordinated slowdown | 15% | 0.79× | $26.43 | $16.18 | $15.74–$16.63 | 0.95× | 0.50 | $13.87 | $15,484 | 0.40× |
| **Probability-weighted** | | | | **$19.56** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.96
- **Downside (worst scenario − price):** $-7.92
- **Expected value vs current** (weighted FV − price): $-4.54 (-18.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
