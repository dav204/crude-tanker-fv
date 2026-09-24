# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $22.34
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $19.40 (-13.2% vs price)
- **Breakeven TCE (scenario-invariant):** $29,091/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.04× | $33.79 | $22.92 | $22.41–$23.42 | 1.75× | 0.70 | $21.21 | $29,156 | 1.00× |
| Moderate growth (base) | 40% | 0.91× | $30.08 | $19.70 | $19.18–$20.22 | 1.33× | 0.60 | $17.66 | $22,004 | 0.76× |
| China property drag | 25% | 0.85× | $28.32 | $18.09 | $17.52–$18.67 | 1.14× | 0.50 | $16.36 | $18,352 | 0.63× |
| Coordinated slowdown | 15% | 0.78× | $26.24 | $16.07 | $15.62–$16.52 | 0.95× | 0.50 | $13.78 | $15,484 | 0.53× |
| **Probability-weighted** | | | | **$19.40** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.58
- **Downside (worst scenario − price):** $-6.27
- **Expected value vs current** (weighted FV − price): $-2.94 (-13.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
