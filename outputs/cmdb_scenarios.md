# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $19.08
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $31.33 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $20.34 (+6.6% vs price)
- **Breakeven TCE (scenario-invariant):** $12,866/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.17× | $35.97 | $24.32 | $23.81–$24.83 | 1.75× | 0.70 | $22.31 | $29,570 | 2.30× |
| Moderate growth (base) | 40% | 1.01× | $31.61 | $20.67 | $20.15–$21.19 | 1.33× | 0.60 | $18.49 | $22,287 | 1.73× |
| China property drag | 25% | 0.93× | $29.51 | $18.85 | $18.27–$19.43 | 1.14× | 0.50 | $17.05 | $18,504 | 1.44× |
| Coordinated slowdown | 15% | 0.84× | $27.10 | $16.63 | $16.18–$17.08 | 0.95× | 0.50 | $14.30 | $15,639 | 1.22× |
| **Probability-weighted** | | | | **$20.34** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.24
- **Downside (worst scenario − price):** $-2.45
- **Expected value vs current** (weighted FV − price): $+1.26 (+6.6%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
