"""Safe Bulkers (SB) tests — 4th dry-bulk validator (METHODOLOGY §11.7)."""

import pytest

from crude_tanker_fv.loaders import load_company_inputs


def test_inputs_load():
    ci = load_company_inputs("SB", "2026-Q1")
    assert ci is not None


def test_fleet_shape():
    ci = load_company_inputs("SB", "2026-Q1")
    counts: dict[str, int] = {}
    for v in ci.fleet.vessels:
        counts[v.cls] = counts.get(v.cls, 0) + v.count
    assert counts == {"Pana": 36, "Cape": 7}     # 43 on-curve (2 HFS off-curve)
    assert sum(counts.values()) == 43


def test_dwt_is_populated_for_dwt_scaling():
    """dwt is load-bearing under §11.7.10 dwt-scaling — every dry-bulk vessel needs it."""
    ci = load_company_inputs("SB", "2026-Q1")
    assert all(v.dwt and v.dwt > 0 for v in ci.fleet.vessels)
    # Post-Panamax outliers present (the §11.7.10 over-valuation watch case).
    assert max(v.dwt for v in ci.fleet.vessels if v.cls == "Pana") >= 95000


def test_preferred_subtracts_from_nav():
    ci = load_company_inputs("SB", "2026-Q1")
    assert ci.balance_sheet.preferred_equity == pytest.approx(100_000_000)
