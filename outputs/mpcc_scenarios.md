# MPCC — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $2.42
- **Analyst target:** $2.63
- **NAV / share (reference, unflexed):** $2.02 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $2.11 (-13.0% vs price)
- **Breakeven TCE (scenario-invariant):** $108,107/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 1.02× | $2.09 | $2.26 | $2.22–$2.30 | 1.20× | 0.60 | $2.51 | $36,801 | 0.34× |
| Gradual normalization (base) | 40% | 0.97× | $1.93 | $2.19 | $2.15–$2.24 | 1.16× | 0.50 | $2.45 | $35,588 | 0.33× |
| Normalization + orderbook overhang | 20% | 0.93× | $1.79 | $2.04 | $2.00–$2.08 | 1.13× | 0.50 | $2.28 | $34,407 | 0.32× |
| Demand recession | 15% | 0.85× | $1.49 | $1.72 | $1.69–$1.75 | 0.99× | 0.50 | $1.95 | $30,187 | 0.28× |
| **Probability-weighted** | | | | **$2.11** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.16
- **Downside (worst scenario − price):** $-0.70
- **Expected value vs current** (weighted FV − price): $-0.31 (-13.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
