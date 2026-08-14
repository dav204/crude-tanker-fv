# Tier Semantics Amendment — read-corroboration out of the tier

Date: 2026-08-13 · Repo: crude-tanker-fv (drafted against `410e78b`, 2026-08-13)
Amends: the 2026-06-30 tier wiring (`robust` ∈ TIGHT).
Interfaces with: governance dated rule 2026-06-29 (TRADE_PREREG #4) — governance-repo edits are a
separate work order (§6 here is routing text only, do not edit that repo from this one).
Status: owner-ratified ruling; implementation delegated to local agent. Suite must be green before
the RATIFY_LOG entry.

## 0. Ruling (for the record)

1. **Tier = estimate construction only.** VALIDATED-TIGHT / GOVERNED-WIDE / PROVISIONAL certify how
   the NAV is built: traced resale-uniform basis, sourced NAV-driving figures, on-convention,
   known-gap surfaces immaterial. A price movement may never change a tier. (Doctrine already on
   the books: ECO 2026-07-01 — "VALIDATED-TIGHT means the NAV is SOLID, NOT that ECO is cheap.")
2. **`robust` is real information in the wrong channel.** Read-agreement across the §17 bases
   corroborates the call, not the estimate — it is a function of where the price sits. It leaves
   the tier and ships as a standalone read-corroboration line beside `weight_sign_stable`, per the
   TNK precedent: the tier does not double-count it.
3. **The 2026-06-29 sizing seam is amended.** The WIDE cap applies to construction failures only.
   Read-flips carries its own sizing consequence (edge must clear the weaker basis for full
   discount-justified size). Where both bind, combine by min — two different defects may both cap,
   but neither re-prices the discount the other already priced.
4. **Why the 6/30 wiring was wrong:** it accepted two-basis read-agreement as "internal
   corroboration of comparable force" to a broker cross-foot. A broker cross-foot is estimate-level
   (their NAV vs ours); read-agreement is call-level, and the two coincide only at deep discounts —
   which is why the flaw stayed invisible until SBLK drifted into the seam. The valid half
   survives: an external broker cross-foot remains estimate-level evidence and may inform the tier
   where coverage exists, never as a requirement (APPROX-pnav still does not demote).

**Evidence base** (all repo-traced): `provenance.confidence_tier` gate; `justified_pnav.robust` =
`read == read_hist`; scorecard charter line "the FV's reliability for a sizing decision"; SB 0.60×
robust TIGHT vs SBLK 0.87× flips WIDE with SB the only wide-mark-node holder (PPMX, −1.5% NAV,
`ppmx_fit_seed_prereg_2026-07-18.md`); the 2026-08-13 SBLK demotion at the rebase with "every other
tier input unchanged and clean"; the +0.62% flip-back knife-edge ($27.72 boundary vs $27.89 close).
Under current wiring a 62 bp red open upgrades SBLK's grade — the label improves on adverse price
action hours after degrading on a data repair, NAV byte-identical through both. That is the reductio.

## 1. Code changes — `src/crude_tanker_fv/provenance.py`

* `confidence_tier()`: drop the `robust` parameter and remove it from the TIGHT gate. Retained
  logic, in order: sector-v1 lock → PROVISIONAL; figure-uncited / off-convention /
  scrubber-unverified queues → PROVISIONAL; `NEWBUILD_PRICE_PENDING` → GOVERNED-WIDE;
  `UNANCHORED_VALUE_CLASS_CAP` (§11.7.11) → GOVERNED-WIDE; then TIGHT ⇐ traced ∧
  ¬op_scrubber_material; else GOVERNED-WIDE. Update the rule-numbering comments (logs reference
  "falls through rule 2").
* Update the single production call site, `scorecard.py:217`, to the new signature.
* `TIER_SUBREASON`: remove the `read-flips` entries (SBLK, CMDB, GNK). Read state is computed live
  from §17 each run, not registered. All other subreasons (newbuild-indeterminate, basis-pending,
  etc.) stay. Annotate the SBLK GOVERNANCE SEAM comment block as superseded by this record; the
  demotion history stays in `sblk_log.md` as history.

## 2. `src/crude_tanker_fv/justified_pnav.py` — the §17 margin block

* `robust` property: unchanged. It is now the flag source ("the P1 deliverable" docstring stands).
* Add per-name, per-basis boundary prices from the documented band form (`FAIR_BAND = 0.10` at :84,
  band as a fraction of P/NAV(mkt)):
  * cheap|fair boundary price = `NAV × J_basis / (1 + FAIR_BAND)`
  * fair|rich boundary price = `NAV × J_basis / (1 − FAIR_BAND)`
* Add `flip_margin_pct`: signed % distance of the live price from the nearest boundary whose
  crossing would change the `robust` state. Worked example pinned as a test fixture: SBLK 8/13 —
  NAV 32.785, J_hist 0.930 → boundary $27.72, live $27.89 → +0.62%.

## 3. Hysteresis — governed flag, not the tier

* Print two columns: `robust` (instantaneous, truthful every run) and `read_flag` (governed).
  `read_flag` adopts the instantaneous state only when `|flip_margin_pct| ≥ READ_FLAG_HYST_PCT`
  beyond the transition; otherwise it holds prior state. Persist prior state in `state/` alongside
  the existing state files.
* New constant `READ_FLAG_HYST_PCT = 2.0` (owner-set at ratification; the SBLK ±0.6% strobe zone is
  the sizing motivation). Only `read_flag` is consumed by governance; `robust` is display.

## 4. `src/crude_tanker_fv/scorecard.py` — charter text and surface

* Rewrite the "Confidence tier (governance handoff)" paragraph: tier describes estimate
  construction only; the read-corroboration line stands beside it and beside
  `weight_sign_stable`, and the TNK sentence now covers both: the tier does not double-count them.
* Tier table: keep the Robust? column (it is §17 information) — it no longer implies the tier. Add
  the §17 margin block columns: `J_par`, `J_hist`, per-basis read, boundary price,
  `flip_margin_pct`, `read_flag`. (These currently reach paper nowhere — the table prints the
  verdict of the comparison but not the numbers compared. That gap closes here.)
* Summary metrics: print both counts — "construction-validated" (TIGHT) and "edge-cleared subset"
  (TIGHT ∧ robust ∧ BUY) — so the monitor keeps continuity with prior reports' actionable-surface
  line.

## 5. Tests and guards

* Price-invariance test (the point of the amendment): regenerate tiers under a price-only
  perturbation (±20% all names, inputs snapshot fixed) and assert every tier byte-identical. Name
  the regression: SBLK-2026-08-13.
* `tests/test_confidence_tier.py`: update the signature throughout; line 53 pins the old rule
  (`GNK … "flips (cheap/fair)" == GOVERNED-WIDE`) and must be rewritten to the new semantics (GNK:
  construction-clean → TIGHT regardless of read). Lines 35–51 update mechanically. List every
  changed assertion in the commit message.
* `tests/test_scorecard.py:82` (SB robust pin) is a §17 assertion — stays valid.
* Hysteresis unit test: a margin path crossing the boundary within ±HYST does not move
  `read_flag`; beyond it does.
* Guard: assert `read-flips` never re-enters `TIER_SUBREASON`.

## 6. Governance-repo clause (route separately — do not edit from this repo)

TRADE_PREREG #4 replacement text: "VALIDATED-TIGHT lets valuation bear full size only where
`read_flag` is robust; construction failures cap via tier (GOVERNED-WIDE caps size below what the
same discount would justify); read-flips caps independently (size to the weaker-basis read until
the edge clears it). Where both bind, apply the smaller authorization — the two caps never stack as
a repeated discount penalty." The weekly monitor consumes `read_flag`, not instantaneous `robust`.

## 7. Expected regen migrations — acceptance criteria

* SBLK, CMDB, GNK → VALIDATED-TIGHT, each carrying `read_flag = flips` (their only WIDE reason was
  read-flips). No other tier changes: structural / newbuild-pending / unanchored-cap /
  basis-pending WIDEs unchanged; PROVISIONALs unchanged; ECO TIGHT unchanged; SB TIGHT unchanged
  (PPMX stays in the mark-wide flag channel).
* The edge-cleared long set is {SB} before and after. This amendment relocates the constraint; it
  does not enlarge any position authorization. Assert this in the regen diff.
* Owner surfaces re-print under the new labels, surfaced not acted: the SBLK leg-2 trim GTC $31.30
  (instruction id 100) and the frozen 8/09 BUY→HOLD band-mech flip — the three-thread SBLK owner
  sitting stands as docketed.

## 8. Logs and ratification mechanics

* This file lands in `decisions/` unchanged. CHANGELOG entry summarizing §0. Per-name annotations
  in `sblk_log.md` / `cmdb_log.md` / `gnk_log.md`: tier restoration is a semantic amendment, not
  new information (the BRUT "mechanical move" language is the template). RATIFY_LOG entry after
  suite-green regen, owner countersigns.

## 9. Out of scope for the agent

No order changes, no GTC edits, no watchlist sizing edits, no governance-repo commits, no promotion
of `read_flag` into any prereg gate until the RATIFY_LOG entry exists. Full before/after tier table
in the commit message.

---

# ADDENDUM A — the `robust = "n/a"` case (owner ruling, 2026-08-13)

Amends §1, §2, §5, §7 of this record.

**Raised by the implementing agent before any code changed.** Simulating §1 as drafted showed it
promotes FIVE names, not three. Besides SBLK/CMDB/GNK, both **BRUT** and **CAPT** would have moved
GOVERNED-WIDE → VALIDATED-TIGHT, because their `robust` is `"n/a"` — the §17 read is blocked by the
`newbuild-heavy (unreliable)` guard, so `robust == "robust"` was false and they fell through to
WIDE on the retired leg. That would have promoted a going-concern-unfinanced, `POSITION_UNRELIABLE`
name to construction-validated, overturned the 2026-08-13 BRUT ruling by side effect, and left CAPT
TIGHT while still carrying a `newbuild-heavy` WIDE resolution-path subreason — breaking §7 on both
its clauses.

**RULING:** `robust = "n/a"` (§17-blocked) is a **CONSTRUCTION** fact and stays in the tier.
`robust = "flips"` is an **EDGE** fact and leaves it. **TIGHT gates on evaluability, never on
agreement.**

**§1 (revised):** `confidence_tier` does not take `robust`. It takes `read_blocked:
Optional[str]` — None when §17 evaluated; otherwise the blocking guard's label. TIGHT ⇐ traced ∧
¬op_scrubber_material ∧ `read_blocked is None`. Non-None `read_blocked` → GOVERNED-WIDE, with the
label printing as TIER_SUBREASON (CAPT: "newbuild-heavy"). BRUT remains GOVERNED-WIDE —
read-blocked here, and its 2026-08-13 STANDS ruling on the going-concern-unfinanced ground is
untouched and independently sufficient. The tier never sees what the read said; only whether a read
was producible.

**§2 (extended):** blocked names print the blocker label in the J/boundary/margin columns;
`read_flag = n/a`; no governed-flag state is persisted for them.

**§5 (extended):** the price-invariance test is hereby also the standing guard on future blockers —
any price-dependent guard later added to `evaluate()` will move a tier under the ±20% perturbation
and fail the suite. Comment the blocker set with the invariant: §17 blockers must be
price-independent.

**§7 (revised):** migrations are exactly {SBLK, CMDB, GNK} → VALIDATED-TIGHT, each with
`read_flag = flips`. BRUT and CAPT remain GOVERNED-WIDE. No other tier changes. Edge-cleared long
set is {SB} before and after. All other clauses of the work order stand as written.

**Supporting finding recorded at ruling time:** every blocking guard in `justified_pnav.evaluate`
(`nav<=0`, `no cost data`, `r≤g`, `no anchor`, `newbuild-heavy`, `negative mid-cycle EPS`,
`sub-growth returns`) is price-INDEPENDENT. Only the cheap/fair/rich read is price-dependent. That
is what lets `read_blocked` stay in the tier without reopening the hole this amendment closes, and
it is why §5's perturbation test is the right guard on the invariant.

---

## Implementation record (2026-08-14)

Landed as specified above, with Addendum A. Verified:

* **Migrations exactly {SBLK, CMDB, GNK} → VALIDATED-TIGHT**, each `read_flag = flips
  (cheap/fair)`; BRUT and CAPT hold GOVERNED-WIDE with subreasons `going-concern-unfinanced` and
  `newbuild-heavy`. 22 of 25 rows unchanged. Full table in the commit message.
* **Edge-cleared long set = {SB}** before and after. The report line reads
  "validated-and-actionable-long surface is **1 (SB — dry bulk, cheap on both NAV bases)**",
  alongside the new "**8 are construction-validated**" count.
* **Drift gate: 25 rows, 0 UNEXPLAINED, +0.0pp / +0.0% / stable on every row.** The amendment moved
  no NAV, no EV, no position band, no k_broker — it relocates a label, it does not move a number.
  No baseline re-anchor is warranted on the numbers.
* Handoff JSON `schema_version` 2.7 → **2.8** (additive: `read_flag`, `robust`, `flip_margin_pct`,
  `read_flag_hyst_pct`). `confidence_tier` keeps its name and its meaning-of-record, so a 2.7
  consumer still reads it correctly — it simply stops encoding the read. **Governance must migrate
  to `read_flag` for the edge cap** (§6, separate work order).

**Two items carried to the owner rather than decided here:**

1. **The edge-cleared filter gates on `read_flag == "robust"`, not §4's literal "TIGHT ∧ robust ∧
   BUY".** Taken literally that phrase admits TNK — robust, raw-BUY, but reading *rich/rich* and
   registered `POSITION_UNRELIABLE` — which would have enlarged the actionable surface, against
   §7. The filter also now *needs* an explicit robustness conjunct: before the amendment the tier
   gate kept every flipping name out of TIGHT, so `read_hist == "cheap"` was sufficient on its
   own; it no longer is.
2. **The §17 margin prices off the watchlist vintage, not the tape** — see the note below.

### Note: which price the margin measures

`justified_pnav` prices off the vintage-matched watchlist static (`as_of_price`/`current_price`),
not the daily overlay. SBLK's row therefore reports `flip_margin_pct = +3.18%` at the $28.60
watchlist vintage, while the +0.62% in §2 is the $27.89 tape close. Both are correct and they
measure different things:

* **+3.18% (row)** — how far the *current governed read* sits from flipping, at the same price the
  read itself is computed on. The deadband must use this, or the flag and the margin governing it
  would disagree.
* **+0.62% (tape)** — how far the read *would* sit from flipping once the watchlist rebases to
  today's tape. That is the forward-looking strobe warning, and it is the number §3 names as the
  sizing motivation.

The fixture pins the arithmetic with the tape scalars, so the +0.62% is regression-locked. But **as
built, the live surface does not flag the hazard §3 was written for**: SBLK reports +3.18%, outside
the ±2.0% deadband, so the strobe zone the ruling cites would not register on the report. Closing
that would mean surfacing a second, tape-basis margin as a forward-looking column — additive and
non-breaking, but beyond this work order. Flagged for the owner, not taken.
