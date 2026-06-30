"""Structural guard — uniform newbuild NAV convention (METHODOLOGY §3.1 / §9.6).

A newbuild's NAV contribution must be delivered-market PV LESS the remaining commitment,
NOT advances-only (sunk cost) and NOT commitment-net-without-the-asset. nav.py reaches
this when the hull is ON the curve (``years_to_delivery > 0``) at its age-0 delivered
value with the REMAINING commitment subtracted (the BRUT/CAPT/FRO/MPCC convention).

Three clauses (see PRE_REGISTRATION_NEWBUILD_CONVENTION.md §4):
  1. FIXABLE (newbuild classes have a curve mark) -> must be on-curve.
  2. STRUCTURAL (no curve mark; enumerated in newbuild_convention.yaml) -> commitment-net,
     never advances-only (book the obligation even when the asset can't be marked).
  3. The structural exemption is enumerated in data; an unlisted NB name defaults to
     clause 1, so an unclassified name cannot land off-convention silently (the MR-hole).

The not-yet-converted names are the visible work queue, encoded as ``xfail(strict=True)``
so the suite (and the in-suite drift gate) stays operable while the queue reds honestly.
A name leaves the queue ONLY via its own pre-registered fix; removing a marker without
fixing the name -> strict xpass -> hard fail. New unclassified NB name -> immediate fail.
"""

import pytest
import yaml

from crude_tanker_fv.loaders import INPUTS_DIR, load_company_inputs, load_watchlist

QUARTER = "2026-Q1"

# Off-convention work queue (NB pre-reg §4). Each name leaves ONLY via its own
# pre-registered fix. strict xfail. (SB+SBLK are removed by the pass-1 wiring commit.)
OFF_CONVENTION_QUEUE = {
    "ASC", "CMBT", "DHT", "ECO", "HAFN", "NAT", "SB", "SBLK", "STNG", "TEN", "TRMD",
}


def _structural_exempt() -> dict[str, str]:
    doc = yaml.safe_load(open(INPUTS_DIR / "market_data" / "newbuild_convention.yaml"))
    return doc["structural_exempt"]


def _classify(ci) -> str:
    bs = ci.balance_sheet
    com = bs.newbuild_capex_commitments or 0
    adv = bs.newbuild_advances_paid or 0
    on_curve = any((v.years_to_delivery or 0) > 0 for v in ci.fleet.vessels)
    if on_curve:
        return "on-curve"
    if com > 0:
        return "commitment-net"
    if adv > 0:
        return "advances-only"
    return "no-NB"


def _nb_names() -> list[str]:
    names = []
    for t in load_watchlist():
        if _classify(load_company_inputs(t, QUARTER)) != "no-NB":
            names.append(t)
    return sorted(names)


def _param(name: str):
    marks = (
        [pytest.mark.xfail(strict=True, reason=f"{name}: off-convention, queued (NB pre-reg §4)")]
        if name in OFF_CONVENTION_QUEUE
        else []
    )
    return pytest.param(name, marks=marks)


@pytest.mark.parametrize("name", [_param(n) for n in _nb_names()])
def test_newbuild_convention(name):
    exempt = _structural_exempt()
    cls = _classify(load_company_inputs(name, QUARTER))
    if name in exempt:
        # Clause 2: structural -> commitment-net (or on-curve), never advances-only.
        assert cls in ("commitment-net", "on-curve"), (
            f"{name}: structural-exempt ({exempt[name]}) but classified {cls!r} — must book "
            f"the remaining commitment (commitment-net), never advances-only."
        )
    else:
        # Clause 1 (+3): fixable / unlisted -> must carry delivered value on the curve.
        assert cls == "on-curve", (
            f"{name}: NB-carrying name is {cls!r} — must value its newbuilds ON the curve "
            f"(§9.6 delivered-market PV less remaining commitment). If it structurally "
            f"cannot (no curve mark), add it to newbuild_convention.yaml structural_exempt "
            f"with a reason; do not leave it off-convention."
        )


def test_structural_exempt_names_are_classifiable():
    """Every structural-exempt name actually carries newbuilds (no stale exemptions)."""
    nb = set(_nb_names())
    for name in _structural_exempt():
        assert name in nb, f"{name}: structural-exempt but carries no newbuilds — stale entry"
