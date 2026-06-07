# TRMD — Scenario Fair Value (scenario framework)

- **Current price:** $28.20
- **Analyst target:** $25.00
- **NAV / share (reference, unflexed):** $26.74 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $25.59 (-9.3% vs price)
- **Breakeven TCE (scenario-invariant):** $58,812/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| refinery_squeeze | 15% | 1.25× | $36.08 | $40.58 | $38.77–$42.68 | 4.59× | 0.70 | $51.07 | $109,834 | 1.87× |
| moderate_correction | 25% | 1.16× | $32.77 | $34.18 | $33.08–$35.44 | 2.85× | 0.70 | $37.49 | $66,209 | 1.13× |
| Glut base case | 45% | 0.81× | $19.81 | $19.33 | $18.57–$20.13 | 1.57× | 0.70 | $18.21 | $34,244 | 0.58× |
| demand_softening | 15% | 0.74× | $16.85 | $15.07 | $14.22–$16.00 | 1.12× | 0.50 | $13.28 | $24,111 | 0.41× |
| structural_decline | 0% | 0.65× | $13.66 | $11.69 | $11.13–$12.50 | 0.94× | 0.50 | $9.73 | $20,074 | 0.34× |
| **Probability-weighted** | | | | **$25.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+12.38
- **Downside (worst scenario − price):** $-16.51
- **Expected value vs current** (weighted FV − price): $-2.61 (-9.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
