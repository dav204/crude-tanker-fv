# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $32.06
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $33.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.34 (-11.6% vs price)
- **Breakeven TCE (scenario-invariant):** $23,456/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.04× | $34.90 | $34.68 | $33.81–$35.55 | 1.81× | 0.70 | $34.17 | $30,439 | 1.30× |
| Moderate growth (base) | 40% | 0.91× | $29.68 | $28.82 | $27.93–$29.70 | 1.37× | 0.60 | $27.52 | $22,858 | 0.97× |
| China property drag | 25% | 0.84× | $27.12 | $26.07 | $25.10–$27.05 | 1.16× | 0.50 | $25.02 | $18,776 | 0.80× |
| Coordinated slowdown | 15% | 0.77× | $24.35 | $22.37 | $21.61–$23.13 | 0.97× | 0.50 | $20.40 | $15,947 | 0.68× |
| **Probability-weighted** | | | | **$28.34** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.62
- **Downside (worst scenario − price):** $-9.69
- **Expected value vs current** (weighted FV − price): $-3.72 (-11.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
