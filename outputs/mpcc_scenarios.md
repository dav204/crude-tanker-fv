# MPCC — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $3.04
- **Analyst target:** $2.63
- **NAV / share (reference, unflexed):** $2.15 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $2.16 (-28.9% vs price)
- **Breakeven TCE (scenario-invariant):** $229,157/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 0.99× | $2.11 | $2.30 | $2.26–$2.34 | 1.20× | 0.60 | $2.58 | $36,788 | 0.16× |
| Gradual normalization (base) | 40% | 0.95× | $1.97 | $2.24 | $2.20–$2.29 | 1.16× | 0.50 | $2.52 | $35,576 | 0.16× |
| Normalization + orderbook overhang | 20% | 0.91× | $1.84 | $2.10 | $2.06–$2.14 | 1.13× | 0.50 | $2.36 | $34,396 | 0.15× |
| Demand recession | 15% | 0.83× | $1.56 | $1.80 | $1.77–$1.83 | 0.99× | 0.50 | $2.03 | $30,177 | 0.13× |
| **Probability-weighted** | | | | **$2.16** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.74
- **Downside (worst scenario − price):** $-1.24
- **Expected value vs current** (weighted FV − price): $-0.88 (-28.9%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
