from crude_tanker_fv.dividend_window import DividendWindowRow
from crude_tanker_fv.overlay_ledger import (
    curated_rows, dividend_window_overlay, governance_rows, render,
)

REQUIRED = {"name", "overlay_id", "direction", "magnitude", "applied", "retire_trigger"}


def _dw_row(**kw):
    base = dict(ticker="NAT", sector="crude", price=5.2, tool_nav=2.07, premium_x=2.51,
                payout_ratio=1.0, herfindahl=1.0, cycle_position=1.9, gated=True,
                gap=3.13, q_star=None, supported_horizon=8.0, classification="TRIM-stands")
    base.update(kw)
    return DividendWindowRow(**base)


def test_curated_rows_carry_required_fields():
    for r in curated_rows():
        missing = REQUIRED - set(r)
        assert not missing, f"{r.get('name')}: missing {missing}"
        assert r["direction"] in ("up", "down")


def test_governance_rows_auto_populate_from_balance_sheets():
    names = {r["name"] for r in governance_rows("2026-Q1")}
    # The two applied §15 cases must always surface; a curated copy is forbidden.
    assert {"TEN", "CMDB"} <= names
    assert all(r["overlay_id"] == "§15" for r in governance_rows("2026-Q1"))
    curated_15 = [r for r in curated_rows() if r["overlay_id"] == "§15"]
    assert not curated_15, "§15 rows must come from balance sheets, not overlays.yaml"


def test_governance_rows_resolve_at_or_before_never_a_staged_future_sheet():
    """The ledger's §15 rows read the SAME sheet vintage the valuation resolves
    (vet 2026-08-08): a staged future-quarter sheet must not leak into a
    current-quarter ledger — the second instance of the half-application shape."""
    for r in governance_rows("2026-Q1"):
        assert "_2026-Q2.yaml" not in r["note"]


def test_render_contains_every_row():
    rows = curated_rows() + governance_rows("2026-Q1")
    md = render(rows)
    for r in rows:
        assert f"| {r['name']} | {r['overlay_id']} |" in md


def test_dividend_window_overlay_maps_computed_classification():
    # TRIM-stands → neutral §12.6 row (override evaluated, did NOT fire)
    trim = dividend_window_overlay(_dw_row(classification="TRIM-stands", q_star=None))
    assert trim["overlay_id"] == "§12.6"
    assert trim["direction"] == "none"
    assert "TRIM stands" in trim["magnitude"]
    assert trim["_auto"] is True
    # undervaluation → up
    under = dividend_window_overlay(_dw_row(classification="undervaluation", q_star=4.0, supported_horizon=8.0))
    assert under["direction"] == "up" and "undervaluation" in under["magnitude"]
    # not gated → no overlay row at all
    assert dividend_window_overlay(_dw_row(gated=False, classification="n/a")) is None


def test_render_handles_neutral_direction():
    md = render([dividend_window_overlay(_dw_row())])
    assert "| NAT | §12.6 | · |" in md           # neutral arrow, row present


def test_no_stale_nat_floor_override_in_curated():
    """audit E-2: the §12 'NAV floor' hand-row must be gone — §12 dividend-window
    direction is now the COMPUTED §12.6 row, never a curated assertion."""
    for r in curated_rows():
        assert not (r["name"] == "NAT" and r["overlay_id"].startswith("§12")), \
            "NAT §12 must auto-derive from the dividend-window test, not overlays.yaml"
        assert r["overlay_id"] != "§12.6", "§12.6 rows must be auto-derived, not curated"
