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
