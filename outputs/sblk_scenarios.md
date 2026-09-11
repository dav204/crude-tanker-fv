# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $30.74
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $33.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.59 (-7.0% vs price)
- **Breakeven TCE (scenario-invariant):** $16,536/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.05× | $35.30 | $35.04 | $34.17–$35.91 | 1.81× | 0.70 | $34.42 | $30,439 | 1.84× |
| Moderate growth (base) | 40% | 0.92× | $29.98 | $29.08 | $28.19–$29.97 | 1.37× | 0.60 | $27.73 | $22,858 | 1.38× |
| China property drag | 25% | 0.85× | $27.38 | $26.29 | $25.32–$27.26 | 1.16× | 0.50 | $25.20 | $18,776 | 1.14× |
| Coordinated slowdown | 15% | 0.78× | $24.55 | $22.54 | $21.78–$23.30 | 0.97× | 0.50 | $20.54 | $15,947 | 0.96× |
| **Probability-weighted** | | | | **$28.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.30
- **Downside (worst scenario − price):** $-8.20
- **Expected value vs current** (weighted FV − price): $-2.15 (-7.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
