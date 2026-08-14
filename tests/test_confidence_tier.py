"""Confidence tier — computed from the existing validation state (no new model).

VALIDATED-TIGHT / GOVERNED-WIDE / PROVISIONAL, for the portfolio-governance handoff. Tests pin the
three archetypes (SB / CMBT / NAT), the decision-tree edge cases the owner specified (APPROX does not
demote; an immaterial operating-scrubber surface does not either), the handoff gate (PROVISIONAL
never passes a governed FV), and that the queues here track the guards' (no drift).

AMENDED 2026-08-13 (decisions/tier_semantics_amendment_2026-08-13.md + Addendum A): the tier
certifies CONSTRUCTION only and no longer takes read agreement. It gates on EVALUABILITY —
`read_blocked` is the §17 blocking guard's label, or None when a multiple was producible. The
price-invariance guard the amendment turns on lives in test_tier_semantics_amendment.py.
"""

from conftest import BOOK_QUARTER  # follows the book across quarter rolls
import crude_tanker_fv.provenance as prov
from crude_tanker_fv.provenance import confidence_tier, is_handoff_ready
from crude_tanker_fv.scorecard import compute_scorecard


def test_archetypes_from_scorecard():
    tiers = {r.ticker: r.confidence_tier for r in compute_scorecard(BOOK_QUARTER)}
    assert tiers["SB"] == "VALIDATED-TIGHT"      # traced + §17 evaluable, op-scrubber immaterial
    assert tiers["CMBT"] == "GOVERNED-WIDE"      # structural-unavailable container class breaks the second basis
    assert tiers["NAT"] == "GOVERNED-WIDE"       # de-voided 2026-06-30; newbuild parked at $0 pending a filed price


def test_provisional_is_never_handoff_ready():
    assert not is_handoff_ready("PROVISIONAL")
    assert is_handoff_ready("VALIDATED-TIGHT")
    assert is_handoff_ready("GOVERNED-WIDE")
    rows = compute_scorecard(BOOK_QUARTER)
    for r in rows:
        if r.confidence_tier == "PROVISIONAL":
            assert not is_handoff_ready(r.confidence_tier), f"{r.ticker} PROVISIONAL must not hand off"


def test_approx_pnav_does_not_demote_a_traced_name():
    # SB is APPROX-pnav (no broker check) but resale-uniform with an evaluable §17 multiple. An
    # external broker cross-foot is estimate-level evidence that MAY inform the tier where coverage
    # exists, never a requirement -> still TIGHT.
    assert confidence_tier("SB", "resale-uniform", op_scrubber_error_pct=0.05) == "VALIDATED-TIGHT"


def test_material_operating_scrubber_surface_widens_but_immaterial_does_not():
    # Immaterial uncited surface (5% < 10% threshold) -> stays TIGHT; a material one -> WIDE.
    assert confidence_tier("SB", "resale-uniform", op_scrubber_error_pct=0.05) == "VALIDATED-TIGHT"
    assert confidence_tier("SB", "resale-uniform", op_scrubber_error_pct=0.20) == "GOVERNED-WIDE"


def test_decision_tree_edges():
    # newbuild parked at $0 pending a filed price (NEWBUILD_PRICE_PENDING) -> GOVERNED-WIDE, never TIGHT.
    # The NAV rests on sourced figures with the uncited number out of the equation, so not PROVISIONAL.
    assert confidence_tier("NAT", "resale-uniform") == "GOVERNED-WIDE"
    # an uncited figure IN the NAV equation (figure-provenance queue, non-structural) -> PROVISIONAL
    assert confidence_tier("HAFN", "resale-uniform") == "PROVISIONAL"
    # structural-unavailable input -> GOVERNED-WIDE, never PROVISIONAL (figure is cited; issue is structural)
    assert confidence_tier("CMBT", "structural-unavailable") == "GOVERNED-WIDE"
    # AMENDED 2026-08-13. This line formerly pinned the retired rule — GNK "flips (cheap/fair)" ==
    # GOVERNED-WIDE. A flipping read is an EDGE fact: GNK is construction-clean (resale-uniform,
    # queues clear, §17 evaluable), so it is TIGHT regardless of what the read said. The flip caps
    # size on the read_flag channel instead.
    assert confidence_tier("GNK", "resale-uniform") == "VALIDATED-TIGHT"
    # ...and the tier says the same thing whichever way the read came out, because it never sees it.
    assert confidence_tier("GNK", "resale-uniform", read_blocked=None) == "VALIDATED-TIGHT"
    # EVALUABILITY still gates: no producible multiple is a CONSTRUCTION defect (Addendum A).
    assert confidence_tier("CAPT", "resale-uniform",
                           read_blocked="newbuild-heavy (unreliable)") == "GOVERNED-WIDE"


def test_provenance_queues_track_the_guards():
    """provenance.py is the single source; assert the guard modules carry the same sets (no drift)."""
    import tests.test_manifest_provenance as mp
    import tests.test_newbuild_convention as nc
    import tests.test_scrubber_provenance as sp

    assert prov.OFF_CONVENTION_QUEUE == nc.OFF_CONVENTION_QUEUE
    assert prov.SCRUBBER_UNVERIFIED_QUEUE == nc.SCRUBBER_UNVERIFIED_QUEUE
    assert prov.OPERATING_SCRUBBER_QUEUE == sp.OPERATING_SCRUBBER_QUEUE
    assert prov.OPERATING_SCRUBBER_VERIFIED == sp.OPERATING_SCRUBBER_VERIFIED
    assert prov.NAV_FIGURE_ESTIMATE_QUEUE == mp.NAV_FIGURE_ESTIMATE_QUEUE
