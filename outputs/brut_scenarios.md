# BRUT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $5.40
- **Analyst target:** $7.13
- **NAV / share (reference, unflexed):** $9.40 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $10.65 (+97.3% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $16.88 | $17.04 | $17.04–$17.04 | 8.44× | 0.70 | $17.42 | $337,500 | 110408278084394174132737015808.00× |
| Pre-MoU baseline | 45% | 1.11× | $12.71 | $13.00 | $13.00–$13.00 | 4.74× | 0.70 | $13.67 | $189,500 | 61992203546645028059620573184.00× |
| MoU base case | 18% | 0.74× | $1.73 | $2.35 | $2.35–$2.35 | 2.12× | 0.70 | $3.79 | $84,875 | 27765637340482830208191168512.00× |
| MoU bear | 12% | 0.70× | $0.33 | $0.99 | $0.99–$0.99 | 1.63× | 0.70 | $2.53 | $65,250 | 21345600429649538631751172096.00× |
| **Probability-weighted** | | | | **$10.65** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+11.64
- **Downside (worst scenario − price):** $-4.41
- **Expected value vs current** (weighted FV − price): $+5.25 (+97.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
