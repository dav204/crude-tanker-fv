"""Tests for the through-cycle normal-rate layer (P1 — METHODOLOGY §18).

The pre-registered halt conditions (PRE_REGISTRATION_NORMAL_RATES.md §4) are
band-locked here: if a parity rate drifts out of its registered band, this fails
and the INPUT is investigated — never the band widened to match.
"""

from __future__ import annotations

import pytest

from crude_tanker_fv.normal_rates import (
    OPERATING_DAYS,
    PARITY_BANDS,
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


# PRE_REGISTRATION Amendment 1 §A1.2 + Amendment 2: frozen per-class bands on the
# registered newbuild_CONTRACT prices. Outside band ⇒ investigate the INPUT, never widen.
# Single-sourced from normal_rates.PARITY_BANDS (the engine + scorecard read the same map).
FROZEN_BANDS = PARITY_BANDS


@pytest.mark.parametrize("cls,lo,hi", [(c, lo, hi) for c, (lo, hi) in FROZEN_BANDS.items()])
def test_HALT_parity_in_registered_band(cls, lo, hi):
    """Every trusted class's parity must land in its frozen band — the out-of-sample gate."""
    p = normal_rate_table(QUARTER, [cls])[cls].parity
    assert p is not None and lo <= p <= hi, f"{cls} parity {p:.0f} outside band [{lo}-{hi}]"


def test_divergence_sign_dry_bulk_under_ordered():
    # historical < parity ⇒ negative divergence ⇒ under-ordered (the provisional §18.6 signal).
    t = normal_rate_table(QUARTER, ["Cape", "Pana"])
    for cls in ("Cape", "Pana"):
        assert t[cls].divergence < 0


def test_unvalidated_classes_have_no_parity():
    # Amendment 1 §A1.4: LNG/container have no broker contract mark -> parity None
    # (no validated normal rate on either basis; suppressed from the headline vector).
    t = normal_rate_table(QUARTER, ["Ctr-Large", "LNGC", "MGC"])
    for cls in ("Ctr-Large", "LNGC", "MGC"):
        assert t[cls].parity is None
        assert t[cls].historical_mean is not None   # historical exists but is boom-tilted


def test_post_panamax_registered_on_replacement_equivalent():
    # Amendment 2: Post-Panamax = Kamsarmax-contract replacement, predicted band $14.5-15.5k.
    pp = normal_rate_table(QUARTER, ["Post-Panamax"])["Post-Panamax"].parity
    assert pp is not None and 14_500 <= pp <= 15_500


def test_resale_invariant_fires_on_resale_as_contract():
    from crude_tanker_fv.normal_rates import validate_contract_resale
    # corrected contract passes; the original $175M-as-contract (>= resale $145M) halts.
    validate_contract_resale({"VLCC": 128e6}, {"VLCC": 145e6})  # no raise
    with pytest.raises(ValueError, match="input-basis"):
        validate_contract_resale({"VLCC": 175e6}, {"VLCC": 145e6})


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
