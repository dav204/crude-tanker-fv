# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $20.52
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $19.51 (-4.9% vs price)
- **Breakeven TCE (scenario-invariant):** $16,931/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.05× | $34.05 | $23.08 | $22.57–$23.58 | 1.75× | 0.70 | $21.32 | $29,156 | 1.72× |
| Moderate growth (base) | 40% | 0.92× | $30.28 | $19.82 | $19.30–$20.33 | 1.33× | 0.60 | $17.75 | $22,004 | 1.30× |
| China property drag | 25% | 0.86× | $28.49 | $18.19 | $17.61–$18.77 | 1.14× | 0.50 | $16.44 | $18,352 | 1.08× |
| Coordinated slowdown | 15% | 0.78× | $26.37 | $16.15 | $15.70–$16.60 | 0.95× | 0.50 | $13.84 | $15,484 | 0.91× |
| **Probability-weighted** | | | | **$19.51** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.56
- **Downside (worst scenario − price):** $-4.37
- **Expected value vs current** (weighted FV − price): $-1.01 (-4.9%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
