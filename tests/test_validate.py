"""Input-validation tests (data-pipeline sanity checks)."""

from dataclasses import replace

from conftest import BOOK_QUARTER  # follows the book across quarter rolls
import pytest

from crude_tanker_fv.loaders import load_balance_sheet, load_company_inputs
from crude_tanker_fv.validate import validate_inputs


def test_flags_implausible_dht_spot():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    warnings = validate_inputs(ci)
    assert any("spot TCE VLCC" in w and "unsustainable" in w for w in warnings)


def test_clean_inputs_have_no_warnings():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    # Replace the spike with a plausible spot (~3x mean) -> no warnings.
    fixed = replace(ci.market_data, spot_tce={**ci.market_data.spot_tce, "VLCC": 120_000})
    ci = replace(ci, market_data=fixed)
    assert validate_inputs(ci) == []


def test_flags_nonpositive_shares():
    ci = load_company_inputs("DHT", BOOK_QUARTER)
    fixed_md = replace(ci.market_data, spot_tce={"VLCC": 120_000})
    ci = replace(
        ci,
        market_data=fixed_md,
        balance_sheet=replace(ci.balance_sheet, diluted_shares_outstanding=0),
    )
    assert any("shares outstanding" in w for w in validate_inputs(ci))


def test_zero_shares_fails_at_load_not_in_nav(tmp_path):
    """Shares divide nav_per_share and the strip; validate.py only WARNS (warnings
    never stop a run), so a zero must hard-fail at load with the file named —
    not surface as a ZeroDivisionError downstream (audit 2026-07-02, F-12)."""
    import yaml

    (tmp_path / "balance_sheets").mkdir()
    doc = {
        "ticker": "ZZZ", "quarter": "2026-Q1",
        "cash_and_equivalents": 100.0, "working_capital_net": 0.0,
        "total_debt": 0.0, "lease_liabilities": 0.0,
        "newbuild_capex_commitments": 0.0, "newbuild_advances_paid": 0.0,
        "diluted_shares_outstanding": 0.0,
    }
    (tmp_path / "balance_sheets" / "zzz_2026-Q1.yaml").write_text(yaml.safe_dump(doc))
    with pytest.raises(ValueError, match="diluted_shares_outstanding must be > 0"):
        load_balance_sheet("ZZZ", "2026-Q1", tmp_path)


def test_fleet_summary_totals_cross_foot_against_vessel_rows():
    # Guard added 2026-06-11 after the TEN June-5 data-kit reconcile: the
    # manifest claimed on_curve_total 60 while listing 58 vessels (two
    # 2025-delivered Suezmaxes omitted at onboarding). When a manifest's
    # fleet_summary states a fleet-wide total, it must equal the sum of
    # vessel-row counts.
    import glob

    import yaml

    checked = 0
    for path in sorted(glob.glob("inputs/fleet_manifests/*.yaml")):
        if "_template" in path:
            continue
        data = yaml.safe_load(open(path))
        summary = data.get("fleet_summary") or {}
        # The two total keys mean different things once a name carries §9.6 on-curve
        # newbuilds (years_to_delivery > 0): on_curve_total counts EVERY curve-valued row
        # (operating + newbuilds), while total_operating counts the OPERATING fleet only
        # (newbuilds are orderbook). For a name without newbuilds the two coincide.
        all_rows = sum(v.get("count", 1) for v in data["vessels"])
        onwater_rows = sum(
            v.get("count", 1) for v in data["vessels"] if not (v.get("years_to_delivery") or 0)
        )
        for key, expected in (("on_curve_total", all_rows), ("total_operating", onwater_rows)):
            if key in summary:
                assert summary[key] == expected, (
                    f"{path}: fleet_summary.{key}={summary[key]} but expected {expected} "
                    f"(all_rows={all_rows}, on_water_rows={onwater_rows})"
                )
                checked += 1
    assert checked >= 7  # ten/stng/hafn/trmd/sb/mpcc on_curve_total + sblk/gnk/cmdb total_operating
