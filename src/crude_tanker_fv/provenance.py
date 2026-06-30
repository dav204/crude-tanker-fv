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
OFF_CONVENTION_QUEUE = {"ASC", "CMBT", "ECO", "HAFN", "NAT", "STNG", "TEN", "TRMD"}
SCRUBBER_UNVERIFIED_QUEUE: set[str] = set()   # NEWBUILD-value scrubber flag unverified (now empty)

# --- Operating-scrubber audit (test_scrubber_provenance) ---------------------------------------
OPERATING_SCRUBBER_VERIFIED = {"CAPT": 5}      # name -> audited operating scrubber-fitted count
OPERATING_SCRUBBER_QUEUE = {
    "DHT", "ECO", "FRO", "GNK", "HAFN", "INSW", "SB", "SBLK", "STNG", "TEN", "TRMD",
}

# --- NAV-equation figure provenance (test_manifest_provenance) ----------------------------------
# Names with an uncited estimate on a NAV-equation figure (lowercase, as the scan emits).
NAV_FIGURE_ESTIMATE_QUEUE = {"asc", "brut", "cmbt", "flng", "hafn", "nat", "stng", "ten", "trmd"}

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
# like the FV, and the position direction is void too. NAT: the ~$17M advance is contradicted by
# the Q1-2026 cash flow (+$38K inflow, no outflow); the ~$153M commitment ties to no disclosure
# (nat_log.md). Verified UNIQUE among the 7 PROVISIONAL names (the other 6 are uncited, not disproven).
NAV_DERIVED_VOID = {"NAT"}

# Position relabel — a TRIM/SHORT (or rich) position that is NOT an actionable directional short:
#   cycle-position : rich because §17 RONAV is through-cycle while price embeds the near-peak rate
#                    (§12) — a NAV-relative read, not a trade signal. Crude AND product near peak.
#   unreliable-read: an artifact of a newbuild-heavy / PV-haircut read that can't be trusted either
#                    way (MPCC — the tanker method applied to a containership's forward-committed book).
# Of the book's 8 TRIM/SHORT positions, ALL 8 are here or void — not one is a name-specific short.
POSITION_CYCLE_RELABEL = {"DHT", "FRO", "ECO", "INSW", "ASC", "HAFN"}
POSITION_UNRELIABLE = {"MPCC"}

# Tier sub-reason — why the band is wide / why PROVISIONAL, and thus the resolution PATH. Surfaced
# in the verdict's tier cell so GOVERNED-WIDE / PROVISIONAL aren't junk drawers.
#   structural-class : dominant class has no clean resale market (LNG/container Group-B) — not resolvable w/o a new data regime
#   newbuild-heavy   : justified leg can't price it (NAV PV-haircut vs strip full-year) — resolves only as hulls deliver
#   pending-anchor   : a sleeve's mark is unsourced but SOURCEABLE now (Thread 1A) — resolvable
#   mixed            : two of the above (TEN: structural LNGC sleeve + pending-anchor Handy/LR1)
#   read-flips       : read flips cheap<->fair across the §17 bases — needs the §18.5 gate data
#   void / uncited-figure / off-curve : the PROVISIONAL reasons (contradicted / uncited estimate / off the §9.6 curve)
TIER_SUBREASON = {
    "GSL": "structural-class", "CCEC": "structural-class", "FLNG": "structural-class",
    "CMBT": "structural-class", "MPCC": "structural-class",
    "CAPT": "newbuild-heavy",
    "INSW": "pending-anchor",
    "TEN": "mixed",
    "CMDB": "read-flips", "GNK": "read-flips",
    "NAT": "void",
    "BRUT": "uncited-figure", "ASC": "uncited-figure", "HAFN": "uncited-figure",
    "STNG": "uncited-figure", "TRMD": "uncited-figure",
    "ECO": "off-curve",
}


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
