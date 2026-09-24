# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $30.40
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $33.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.36 (-6.7% vs price)
- **Breakeven TCE (scenario-invariant):** $15,065/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.04× | $34.94 | $34.72 | $33.85–$35.59 | 1.81× | 0.70 | $34.20 | $30,439 | 2.02× |
| Moderate growth (base) | 40% | 0.91× | $29.71 | $28.84 | $27.96–$29.73 | 1.37× | 0.60 | $27.55 | $22,858 | 1.52× |
| China property drag | 25% | 0.84× | $27.15 | $26.10 | $25.12–$27.07 | 1.16× | 0.50 | $25.04 | $18,776 | 1.25× |
| Coordinated slowdown | 15% | 0.77× | $24.37 | $22.39 | $21.63–$23.15 | 0.97× | 0.50 | $20.41 | $15,947 | 1.06× |
| **Probability-weighted** | | | | **$28.36** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.32
- **Downside (worst scenario − price):** $-8.01
- **Expected value vs current** (weighted FV − price): $-2.04 (-6.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
