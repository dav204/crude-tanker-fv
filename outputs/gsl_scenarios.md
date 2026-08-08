# GSL — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $42.44
- **Analyst target:** $52.04
- **NAV / share (reference, unflexed):** $41.20 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $43.02 (+1.4% vs price)
- **Breakeven TCE (scenario-invariant):** $16,874/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 1.03× | $42.46 | $46.80 | $46.09–$47.52 | 1.44× | 0.60 | $53.32 | $56,354 | 3.34× |
| Gradual normalization (base) | 40% | 0.97× | $39.56 | $43.68 | $43.08–$44.28 | 1.38× | 0.60 | $49.86 | $53,880 | 3.19× |
| Normalization + orderbook overhang | 20% | 0.90× | $36.27 | $40.24 | $39.75–$40.73 | 1.30× | 0.60 | $46.19 | $50,793 | 3.01× |
| Demand recession | 15% | 0.87× | $35.18 | $38.70 | $38.31–$39.09 | 1.21× | 0.60 | $43.96 | $47,483 | 2.81× |
| **Probability-weighted** | | | | **$43.02** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.36
- **Downside (worst scenario − price):** $-3.74
- **Expected value vs current** (weighted FV − price): $+0.58 (+1.4%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
