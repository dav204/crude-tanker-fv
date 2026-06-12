from crude_tanker_fv.overlay_ledger import curated_rows, governance_rows, render

REQUIRED = {"name", "overlay_id", "direction", "magnitude", "applied", "retire_trigger"}


def test_curated_rows_carry_required_fields():
    for r in curated_rows():
        missing = REQUIRED - set(r)
        assert not missing, f"{r.get('name')}: missing {missing}"
        assert r["direction"] in ("up", "down")


def test_governance_rows_auto_populate_from_balance_sheets():
    names = {r["name"] for r in governance_rows()}
    # The two applied §15 cases must always surface; a curated copy is forbidden.
    assert {"TEN", "CMDB"} <= names
    assert all(r["overlay_id"] == "§15" for r in governance_rows())
    curated_15 = [r for r in curated_rows() if r["overlay_id"] == "§15"]
    assert not curated_15, "§15 rows must come from balance sheets, not overlays.yaml"


def test_render_contains_every_row():
    rows = curated_rows() + governance_rows()
    md = render(rows)
    for r in rows:
        assert f"| {r['name']} | {r['overlay_id']} |" in md
