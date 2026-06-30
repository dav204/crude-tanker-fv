"""Confidence tier — computed from the existing validation state (no new model).

VALIDATED-TIGHT / GOVERNED-WIDE / PROVISIONAL, for the portfolio-governance handoff. Tests pin the
three archetypes (SB / CMBT / NAT), the decision-tree edge cases the owner specified (APPROX does not
demote a robust name; an immaterial operating-scrubber surface does not either), the handoff gate
(PROVISIONAL never passes a governed FV), and that the queues here track the guards' (no drift).
"""

import crude_tanker_fv.provenance as prov
from crude_tanker_fv.provenance import confidence_tier, is_handoff_ready
from crude_tanker_fv.scorecard import compute_scorecard


def test_archetypes_from_scorecard():
    tiers = {r.ticker: r.confidence_tier for r in compute_scorecard("2026-Q1")}
    assert tiers["SB"] == "VALIDATED-TIGHT"      # traced + robust (internal two-basis), op-scrubber immaterial
    assert tiers["CMBT"] == "GOVERNED-WIDE"      # structural-unavailable container class breaks the second basis
    assert tiers["NAT"] == "PROVISIONAL"         # uncited newbuild commitment — not handoff-ready


def test_provisional_is_never_handoff_ready():
    assert not is_handoff_ready("PROVISIONAL")
    assert is_handoff_ready("VALIDATED-TIGHT")
    assert is_handoff_ready("GOVERNED-WIDE")
    rows = compute_scorecard("2026-Q1")
    for r in rows:
        if r.confidence_tier == "PROVISIONAL":
            assert not is_handoff_ready(r.confidence_tier), f"{r.ticker} PROVISIONAL must not hand off"


def test_approx_pnav_does_not_demote_a_robust_traced_name():
    # SB is APPROX-pnav (no broker check) but resale-uniform + robust across both bases: the missing
    # external check is replaced by the internal two-basis corroboration -> still TIGHT.
    assert confidence_tier("SB", "resale-uniform", "robust", op_scrubber_error_pct=0.05) == "VALIDATED-TIGHT"


def test_material_operating_scrubber_surface_widens_but_immaterial_does_not():
    # Immaterial uncited surface (5% < 10% threshold) -> stays TIGHT; a material one -> WIDE.
    assert confidence_tier("SB", "resale-uniform", "robust", op_scrubber_error_pct=0.05) == "VALIDATED-TIGHT"
    assert confidence_tier("SB", "resale-uniform", "robust", op_scrubber_error_pct=0.20) == "GOVERNED-WIDE"


def test_decision_tree_edges():
    # uncited figure (in the figure-provenance queue, non-structural) -> PROVISIONAL
    assert confidence_tier("NAT", "resale-uniform", "robust") == "PROVISIONAL"
    # structural-unavailable input -> GOVERNED-WIDE, never PROVISIONAL (figure is cited; issue is structural)
    assert confidence_tier("CMBT", "structural-unavailable", "n/a") == "GOVERNED-WIDE"
    # traced but the read flips between bases (no internal corroboration) -> GOVERNED-WIDE
    assert confidence_tier("GNK", "resale-uniform", "flips (cheap/fair)") == "GOVERNED-WIDE"


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
