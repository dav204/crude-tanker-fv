"""Provenance / validation-state queues + the confidence tier — single source of truth.

The queues here are imported by the guards (test_newbuild_convention, test_scrubber_provenance,
test_manifest_provenance) AND by the confidence tier, so the two can never drift.

The **confidence tier** answers ONE question for portfolio-governance handoff: how the NAV is BUILT —
traced resale-uniform basis, sourced NAV-driving figures, on-convention, known-gap surfaces immaterial.
It reads FV-MATERIAL validation strength, NOT paperwork completeness (that is the guards' job — a row
can be a legitimate audit red while being tier-immaterial). **A price movement may never change a
tier** (tier semantics amendment 2026-08-13; ECO doctrine 2026-07-01 — "VALIDATED-TIGHT means the NAV
is SOLID, NOT that ECO is cheap"). Owner decision tree (2026-06-30, amended 2026-08-13):

  1. A NAV-driving FIGURE that does not trace — an uncited commitment/advance (figure-provenance
     queue) on a non-structural name, or a FIXABLE name still off the §9.6 curve (NAV on the wrong
     basis) -> **PROVISIONAL**. The number itself isn't sound; not handoff-ready, flag don't pass.

  2. Else, traced inputs (resale-uniform NAV basis) AND no FV-material untraced surface AND the §17
     justified-P/NAV multiple is EVALUABLE -> **VALIDATED-TIGHT**. APPROX-pnav does NOT demote: an
     external broker cross-foot is estimate-level evidence that may inform the tier where coverage
     exists, never a requirement (SB earns tightness without one).

  3. Else (traced but structurally incomplete — a structural-unavailable input, a §17-blocked name
     whose multiple cannot be produced at all, or an FV-material untraced surface) ->
     **GOVERNED-WIDE**. A directional anchor with a wide band (CMBT: APPROX + structural container class).

EVALUABILITY, NEVER AGREEMENT (Addendum A, 2026-08-13). Rule 2 asks whether a §17 read was
*producible*, not what it *said*. `read_blocked` (the blocking guard's label, else None) is a
CONSTRUCTION fact — a fleet whose multiple cannot be computed has a NAV the tier cannot certify.
Read AGREEMENT across the two §17 bases (`justified_pnav.robust`) is an EDGE fact — a function of
where the price sits — and has LEFT the tier; it ships beside `weight_sign_stable` as the
read-corroboration line and caps size independently. The tier never sees what the read said.
INVARIANT: every §17 blocker must be price-independent, or rule 2 leaks price back into the tier —
`test_tier_is_price_invariant` is the standing guard.

Materiality: an uncited OPERATING-scrubber flag widens the tier ONLY if its max possible FV error
(scrubber premium x uncited hulls on that name) is large relative to the sizing band. The common
immaterial case (a handful of hulls, sub-band) is a tracked paperwork item, not a tier input — it
must not drag a clean name (SB: ~5% NAV worst-case) into a wider tier.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import yaml

from .loaders import INPUTS_DIR

# --- Newbuild convention (clause 1/2 of test_newbuild_convention) ------------------------------
# FIXABLE names whose newbuilds have a curve mark but are not yet on-curve §9.6 (NAV on the wrong
# basis) + structural names pending commitment-net. (SB/SBLK/DHT have left; the structural CCEC/CMBT
# are handled via STRUCTURAL_NB_NAMES below, not as PROVISIONAL.)
OFF_CONVENTION_QUEUE = {"CMBT", "GSL", "STNG", "TEN"}  # NAT/ASC/ECO/HAFN left; TRMD left 2026-07-02. GSL ADDED 2026-08-08 (Q2 refresh): the 15-ship container NB program enters ADVANCES-ONLY (Group-B structural — no Ctr resale mark §A1.4; naive on-curve wiring reads −$200M-class PV-asymmetry artifacts on 4Q28-1Q30 deliveries) — queued for the SAME containers commitment-net pre-reg as CMBT; structural flag keeps the tier GOVERNED-WIDE, not PROVISIONAL.
SCRUBBER_UNVERIFIED_QUEUE: set[str] = set()   # NEWBUILD-value scrubber flag unverified (now empty)

# --- Operating-scrubber audit (test_scrubber_provenance) ---------------------------------------
OPERATING_SCRUBBER_VERIFIED = {"CAPT": 5, "TRMD": 85,   # name -> audited operating scrubber-fitted count
                               # ECO 16->17 at the 2026-08-08 Q2 refresh: Nissos Tigani
                               # delivered 5/26 -> operating; issuer aggregate in the 8/4
                               # H1 release ex-99.1 ("ten modern scrubber-fitted Suezmax
                               # tankers and eight modern scrubber-fitted VLCC tankers")
                               # covers the whole sailing fleet incl. Tigani + Vous ->
                               # Tigani/Vous flags issuer-evidenced (were peer-trap false).
                               "ECO": 17,
                               # STNG 2026-08-08: Q2 6-K (acc 0001628280-26-051064) fleet
                               # list per-vessel Scrubber column — 25/25 LR2 + 29/35 MR +
                               # 0/14 Handymax = 54 operating at the 74-hull census.
                               "STNG": 54,
                               # SB 20->19 at the 2026-07-31 Q2 refresh: the 20-F set is 21
                               # (all Capes + 13 non-Cape); at 6/30 Michalis H (scrubber Cape)
                               # is SOLD and Xenia (scrubber PPMX) is HFS -> 19 operating.
                               "SB": 19,
                               # LPG/BWLP verified AT onboarding (2026-07-10, WO3 Phase 4) — per-vessel
                               # issuer columns, not blanket flags: Dorian FY2026 10-K Item 4 fleet-table
                               # "Scrubber Equipped and/or Dual-Fuel" ("S" flags; 16 of 22 owned hulls);
                               # BW LPG FY2025 20-F fleet-table propulsion column ("Scrubber"; 10 parent
                               # + BW Kyoto + BW Loyalty = 12 of 39). Value-NEUTRAL for VLGC (scrubber
                               # premium 0, §11.10) — classified for the provenance gate, not for value.
                               # LPG 16->13 at the 2026-08-08 Q2 refresh: the Item-4 "S" set loses
                               # Corsair/Constellation/Clermont (HFS at 6/30, off-curve; Cobra was
                               # unlisted-false) — 13 operating of 18 on-curve.
                               "LPG": 13, "BWLP": 12}
OPERATING_SCRUBBER_QUEUE = {   # SB/ECO left 2026-07-01; TRMD left 2026-07-02 (FY2025 20-F "installed scrubbers on 85 of our vessels" = all 22 LR2 + all 63 MR)
    "DHT", "FRO", "GNK", "HAFN", "INSW", "SBLK", "TEN",
}   # STNG left 2026-08-08: the Q2 6-K fleet list has a per-vessel Scrubber column -> VERIFIED 54
# 2343 is deliberately NOT queued (2026-07-14): the queue tracks UNTRACED scrubber=TRUE flags;
# 2343 carries NONE — its AR2025 p.26 aggregate ("scrubbers fitted to our 35 core Supramax
# vessels") has no public per-vessel identification, so all flags are FALSE (the ECO-NB
# conservative-omission pattern, NOT the CAPT blanket-flag pattern). NAV understated ~$52.5M
# ≈ 2.5% (< the 10% gate). On per-vessel identification (IR query / Interim ESG tables):
# flip the 35 flags true and register VERIFIED{"2343": 35}.

# --- Un-anchored value-class cap (§11.7.11 Option B, 2026-07-14) --------------------------------
# Names with a MATERIAL sleeve marking on a class that has NO §9.9 transaction fit (broker-static
# curve). Their age-0 basis can be resale-uniform while the mid-age level is un-anchored, so the
# basis rollup alone would over-grade the tier to VALIDATED-TIGHT. confidence_tier caps these at
# GOVERNED-WIDE (sub-reason pending-anchor). An entry is REMOVED when its class's re-fit trigger
# fires and the §9.9 fit lands (2343: handy_bulk_txn_refit — Handy-Bulk is 51% of its hulls).
# BOUNDARY PRECEDENT (SB/PPMX, owner-ruled 2026-07-18 "Flag not cap"): this cap is for
# NO-fit classes only. A class with a real-but-WIDE fit registers in MARK_WIDE_NODES
# instead, and the holder's tier STANDS iff the registered band cannot flip the name's
# read (SB: BUY invariant across the whole PPMX leave-one-out space, worst edge ~+25%).
# A band edge that flips a read = cap territory. ppmx_fit_seed_prereg_2026-07-18.md §4.
UNANCHORED_VALUE_CLASS_CAP = {"2343"}

# --- NAV-equation figure provenance (test_manifest_provenance) ----------------------------------
# Names with an uncited estimate on a NAV-equation figure (lowercase, as the scan emits).
NAV_FIGURE_ESTIMATE_QUEUE = {"cmbt", "hafn"}  # FLNG LEFT 2026-08-25 (Q2 refresh at the frozen prereg: the Q1 "~$10M assumed" other-current-liabilities WC plug retired — all six WC components filing-cited to 6-K 0001628280-26-057822 F-3, net -$0.7M); BRUT LEFT 2026-08-13 (H1-2026: cash $11.828M sourced to Note 9 — the `cash-pending-H1-report` flag booked 7/01 resolved exactly at its pre-registered venue); nat/asc/stng left; trmd left 2026-07-02; ten left 2026-07-15 (full reconciliation vs Q1-2026 6-K condensed BS + FY2025 20-F — advances/WC/debt all filing-cited, NCI netted, 4 not-owned hulls out of the manifest; stays OFF_CONVENTION + OPERATING_SCRUBBER)

# Operating-scrubber materiality: max possible FV error as a fraction of NAV above which an uncited
# operating-scrubber surface widens the tier. Below it, the surface is a tracked-but-immaterial
# paperwork item (SB's ~5% sits below). Tuned so a handful of hulls is immaterial and a large
# uncited share of a fleet is material.
OPERATING_SCRUBBER_MATERIAL_PCT = 0.10

# --- Verdict labeling (consolidated scorecard read) — verified 2026-06-30 ----------------------
# The owner's three corrections to the verdict so the tiers DO their job and a skim can't misread:
#   (1) a NAV-relative cycle read is not a trade signal; (2) GOVERNED-WIDE is not a junk drawer —
#   each name's wideness maps to a resolution path; (3) a number derived off a CONTRADICTED figure
#   is void, not just unverified. Each set was classified per name from the filings/decision logs
#   and adversarially verified; the no-drift test asserts coverage so these can't silently rot.

# Derived NAV + broker gap are VOID (not merely unverified): a NAV-driving figure is CONTRADICTED
# by the name's OWN filing, so anything computed off it is known-suspect — struck in the verdict
# like the FV, and the position direction is void too. The verdict-rendering path (scorecard.py)
# stays as defensive coverage for the NEXT contradicted-figure name.
# NAT was here (the ~$17M advance was contradicted by the Q1-2026 cash flow) — DE-VOIDED 2026-06-30
# once the full 20-F/6-K reconciliation set advances->0 and sourced the balance sheet; the newbuild
# price (the only remaining unsourced number) is PARKED, not contradicted (see NEWBUILD_PRICE_PENDING).
NAV_DERIVED_VOID: set[str] = set()

# Position relabel — a TRIM/SHORT (or rich) position that is NOT an actionable directional short:
#   cycle-position : rich because §17 RONAV is through-cycle while price embeds the near-peak rate
#                    (§12) — a NAV-relative read, not a trade signal. Crude AND product near peak.
#   unreliable-read: a read that can't be trusted either way — a newbuild-heavy / PV-haircut method
#                    mismatch (MPCC — the tanker method on a containership's forward-committed book), OR a
#                    NAV built on stacked structural uncertainties (BRUT — a 0.59x "BUY" resting on a cash
#                    floor pending H1 AND going-concern doubt; the VLCC resale level, formerly the third
#                    leg, was CONFIRMED CURRENT 2026-07-15 [thread (d) signed] — two legs remain, and the
#                    eye-catching discount and the untrustworthiness are the SAME max-torque fact).
# Names NOT in either set print their raw TRIM/SHORT as a name-specific read (CAPT/CMBT/STNG at
# 2026-07-10) — the tier cell (⛔/sub-reason), handoff flag, and W-frag marker carry their caveats.
# (Was "not one is a name-specific short" — stale since the 2026-07-02 relabel rework; fixed 2026-07-10.)
POSITION_CYCLE_RELABEL = {"DHT", "FRO", "ECO", "INSW", "HAFN", "NAT",  # NAT: the §12 archetype (de-voided 2026-06-30). ASC left 2026-07-01: the reconciliation lifted NAV $15.96->$17.80, so it reads mildly CHEAP (0.90x), not rich -> raw BUY; the product-cycle caveat on the near-peak earnings/strip leg lives in asc_log, not a rich-relabel
                          "LPG", "BWLP"}  # 2026-07-10 (WO3 Phase-4 onboarding): both VLGC validators read rich AT a 1.59x war-elevated cycle (w_nav 0.70) — the same §12 late-cycle shape as DHT/FRO/ECO, not name-specific shorts; charter B-4 (read the sector honestly) cuts BOTH ways — no flattering tier, and no fake short signal either
POSITION_UNRELIABLE = {"MPCC", "BRUT",  # BRUT 2026-07-01: the position cell must reflect the untrustworthiness, not the 0.59x discount, so it can't sit as a raw BUY next to PROVISIONAL⛔NO (the ASC "rich·cycle" holdover lesson)
                       "CAPT", "TNK"}  # 2026-08-10 Stage-A halt disposition (owner RULED B,
# decisions/stage_a_halt_investigation_2026-08-10.md): the war-calibrated ABSOLUTE scenario
# deck against the re-anchored base makes the de-escalation legs near-no-ops — the BUY-ward
# flips (BRUT +44.3pp / CAPT +17.8 / TNK +5.0) are deck-incoherence ARTIFACTS, not signal.
# RETIRES for CAPT/TNK (and re-reads for BRUT) at the crude_day60_toll_cliff re-derivation
# (2026-08-16) which re-expresses the deck against the landed Stage-A base.

# Newbuild carried at $0 NAV pending a FILED contract price — the name discloses the order but not the
# price, and the only price is a broker LOI (not out of the figure-provenance queue), so the §9.6
# on-curve mark is unauthorized (CLAUDE.md). Both newbuild legs are PARKED, so the NAV rests entirely
# on sourced figures with the uncited number out of the equation. This is NOT a contradicted figure
# (not void) and NOT an uncited figure IN the NAV equation (not figure-PROVISIONAL) — it is a known,
# flagged indeterminate that makes the name a directional anchor, GOVERNED-WIDE, never TIGHT, until a
# filed price lets the newbuild go on-curve. NAT (owner decision 2026-06-30). Tier: newbuild-indeterminate.
NEWBUILD_PRICE_PENDING = {"NAT"}

# §9.9 WIDE curve nodes — a FITTED mid-age anchor whose value is EXTRAPOLATED (no prints at the
# node), machine-readable so age-node-dependent NAV can't print unmarked to the consumer (owner
# review 2026-07-09, finding 1: the flag lived only in YAML comments/prose while BW LPG's 2019-21
# hulls sit right on the node). Registry, not detection: an entry is placed by the marks decision
# record and removed when a print lands at the node (then the band is FIT, not extrapolated).
# age_window = fleet ages whose interpolated value has >=50% sensitivity to the node's anchor
# (linear interp: value(a) on [0,5] has d/d(5yr) = a/5, on [5,10] = (10-a)/5 -> [2.5, 7.5] for a
# five_year node). scorecard._mark_wide_exposure maps a fleet against this; the JSON emits
# mark_wide_nodes per name (schema 2.3).
MARK_WIDE_NODES = {
    "VLGC": {
        "node": "five_year",
        "age_window": (2.5, 7.5),
        "band_usd_m": (89.7, 95.9),      # fit 92.3; range across single-source exclusion cuts
        "reason": "age-5 anchor EXTRAPOLATED — zero 5-yr prints in the §9.9 sample "
                  "(only the BW Yushi option strike, a floor); slope carried by the "
                  "17-yr BW pair",
        "record": "decisions/vlgc_marks_2026-07-09.md",
        "added": "2026-07-09",
    },
    "Post-Panamax": {
        "node": "five_year+ten_year",
        "age_window": (2.5, 17.5),
        "band_usd_m": (18.1, 30.6),      # 10yr leave-one-out range; 5yr LOO 21.1-43.7
        "reason": "seeded fit's prints CLUSTER at ages 15-16 — both anchors "
                  "extrapolated with a wide leave-one-out band (one tc_attached "
                  "print swings the 5yr +/-30%); refit trigger ppmx_txn_refit armed",
        "record": "decisions/ppmx_fit_seed_prereg_2026-07-18.md",
        "added": "2026-07-18",
    },
}

# Tier sub-reason — why the band is wide / why PROVISIONAL, and thus the resolution PATH. Surfaced
# in the verdict's tier cell so GOVERNED-WIDE / PROVISIONAL aren't junk drawers.
#   structural-class : dominant class has no clean resale market (LNG/container Group-B) — not resolvable w/o a new data regime
#   newbuild-heavy   : justified leg can't price it (NAV PV-haircut vs strip full-year) — resolves only as hulls
#                  deliver. A §17 BLOCKER, so it is also derivable from read_blocked (tier_subreason falls back
#                  to the blocker label for any unregistered blocked name); CAPT/BRUT carry it live.
#   pending-anchor   : a sleeve's mark is unsourced but SOURCEABLE now (Thread 1A) — resolvable
#   basis-pending    : figures all sourced + queues cleared, but the name's product resale-curve marks are
#                  sourceable-but-pending (nav_basis 'pending-sourceable'; thread P1c product newbuild_contract
#                  marks) — GOVERNED-WIDE not TIGHT until those land (TRMD; the product analog of resale-uniform)
#   mixed            : two of the above (TEN: structural LNGC sleeve + pending-anchor Handy/LR1)
#   read-flips       : RETIRED 2026-08-13 (tier semantics amendment). A flipping read is an EDGE fact and no
#                  longer widens a tier, so it can never be a tier sub-reason; it ships as `read_flag` instead.
#   newbuild-indeterminate : newbuild parked at $0 pending a FILED price (NEWBUILD_PRICE_PENDING) — GOVERNED-WIDE
#   cash-pending : PROVISIONAL but sourced EXCEPT one NAV figure pending a known future issuer report
#                  (BRUT: cash → H1-2026 report 2026-08-13) — a well-specified "waiting" state, not "broken"
#   pool-gross-up-pending : PROVISIONAL — every figure sourced/decided EXCEPT operating WC, booked at a
#                  conservative floor because pool custodial receivables gross-up can't be netted from the
#                  filing (HAFN, pool operator); resolves when a filing discloses the pool net
#   void / uncited-figure / off-curve : the PROVISIONAL reasons (contradicted / uncited estimate / off the §9.6 curve)
TIER_SUBREASON = {
    "2343": "pending-anchor",   # Handy-Bulk sleeve (51% of hulls) un-anchored (§11.7.11);
                                # resolves at the handy_bulk_txn_refit §9.9 fit
    "GSL": "structural-class", "CCEC": "structural-class", "FLNG": "structural-class",
    "CMBT": "structural-class", "MPCC": "structural-class", "ASC": "structural-class",
    "CAPT": "newbuild-heavy",
    "INSW": "pending-anchor",
    "TEN": "mixed",
    # SBLK / CMDB / GNK "read-flips" entries REMOVED 2026-08-13 by the tier semantics amendment
    # (decisions/tier_semantics_amendment_2026-08-13.md). SUPERSEDED, not reversed on the facts:
    # the GOVERNANCE SEAM paragraph that stood here — TIGHT -> WIDE caps size below what the same
    # discount would justify — was the 2026-06-29 sizing rule applied to a READ defect. Read-flips
    # no longer demotes: it is an EDGE fact that caps size on its own channel (`read_flag`), while
    # the tier certifies construction only. The reductio that forced it: SBLK's demotion driver was
    # the WATCHLIST PRICE leg (25.20 -> 28.60, tool NAV byte-identical at $32.78) crossing the
    # cheap|fair boundary on the historical-mean basis at $27.72 — with the tape then sitting 0.62%
    # above it, a 62 bp red open would have UPGRADED the grade hours after a data repair degraded
    # it. Read state is now computed LIVE from §17 every run and never registered here. The demotion
    # history stays in decisions/sblk_log.md as history. The live leg-2 trim GTC at $31.30 is
    # surfaced to the owner, not acted on. Guard: test_read_flips_never_reenters_tier_subreason.
    # TNK: the 2026-07-31 "read-flips" entry was REGISTERED ON THE VOIDED half-applied
    # inputs (artifact FV 76.95/EV -3.8% -> family HOLD,HOLD,T/S,T/S,T/S,T/S) and died
    # with them at the 2026-08-08 paired transition: on both halves the family reads
    # 5/6 HOLD (one TRIM at the deepest bracket), the §17 two-basis read is robust, and
    # the tier computes VALIDATED-TIGHT. The residual at-fair-value fragility reaches
    # the consumer via weight_sign_stable=False (family EV range +3.4..-7.3 crosses 0)
    # — the D-M5/W-frag channel built for exactly this; the tier does not double-count
    # it. tnk_log 2026-08-08.
    "NAT": "newbuild-indeterminate",
    # BRUT 2026-08-13: `cash-pending` RETIRED — the H1-2026 report sourced cash to $11.828M
    # (Note 9), exactly at the resolution date the 2026-07-01 fork pre-registered. Clearing the
    # figure queue MECHANICALLY moved the tier PROVISIONAL -> GOVERNED-WIDE (the tier function
    # keys off the queue). That is the consequence of a correct pre-registered action, NOT a
    # tier ruling: RULED BY OWNER 2026-08-13 — GOVERNED-WIDE STANDS. The going-concern §15
    # doubt does NOT hold BRUT at PROVISIONAL independently of the cash flag; §15 stays a
    # prominent qualitative flag (and this subreason), not a tier floor. Note the governance seam: WIDE
    # caps size where PROVISIONAL was NO_DEPLOY-on-the-anchor (governance dated rule 2026-06-29),
    # so this is a live handoff change. The position cell stays POSITION_UNRELIABLE regardless.
    "BRUT": "going-concern-unfinanced", "HAFN": "pool-gross-up-pending",
    "STNG": "off-curve",
    "TRMD": "basis-pending",
    "LPG": "v1-lock-miss", "BWLP": "v1-lock-miss",
}  # ECO left 2026-07-01 -> VALIDATED-TIGHT (crude, resale-uniform). TRMD 2026-07-02: all 3 queues cleared, but
   # product nav_basis is pending-sourceable -> GOVERNED-WIDE·basis-pending (not TIGHT until the product marks land)
   # LPG/BWLP 2026-07-10 (WO3 Phase 4): figures fully cited at onboarding (per-name state would read
   # GOVERNED-WIDE·basis-pending — AGE0_BASIS pending-sourceable + the extrapolated age-5 node), but the
   # SECTOR v1 lock read 0/2 within +/-10% -> SECTOR_V1_UNLOCKED caps both at PROVISIONAL·v1-lock-miss;
   # resolution = the owner's Phase-5 lock ruling (accept the documented miss or re-fit off the trio splits)


def tier_subreason(ticker: str, read_blocked: Optional[str] = None) -> Optional[str]:
    """The resolution PATH behind a wide/provisional tier: registry first, else the §17 blocker.

    Addendum A (2026-08-13) prints a §17-blocked name's blocker label as its sub-reason, so a name
    the amendment holds WIDE on evaluability always explains itself. The registry still wins where
    an entry exists — it carries the owner's ruled ground (BRUT: going-concern-unfinanced, ruled
    STANDS 2026-08-13 and independently sufficient), which is more specific than the blocker."""
    registered = TIER_SUBREASON.get(ticker)
    if registered is not None:
        return registered
    if read_blocked is None:
        return None
    return read_blocked.split(" (")[0]


# Sectors whose v1 calibration lock has NOT passed (CLAUDE.md: new sectors ship >=70% of
# validators within +/-10% of broker NAV at lock-time). While a sector sits here its names
# are capped at PROVISIONAL — the WO3 letter ("document the miss and hold PROVISIONAL"):
# an unlocked sector may not hand off a governed FV regardless of per-name validation state.
# lpg: v1 lock 0/2 within +/-10% (LPG -20.4%, BWLP -17.2% — consistent direction;
# txn-anchored curve vs Pareto's May-2026 raised quotes, k_broker ~1.2). OWNER RULED
# 2026-07-10 (PLAN decision #1b, option (a)): documented miss ACCEPTED, sector holds here
# until the lock RE-RUNS off the Dorian trio per-vessel splits (trigger lpg_v1_lock_rerun,
# due 2026-11-13) — do NOT tune marks toward Pareto; the splits are the sanctioned re-fit
# path. lpg leaves ONLY via that owner-reviewed re-run (or a logged GOVERNED-WIDE amendment
# made WITH the re-fit evidence — never a blind loosening).
SECTOR_V1_UNLOCKED = {"lpg"}


def _structural_nb_names(inputs_dir: Path = INPUTS_DIR) -> set[str]:
    """Group-B newbuild names (no resale curve mark) — their commitment/advance figures are cited;
    their tier issue is the structural input, so they are GOVERNED-WIDE, never figure-PROVISIONAL."""
    doc = yaml.safe_load(open(inputs_dir / "market_data" / "newbuild_convention.yaml"))
    return {k.upper() for k in (doc.get("structural_exempt") or {})}


def confidence_tier(
    ticker: str,
    nav_basis: str,
    *,
    read_blocked: Optional[str] = None,
    op_scrubber_error_pct: float = 0.0,
    sector: str = "",
    inputs_dir: Path = INPUTS_DIR,
) -> str:
    """Compute the tier from the existing validation state (no new model).

    nav_basis / read_blocked come from the scorecard; op_scrubber_error_pct is the materiality
    (premium x uncited hulls / NAV). ``read_blocked`` is the §17 blocking guard's label when the
    justified-P/NAV multiple could not be produced, else None — EVALUABILITY, not agreement. What
    the read SAID (cheap/fair/rich, and whether it agrees across bases) is not an input here."""
    t = ticker.upper()
    structural = (t in _structural_nb_names(inputs_dir)) or (nav_basis == "structural-unavailable")

    # 0. Sector v1 lock cap — an unlocked sector's names hold at PROVISIONAL (WO3 Phase 5:
    # "document the miss and hold PROVISIONAL"); the per-name state below can't lift it.
    if sector in SECTOR_V1_UNLOCKED:
        return "PROVISIONAL"

    # 1. PROVISIONAL — an FV-material figure that does not trace, or NAV on the wrong basis.
    figure_uncited = (t.lower() in NAV_FIGURE_ESTIMATE_QUEUE) and not structural
    fixable_off_curve = (t in OFF_CONVENTION_QUEUE) and not structural
    if figure_uncited or fixable_off_curve or t in SCRUBBER_UNVERIFIED_QUEUE:
        return "PROVISIONAL"

    # 1b. NEWBUILD-INDETERMINATE — a newbuild parked at $0 pending a filed price. The NAV rests on
    # sourced figures (the uncited number is OUT of the equation), so it is not PROVISIONAL; but the
    # parked newbuild is a known indeterminate, so it is a directional anchor, never TIGHT.
    if t in NEWBUILD_PRICE_PENDING:
        return "GOVERNED-WIDE"

    # 1c. Un-anchored value-class cap (§11.7.11) — a material sleeve on a class with no §9.9
    # fit can carry a resale-uniform age-0 while its mid-age level is un-anchored; the rollup
    # alone would over-grade to TIGHT. Capped until the class's re-fit lands (registry above).
    if t in UNANCHORED_VALUE_CLASS_CAP:
        return "GOVERNED-WIDE"

    # 2. VALIDATED-TIGHT — traced + immaterial gap + an EVALUABLE §17 multiple. (Rule 2's content
    # changed at the 2026-08-13 amendment: it formerly also required two-basis read AGREEMENT, so
    # a log entry predating that reading "falls through rule 2" may mean the retired robust leg.)
    traced = nav_basis == "resale-uniform"
    op_scrubber_material = op_scrubber_error_pct > OPERATING_SCRUBBER_MATERIAL_PCT
    if traced and read_blocked is None and not op_scrubber_material:
        return "VALIDATED-TIGHT"

    # 3. GOVERNED-WIDE — traces, but structural / §17-unevaluable / FV-material untraced surface.
    return "GOVERNED-WIDE"


HANDOFF_READY = {"VALIDATED-TIGHT", "GOVERNED-WIDE"}


def is_handoff_ready(tier: str) -> bool:
    """A PROVISIONAL name must NOT hand off a governed FV — flag, don't pass."""
    return tier in HANDOFF_READY
