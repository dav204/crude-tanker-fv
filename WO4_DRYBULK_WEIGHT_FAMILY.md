# WO4 — Dry-bulk weight-robustness family (§9.10) extension (charter-funded)

**Authority:** `portfolio-governance/funnels/sector_charter_2026H2.md`, Part-B verdict `fd0277f`
(2026-07-06/DV) — the **dry-bulk deepening half** of this cycle's 50/50 validation-labor split.
Specific driver: the consumer-side rubric `portfolio-governance/funnels/drybulk_2026H2_rubric.md`
(binding blind commit **f54e797**), Gate E screen-resolution #3, verbatim: *"the §9.10 weight family
does NOT yet cover dry bulk — extending it is the FIRST work item of the dry-bulk deepening half
(producer-side). Census + Gates A–D proceed meanwhile; Gate E cannot complete for any candidate until
the family ships. Blocked-on, not waived."*

**What this buys: the §9.10 weight-robustness diagnostic for the dry-bulk sector**, so the consumer's
Gate E can read `weight_sign_stable` / `ev_pct_family_min` / `ev_pct_family_max` for any dry-bulk name.
Gate E's "sign-flip at desk depth = FAIL" maps **directly** to `weight_sign_stable == false`. It
authorizes ZERO capital and changes NO production weight.

**Read before starting — the one thing this WO must not become.** This is a *diagnostic*, not a
recalibration. Crude/product/LNG run their names under bracketing weight sets to MEASURE whether the
position survives, then leave the production lock exactly where it is. Do the same. If the diagnostic
finds a dry-bulk name is weight-driven, that is a *finding to report* (and a Gate-E input), **not** a
license to move Bulk Set A. Reweighting dry bulk is a separate §11.7.x revision with its own lock
test — explicitly out of scope here.

**Kill-switches (consumer-side register `portfolio-governance/funnels/register.md`):**
- **R-1:** dry-bulk orderbook/fleet > **16%** (dwt) → the dry-bulk half is VOID — stop, log where you stopped.
- **R-5:** charter expires **2026-12-26** — no evergreen status.

**Labor budget:** part of the 50% dry-bulk deepening half. A CONTAINED job — one diagnostic script +
one lock test + a validation run, on machinery that already generalizes across sectors. NOT a sector
onboarding (dry bulk is a full existing stack); scope it as well under one reconciliation cycle.

---

## Existing assets (verified 2026-07-07 by two read-only surveys — do not rebuild)
- **The scorecard seam is DONE and sector-generic.** `src/crude_tanker_fv/scorecard.py`:
  `weight_family_basis()` (:308–333) SHA-stamps the family against `scenario_inputs.yaml` and withholds
  fields when stale (WO1-F4); `load_weight_fragility()` (:372–397) reads any family; `_write_handoff_json()`
  (:784–791) emits `weight_sign_stable` / `ev_pct_family_min` / `ev_pct_family_max` for ANY family in the
  sidecar. `tests/test_scorecard.py::test_weight_fragility_flag_renders_and_reaches_the_json` (:353) proves
  the seam. **No scorecard code changes** — the fields are null for dry bulk only because the sidecar has
  no dry-bulk entries.
- **The engine is sector-agnostic.** `src/crude_tanker_fv/scenarios.py`: `SCENARIO_CLASS_MAP_BY_SECTOR["dry_bulk"]`
  is already wired (:77); `_run_ticker_under_scenario_mix()` / `run_scenarios()` route any sector via its
  class map. The crude per-ticker override pattern (`modified_docs["crude"] = doc_with_weights(...)`,
  `scripts/crude_weight_robustness.py:136–142`) works verbatim with `"dry_bulk"` substituted.
- **The sidecar merger is generic.** `scorecard.py::update_weight_fragility_sidecar(family, weight_sets, names)`
  (:336) accepts `"dry_bulk"` and stamps `scenario_inputs_sha()`.
- **Production Bulk Set A is locked and FFA-calibrated.** `inputs/scenario_inputs.yaml`
  `sectors.dry_bulk.scenarios.<s>.weight`: **china_acceleration 0.2 / moderate_growth 0.4 (base) /
  china_property_drag 0.25 / coordinated_slowdown 0.15** (locked 2026-06-09; METHODOLOGY §11.7.4:1603).
  The strip already sits within ±5% of the traded FFA on 8/9 legs (§11.7.8) — that calibration is the
  guardrail, untouched by this WO.
- **Templates to mirror:** `scripts/crude_weight_robustness.py` (5 sets / 10 tickers — the fullest),
  `scripts/product_weight_comparison.py` (3 sets), `scripts/lng_weight_comparison.py` (3 sets). The
  dry-bulk script parallels these.

