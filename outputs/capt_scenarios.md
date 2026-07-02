# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $12.58
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $15.49 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $17.16 (+36.4% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $22.51 | $24.41 | $23.64–$25.30 | 7.00× | 0.70 | $28.86 | $246,237 | 104503259906263101432049696768.00× |
| Pre-MoU baseline | 45% | 1.11× | $18.55 | $19.32 | $18.84–$19.85 | 4.14× | 0.70 | $21.10 | $144,604 | 61370126211098908301425901568.00× |
| MoU base case | 18% | 0.75× | $8.51 | $8.33 | $8.08–$8.57 | 1.90× | 0.70 | $7.89 | $66,142 | 28070586167461704976268525568.00× |
| MoU bear | 12% | 0.71× | $7.25 | $7.20 | $6.94–$7.47 | 1.50× | 0.60 | $7.14 | $51,975 | 22058368362980608734652268544.00× |
| **Probability-weighted** | | | | **$17.16** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+11.83
- **Downside (worst scenario − price):** $-5.38
- **Expected value vs current** (weighted FV − price): $+4.58 (+36.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
