# INSW [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY = crude sleeve (65.4% of vessel value) + product sleeve (34.6%) AGGREGATED. Compared to the WHOLE-COMPANY tape price (not the crude-allocated proxy). Each sleeve is probability-weighted by its OWN sector's scenario weights (cross-sector independence; METHODOLOGY 6 v2, rank-1 pairing removed 2026-07-02).

- **Current price:** $77.78
- **Analyst target:** $79.50
- **NAV / share (reference, unflexed):** $52.59 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $48.00 (-38.3% vs price)
- **Breakeven TCE (scenario-invariant):** $262,407/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $65.76 | $77.87 | $73.97–$82.38 | 6.14× | 0.70 | $106.13 | $167,398 | 0.64× |
| Pre-MoU baseline | 20% | 0.82× | $50.79 | $52.57 | $50.75–$54.57 | 2.15× | 0.70 | $56.74 | $65,719 | 0.25× |
| MoU base case | 45% | 0.75× | $42.54 | $42.30 | $40.72–$43.96 | 1.77× | 0.70 | $42.17 | $48,249 | 0.18× |
| MoU bear | 25% | 0.71× | $39.55 | $38.53 | $36.88–$40.27 | 1.45× | 0.60 | $37.49 | $38,938 | 0.15× |
| **Probability-weighted** | | | | **$48.00** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.09
- **Downside (worst scenario − price):** $-41.71
- **Expected value vs current** (weighted FV − price): $-29.78 (-38.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

## Hybrid sleeve breakdown (v2 whole-company aggregation)

| Sleeve | Share | Allocated price | Weighted FV | EV% | Position |
|---|--:|--:|--:|--:|---|
| Crude | 65.4% | $50.89 | $29.50 | -42.0% | TRIM/SHORT |
| Product | 34.6% | $26.89 | $18.50 | -31.2% | TRIM/SHORT |
| **WHOLE-COMPANY** | 100% | **$77.78** | **$48.00** | **-38.3%** | **TRIM/SHORT** |

_Whole-company FV = crude FV + product FV (both per shares-outstanding); compared against the whole-company tape price, not the carved proxy. The product sleeve uses CLEAN trading rates (LR1/LR2 via clean curves, MR via its own scenario forwards). The product sleeve carries MORE downside than crude because product is leading the MoU rate normalisation (MR -52% w/w, LR2 -28% w/w as of 2026-05-29) — flagged in METHODOLOGY 6 v2._
