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
# DHT converted to on-curve §9.6 2026-06-30 (1 VLCC, DHT Impala) — removed from the queue.
OFF_CONVENTION_QUEUE = {
    "CMBT", "HAFN", "STNG", "TEN", "TRMD",
}  # NAT left 2026-06-30 (parked); ASC left 2026-07-01 (April subsequent event); ECO left 2026-07-01 (2 Suezmax NBs on-curve §9.6 via years_to_delivery)


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


# ---------------------------------------------------------------------------
# Newbuild value-flag provenance: eco/scrubber must trace to the name's OWN
# disclosure, never a peer default (the trap that put a fabricated scrubber
# premium on SB before the 2026-06-30 verification). See newbuild_specs.yaml.

def _newbuild_specs() -> dict:
    return yaml.safe_load(open(INPUTS_DIR / "market_data" / "newbuild_specs.yaml"))


def _oncurve_nb_names() -> list[str]:
    out = []
    for t in load_watchlist():
        ci = load_company_inputs(t, QUARTER)
        if any((v.years_to_delivery or 0) > 0 for v in ci.fleet.vessels):
            out.append(t)
    return sorted(out)


def test_newbuild_value_flags_trace_to_registered_disclosure():
    """Every on-curve newbuild's eco/scrubber flags must match the name's registered,
    disclosure-sourced spec. A value-adding flag cannot enter NAV on peer-consistency —
    a name with on-curve newbuilds but no registry entry, a flag mismatch, or an empty
    source citation hard-fails (the durable fix for the peer-borrowed-scrubber trap)."""
    specs = _newbuild_specs()
    for name in _oncurve_nb_names():
        ci = load_company_inputs(name, QUARTER)
        nb = [v for v in ci.fleet.vessels if (v.years_to_delivery or 0) > 0]
        assert name in specs, (
            f"{name}: carries on-curve newbuilds but has no newbuild_specs.yaml entry — "
            f"register eco/scrubber WITH the filing citation; a value flag may not default."
        )
        spec = specs[name]
        assert str(spec.get("source", "")).strip(), f"{name}: newbuild_specs entry has no source citation"
        for v in nb:
            assert bool(v.eco) == bool(spec["eco"]), (
                f"{name}: NB-row eco={v.eco} != registered {spec['eco']} (newbuild_specs.yaml)"
            )
        sc = spec["scrubber"]
        if sc == "mixed":
            # Non-uniform name: the contradiction check is on the COUNT — the manifest's
            # scrubber-fitted NB count must equal the registered, ledger-verified count.
            got = sum(v.count for v in nb if v.scrubber)
            assert got == spec["scrubber_nb_count"], (
                f"{name}: NB scrubber-fitted count {got} != registered {spec['scrubber_nb_count']} "
                f"(newbuild_specs.yaml — manifest contradicts the verified per-vessel ledger)"
            )
        else:
            for v in nb:
                assert bool(v.scrubber) == bool(sc), (
                    f"{name}: NB-row scrubber={v.scrubber} != registered {sc} (newbuild_specs.yaml)"
                )


# Scrubber-verification work queue: on-curve NB names whose scrubber=true has NOT been
# verified against the name's own filing. xfail(strict) — each leaves ONLY by verifying
# (or correcting) its scrubber flag against its 6-K. eco needs no such queue (§3.1 rule).
# BRUT/CAPT/FRO all verified against their own filings 2026-06-30 (BRUT: official Euronext
# Annual Report 2025; FRO: Q1 6-K; CAPT: Pareto per-vessel ledger + Euronext info doc, corrected
# to 18/30). The newbuild scrubber-verification queue is now EMPTY — every on-curve NB name's
# scrubber flag traces to its own disclosure.
SCRUBBER_UNVERIFIED_QUEUE: set[str] = set()


def _scrubber_param(name: str):
    marks = (
        [pytest.mark.xfail(strict=True, reason=f"{name}: NB scrubber=true not yet verified vs filing")]
        if name in SCRUBBER_UNVERIFIED_QUEUE
        else []
    )
    return pytest.param(name, marks=marks)


_SCRUBBER_TRUE_NAMES = [n for n, s in _newbuild_specs().items() if s.get("scrubber")]


@pytest.mark.parametrize("name", [_scrubber_param(n) for n in sorted(_SCRUBBER_TRUE_NAMES)])
def test_newbuild_scrubber_verified_against_filing(name):
    """A registered scrubber=true flag must be verified against the name's own filing.
    The pre-existing on-curve names (BRUT/CAPT/FRO) carried scrubber=true on peer-convention
    grounds and sit in the xfail queue until checked — their VLCC scrubber premium is large."""
    assert _newbuild_specs()[name].get("scrubber_verified") is True, (
        f"{name}: scrubber=true is not scrubber_verified — verify against the filing or set "
        f"scrubber=false (newbuild_specs.yaml). A value-adding flag may not rest on peer practice."
    )
