"""Handy-Bulk (dry-bulk Handysize, §11.7.11 — Option B, owner-ratified 2026-07-14).

Locks the un-anchored static class exactly as wired by
decisions/handy_curve_sourcing_prereg_2026-07-14.md:
  1. curve statics (xclusiv 2026-06-22 committed vintage);
  2. the DERIVED scenario deck identity (= supra_ultra x 0.90, nearest-10) —
     the two-surfaces rule: a supra promotion that forgets handy REDS here;
  3. routing + sleeve assignment (distinct from product-tanker Handysize);
  4. rate-surface entries exist with their documented values;
  5. gate-neutrality: NO live watchlist manifest carries the class (wiring
     is provably inert until 2343/PANL onboard).
"""

from pathlib import Path

import yaml

from crude_tanker_fv.carveout import DRY_BULK_CLASSES, PRODUCT_CLASSES
from crude_tanker_fv.loaders import ALLOWED_CLASSES, INPUTS_DIR, load_market_data
from crude_tanker_fv.scenarios import SCENARIO_CLASS_MAP_BY_SECTOR

BASIS = 0.90   # locked spot-basis ratio (prereg §2; observed BHSI/BSI cluster 0.87-0.92)


def _scenarios():
    doc = yaml.safe_load(open(INPUTS_DIR / "scenario_inputs.yaml"))
    return doc["sectors"]["dry_bulk"]


def test_handy_bulk_curve_statics_locked():
    c = load_market_data().vessel_value_curves["Handy-Bulk"]
    assert c.dwt == 38000 and c.dwt_scaled
    assert c.newbuild == 36.0e6            # xclusiv Resale 2026-06-22 (alias:Handysize, bulk row)
    assert c.five_year_benchmark == 29.5e6
    assert c.ten_year_benchmark == 23.3e6
    assert c.scrap_25yr == 4.5e6
    assert c.scrubber_premium == 0 and c.eco_premium_pct == 0.0


def test_handy_bulk_ffa_row_is_supra_times_basis():
    """The ffa_forward_curve Handy-Bulk row == Supra-Ultra x 0.90 (nearest 10) —
    the third derived surface (deck + ffa row + this guard = one basis)."""
    doc = yaml.safe_load(open(INPUTS_DIR / "market_data" / "ffa_forward_curve.yaml"))
    su = doc["ffa_forward_curve"]["Supra-Ultra"]
    hb = doc["ffa_forward_curve"]["Handy-Bulk"]
    assert hb == [round(v * BASIS / 10) * 10 for v in su], (
        "ffa Handy-Bulk row drifted from Supra-Ultra x 0.90 — regenerate it with "
        "the supra promotion (same rule as the scenario deck)")


def test_handy_bulk_deck_is_supra_times_basis():
    """Every handy_bulk scenario point == round(supra_ultra * 0.90, nearest 10).
    Re-derive BOTH together on any supra promotion — this is the guard."""
    dry = _scenarios()["scenarios"]
    assert set(dry) == {"china_acceleration", "moderate_growth",
                        "china_property_drag", "coordinated_slowdown"}
    for name, sc in dry.items():
        su, hb = sc["supra_ultra"], sc["handy_bulk"]
        assert set(su) == set(hb), name
        for q in su:
            want = [round(p * BASIS / 10) * 10 for p in su[q]]
            assert hb[q] == want, (
                f"{name}.{q}: handy_bulk {hb[q]} != supra_ultra x {BASIS} {want} — "
                "the derived deck drifted from its basis (did a supra promotion "
                "forget to regenerate handy_bulk?)")


def test_handy_bulk_routing_and_sleeve():
    assert "Handy-Bulk" in ALLOWED_CLASSES
    assert "Handy-Bulk" in DRY_BULK_CLASSES
    assert "Handy-Bulk" not in PRODUCT_CLASSES          # distinct from product Handysize
    assert SCENARIO_CLASS_MAP_BY_SECTOR["dry_bulk"]["Handy-Bulk"] == "handy_bulk"
    assert "Handysize" not in SCENARIO_CLASS_MAP_BY_SECTOR["dry_bulk"]   # product key stays product
    dry = _scenarios()
    assert "handy_bulk" in dry["class_routes"]
    assert "handy_bulk" in dry["confidence"]
    assert dry["cycle_anchors"]["handy_bulk"]["ten_year_mean"] == 12850
    assert dry["cycle_anchors"]["handy_bulk"]["anchor_basis"] == "archive_22mo_median"


def test_handy_bulk_rate_surfaces():
    md = load_market_data()
    assert md.twelve_month_tc["Handy-Bulk"] == 14500    # MB DBW 28, 38k net (2026-07-10)
    assert md.historical_tce_means["Handy-Bulk"] == 12850
    assert md.spot_tce["Handy-Bulk"] == 16466           # BHSI week-close 2026-07-10
    # invariant: contract strictly below prompt resale (hot-market norm)
    nb = yaml.safe_load(open(INPUTS_DIR / "market_data" / "newbuild_contract_prices.yaml"))
    assert nb["newbuild_contract"]["Handy-Bulk"] == 30.5e6
    assert nb["prompt_resale"]["Handy-Bulk"] == 36.0e6
    assert nb["newbuild_contract"]["Handy-Bulk"] < nb["prompt_resale"]["Handy-Bulk"]
    basis = yaml.safe_load(open(INPUTS_DIR / "market_data" / "basis_status.yaml"))
    assert basis["basis_status"]["Handy-Bulk"] == "resale-uniform"


def test_handy_bulk_gate_neutral_no_live_name_routes_it():
    """Wiring must be inert: no committed fleet manifest carries the class today.
    When 2343/PANL onboard, DELETE this test (its job is done) — the prereg's
    band checks take over as the class's validation surface."""
    manifests = Path(INPUTS_DIR / "fleet_manifests").glob("*.yaml")
    carriers = []
    for m in manifests:
        doc = yaml.safe_load(open(m)) or {}
        for v in doc.get("vessels", []) or []:
            if isinstance(v, dict) and v.get("class") == "Handy-Bulk":
                carriers.append(m.name)
    assert not carriers, f"Handy-Bulk routed by live manifests {carriers} — no longer gate-neutral"
