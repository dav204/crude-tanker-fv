# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (24.3%) + dry_bulk (72.3%) + containerships (3.3%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $14.10
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $15.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $15.64 (+10.9% vs price)
- **Breakeven TCE (scenario-invariant):** $54,299/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $21.18 | $21.51 | $20.81–$22.27 | 6.39× | 0.70 | $22.30 | $83,178 | 1.53× |
| Pre-MoU baseline | 45% | 1.11× | $16.53 | $16.13 | $15.56–$16.73 | 4.00× | 0.70 | $15.89 | $55,413 | 1.02× |
| MoU base case | 18% | 0.76× | $11.86 | $10.82 | $10.35–$11.28 | 1.86× | 0.70 | $9.69 | $32,877 | 0.61× |
| MoU bear | 12% | 0.72× | $10.10 | $8.81 | $8.43–$9.19 | 1.53× | 0.70 | $7.35 | $28,093 | 0.52× |
| **Probability-weighted** | | | | **$15.64** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+7.41
- **Downside (worst scenario − price):** $-5.29
- **Expected value vs current** (weighted FV − price): $+1.54 (+10.9%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
