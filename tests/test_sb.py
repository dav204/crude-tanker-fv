"""Safe Bulkers (SB) tests — 4th dry-bulk validator (METHODOLOGY §11.7)."""

import pytest

from crude_tanker_fv.loaders import load_company_inputs


def test_inputs_load():
    # Re-pinned 2026-07-31 (Q2 refresh): Katerina+Maritsa delivered (Pana 20->21 net of
    # Pedhoulas Commander->HFS); Xenia (PPMX)->HFS (17->16). 9 NBs on-curve + Capesize NB
    # parked $0 (lease-funded, price pending). decisions/sb_log.md 2026-07-31.
    ci = load_company_inputs("SB", "2026-Q2")
    assert ci is not None


def test_fleet_shape():
    # Re-pinned 2026-07-31 (Q2 refresh): Katerina+Maritsa delivered (Pana 20->21 net of
    # Pedhoulas Commander->HFS); Xenia (PPMX)->HFS (17->16). 9 NBs on-curve + Capesize NB
    # parked $0 (lease-funded, price pending). decisions/sb_log.md 2026-07-31.
    ci = load_company_inputs("SB", "2026-Q2")
    counts: dict[str, int] = {}
    nb = 0
    for v in ci.fleet.vessels:
        if (v.years_to_delivery or 0) > 0:  # §9.6 on-curve newbuilds — orderbook, not operating
            nb += v.count
            continue
        counts[v.cls] = counts.get(v.cls, 0) + v.count
    # 2026-03-31 snapshot (date-consistency correction 2026-07-01): 20 Pana + 17 PPMX + 7 Cape.
    # (Katerina is a newbuild at 3/31, not operating; Xenia + Pedhoulas Commander are operating —
    # their sales were only agreed May-2026. Michalis H is the ONE HFS, off-curve.)
    assert counts == {"Pana": 21, "Post-Panamax": 16, "Cape": 7}   # 44 operating (1 HFS off-curve)
    assert sum(counts.values()) == 44
    # 8 Kamsarmax newbuilds on the curve at age-0 delivered PV (§9.6; 6-K line 398 confirms 8 at 3/31).
    assert nb == 9


def test_dwt_is_populated_for_dwt_scaling():
    """dwt is load-bearing under §11.7.10 dwt-scaling — every dry-bulk vessel needs it."""
    # Re-pinned 2026-07-31 (Q2 refresh): Katerina+Maritsa delivered (Pana 20->21 net of
    # Pedhoulas Commander->HFS); Xenia (PPMX)->HFS (17->16). 9 NBs on-curve + Capesize NB
    # parked $0 (lease-funded, price pending). decisions/sb_log.md 2026-07-31.
    ci = load_company_inputs("SB", "2026-Q2")
    assert all(v.dwt and v.dwt > 0 for v in ci.fleet.vessels)
    # The 85-95.8k cohort is now its own Post-Panamax class (the §11.7.10 fix);
    # Pana tops out at the 82k Kamsarmax, the large hulls live in Post-Panamax.
    assert max(v.dwt for v in ci.fleet.vessels if v.cls == "Pana") <= 84000   # Kamsarmax tops ~84k (Pedhoulas Commander 83.7k)
    assert max(v.dwt for v in ci.fleet.vessels if v.cls == "Post-Panamax") >= 95000


def test_preferred_subtracts_from_nav():
    # Re-pinned 2026-07-31 (Q2 refresh): Katerina+Maritsa delivered (Pana 20->21 net of
    # Pedhoulas Commander->HFS); Xenia (PPMX)->HFS (17->16). 9 NBs on-curve + Capesize NB
    # parked $0 (lease-funded, price pending). decisions/sb_log.md 2026-07-31.
    ci = load_company_inputs("SB", "2026-Q2")
    assert ci.balance_sheet.preferred_equity == pytest.approx(100_000_000)
