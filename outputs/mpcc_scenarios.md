# MPCC — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $2.51
- **Analyst target:** $2.63
- **NAV / share (reference, unflexed):** $2.04 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $2.06 (-17.8% vs price)
- **Breakeven TCE (scenario-invariant):** $130,005/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 1.00× | $2.03 | $2.21 | $2.17–$2.25 | 1.20× | 0.60 | $2.47 | $36,713 | 0.28× |
| Gradual normalization (base) | 40% | 0.95× | $1.88 | $2.15 | $2.10–$2.19 | 1.16× | 0.50 | $2.41 | $35,505 | 0.27× |
| Normalization + orderbook overhang | 20% | 0.91× | $1.74 | $2.00 | $1.96–$2.04 | 1.13× | 0.50 | $2.25 | $34,329 | 0.26× |
| Demand recession | 15% | 0.83× | $1.46 | $1.69 | $1.66–$1.72 | 0.99× | 0.50 | $1.92 | $30,118 | 0.23× |
| **Probability-weighted** | | | | **$2.06** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.30
- **Downside (worst scenario − price):** $-0.82
- **Expected value vs current** (weighted FV − price): $-0.45 (-17.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
