# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $23.91
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.60 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $19.30 (-19.3% vs price)
- **Breakeven TCE (scenario-invariant):** $41,984/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.03× | $33.56 | $22.78 | $22.27–$23.29 | 1.75× | 0.70 | $21.11 | $29,156 | 0.69× |
| Moderate growth (base) | 40% | 0.91× | $29.91 | $19.60 | $19.08–$20.11 | 1.33× | 0.60 | $17.58 | $22,004 | 0.52× |
| China property drag | 25% | 0.85× | $28.18 | $18.01 | $17.43–$18.58 | 1.14× | 0.50 | $16.29 | $18,352 | 0.44× |
| Coordinated slowdown | 15% | 0.78× | $26.12 | $16.01 | $15.56–$16.45 | 0.95× | 0.50 | $13.72 | $15,484 | 0.37× |
| **Probability-weighted** | | | | **$19.30** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.13
- **Downside (worst scenario − price):** $-7.90
- **Expected value vs current** (weighted FV − price): $-4.61 (-19.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
