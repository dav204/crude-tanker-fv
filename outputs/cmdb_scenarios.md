# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $23.91
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $19.37 (-19.0% vs price)
- **Breakeven TCE (scenario-invariant):** $42,084/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.04× | $33.72 | $22.88 | $22.37–$23.38 | 1.75× | 0.70 | $21.18 | $29,156 | 0.69× |
| Moderate growth (base) | 40% | 0.91× | $30.03 | $19.67 | $19.15–$20.19 | 1.33× | 0.60 | $17.64 | $22,004 | 0.52× |
| China property drag | 25% | 0.85× | $28.28 | $18.07 | $17.49–$18.65 | 1.14× | 0.50 | $16.34 | $18,352 | 0.44× |
| Coordinated slowdown | 15% | 0.78× | $26.21 | $16.05 | $15.61–$16.50 | 0.95× | 0.50 | $13.76 | $15,484 | 0.37× |
| **Probability-weighted** | | | | **$19.37** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.03
- **Downside (worst scenario − price):** $-7.86
- **Expected value vs current** (weighted FV − price): $-4.54 (-19.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
