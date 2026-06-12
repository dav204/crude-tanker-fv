# GSL — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $38.99
- **Analyst target:** $52.04
- **NAV / share (reference, unflexed):** $38.59 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $31.76 (-18.5% vs price)
- **Breakeven TCE (scenario-invariant):** $2,757,173/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 1.03× | $39.95 | $34.74 | $34.74–$34.74 | 1.44× | 0.60 | $26.93 | $56,335 | 0.02× |
| Gradual normalization (base) | 40% | 0.97× | $36.97 | $32.26 | $32.26–$32.26 | 1.38× | 0.60 | $25.20 | $53,862 | 0.02× |
| Normalization + orderbook overhang | 20% | 0.90× | $33.60 | $29.45 | $29.45–$29.45 | 1.30× | 0.60 | $23.24 | $50,777 | 0.02× |
| Demand recession | 15% | 0.87× | $32.48 | $28.52 | $28.52–$28.52 | 1.21× | 0.60 | $22.59 | $47,465 | 0.02× |
| **Probability-weighted** | | | | **$31.76** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-4.25
- **Downside (worst scenario − price):** $-10.47
- **Expected value vs current** (weighted FV − price): $-7.23 (-18.5%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
