# MPCC — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $2.94
- **Analyst target:** $2.63
- **NAV / share (reference, unflexed):** $2.10 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $2.13 (-27.6% vs price)
- **Breakeven TCE (scenario-invariant):** $214,851/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 0.99× | $2.06 | $2.26 | $2.22–$2.30 | 1.20× | 0.60 | $2.55 | $36,927 | 0.17× |
| Gradual normalization (base) | 40% | 0.95× | $1.93 | $2.21 | $2.16–$2.25 | 1.17× | 0.50 | $2.49 | $35,708 | 0.17× |
| Normalization + orderbook overhang | 20% | 0.91× | $1.79 | $2.06 | $2.02–$2.10 | 1.13× | 0.50 | $2.33 | $34,519 | 0.16× |
| Demand recession | 15% | 0.83× | $1.53 | $1.77 | $1.74–$1.80 | 0.99× | 0.50 | $2.01 | $30,287 | 0.14× |
| **Probability-weighted** | | | | **$2.13** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.68
- **Downside (worst scenario − price):** $-1.17
- **Expected value vs current** (weighted FV − price): $-0.81 (-27.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
