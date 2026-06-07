# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $70.80
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $83.32 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $69.31 (-2.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $96.26 | $92.19 | $91.47–$93.02 | 4.26× | 0.70 | $82.69 | $135,438 | 81134824786669751959438753792.00× |
| Pre-MoU baseline | 15% | 1.04× | $85.45 | $81.22 | $80.76–$81.74 | 2.83× | 0.70 | $71.36 | $89,350 | 53525439353503580750239236096.00× |
| MoU base case | 50% | 0.75× | $70.57 | $64.97 | $64.61–$65.34 | 1.42× | 0.60 | $56.57 | $45,090 | 27011042483329739080152907776.00× |
| MoU bear | 25% | 0.72× | $68.68 | $61.68 | $61.30–$62.05 | 1.19× | 0.50 | $54.67 | $37,903 | 22705917558781575738995769344.00× |
| **Probability-weighted** | | | | **$69.31** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+21.39
- **Downside (worst scenario − price):** $-9.12
- **Expected value vs current** (weighted FV − price): $-1.49 (-2.1%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
