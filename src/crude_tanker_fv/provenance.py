"""Provenance / validation-state queues + the confidence tier — single source of truth.

The queues here are imported by the guards (test_newbuild_convention, test_scrubber_provenance,
test_manifest_provenance) AND by the confidence tier, so the two can never drift.

The **confidence tier** answers ONE question for portfolio-governance handoff: how much can a sizing
decision lean on this FV. It reads FV-MATERIAL validation strength, NOT paperwork completeness (that
is the guards' job — a row can be a legitimate audit red while being tier-immaterial). Owner decision
tree (2026-06-30):

  1. A NAV-driving FIGURE that does not trace — an uncited commitment/advance (figure-provenance
     queue) on a non-structural name, or a FIXABLE name still off the §9.6 curve (NAV on the wrong
     basis) -> **PROVISIONAL**. The number itself isn't sound; not handoff-ready, flag don't pass.

  2. Else, traced inputs (resale-uniform NAV basis) AND a STRONG corroboration -- external (broker
     P/NAV) OR internal (justified P/NAV robust across BOTH bases) -- AND no FV-material untraced
     surface -> **VALIDATED-TIGHT**. APPROX-pnav does NOT demote here: the missing broker check is
     replaced by the two-basis internal corroboration (SB earns tightness internally).

  3. Else (traced but no strong corroboration — a structural-unavailable input that breaks the second
     basis, a read that flips between bases, or an FV-material untraced surface) -> **GOVERNED-WIDE**.
     Usable as a directional anchor, but the band is wide (CMBT: APPROX + structural container class).

Materiality: an uncited OPERATING-scrubber flag widens the tier ONLY if its max possible FV error
(scrubber premium x uncited hulls on that name) is large relative to the sizing band. The common
immaterial case (a handful of hulls, sub-band) is a tracked paperwork item, not a tier input — it
must not drag a clean name (SB: ~5% NAV worst-case) into a wider tier.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from .loaders import INPUTS_DIR

# --- Newbuild convention (clause 1/2 of test_newbuild_convention) ------------------------------
# FIXABLE names whose newbuilds have a curve mark but are not yet on-curve §9.6 (NAV on the wrong
# basis) + structural names pending commitment-net. (SB/SBLK/DHT have left; the structural CCEC/CMBT
# are handled via STRUCTURAL_NB_NAMES below, not as PROVISIONAL.)
OFF_CONVENTION_QUEUE = {"CMBT", "HAFN", "STNG", "TEN", "TRMD"}  # NAT left 2026-06-30 (parked, NEWBUILD_PRICE_PENDING); ASC left 2026-07-01 (April subsequent event, no 3/31 NB); ECO left 2026-07-01 (2 Suezmax NBs wired on-curve §9.6 via years_to_delivery, figures issuer-verified)
SCRUBBER_UNVERIFIED_QUEUE: set[str] = set()   # NEWBUILD-value scrubber flag unverified (now empty)

# --- Operating-scrubber audit (test_scrubber_provenance) ---------------------------------------
OPERATING_SCRUBBER_VERIFIED = {"CAPT": 5, "SB": 20, "ECO": 16}   # name -> audited operating scrubber-fitted count
OPERATING_SCRUBBER_QUEUE = {   # SB left 2026-07-01 (20-F ftn-15, 20); ECO left 2026-07-01 (Q1-2026 6-K "all scrubber-fitted", 16 on-water)
    "DHT", "FRO", "GNK", "HAFN", "INSW", "SBLK", "STNG", "TEN", "TRMD",
}

# --- NAV-equation figure provenance (test_manifest_provenance) ----------------------------------
# Names with an uncited estimate on a NAV-equation figure (lowercase, as the scan emits).
NAV_FIGURE_ESTIMATE_QUEUE = {"brut", "cmbt", "flng", "hafn", "stng", "ten", "trmd"}  # nat left 2026-06-30 (newbuild figures parked, rest sourced); asc left 2026-07-01 (full 3/31 reconciliation; chem-Handy sleeve -> cited 20-F carrying-value floor)

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
#                    floor pending H1, a level-provisional VLCC resale mark, AND going-concern doubt; the
#                    eye-catching discount and the untrustworthiness are the SAME max-torque fact).
# Of the book's TRIM/SHORT positions, ALL are here or void — not one is a name-specific short.
POSITION_CYCLE_RELABEL = {"DHT", "FRO", "ECO", "INSW", "HAFN", "NAT"}  # NAT: the §12 archetype (de-voided 2026-06-30). ASC left 2026-07-01: the reconciliation lifted NAV $15.96->$17.80, so it reads mildly CHEAP (0.90x), not rich -> raw BUY; the product-cycle caveat on the near-peak earnings/strip leg lives in asc_log, not a rich-relabel
POSITION_UNRELIABLE = {"MPCC", "BRUT"}  # BRUT 2026-07-01: the position cell must reflect the untrustworthiness, not the 0.59x discount, so it can't sit as a raw BUY next to PROVISIONAL⛔NO (the ASC "rich·cycle" holdover lesson)

# Newbuild carried at $0 NAV pending a FILED contract price — the name discloses the order but not the
# price, and the only price is a broker LOI (not out of the figure-provenance queue), so the §9.6
# on-curve mark is unauthorized (CLAUDE.md). Both newbuild legs are PARKED, so the NAV rests entirely
# on sourced figures with the uncited number out of the equation. This is NOT a contradicted figure
# (not void) and NOT an uncited figure IN the NAV equation (not figure-PROVISIONAL) — it is a known,
# flagged indeterminate that makes the name a directional anchor, GOVERNED-WIDE, never TIGHT, until a
# filed price lets the newbuild go on-curve. NAT (owner decision 2026-06-30). Tier: newbuild-indeterminate.
NEWBUILD_PRICE_PENDING = {"NAT"}

# Tier sub-reason — why the band is wide / why PROVISIONAL, and thus the resolution PATH. Surfaced
# in the verdict's tier cell so GOVERNED-WIDE / PROVISIONAL aren't junk drawers.
#   structural-class : dominant class has no clean resale market (LNG/container Group-B) — not resolvable w/o a new data regime
#   newbuild-heavy   : justified leg can't price it (NAV PV-haircut vs strip full-year) — resolves only as hulls deliver
#   pending-anchor   : a sleeve's mark is unsourced but SOURCEABLE now (Thread 1A) — resolvable
#   mixed            : two of the above (TEN: structural LNGC sleeve + pending-anchor Handy/LR1)
#   read-flips       : read flips cheap<->fair across the §17 bases — needs the §18.5 gate data
#   newbuild-indeterminate : newbuild parked at $0 pending a FILED price (NEWBUILD_PRICE_PENDING) — GOVERNED-WIDE
#   cash-pending : PROVISIONAL but sourced EXCEPT one NAV figure pending a known future issuer report
#                  (BRUT: cash → H1-2026 report 2026-08-13) — a well-specified "waiting" state, not "broken"
#   void / uncited-figure / off-curve : the PROVISIONAL reasons (contradicted / uncited estimate / off the §9.6 curve)
TIER_SUBREASON = {
    "GSL": "structural-class", "CCEC": "structural-class", "FLNG": "structural-class",
    "CMBT": "structural-class", "MPCC": "structural-class", "ASC": "structural-class",
    "CAPT": "newbuild-heavy",
    "INSW": "pending-anchor",
    "TEN": "mixed",
    "CMDB": "read-flips", "GNK": "read-flips",
    "NAT": "newbuild-indeterminate",
    "BRUT": "cash-pending", "HAFN": "uncited-figure",
    "STNG": "uncited-figure", "TRMD": "uncited-figure",
}  # ECO left 2026-07-01: §9.6 on-curve + scrubbers verified -> VALIDATED-TIGHT (no sub-reason)


def _structural_nb_names(inputs_dir: Path = INPUTS_DIR) -> set[str]:
    """Group-B newbuild names (no resale curve mark) — their commitment/advance figures are cited;
    their tier issue is the structural input, so they are GOVERNED-WIDE, never figure-PROVISIONAL."""
    doc = yaml.safe_load(open(inputs_dir / "market_data" / "newbuild_convention.yaml"))
    return {k.upper() for k in (doc.get("structural_exempt") or {})}


def confidence_tier(
    ticker: str,
    nav_basis: str,
    robust: str,
    *,
    op_scrubber_error_pct: float = 0.0,
    inputs_dir: Path = INPUTS_DIR,
) -> str:
    """Compute the tier from the existing validation state (no new model).

    nav_basis / robust come from the scorecard; op_scrubber_error_pct is the materiality
    (premium x uncited hulls / NAV)."""
    t = ticker.upper()
    structural = (t in _structural_nb_names(inputs_dir)) or (nav_basis == "structural-unavailable")

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

    # 2. VALIDATED-TIGHT — traced + strong (two-basis robust) internal corroboration + immaterial gap.
    traced = nav_basis == "resale-uniform"
    op_scrubber_material = op_scrubber_error_pct > OPERATING_SCRUBBER_MATERIAL_PCT
    if traced and robust == "robust" and not op_scrubber_material:
        return "VALIDATED-TIGHT"

    # 3. GOVERNED-WIDE — traces, but structural / not-robust / FV-material untraced surface.
    return "GOVERNED-WIDE"


HANDOFF_READY = {"VALIDATED-TIGHT", "GOVERNED-WIDE"}


def is_handoff_ready(tier: str) -> bool:
    """A PROVISIONAL name must NOT hand off a governed FV — flag, don't pass."""
    return tier in HANDOFF_READY
