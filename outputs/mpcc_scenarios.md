# MPCC — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $2.78
- **Analyst target:** $2.63
- **NAV / share (reference, unflexed):** $2.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $1.96 (-29.6% vs price)
- **Breakeven TCE (scenario-invariant):** $350,590/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 1.02× | $2.34 | $2.19 | $2.17–$2.22 | 1.20× | 0.60 | $1.98 | $37,118 | 0.11× |
| Gradual normalization (base) | 40% | 0.97× | $2.17 | $2.01 | $1.98–$2.03 | 1.16× | 0.50 | $1.84 | $35,889 | 0.10× |
| Normalization + orderbook overhang | 20% | 0.93× | $2.02 | $1.86 | $1.84–$1.88 | 1.13× | 0.50 | $1.71 | $34,690 | 0.10× |
| Demand recession | 15% | 0.85× | $1.70 | $1.57 | $1.55–$1.58 | 0.99× | 0.50 | $1.44 | $30,437 | 0.09× |
| **Probability-weighted** | | | | **$1.96** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.59
- **Downside (worst scenario − price):** $-1.21
- **Expected value vs current** (weighted FV − price): $-0.82 (-29.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
