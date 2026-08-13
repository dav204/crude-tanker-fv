# LNG Weight Robustness Diagnostic — Set B vs Set B-revised

**Purpose** (METHODOLOGY §13): the recurring per-LNG-name weight-
sensitivity diagnostic. Identifies which calls are weight-robust
(small EV% spread across plausible weight sets) vs weight-driven
(call would flip under reasonable alternative weights). Refresh at
the start of each quarterly cycle alongside the refresh checklist.

**Current production lock:** Set B-revised (v3, 2026-06-01).
Comparison reference: Set B (v2, prior lock, same day).

**Lock driver:** Ras Laffan Trains 4 & 6 (12.8 mtpa / ~17% of Qatar LNG) offline through end-summer 2026 at earliest; restart risk from subsurface complications. Partially offsets Cheniere Stage 3 ramp through H2 2026. Empirical pricing: spot $67.5k (+391% YoY), TFDE $98.5k — tight-market levels, not glut levels.

**Weights:**

| Scenario | Set B (v2, prior) | **Set B-revised (v3, current)** | Δ |
|---|--:|--:|--:|
| tight_resurgence | 0.10 | 0.15 | +0.05 |
| moderate_tightening | 0.15 | 0.25 | +0.10 |
| glut_base | 0.55 | 0.45 | -0.10 |
| glut_intensifies | 0.20 | 0.15 | -0.05 |
| structural_reset | 0.00 | 0.00 | +0.00 |

## FLNG — at price $29.50, target $25.00

**Per-scenario FV (identical under both weight sets — only weights change, scenario forwards unchanged):**

| Scenario | Vessel× | NAV/sh | FV (base) | Strip NPV | Assumed 12M TCE |
|---|--:|--:|--:|--:|--:|
| tight_resurgence | 1.25× | $41.93 | $39.36 | $33.37 | $147,500 |
| moderate_tightening | 1.13× | $35.59 | $33.67 | $31.75 | $78,750 |
| glut_base | 0.96× | $26.34 | $26.25 | $26.19 | $58,000 |
| glut_intensifies | 0.84× | $19.84 | $20.36 | $20.71 | $43,250 |
| structural_reset | 0.72× | $13.60 | $16.11 | $17.19 | $40,500 |

**Headline:**

| Metric | Set B | Set B-revised | Δ |
|---|--:|--:|--:|
| PW FV | $27.50 | $29.19 | $+1.69 (+6.2%) |
| EV% | -6.8% | -1.1% | +5.7pp |
| Position | TRIM/SHORT | HOLD | **FLIP** |

**Threshold analysis** (alpha = 0: Set B; alpha = 1: Set B-revised; FV is linear in weights so the convex combination is exact):

- HOLD threshold (FV ≥ $28.02, EV ≥ -5%): alpha ≥ **0.31**
- BUY threshold (FV ≥ $30.98, EV ≥ +5%): _not reachable on the [Set B → Set B-revised] line_

**Weights at the minimum HOLD threshold (alpha = 0.31):**

| Scenario | Weight at HOLD threshold | vs Set B |
|---|--:|--:|
| tight_resurgence | 0.116 | +0.016 |
| moderate_tightening | 0.181 | +0.031 |
| glut_base | 0.519 | -0.031 |
| glut_intensifies | 0.184 | -0.016 |
| structural_reset | 0.000 | +0.000 |

---

## CCEC — at price $22.59, target $25.17

**Per-scenario FV (identical under both weight sets — only weights change, scenario forwards unchanged):**

| Scenario | Vessel× | NAV/sh | FV (base) | Strip NPV | Assumed 12M TCE |
|---|--:|--:|--:|--:|--:|
| tight_resurgence | 1.25× | $50.28 | $47.20 | $40.03 | $136,327 |
| moderate_tightening | 1.13× | $38.81 | $39.08 | $39.35 | $73,865 |
| glut_base | 0.96× | $22.11 | $26.78 | $29.89 | $54,599 |
| glut_intensifies | 0.84× | $10.31 | $16.27 | $20.24 | $40,848 |
| structural_reset | 0.72× | $-1.37 | $6.00 | $10.90 | $37,815 |

**Headline:**

| Metric | Set B | Set B-revised | Δ |
|---|--:|--:|--:|
| PW FV | $28.57 | $31.34 | $+2.78 (+9.7%) |
| EV% | +26.5% | +38.7% | +12.3pp |
| Position | BUY | BUY | unchanged |

**Threshold analysis** (alpha = 0: Set B; alpha = 1: Set B-revised; FV is linear in weights so the convex combination is exact):

- HOLD threshold (FV ≥ $21.46, EV ≥ -5%): _not reachable on the [Set B → Set B-revised] line_
- BUY threshold (FV ≥ $23.72, EV ≥ +5%): _not reachable on the [Set B → Set B-revised] line_

---
