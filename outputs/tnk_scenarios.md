# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $72.50
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $77.47 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $73.72 (+1.7% vs price)
- **Breakeven TCE (scenario-invariant):** $39,131/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $88.95 | $85.71 | $84.98–$86.54 | 4.23× | 0.70 | $78.13 | $134,435 | 3.44× |
| Pre-MoU baseline | 45% | 1.04× | $79.37 | $75.83 | $75.36–$76.34 | 2.82× | 0.70 | $67.58 | $89,207 | 2.28× |
| MoU base case | 18% | 0.75× | $66.16 | $61.22 | $60.86–$61.59 | 1.41× | 0.60 | $53.82 | $44,890 | 1.15× |
| MoU bear | 12% | 0.72× | $64.56 | $59.58 | $59.28–$59.89 | 1.20× | 0.60 | $52.13 | $38,241 | 0.98× |
| **Probability-weighted** | | | | **$73.72** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+13.21
- **Downside (worst scenario − price):** $-12.92
- **Expected value vs current** (weighted FV − price): $+1.22 (+1.7%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
