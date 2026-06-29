# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $17.99
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $31.33 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $20.43 (+13.6% vs price)
- **Breakeven TCE (scenario-invariant):** $5,949/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.18× | $36.17 | $24.44 | $23.93–$24.95 | 1.75× | 0.70 | $22.39 | $29,570 | 4.97× |
| Moderate growth (base) | 40% | 1.02× | $31.76 | $20.76 | $20.24–$21.28 | 1.33× | 0.60 | $18.56 | $22,287 | 3.75× |
| China property drag | 25% | 0.94× | $29.63 | $18.93 | $18.35–$19.51 | 1.14× | 0.50 | $17.11 | $18,504 | 3.11× |
| Coordinated slowdown | 15% | 0.85× | $27.20 | $16.69 | $16.24–$17.14 | 0.95× | 0.50 | $14.35 | $15,639 | 2.63× |
| **Probability-weighted** | | | | **$20.43** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.45
- **Downside (worst scenario − price):** $-1.30
- **Expected value vs current** (weighted FV − price): $+2.44 (+13.6%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
