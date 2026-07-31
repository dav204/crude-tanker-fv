# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $13.51
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $15.49 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.38 (-1.0% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $22.50 | $24.41 | $23.64–$25.30 | 7.00× | 0.70 | $28.88 | $246,248 | n/a |
| Pre-MoU baseline | 57% | 0.82× | $10.40 | $10.39 | $10.10–$10.69 | 2.32× | 0.70 | $10.36 | $81,128 | n/a |
| MoU base case | 5% | 0.75× | $8.51 | $8.33 | $8.08–$8.57 | 1.90× | 0.70 | $7.90 | $66,145 | n/a |
| MoU bear | 13% | 0.71× | $7.24 | $7.21 | $6.94–$7.47 | 1.50× | 0.60 | $7.15 | $51,979 | n/a |
| **Probability-weighted** | | | | **$13.38** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+10.91
- **Downside (worst scenario − price):** $-6.30
- **Expected value vs current** (weighted FV − price): $-0.13 (-1.0%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
