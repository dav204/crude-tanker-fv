# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $30.48
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $33.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.59 (-6.2% vs price)
- **Breakeven TCE (scenario-invariant):** $15,280/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.05× | $35.30 | $35.03 | $34.16–$35.91 | 1.81× | 0.70 | $34.42 | $30,439 | 1.99× |
| Moderate growth (base) | 40% | 0.92× | $29.98 | $29.07 | $28.19–$29.96 | 1.37× | 0.60 | $27.72 | $22,858 | 1.50× |
| China property drag | 25% | 0.85× | $27.38 | $26.29 | $25.31–$27.26 | 1.16× | 0.50 | $25.20 | $18,776 | 1.23× |
| Coordinated slowdown | 15% | 0.78× | $24.55 | $22.54 | $21.78–$23.30 | 0.97× | 0.50 | $20.54 | $15,947 | 1.04× |
| **Probability-weighted** | | | | **$28.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.55
- **Downside (worst scenario − price):** $-7.94
- **Expected value vs current** (weighted FV − price): $-1.89 (-6.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
