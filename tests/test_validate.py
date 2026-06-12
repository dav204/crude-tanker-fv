"""Input-validation tests (data-pipeline sanity checks)."""

from dataclasses import replace

from crude_tanker_fv.loaders import load_company_inputs
from crude_tanker_fv.validate import validate_inputs


def test_flags_implausible_dht_spot():
    ci = load_company_inputs("DHT", "2026-Q1")
    warnings = validate_inputs(ci)
    assert any("spot TCE VLCC" in w and "unsustainable" in w for w in warnings)


def test_clean_inputs_have_no_warnings():
    ci = load_company_inputs("DHT", "2026-Q1")
    # Replace the spike with a plausible spot (~3x mean) -> no warnings.
    fixed = replace(ci.market_data, spot_tce={**ci.market_data.spot_tce, "VLCC": 120_000})
    ci = replace(ci, market_data=fixed)
    assert validate_inputs(ci) == []


def test_flags_nonpositive_shares():
    ci = load_company_inputs("DHT", "2026-Q1")
    fixed_md = replace(ci.market_data, spot_tce={"VLCC": 120_000})
    ci = replace(
        ci,
        market_data=fixed_md,
        balance_sheet=replace(ci.balance_sheet, diluted_shares_outstanding=0),
    )
    assert any("shares outstanding" in w for w in validate_inputs(ci))


def test_fleet_summary_totals_cross_foot_against_vessel_rows():
    # Guard added 2026-06-11 after the TEN June-5 data-kit reconcile: the
    # manifest claimed on_curve_total 60 while listing 58 vessels (two
    # 2025-delivered Suezmaxes omitted at onboarding). When a manifest's
    # fleet_summary states a fleet-wide total, it must equal the sum of
    # vessel-row counts.
    import glob

    import yaml

    total_keys = ("on_curve_total", "total_operating")
    checked = 0
    for path in sorted(glob.glob("inputs/fleet_manifests/*.yaml")):
        if "_template" in path:
            continue
        data = yaml.safe_load(open(path))
        summary = data.get("fleet_summary") or {}
        rows_sum = sum(v.get("count", 1) for v in data["vessels"])
        for key in total_keys:
            if key in summary:
                assert summary[key] == rows_sum, (
                    f"{path}: fleet_summary.{key}={summary[key]} but vessel "
                    f"rows sum to {rows_sum}"
                )
                checked += 1
    assert checked >= 7  # ten/stng/hafn/trmd on_curve_total + sblk/gnk/cmdb total_operating
