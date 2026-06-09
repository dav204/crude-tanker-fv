"""SBLK (Star Bulk Carriers) tests — first dry-bulk Pareto-anchored validator.

Data assembled 2026-06-09 from Q1 2026 6-K (ex99-1.htm, filed 2026-05-20,
accession 0000950157-26-000639) + 2025 20-F (filed 2026-03-19, accession
0000950157-26-000397). See inputs/fleet_manifests/sblk.yaml for source notes
and the data caveats flagged for user review (per-vessel scrubber/charter
detail uses fleet-level proxies)."""

from crude_tanker_fv.loaders import load_company_inputs


def test_inputs_load():
    """Sanity: company inputs load without schema error."""
    ci = load_company_inputs("SBLK", "2026-Q1")
    assert ci is not None


def test_fleet_class_counts():
    """SBLK fleet at Q1 2026 — 135 operating vessels per the 6-K enumeration,
    + 8 newbuildings on order (captured via balance sheet). Class breakdown
    per METHODOLOGY §11.7.1 (Newcastlemax+Capesize→Cape, Post-Panamax+
    Kamsarmax→Pana, Ultramax+Supramax→Supra-Ultra)."""
    ci = load_company_inputs("SBLK", "2026-Q1")
    vessels = ci.fleet.vessels
    assert len(vessels) == 135
    counts = {cls: 0 for cls in ("Cape", "Pana", "Supra-Ultra")}
    for v in vessels:
        counts[v.cls] += 1
    assert counts["Cape"] == 31
    assert counts["Pana"] == 46
    assert counts["Supra-Ultra"] == 58


def test_newbuilds_in_balance_sheet():
    """8 × 82,000 dwt Kamsarmax newbuilds captured as balance-sheet line items
    (METHODOLOGY §3.1 / §9.6 — NBs valued at delivered market less remaining
    commitment, not on the fleet manifest until they deliver)."""
    ci = load_company_inputs("SBLK", "2026-Q1")
    # Total contract price $195,556k; advances paid $99,999k
    assert ci.balance_sheet.newbuild_capex_commitments == 195556000
    assert ci.balance_sheet.newbuild_advances_paid == 99999000
