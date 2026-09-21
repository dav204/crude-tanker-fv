# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $32.48
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $33.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.20 (-13.2% vs price)
- **Breakeven TCE (scenario-invariant):** $25,530/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.04× | $34.69 | $34.49 | $33.62–$35.36 | 1.81× | 0.70 | $34.04 | $30,439 | 1.19× |
| Moderate growth (base) | 40% | 0.90× | $29.51 | $28.68 | $27.79–$29.56 | 1.37× | 0.60 | $27.42 | $22,858 | 0.90× |
| China property drag | 25% | 0.84× | $26.99 | $25.96 | $24.98–$26.93 | 1.16× | 0.50 | $24.93 | $18,776 | 0.74× |
| Coordinated slowdown | 15% | 0.77× | $24.24 | $22.28 | $21.52–$23.04 | 0.97× | 0.50 | $20.32 | $15,947 | 0.62× |
| **Probability-weighted** | | | | **$28.20** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.01
- **Downside (worst scenario − price):** $-10.20
- **Expected value vs current** (weighted FV − price): $-4.28 (-13.2%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
