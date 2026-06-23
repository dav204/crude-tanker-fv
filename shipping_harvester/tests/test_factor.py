"""Factor adapter tests. Builds synthetic multi-broker panels and checks
reconciliation, segment-keying, schema shaping, and the demolition->scrap path.

Run:  pytest -q tests/test_factor.py
"""
from __future__ import annotations

import pandas as pd
import pytest

from shipping_harvester import factor
from shipping_harvester.factor import segment_of, to_factor_marks, to_schema_dict


def row(quarter, broker, kind, vclass, value, *, metric="", anchor=None,
        unit="usd_per_day", note=None, report_date="2026-06-20"):
    return dict(quarter=quarter, broker=broker, report_date=report_date, kind=kind,
                vessel_class=vclass, age_anchor=anchor, metric=metric, value=value,
                unit=unit, note=note)


# --- segment classification -------------------------------------------------
@pytest.mark.parametrize("vclass,broker,expected", [
    ("VLCC", "weber", "tanker"),
    ("VLCC", "allied", "tanker"),
    ("Capesize", "intermodal", "dry"),
    ("Panamax", "weber", "tanker"),     # Weber Panamax = product tanker
    ("Panamax", "allied", "dry"),       # dry house Panamax = bulker
    ("Handysize", "weber", "tanker"),
    ("Handysize", "xclusiv", "dry"),
    ("LNGC", "fearnleys", "gas"),
])
def test_segment_of(vclass, broker, expected):
    assert segment_of(vclass, broker) == expected


# --- precedence + dispersion ------------------------------------------------
def test_precedence_picks_preferred_source_and_records_spread():
    panel = pd.DataFrame([
        row("2026Q2", "weber", "spot_tce", "VLCC", 20490.0, metric="spot_tce"),
        row("2026Q2", "xclusiv", "spot_tce", "VLCC", 21000.0, metric="spot_tce"),
        row("2026Q2", "intermodal", "spot_tce", "VLCC", 19000.0, metric="spot_tce"),
    ])
    res = to_factor_marks(panel)
    r = res[(res.vessel_class == "VLCC") & (res.field == "spot_tce")].iloc[0]
    assert r["source"] == "weber"          # weber heads the tanker spot precedence
    assert r["value"] == 20490.0
    assert r["n_sources"] == 3
    assert r["sources"] == "intermodal,weber,xclusiv"
    assert r["value_min"] == 19000.0 and r["value_max"] == 21000.0


def test_vessel_value_precedence_allied_over_intermodal():
    panel = pd.DataFrame([
        row("2026Q2", "intermodal", "vessel_value", "Capesize", 70.0,
            metric="value", anchor="five_year", unit="musd"),
        row("2026Q2", "allied", "vessel_value", "Capesize", 72.0,
            metric="value", anchor="five_year", unit="musd"),
    ])
    res = to_factor_marks(panel)
    r = res[res.anchor == "five_year"].iloc[0]
    assert r["source"] == "allied"
    assert r["value"] == 72.0


def test_tanker_and_dry_panamax_stay_separate():
    panel = pd.DataFrame([
        row("2026Q2", "weber", "spot_tce", "Panamax", 30000.0, metric="spot_tce"),
        row("2026Q2", "allied", "vessel_value", "Panamax", 60.0,
            metric="value", anchor="five_year", unit="musd"),
    ])
    res = to_factor_marks(panel)
    segs = set(res["segment"])
    assert segs == {"tanker", "dry"}
    # they were never reconciled together
    assert (res["n_sources"] == 1).all()


# --- consensus modes --------------------------------------------------------
def test_mean_mode_consensus():
    panel = pd.DataFrame([
        row("2026Q2", "weber", "spot_tce", "VLCC", 20490.0, metric="spot_tce"),
        row("2026Q2", "xclusiv", "spot_tce", "VLCC", 21000.0, metric="spot_tce"),
        row("2026Q2", "intermodal", "spot_tce", "VLCC", 19000.0, metric="spot_tce"),
    ])
    policy = factor.replace(factor.DEFAULT_POLICY, mode="mean")
    res = to_factor_marks(panel, policy)
    r = res[res.field == "spot_tce"].iloc[0]
    assert r["value"] == pytest.approx((20490 + 21000 + 19000) / 3, abs=0.01)
    assert r["source"].startswith("consensus:mean")


