"""BWLP NCI-via-preferred_equity — the curve↔NCI agreement guard.

Owner ratified the NAV-basis convention 2026-07-13 (rider (a) of the ruling;
decisions/bwlp_log.md item #1): preferred_equity carries the minority claims
at MARKED-TO-CURVE, derived as

    48% x (8 India hulls at VLGC curve marks + India CA - India CL
           - India non-current borrowings)  +  19% x PS net assets at book.

The figure is MARKS-DEPENDENT: a VLGC curve re-fit (the lpg_v1_lock_rerun
path, or any §9.9 update) silently invalidates the static YAML number. Two
surfaces assumed to agree get a TEST that they agree (2026-07-02 rule) — this
one recomputes the derivation off the LIVE post-transaction-anchor curve and
reds until the current bwlp quarter YAML is re-derived alongside the re-fit.

The sub-balance-sheet statics below are the Q1-2026 note figures cited in the
balance-sheet YAML; they refresh at quarterly re-derivations (Q2 carry-forward,
~Aug-2026) IN THE SAME COMMIT as the YAML.
"""

from crude_tanker_fv.loaders import (
    INPUTS_DIR,
    load_balance_sheet,
    load_fleet_manifest,
    load_market_data,
)
from crude_tanker_fv.transactions import (
    apply_transaction_anchored_curves,
    load_all_transactions,
)
from crude_tanker_fv.vessel_values import vessel_market_value

INDIA_HULLS = {"BW_Chinook", "BW_Pampero", "BW_Pine", "BW_Loyalty",
               "BW_Oak", "BW_Tyr", "BW_Birch", "BW_Elm"}

# Q2-2026 India sub-balance-sheet (bwlp_2026-Q2.yaml preferred_equity note;
# 6-K acc 0001104659-26-102581 Note 10 summarised BS — updated 2026-08-31 in
# the same commit as the YAML re-derivation, per rider (a)).
INDIA_CURRENT_ASSETS = 99_018_000
INDIA_CURRENT_LIABILITIES = 33_963_000
INDIA_NONCURRENT_BORROWINGS = 166_974_000
INDIA_NCI_SHARE = 0.48
# Product Services at book (Q2 Note 10), 19% NCI.
PS_NET_ASSETS_BOOK = 118_826_000
PS_NCI_SHARE = 0.19

TOLERANCE = 2_000_000  # rounding headroom only; a real re-fit moves $5M+


def test_bwlp_nci_agrees_with_live_curve():
    md = load_market_data()
    md, _ = apply_transaction_anchored_curves(md, load_all_transactions(INPUTS_DIR))
    curve = md.vessel_value_curves["VLGC"]

    manifest = load_fleet_manifest("BWLP")
    india = [v for v in manifest.vessels if v.id in INDIA_HULLS]
    assert len(india) == 8, "India sub fleet changed — re-derive the NCI"

    india_fleet = sum(vessel_market_value(v, curve) for v in india)
    sub_nav = (india_fleet + INDIA_CURRENT_ASSETS
               - INDIA_CURRENT_LIABILITIES - INDIA_NONCURRENT_BORROWINGS)
    derived = INDIA_NCI_SHARE * sub_nav + PS_NCI_SHARE * PS_NET_ASSETS_BOOK

    bs = load_balance_sheet("BWLP", "2026-Q2")
    assert abs(derived - bs.preferred_equity) <= TOLERANCE, (
        f"preferred_equity ${bs.preferred_equity/1e6:.1f}M no longer ties to the "
        f"live-curve derivation ${derived/1e6:.1f}M — the VLGC curve moved; "
        f"re-derive the NCI in bwlp_2026-Q2.yaml (decisions/bwlp_log.md item #1)"
    )
