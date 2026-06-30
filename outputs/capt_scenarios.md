# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $12.73
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $15.59 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $17.26 (+35.6% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $22.63 | $24.54 | $23.76–$25.42 | 7.01× | 0.70 | $28.98 | $246,582 | 104547064316456429578132389888.00× |
| Pre-MoU baseline | 45% | 1.11× | $18.66 | $19.43 | $18.95–$19.96 | 4.14× | 0.70 | $21.21 | $144,771 | 61380769121813425805552779264.00× |
| MoU base case | 18% | 0.75× | $8.59 | $8.40 | $8.15–$8.64 | 1.90× | 0.70 | $7.96 | $66,208 | 28071266217373224329057140736.00× |
| MoU bear | 12% | 0.71× | $7.31 | $7.27 | $7.00–$7.54 | 1.50× | 0.60 | $7.21 | $52,019 | 22055091253178172371369984000.00× |
| **Probability-weighted** | | | | **$17.26** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+11.81
- **Downside (worst scenario − price):** $-5.46
- **Expected value vs current** (weighted FV − price): $+4.53 (+35.6%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