# --- disagreement flag ------------------------------------------------------
def test_disagreement_flagged_when_spread_exceeds_threshold():
    panel = pd.DataFrame([
        row("2026Q2", "weber", "spot_tce", "Suezmax", 20000.0, metric="spot_tce"),
        row("2026Q2", "xclusiv", "spot_tce", "Suezmax", 24000.0, metric="spot_tce"),
    ])
    res = to_factor_marks(panel)               # default warn = 10%
    r = res[res.vessel_class == "Suezmax"].iloc[0]
    assert r["spread_pct"] > 0.10
    assert r["disagreement"]
    assert len(factor.disagreements(res)) == 1


# --- schema dict ------------------------------------------------------------
def test_to_schema_dict_shapes_and_renames():
    panel = pd.DataFrame([
        row("2026Q2", "allied", "vessel_value", "VLCC", 131.5,
            metric="value", anchor="newbuild", unit="musd"),
        row("2026Q2", "allied", "vessel_value", "VLCC", 105.0,
            metric="value", anchor="five_year", unit="musd"),
        row("2026Q2", "allied", "vessel_value", "VLCC", 80.0,
            metric="value", anchor="ten_year", unit="musd"),
        row("2026Q2", "weber", "period_tc", "VLCC", 45000.0, metric="1yr_tc"),
        row("2026Q2", "weber", "spot_tce", "VLCC", 20490.0, metric="spot_tce"),
    ])
    res = to_factor_marks(panel)
    schema = to_schema_dict(res)
    curve = schema["2026Q2"]["tanker"]["vessel_value_curves"]["VLCC"]
    # harvested anchors renamed to your schema keys
    assert curve["newbuild"] == 131.5
    assert curve["five_year_benchmark"] == 105.0
    assert curve["ten_year_benchmark"] == 80.0
    # full schema shape present, judgment/unsourced fields left None
    assert curve["scrap_25yr"] is None
    assert curve["scrubber_premium"] is None and curve["eco_premium_pct"] is None
    assert schema["2026Q2"]["tanker"]["twelve_month_tc"]["VLCC"] == 45000.0
    assert schema["2026Q2"]["tanker"]["spot_tce"]["VLCC"] == 20490.0


# --- scrap from demolition --------------------------------------------------
def test_scrap_curve_and_schema_fold_in():
    panel = pd.DataFrame([
        row("2026Q2", "gms", "demolition", "*", 500.0, metric="$/ldt",
            unit="usd_per_ldt", note="bangladesh"),
        row("2026Q2", "gms", "demolition", "*", 480.0, metric="$/ldt",
            unit="usd_per_ldt", note="india"),
        row("2026Q2", "allied", "vessel_value", "VLCC", 131.5,
            metric="value", anchor="newbuild", unit="musd"),
    ])
    scrap = factor.scrap_curve(panel)
    # bangladesh chosen by priority: 500 $/ldt * 42,000 ldt / 1e6 = 21.0 musd
    assert scrap[("2026Q2", "tanker", "VLCC")] == 21.0

    res = to_factor_marks(panel)
    schema = to_schema_dict(res, panel)
    assert schema["2026Q2"]["tanker"]["vessel_value_curves"]["VLCC"]["scrap_25yr"] == 21.0


def test_scrap_type_aware_dry_vs_tanker():
    """GMS-style typed demolition: tanker classes use the tanker $/ldt, dry
    classes use the dry $/ldt."""
    panel = pd.DataFrame([
        row("2026Q2", "gms", "demolition", "Dry", 400.0, metric="$/ldt",
            unit="usd_per_ldt", note="bangladesh"),
        row("2026Q2", "gms", "demolition", "Tanker", 420.0, metric="$/ldt",
            unit="usd_per_ldt", note="bangladesh"),
        # track one tanker and one dry class so they appear in the curve
        row("2026Q2", "allied", "vessel_value", "VLCC", 131.5,
            metric="value", anchor="newbuild", unit="musd"),
        row("2026Q2", "xclusiv", "vessel_value", "Capesize", 72.0,
            metric="value", anchor="five_year", unit="musd"),
    ])
    scrap = factor.scrap_curve(panel)
    assert scrap[("2026Q2", "tanker", "VLCC")] == round(420 * 42000 / 1e6, 2)   # 17.64
    assert scrap[("2026Q2", "dry", "Capesize")] == round(400 * 22000 / 1e6, 2)  # 8.8

    schema = to_schema_dict(to_factor_marks(panel), panel)
    assert schema["2026Q2"]["tanker"]["vessel_value_curves"]["VLCC"]["scrap_25yr"] == 17.64
    assert schema["2026Q2"]["dry"]["vessel_value_curves"]["Capesize"]["scrap_25yr"] == 8.8
