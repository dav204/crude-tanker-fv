"""Container Set A sector wiring (METHODOLOGY §11.8) — shape + signatures."""

import pytest

from crude_tanker_fv.scenarios import (
    SCENARIO_CLASS_MAP_BY_SECTOR,
    load_scenarios,
    quarter_keys,
)

CLASSES = ["ctr_feeder", "ctr_intermediate", "ctr_large"]


@pytest.fixture(scope="module")
def doc():
    return load_scenarios(sector="containerships")


def test_strip_horizon_is_10(doc):
    assert int(doc["strip_horizon"]) == 10


def test_weights_sum_to_one(doc):
    assert sum(s["weight"] for s in doc["scenarios"].values()) == pytest.approx(1.0)


def test_class_map_routes_manifest_classes(doc):
    m = SCENARIO_CLASS_MAP_BY_SECTOR["containerships"]
    assert m == {
        "Ctr-Feeder": "ctr_feeder",
        "Ctr-Intermediate": "ctr_intermediate",
        "Ctr-Large": "ctr_large",
    }
    for scen in doc["scenarios"].values():
        for key in m.values():
            assert key in scen


def test_curves_carry_10_quarters_low_base_high(doc):
    keys = quarter_keys(10)
    assert keys[-1] == "q4_2028"
    for scen in doc["scenarios"].values():
        for cls in CLASSES:
            for k in keys:
                lo, base, hi = scen[cls][k]
                assert lo < base < hi


def test_downside_class_signatures_differentiate(doc):
    """A2 (owner direction): the two downsides must NOT be one bucket.

    normalization_plus_overhang is SUPPLY-led — hardest on ctr_large
    (record orderbook concentrates in big ships), feeder near base.
    demand_recession is DEMAND-led — feeder/intermediate at least as
    hard-hit as large relative to anchor.
    """
    scen = doc["scenarios"]
    anchors = {c: doc["cycle_anchors"][c]["ten_year_mean"] for c in CLASSES}
    end = "q4_2028"
    overhang = {c: scen["normalization_plus_overhang"][c][end][1] for c in CLASSES}
    recession = {c: scen["demand_recession"][c][end][1] for c in CLASSES}
    base = {c: scen["gradual_normalization"][c][end][1] for c in CLASSES}

    # Overhang: large is the WORST scenario for large (below even recession);
    # feeder stays near base (clearly above its recession level).
    assert overhang["ctr_large"] < recession["ctr_large"]
    assert overhang["ctr_feeder"] > recession["ctr_feeder"]
    assert overhang["ctr_feeder"] >= 0.95 * base["ctr_feeder"]

    # Recession: feeder/intermediate at least as hard-hit as large vs anchor.
    rec_vs_anchor = {c: recession[c] / anchors[c] for c in CLASSES}
    assert rec_vs_anchor["ctr_feeder"] <= rec_vs_anchor["ctr_large"]
    assert rec_vs_anchor["ctr_intermediate"] <= rec_vs_anchor["ctr_large"]


def test_market_data_carries_container_classes():
    from crude_tanker_fv.loaders import load_market_data

    md = load_market_data()
    for cls in ("Ctr-Feeder", "Ctr-Intermediate", "Ctr-Large"):
        assert len(md.ffa_forward_curve[cls]) == 10  # strip_horizon: 10
        assert md.twelve_month_tc[cls] > 0
        assert md.historical_tce_means[cls] > 0
        vc = md.vessel_value_curves[cls]
        assert vc.newbuild > vc.five_year_benchmark > vc.ten_year_benchmark > vc.scrap_25yr
