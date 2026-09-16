# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $30.79
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $33.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.71 (-6.7% vs price)
- **Breakeven TCE (scenario-invariant):** $16,893/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.06× | $35.49 | $35.21 | $34.33–$36.08 | 1.81× | 0.70 | $34.54 | $30,439 | 1.80× |
| Moderate growth (base) | 40% | 0.92× | $30.12 | $29.20 | $28.31–$30.09 | 1.37× | 0.60 | $27.82 | $22,858 | 1.35× |
| China property drag | 25% | 0.85× | $27.50 | $26.39 | $25.42–$27.37 | 1.16× | 0.50 | $25.28 | $18,776 | 1.11× |
| Coordinated slowdown | 15% | 0.78× | $24.64 | $22.62 | $21.86–$23.38 | 0.97× | 0.50 | $20.60 | $15,947 | 0.94× |
| **Probability-weighted** | | | | **$28.71** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.42
- **Downside (worst scenario − price):** $-8.17
- **Expected value vs current** (weighted FV − price): $-2.08 (-6.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
