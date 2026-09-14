# SBLK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $31.17
- **Analyst target:** $34.50
- **NAV / share (reference, unflexed):** $33.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.26 (-9.3% vs price)
- **Breakeven TCE (scenario-invariant):** $18,888/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.04× | $34.78 | $34.58 | $33.70–$35.45 | 1.81× | 0.70 | $34.10 | $30,439 | 1.61× |
| Moderate growth (base) | 40% | 0.91× | $29.59 | $28.74 | $27.85–$29.63 | 1.37× | 0.60 | $27.47 | $22,858 | 1.21× |
| China property drag | 25% | 0.84× | $27.05 | $26.01 | $25.04–$26.99 | 1.16× | 0.50 | $24.97 | $18,776 | 0.99× |
| Coordinated slowdown | 15% | 0.77× | $24.29 | $22.32 | $21.56–$23.08 | 0.97× | 0.50 | $20.35 | $15,947 | 0.84× |
| **Probability-weighted** | | | | **$28.26** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.41
- **Downside (worst scenario − price):** $-8.85
- **Expected value vs current** (weighted FV − price): $-2.91 (-9.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
