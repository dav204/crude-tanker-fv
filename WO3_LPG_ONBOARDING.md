# WO3 — LPG/VLGC sector onboarding (charter-funded)

**Authority:** `portfolio-governance/funnels/sector_charter_2026H2.md`, Part-B verdict `fd0277f`
(2026-07-06/DV): this cycle's validation labor SPLIT 50% dry-bulk deepening / **50% LPG (VLGC-first)**.
**What this buys: governed valuation surface.** It authorizes ZERO capital and implies no position.
**Read before starting, verbatim from the charter's B-4:** the LPG half was chosen partly for its low
infra cost ("under the streetlight") — *"the allocation should not be read as a supply call on VLGCs."*
The sector's market cells are adverse (~30% VLGC orderbook, avg age 11.7y, no scrappage lever). The
engine's job here is to read the sector honestly, not to justify the allocation.

**Kill-switches (consumer-side register `portfolio-governance/funnels/register.md`):**
- **R-2:** VLGC orderbook/fleet > **38%** (units) → the LPG half is VOID — stop work, log where you stopped.
- **R-5:** charter expires **2026-12-26** — no evergreen status; unfinished work needs a new charter.

**Labor budget:** 50% of the cycle's validation labor (the other half is the dry-bulk funnel,
consumer-side rubric). Suggested shape: Phase 0 one session (time-boxed, per the sector-onboarding
workflow); Phases 1–5 ≈ one reconciliation cycle per validator.

---

## Existing assets (verified 2026-07-05, charter evidence packet — do not rebuild)
- **Rate feed EXISTS:** `pareto_daily.csv` already parses `vlgc_me_asia_usd_day` +
  `vlgc_usgom_asia_usd_day` (+ propane/LPG-import columns) daily. No new parser needed for VLGC spot.
- **Consensus anchors EXIST:** Pareto prints P/NAV for **BWLP (1.02), Dorian LPG (1.01), NVGS (0.86)**
  (`pareto_share_prices.csv`, 2026-06/07 rows; consensus-pair recapture `6314357` refreshed vintages Jul-3).
- **MGC class precedent:** `sectors.lng.scenarios.*.mgc` + MGC 10-yr mean ($20k) — the small-gas class
  framework exists; **no VLGC class exists** (the named build).
- **Lock bar pre-named:** CLAUDE.md:74 — "new sectors (dry bulk / containers / **LPG** / offshore) ship
  ≥70%/±10% v1" — LPG has been on the producer's own list since the bars were written.

## Phase 0 — Methodology decision doc FIRST (one session, time-boxed; per WORKFLOWS.md)
Decide and write down, before any YAML:
1. **Sector definition & scope:** v1 = **VLGC-first** (per charter). Midsize/ethane (NVGS) and small
   pressurized (GASS) are OUT of v1 scope — different classes, different trades; note them for a later
   phase or never. State the classes v1 will value: VLGC (+MGC if a validator carries them).
2. **Cycle-anchor basis:** pick and name it (the book already spans 3 incompatible bases —
   `delta_report.md` caveat; §10 TC-anchored-not-spot applies). A VLGC 12M-TC series + 10-yr mean must
   be SOURCED and CITED (Compass/Poten/Clarksons-class; the daily spot columns are not a TC anchor).
3. **Demand-scenario axis:** LPG is a **demand-story sector** (US NGL export arb, petchem/PDH buildout,
   Panama transit) — name the scenario family's driver honestly; do NOT clone the dry-bulk China axis.
4. **Charter-book convention:** VLGC fleets carry meaningful time-charter cover — decide the
   §11.8.6-style convention (or its LPG variant) up front.
5. **Governance screen (§15):** BW group structure (BW Group bloc in BWLP) gets the standard screen.

## Phase 1 — Scenario family + routing
- `sectors.lpg` in `inputs/scenario_inputs.yaml`: 4 scenarios, weights **sector-namespaced**
  ("**LPG Set A (<driver>)**" — a bare "Set A" is a methodology error per CLAUDE.md).
- Weight-family coverage from birth: the schema-2.2 handoff carries `ev_pct_family_min/max` +
  `weight_sign_stable` — ship the §9.10 weight-robustness family WITH the sector, not as a retrofit
  (dry bulk's missing family fields are the counterexample the consumer keeps hitting).

## Phase 2 — Marks: the VLGC class
- New age-value curve for VLGC in `vessel_value_curves.yaml`.
- **§9.9 bar applies:** transaction-anchored fits require a comparable sample. Run `sp_scan --names` +
  the S&P print harvest for VLGC transactions → human-classified into `transactions/vlgc.yaml`. If the
  sample is insufficient, **v1 ships on-curve un-anchored with the basis documented** (the LNG sector's
  deliberate precedent) — do NOT force a fit, do NOT back-solve to Pareto NAVs (the SBLK lesson).
- Age-0 basis: the uniform xclusiv Resale line if a VLGC resale print exists; else flag the basis
  divergence explicitly (AGE0_BASIS guard).

## Phase 3 — Rates plumbing
- Promote the existing `vlgc_*` daily columns into `twelve_month_tc.yaml` inputs under a **documented
  tenor rule** (the dry-bulk 2-Jul FFA promotion is the precedent). Spot→TC dampening per the
  charter-book convention from Phase 0.

## Phase 4 — Validators (two, per the lock)
1. **Dorian LPG (`LPG`, NYSE, 10-K — EDGAR CIK 1596993):** pure VLGC, cleanest first validator.
2. **BW LPG (`BWLP`, Oslo primary + NYSE, 20-F — EDGAR CIK 1649313):** second validator; §15 screen
   on the BW Group bloc.
- Standard `/add-ticker` flow each: fleet manifest (per-vessel, **every NAV-moving figure cited or
  estimate-flagged** — the figure-provenance queue rule; no "(confirmed)" without a trace), balance
  sheet from the latest filing (trust the report, not the fleet page), cost structure, dividend policy,
  watchlist row with **same-vintage price+pnav+fwd_pe** (Pareto pairs already print — rebase together,
  never mix vintages).
- NVGS/GASS: census-noted, NOT onboarded in v1.

## Phase 5 — Gates & lock
- Full pytest green (drift gate included); `/reconcile` SANITY = OK both validators; drift-gate
  baseline re-ratified with cause (`./scripts/ratify_baseline.sh "WO3 LPG v1 onboarding"`).
- **v1 calibration lock: ≥70% of validators within ±10% of broker NAV at lock time** (CLAUDE.md:74).
  With 2 validators that means both, or document the miss and stop at PROVISIONAL.
- Names land **PROVISIONAL by definition** until reconciled; tier decision tree assigns
  GOVERNED-WIDE / VALIDATED-TIGHT on its own merits. The consumer reads tiers + family fields from
  `book_scorecard.json` — **the tier is the product.** A PROVISIONAL or ⚠ read is a legitimate outcome;
  see the charter's B-4 (do not let the allocation's existence argue for a flattering tier).

## Definition of done
`sectors.lpg` live · VLGC class valued on a documented basis · rates promoted under a tenor rule ·
LPG + BWLP on the watchlist at SANITY-OK with same-vintage consensus pairs · family/W-frag fields
populated · v1 lock passed (or the miss documented and the sector held at PROVISIONAL) · RATIFY_LOG +
CHANGELOG entries · PLAN.md updated. **Non-goals:** any position, any consumer-side cap, NVGS/GASS
onboarding, forcing a txn-anchored fit without a §9.9 sample.
