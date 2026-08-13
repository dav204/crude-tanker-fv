# GSL — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $41.24
- **Analyst target:** $52.04
- **NAV / share (reference, unflexed):** $41.20 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $42.88 (+4.0% vs price)
- **Breakeven TCE (scenario-invariant):** $3,362/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 1.02× | $42.26 | $46.64 | $45.93–$47.35 | 1.44× | 0.60 | $53.21 | $56,354 | 16.76× |
| Gradual normalization (base) | 40% | 0.96× | $39.38 | $43.53 | $42.93–$44.13 | 1.38× | 0.60 | $49.76 | $53,880 | 16.02× |
| Normalization + orderbook overhang | 20% | 0.89× | $36.12 | $40.11 | $39.62–$40.60 | 1.30× | 0.60 | $46.10 | $50,793 | 15.11× |
| Demand recession | 15% | 0.87× | $35.04 | $38.58 | $38.19–$38.97 | 1.21× | 0.60 | $43.88 | $47,483 | 14.12× |
| **Probability-weighted** | | | | **$42.88** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.40
- **Downside (worst scenario − price):** $-2.66
- **Expected value vs current** (weighted FV − price): $+1.64 (+4.0%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
