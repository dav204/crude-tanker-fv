# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $24.51
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $19.36 (-21.0% vs price)
- **Breakeven TCE (scenario-invariant):** $46,840/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.04× | $33.70 | $22.86 | $22.36–$23.37 | 1.75× | 0.70 | $21.17 | $29,156 | 0.62× |
| Moderate growth (base) | 40% | 0.91× | $30.01 | $19.66 | $19.14–$20.17 | 1.33× | 0.60 | $17.63 | $22,004 | 0.47× |
| China property drag | 25% | 0.85× | $28.26 | $18.06 | $17.48–$18.64 | 1.14× | 0.50 | $16.33 | $18,352 | 0.39× |
| Coordinated slowdown | 15% | 0.78× | $26.19 | $16.05 | $15.60–$16.49 | 0.95× | 0.50 | $13.76 | $15,484 | 0.33× |
| **Probability-weighted** | | | | **$19.36** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.65
- **Downside (worst scenario − price):** $-8.46
- **Expected value vs current** (weighted FV − price): $-5.15 (-21.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
