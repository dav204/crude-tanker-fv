"""SBLK (Star Bulk Carriers) tests — first dry-bulk Pareto-anchored validator.

Data assembled 2026-06-09 from Q1 2026 6-K (ex99-1.htm, filed 2026-05-20,
accession 0000950157-26-000639) + 2025 20-F (filed 2026-03-19, accession
0000950157-26-000397). See inputs/fleet_manifests/sblk.yaml for source notes
and the data caveats flagged for user review (per-vessel scrubber/charter
detail uses fleet-level proxies)."""

from conftest import BOOK_QUARTER  # follows the book across quarter rolls
from crude_tanker_fv.loaders import load_company_inputs


def test_inputs_load():
    """Sanity: company inputs load without schema error."""
    ci = load_company_inputs("SBLK", BOOK_QUARTER)
    assert ci is not None


def test_fleet_class_counts():
    """SBLK fleet at Q1 2026 — 135 OPERATING vessels per the 6-K enumeration,
    + 8 Kamsarmax newbuilds now on the curve (§9.6). Class breakdown per
    METHODOLOGY §11.7.1 (Newcastlemax+Capesize→Cape, Post-Panamax+
    Kamsarmax→Pana, Ultramax+Supramax→Supra-Ultra)."""
    ci = load_company_inputs("SBLK", BOOK_QUARTER)
    operating = [v for v in ci.fleet.vessels if not (v.years_to_delivery or 0)]
    assert len(operating) == 134   # re-pinned 2026-08-08 (Q2 refresh + verify catches: dedup -4, SLB hulls +2, Moira/Pendulum out, NB trio in)
    counts = {cls: 0 for cls in ("Cape", "Pana", "Supra-Ultra")}
    for v in operating:
        counts[v.cls] += 1
    assert counts["Cape"] == 31
    assert counts["Pana"] == 45
    assert counts["Supra-Ultra"] == 58


def test_newbuilds_on_curve_delivered_less_commitment():
    """8 × 82,000 dwt Kamsarmax newbuilds valued ON the curve at age-0 delivered-market
    PV (§9.6 on-curve convention, standardized 2026-06-30); the REMAINING commitment
    ($195,556k per 6-K Note 6) is subtracted and advances → 0 (sunk into the on-curve
    delivered value, the BRUT/CAPT convention)."""
    ci = load_company_inputs("SBLK", BOOK_QUARTER)
    assert ci.balance_sheet.newbuild_capex_commitments == 122035000  # Note 6 at 6/30 (5 hulls; re-pinned 2026-08-08)
    assert ci.balance_sheet.newbuild_advances_paid == 0
    nb = [v for v in ci.fleet.vessels if (v.years_to_delivery or 0) > 0]
    assert sum(v.count for v in nb) == 5   # re-pinned 2026-08-08: Emma/Evelina/Ellie delivered in Q2 -> operating
    assert all(v.cls == "Pana" for v in nb)
