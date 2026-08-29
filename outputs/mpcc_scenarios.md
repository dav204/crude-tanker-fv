# MPCC — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $3.01
- **Analyst target:** $2.63
- **NAV / share (reference, unflexed):** $2.05 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $2.07 (-31.4% vs price)
- **Breakeven TCE (scenario-invariant):** $255,556/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 1.00× | $2.04 | $2.21 | $2.17–$2.25 | 1.20× | 0.60 | $2.47 | $36,670 | 0.14× |
| Gradual normalization (base) | 40% | 0.95× | $1.89 | $2.15 | $2.11–$2.20 | 1.16× | 0.50 | $2.41 | $35,464 | 0.14× |
| Normalization + orderbook overhang | 20% | 0.91× | $1.75 | $2.00 | $1.96–$2.04 | 1.13× | 0.50 | $2.25 | $34,290 | 0.13× |
| Demand recession | 15% | 0.83× | $1.46 | $1.69 | $1.66–$1.72 | 0.99× | 0.50 | $1.92 | $30,084 | 0.12× |
| **Probability-weighted** | | | | **$2.07** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.80
- **Downside (worst scenario − price):** $-1.32
- **Expected value vs current** (weighted FV − price): $-0.95 (-31.4%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
