# GSL — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $40.06
- **Analyst target:** $52.04
- **NAV / share (reference, unflexed):** $38.59 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $40.54 (+1.2% vs price)
- **Breakeven TCE (scenario-invariant):** $19,341/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 1.03× | $39.87 | $44.39 | $43.68–$45.10 | 1.44× | 0.60 | $51.16 | $56,335 | 2.91× |
| Gradual normalization (base) | 40% | 0.97× | $36.90 | $41.20 | $40.60–$41.80 | 1.38× | 0.60 | $47.66 | $53,862 | 2.78× |
| Normalization + orderbook overhang | 20% | 0.90× | $33.54 | $37.70 | $37.21–$38.19 | 1.30× | 0.60 | $43.95 | $50,777 | 2.63× |
| Demand recession | 15% | 0.87× | $32.42 | $36.14 | $35.75–$36.53 | 1.21× | 0.60 | $41.71 | $47,465 | 2.45× |
| **Probability-weighted** | | | | **$40.54** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.33
- **Downside (worst scenario − price):** $-3.92
- **Expected value vs current** (weighted FV − price): $+0.48 (+1.2%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
