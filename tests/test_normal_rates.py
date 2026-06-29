"""Tests for the through-cycle normal-rate layer (P1 — METHODOLOGY §18).

The pre-registered halt conditions (PRE_REGISTRATION_NORMAL_RATES.md §4) are
band-locked here: if a parity rate drifts out of its registered band, this fails
and the INPUT is investigated — never the band widened to match.
"""

from __future__ import annotations

import pytest

from crude_tanker_fv.normal_rates import (
    OPERATING_DAYS,
    WACC_DEFAULT,
    class_normalized_opex,
    crf,
    normal_rate_table,
    parity_tce,
)

QUARTER = "2026-Q1"


def test_crf_known_value():
    assert crf(0.08, 25) == pytest.approx(0.093679, abs=1e-5)


def test_parity_uses_pv_of_salvage_not_naive():
    # PV-salvage (registered) vs the naive (NB-scrap)*CRF — they must DIFFER, and
    # the naive form under-charges capital (lower required TCE).
    nb, scrap, opex = 38_000_000, 7_500_000, 5_200.0
    pv = parity_tce(nb, scrap, opex, wacc=0.08, n=25, operating_days=360)
    naive = opex + (nb - scrap) * crf(0.08, 25) / 360
    assert pv > naive                       # discounting salvage charges MORE capital
    assert pv == pytest.approx(14_800, abs=200)   # the registered Kamsarmax level


def test_HALT_capesize_parity_in_registered_band():
    """PRE_REGISTRATION §4: Cape parity ∈ $24,800–25,800 at 8%. Outside ⇒ investigate input."""
    cape = normal_rate_table(QUARTER, ["Cape"])["Cape"].parity
    assert cape is not None
    assert 24_800 <= cape <= 25_800, f"Cape parity {cape:.0f} outside registered band"


def test_HALT_kamsarmax_parity_in_registered_band():
    """PRE_REGISTRATION §4: Kamsarmax (Pana) parity ∈ $14,500–15,500 at 8%."""
    kam = normal_rate_table(QUARTER, ["Pana"])["Pana"].parity
    assert kam is not None
    assert 14_500 <= kam <= 15_500, f"Kamsarmax parity {kam:.0f} outside registered band"


def test_divergence_sign_dry_bulk_under_ordered():
    # historical < parity ⇒ negative divergence ⇒ under-ordered (the provisional §18.6 signal).
    t = normal_rate_table(QUARTER, ["Cape", "Pana"])
    for cls in ("Cape", "Pana"):
        assert t[cls].divergence < 0


def test_container_historical_far_above_parity():
    # The §17.6 boom-anchor caveat made quantitative: container historical >> parity.
    t = normal_rate_table(QUARTER, ["Ctr-Large"])["Ctr-Large"]
    assert t.historical_mean > t.parity            # boom-tilted anchor above replacement
    # divergence = (historical − parity)/parity; container historical sits far ABOVE parity.
    assert t.divergence_pct > 0.20


def test_opex_triangulation_sane_no_wild_outliers():
    opex = class_normalized_opex(QUARTER)
    # Dry-bulk fleet-weighted normalized opex lands in a sane band.
    assert 6_000 <= opex["Cape"] <= 7_500
    assert 4_500 <= opex["Pana"] <= 6_000


def test_wacc_grid_brackets_default():
    cape_8 = normal_rate_table(QUARTER, ["Cape"], wacc=0.08)["Cape"].parity
    cape_7 = normal_rate_table(QUARTER, ["Cape"], wacc=0.07)["Cape"].parity
    cape_10 = normal_rate_table(QUARTER, ["Cape"], wacc=0.10)["Cape"].parity
    assert cape_7 < cape_8 < cape_10               # higher WACC ⇒ higher required TCE
    assert WACC_DEFAULT == 0.08 and OPERATING_DAYS == 360.0
