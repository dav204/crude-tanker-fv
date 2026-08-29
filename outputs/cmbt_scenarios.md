# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (23.8%) + dry_bulk (73.0%) + containerships (3.2%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $18.35
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $16.46 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $14.41 (-21.5% vs price)
- **Breakeven TCE (scenario-invariant):** $170,829/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $20.53 | $20.88 | $20.18–$21.64 | 6.38× | 0.70 | $21.70 | $82,119 | 0.48× |
| Pre-MoU baseline | 62% | 0.95× | $15.15 | $14.23 | $13.74–$14.73 | 2.26× | 0.70 | $12.77 | $41,233 | 0.24× |
| MoU base case | 0% | 0.86× | $12.40 | $11.23 | $10.76–$11.69 | 1.86× | 0.70 | $9.85 | $32,588 | 0.19× |
| MoU bear | 13% | 0.80× | $10.67 | $9.24 | $8.86–$9.62 | 1.53× | 0.70 | $7.55 | $27,852 | 0.16× |
| **Probability-weighted** | | | | **$14.41** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.53
- **Downside (worst scenario − price):** $-9.11
- **Expected value vs current** (weighted FV − price): $-3.94 (-21.5%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
