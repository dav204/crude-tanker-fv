# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (24.3%) + dry_bulk (72.3%) + containerships (3.3%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $14.10
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $15.26 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $15.66 (+11.0% vs price)
- **Breakeven TCE (scenario-invariant):** $54,596/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $21.16 | $21.52 | $20.82–$22.28 | 6.39× | 0.70 | $22.36 | $83,200 | 1.52× |
| Pre-MoU baseline | 45% | 1.11× | $16.52 | $16.15 | $15.57–$16.74 | 4.00× | 0.70 | $15.95 | $55,426 | 1.02× |
| MoU base case | 18% | 0.76× | $11.85 | $10.84 | $10.37–$11.30 | 1.86× | 0.70 | $9.74 | $32,882 | 0.60× |
| MoU bear | 12% | 0.72× | $10.09 | $8.82 | $8.44–$9.20 | 1.53× | 0.70 | $7.40 | $28,098 | 0.51× |
| **Probability-weighted** | | | | **$15.66** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+7.42
- **Downside (worst scenario − price):** $-5.28
- **Expected value vs current** (weighted FV − price): $+1.56 (+11.0%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_
