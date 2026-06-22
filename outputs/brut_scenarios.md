# BRUT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $5.40
- **Analyst target:** $7.13
- **NAV / share (reference, unflexed):** $9.40 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $10.80 (+100.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $16.88 | $17.74 | $17.41–$18.12 | 8.44× | 0.70 | $19.74 | $337,500 | 110408278084394174132737015808.00× |
| Pre-MoU baseline | 45% | 1.11× | $12.71 | $13.18 | $12.98–$13.40 | 4.74× | 0.70 | $14.26 | $189,500 | 61992203546645028059620573184.00× |
| MoU base case | 18% | 0.74× | $1.73 | $2.02 | $1.92–$2.11 | 2.12× | 0.70 | $2.69 | $84,875 | 27765637340482830208191168512.00× |
| MoU bear | 12% | 0.70× | $0.33 | $0.63 | $0.55–$0.71 | 1.63× | 0.70 | $1.32 | $65,250 | 21345600429649538631751172096.00× |
| **Probability-weighted** | | | | **$10.80** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+12.34
- **Downside (worst scenario − price):** $-4.77
- **Expected value vs current** (weighted FV − price): $+5.40 (+100.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
