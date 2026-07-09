# LPG Weight-Robustness Diagnostic (§9.10 — WO3 Phase 1)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked LPG Set A weights. Surfaces which LPG calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Shipped WITH the sector (family-from-birth, WO3 Phase 1).

**Axis:** US-export-arb vs orderbook overhang — the four scenarios' own parameter (arb_wide ↔ overhang / arb_collapse). Set A is the ratified evidence-first overhang-tilted lock (China PDH soft, ~30% orderbook contracted); LPG Set B brackets the arb-bull / PDH-recovery case; LPG Set C the deep-overhang case; both are ±~10pp shifts.

**Naming namespace:** labels are LPG families ("LPG Set …"); crude, LNG, and dry bulk each use "Set A/B" for their own — a bare unprefixed label would be a methodology error.

## No LPG names onboarded yet

The Phase-4 validators (Dorian LPG `LPG`, BW LPG `BWLP`) are not on the watchlist. The weight family is registered in `outputs/weight_robustness.yaml`; re-run this script after Phase 4 onboarding to populate per-name entries.

## Weight sets compared

| Scenario | Set A | Set B | Set C |
|---|--:|--:|--:|
| arb_wide | 0.15 | 0.25 | 0.10 |
| absorption_base | 0.35 | 0.35 | 0.28 |
| overhang | 0.35 | 0.28 | 0.45 |
| arb_collapse | 0.15 | 0.12 | 0.17 |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the LPG sector; crude / LNG / dry-bulk analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md` / `outputs/dry_bulk_weight_robustness.md`.