## Phase 0 — Name the sensitivity axis + define the bracketing sets (methodology decision; write it down first)
The one analytical decision. METHODOLOGY §11.7.4 states the locked weights but does not name the axis
the family should span. **Recommended axis: China dry-bulk demand tension** — it is the axis the four
scenarios already parameterize (china_acceleration ↔ china_property_drag / coordinated_slowdown), and it
is the charter thesis's own load-bearing variable (Simandou ton-mile + supply discipline read against
China property/steel drag). Define, **sector-namespaced** ("Bulk Set B (…)", never a bare "Set B" — a
cross-sector unprefixed name is a methodology error):
- **Bulk Set A (locked, 2026-06-09)** — the production prior; 0.2 / 0.4 / 0.25 / 0.15.
- **Bulk Set B (China-bull / super-cycle bracket)** — mass toward china_acceleration + moderate_growth.
- **Bulk Set C (China-property-drag bracket)** — mass toward china_property_drag + coordinated_slowdown.
- *(Optional Bulk Set D)* — only if the two brackets leave an obvious defensible gap on the axis.
Two bracketing sets are the §9.10 minimum ("current lock plus 2–3 bracketing alternatives"). Each set
must be **defensible** (a ±5–10pp reweighting a reasonable analyst would actually hold), not a strawman.
The sets live in the SCRIPT, never in `scenario_inputs.yaml` — production stays locked.

## Phase 1 — The diagnostic script
Create `scripts/dry_bulk_weight_comparison.py`, parallel to `crude_weight_robustness.py`:
- `DRY_BULK_TICKERS = ["SBLK", "GNK", "CMDB", "SB"]` — the four valued dry-bulk names (`inputs/watchlist.yaml`).
  Census-only names (SHIP / DSX / EDRY / PANL / HSHP) are not onboarded and get no read until they are.
- `DRY_BULK_WEIGHT_SETS` = the Phase-0 dict.
- Per ticker × per set: run the production path via `_run_scenarios_for_ticker(…, modified_docs, …)` with
  `modified_docs["dry_bulk"] = doc_with_weights(base, weights)`; record PW FV / EV% / position.
- Classify **weight-robust** (position identical across all sets) vs **weight-driven** (position flips),
  per §9.10; emit the markdown/table output the peer scripts emit; call
  `update_weight_fragility_sidecar("dry_bulk", DRY_BULK_WEIGHT_SETS, entries)`.

## Phase 2 — Lock test
Add `tests/test_scenarios.py::test_dry_bulk_locked_weights_position()` — analogue to
`test_flng_v3_locked_weights_position` (:296): pin a dry-bulk pure-play's (SBLK or GNK) position under the
locked Bulk Set A, so a future reweight surfaces as a deliberate methodology choice, not a silent regression.

## Phase 3 — Populate + verify the seam
- Run the diagnostic; confirm `outputs/weight_robustness.yaml` carries dry-bulk entries with a
  `computed_against` SHA matching current `scenario_inputs.yaml`.
- Run the scorecard handoff; confirm `outputs/book_scorecard.json` shows non-null `weight_sign_stable` /
  `ev_pct_family_min` / `ev_pct_family_max` for SBLK/GNK/CMDB/SB (schema stays 2.2). `pytest -q` green
  including the new lock test and the existing `test_weight_fragility_flag_renders_and_reaches_the_json`.
- **Production-lock guard (the discipline check):** confirm Bulk Set A in `scenario_inputs.yaml` is
  byte-for-byte unchanged and the locked strip still passes the FFA calibration band (a no-op if
  production wasn't touched — that IS the point). The bracketing sets are diagnostic-only and are NOT
  required to pass FFA.

## Definition of done
`outputs/weight_robustness.yaml` carries a current-SHA dry-bulk family · `book_scorecard.json` emits
non-null family fields for the four valued dry-bulk names (and will for any future-onboarded dry-bulk
candidate — this is what unblocks the consumer's Gate E) · `test_dry_bulk_locked_weights_position`
pinned · full pytest green · RATIFY_LOG + CHANGELOG entries · PLAN.md updated.

**Non-goals / frozen — do not touch while doing weight-family work:**
- the **locked Bulk Set A** production weights (reweighting is a separate §11.7.x revision + lock test);
- the **§11.7.10 dwt-scaling** curves (value, not weight — Newcastlemax double-count risk);
- the **Post-Panamax sub-class** question (known contained over-valuation limit, SBLK ~+1.3% net;
  refinement pending only if SBLK's post-Panamax book grows);
- the **FFA-OCR tenor/tick model** (locked Stage 1, §11.7.8).

Any of those surfacing as *needed* is a finding to report to the owner, not in-scope work.
