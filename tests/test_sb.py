"""Safe Bulkers (SB) tests — 4th dry-bulk validator (METHODOLOGY §11.7)."""

import pytest

from crude_tanker_fv.loaders import load_company_inputs


def test_inputs_load():
    ci = load_company_inputs("SB", "2026-Q1")
    assert ci is not None


def test_fleet_shape():
    ci = load_company_inputs("SB", "2026-Q1")
    counts: dict[str, int] = {}
    nb = 0
    for v in ci.fleet.vessels:
        if (v.years_to_delivery or 0) > 0:  # §9.6 on-curve newbuilds — orderbook, not operating
            nb += v.count
            continue
        counts[v.cls] = counts.get(v.cls, 0) + v.count
    # Post-Panamax split out of Pana 2026-06-29 (§11.7.10): 20 Pana + 16 PPMX + 7 Cape.
    assert counts == {"Pana": 20, "Post-Panamax": 16, "Cape": 7}   # 43 operating (2 HFS off-curve)
    assert sum(counts.values()) == 43
    # 8 Kamsarmax newbuilds on the curve at age-0 delivered PV (§9.6 convention, 2026-06-30).
    assert nb == 8


def test_dwt_is_populated_for_dwt_scaling():
    """dwt is load-bearing under §11.7.10 dwt-scaling — every dry-bulk vessel needs it."""
    ci = load_company_inputs("SB", "2026-Q1")
    assert all(v.dwt and v.dwt > 0 for v in ci.fleet.vessels)
    # The 85-95.8k cohort is now its own Post-Panamax class (the §11.7.10 fix);
    # Pana tops out at the 82k Kamsarmax, the large hulls live in Post-Panamax.
    assert max(v.dwt for v in ci.fleet.vessels if v.cls == "Pana") <= 82500
    assert max(v.dwt for v in ci.fleet.vessels if v.cls == "Post-Panamax") >= 95000


def test_preferred_subtracts_from_nav():
    ci = load_company_inputs("SB", "2026-Q1")
    assert ci.balance_sheet.preferred_equity == pytest.approx(100_000_000)
