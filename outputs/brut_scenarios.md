# BRUT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $5.21
- **Analyst target:** $7.13
- **NAV / share (reference, unflexed):** $8.80 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $10.24 (+96.6% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $16.28 | $17.17 | $16.85–$17.55 | 8.44× | 0.70 | $19.27 | $337,500 | 110408278084394174132737015808.00× |
| Pre-MoU baseline | 45% | 1.11× | $12.11 | $12.62 | $12.42–$12.84 | 4.74× | 0.70 | $13.79 | $189,500 | 61992203546645028059620573184.00× |
| MoU base case | 18% | 0.74× | $1.13 | $1.46 | $1.36–$1.54 | 2.12× | 0.70 | $2.22 | $84,875 | 27765637340482830208191168512.00× |
| MoU bear | 12% | 0.70× | $-0.27 | $0.07 | $-0.01–$0.15 | 1.63× | 0.70 | $0.85 | $65,250 | 21345600429649538631751172096.00× |
| **Probability-weighted** | | | | **$10.24** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+11.96
- **Downside (worst scenario − price):** $-5.14
- **Expected value vs current** (weighted FV − price): $+5.03 (+96.6%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
