"""Transaction-anchored curve recalibration tests (METHODOLOGY 3.1 / 9.9)."""

from datetime import date

import pytest

from conftest import BOOK_QUARTER  # follows the book across quarter rolls
from crude_tanker_fv.loaders import INPUTS_DIR, load_market_data
from crude_tanker_fv.pipeline import (
    run_transaction_anchored_comparison,
    value_company,
)
from crude_tanker_fv.transactions import (
    QUALITY_UPLIFT,
    TransactionPrint,
    TransactionSet,
    apply_transaction_anchored_curves,
    fit_curve_anchors,
    load_all_transactions,
    load_transaction_set,
)


def test_quality_uplifts():
    assert QUALITY_UPLIFT["standard"] == 0.0
    assert QUALITY_UPLIFT["financing"] == 0.05    # sale-leaseback +5%
    assert QUALITY_UPLIFT["distressed"] == 0.10
    assert QUALITY_UPLIFT["newbuild_resale"] == 0.0


def test_clean_price_lifts_for_financing():
    p = TransactionPrint(date=date(2026, 1, 15), age=10, price_usd_m=47.2,
                          quality_flag="financing")
    assert p.clean_price_usd_m == pytest.approx(47.2 * 1.05)


def test_load_aframax_yaml_round_trip():
    path = INPUTS_DIR / "market_data" / "transactions" / "aframax.yaml"
    ts = load_transaction_set(path)
    assert ts.cls == "Aframax"
    assert ts.as_of >= date(2026, 5, 29)   # bumped to 2026-06-09 with the Pareto scan
    assert len(ts.prints) >= 10   # expanded to 12 prints after Pareto scan
    ages = [p.age for p in ts.prints]
    assert min(ages) <= 10 and max(ages) >= 14   # mid-age coverage on both sides


def test_fit_anchors_produces_negative_slope_and_moves_10yr():
    md = load_market_data()
    ts = load_transaction_set(INPUTS_DIR / "market_data" / "transactions" / "aframax.yaml")
    fit = fit_curve_anchors(md.vessel_value_curves["Aframax"], ts)
    assert not fit.fallback
    assert fit.slope_per_year < 0                  # older = cheaper
    assert fit.new_10yr < fit.old_10yr             # 10yr anchor genuinely lower
    assert -25 < fit.delta_10yr_pct < -5           # ~12-13% drop given current sample
    # 5yr anchor barely moves — the public 2018-2019 prints validate the existing 5yr level
    assert abs(fit.delta_5yr_pct) < 10
    assert fit.new_5yr > fit.new_10yr              # monotone within mid-age window


def test_fit_falls_back_when_too_few_prints():
    md = load_market_data()
    ts = TransactionSet(cls="Aframax", as_of=date(2026, 5, 29),
                        prints=[TransactionPrint(date=date(2026, 1, 1), age=10,
                                                  price_usd_m=50, quality_flag="standard")])
    fit = fit_curve_anchors(md.vessel_value_curves["Aframax"], ts)
    assert fit.fallback
    assert fit.new_5yr == fit.old_5yr
    assert fit.new_10yr == fit.old_10yr


def test_lr2_proxy_alias_logic():
    """LR2 inherits the Aframax fit only when LR2's own fit falls back.

    As of 2026-06-09, lr2.yaml has 11 in-window prints (Pareto archive scan
    pulled disclosed STNG/Affinity/Torm prints), so LR2 stands on its own
    and the Aframax→LR2 proxy alias becomes a no-op. To test the proxy
    path we synthesize an empty LR2 transaction set and check that
    `apply_transaction_anchored_curves` still propagates the Aframax fit
    to LR2 — the v1 proxy-alias contract.
    """
    md = load_market_data()
    txs_all = load_all_transactions(INPUTS_DIR)
    assert "Aframax" in txs_all
    # Real LR2 fit now stands on its own (no proxy needed)
    if "LR2" in txs_all:
        own_fit = fit_curve_anchors(md.vessel_value_curves["LR2"], txs_all["LR2"])
        assert not own_fit.fallback   # LR2 self-fits now
    # Synthesize the "LR2 has no own fit" path to verify proxy logic
    txs_no_lr2 = {k: v for k, v in txs_all.items() if k != "LR2"}
    _, fits = apply_transaction_anchored_curves(md, txs_no_lr2)
    assert "Aframax" in fits and "LR2" in fits
    assert "propagated from Aframax" in fits["LR2"].note


def test_lr2_yaml_loads_and_documents_clean_lr2_gap():
    """LR2 stub yaml loads cleanly; the documented STNG print sits well below
    the active Aframax-proxy curve, confirming the §3.1 v1 limitation.
    """
    path = INPUTS_DIR / "market_data" / "transactions" / "lr2.yaml"
    if not path.exists():
        pytest.skip("lr2.yaml not present")
    ts = load_transaction_set(path)
    assert ts.cls == "LR2"
    in_window = [p for p in ts.prints if 3 <= p.age <= 17]
    assert len(in_window) >= 1
    # The STNG 2-vessel print at age 10 sits materially below the active
    # Aframax-proxy curve — empirically documents the clean-LR2-vs-dirty-
    # Aframax gap. Threshold deliberately loose so future prints don't
    # accidentally break the test.
    md = load_market_data()
    afra = md.vessel_value_curves["Aframax"]
    aframax_at_10 = afra.ten_year_benchmark * 1.05  # eco premium
    avg_in_window = sum(p.price_usd_m for p in in_window) / len(in_window)
    assert avg_in_window * 1e6 < aframax_at_10 * 0.85, \
        "LR2 prints should sit at least 15% below the Aframax-proxy curve"


def test_mr_yaml_round_trip_and_fit():
    """MR transactions file loads, in-window fit converges with negative slope
    and meaningful coverage of the right-edge of the [3,17] window.
    """
    path = INPUTS_DIR / "market_data" / "transactions" / "mr.yaml"
    if not path.exists():
        pytest.skip("mr.yaml not present")
    ts = load_transaction_set(path)
    assert ts.cls == "MR"
    in_window = [p for p in ts.prints if 3 <= p.age <= 17]
    assert len(in_window) >= 2
    md = load_market_data()
    fit = fit_curve_anchors(md.vessel_value_curves["MR"], ts)
    assert not fit.fallback
    assert fit.slope_per_year < 0          # older = cheaper
    assert fit.new_5yr > fit.new_10yr      # monotone within mid-age


def test_vlcc_yaml_loads_and_fit_lowers_anchors():
    """VLCC transactions file loads, in-window fit converges, and the fit
    lowers BOTH 5yr and 10yr anchors vs the existing broker-resale curve.
    """
    path = INPUTS_DIR / "market_data" / "transactions" / "vlcc.yaml"
    if not path.exists():
        pytest.skip("vlcc.yaml not present")
    ts = load_transaction_set(path)
    assert ts.cls == "VLCC"
    in_window = [p for p in ts.prints if 3 <= p.age <= 17]
    assert len(in_window) >= 4   # we ship 5 in-window prints
    # Age coverage: at least one print in [3, 7] and one in [10, 17]
    assert any(3 <= p.age <= 7 for p in in_window)
    assert any(10 <= p.age <= 17 for p in in_window)
    md = load_market_data()
    fit = fit_curve_anchors(md.vessel_value_curves["VLCC"], ts)
    assert not fit.fallback
    assert fit.slope_per_year < 0
    # 2026 transaction reality: VLCC curve runs HIGH vs prints — both anchors drop
    assert fit.delta_5yr_pct < -5
    assert fit.delta_10yr_pct < -5


def test_vlcc_recalibration_lowers_dht_nav():
    """Pure-VLCC DHT NAV must drop with the VLCC recalibration (2026-06-04 update).

    NOTE 2026-06-09: txn-anchored marks are now the pipeline DEFAULT — the
    un-anchored baseline side must be requested explicitly with False.
    """
    base = value_company("DHT", BOOK_QUARTER, 16.40, 16.00,
                         use_transaction_anchored=False).nav.nav_per_share
    on = value_company("DHT", BOOK_QUARTER, 16.40, 16.00).nav.nav_per_share
    assert on < base


def test_toggle_on_changes_exposed_names_only(tmp_path):
    # Default-on since 2026-06-09: "base" = explicit False (un-anchored curve).
    # TNK (Suezmax + Aframax): the Aframax recalibration lowers Aframax mid-age
    # more than the Suezmax recalibration lifts Suezmax mid-age, so net NAV drops.
    base = value_company("TNK", BOOK_QUARTER, 70.50, 75.00,
                         use_transaction_anchored=False).nav.nav_per_share
    on = value_company("TNK", BOOK_QUARTER, 70.50, 75.00).nav.nav_per_share
    assert on < base
    # Pure-VLCC: DHT NAV drops materially under the VLCC fit (2026-06-04 update —
    # vlcc.yaml adds 5 in-window prints; the fit lowers VLCC mid-age anchors
    # ~10-15%, which flows through to pure-VLCC names like DHT).
    base_dht = value_company("DHT", BOOK_QUARTER, 16.40, 16.00,
                             use_transaction_anchored=False).nav.nav_per_share
    on_dht = value_company("DHT", BOOK_QUARTER, 16.40, 16.00).nav.nav_per_share
    assert on_dht < base_dht
    # Pure-LNG: FLNG and CCEC are now the only no-exposure controls (no class
    # with a transactions file overlaps with their fleets).
    base_flng = value_company("FLNG", "2026-Q2", 26.40, 28.00,
                              use_transaction_anchored=False).nav.nav_per_share
    on_flng = value_company("FLNG", "2026-Q2", 26.40, 28.00).nav.nav_per_share
    assert on_flng == pytest.approx(base_flng)


def test_comparison_report_writes_outputs(tmp_path):
    rows = run_transaction_anchored_comparison(BOOK_QUARTER, outputs_dir=tmp_path)
    by = {r.ticker: r for r in rows}
    # Pure-LNG: FLNG and CCEC are the remaining no-exposure controls.
    assert by["FLNG"].nav_base == pytest.approx(by["FLNG"].nav_txn)
    assert by["FLNG"].pos_base == by["FLNG"].pos_txn
    assert by["CCEC"].nav_base == pytest.approx(by["CCEC"].nav_txn)
    # Aframax-exposed: TNK NAV drops (Aframax recal dominates Suezmax lift in mixed fleet).
    assert by["TNK"].nav_txn < by["TNK"].nav_base
    # Pure-VLCC: DHT NAV drops under the new VLCC fit (2026-06-04 — vlcc.yaml
    # lowers 5yr/10yr anchors by ~10-15%).
    assert by["DHT"].nav_txn < by["DHT"].nav_base
    # VLCC+Suezmax (ECO): net direction now depends on which fit dominates.
    # With current sample, VLCC -9.5% at 10yr beats Suezmax +1.3%, so ECO drops.
    assert by["ECO"].nav_txn < by["ECO"].nav_base
    assert (tmp_path / "transaction_anchor_comparison.md").exists()


def test_load_suezmax_yaml_round_trip():
    """Suezmax transactions YAML loads cleanly with the expected schema."""
    path = INPUTS_DIR / "market_data" / "transactions" / "suezmax.yaml"
    ts = load_transaction_set(path)
    assert ts.cls == "Suezmax"
    assert ts.as_of >= date(2026, 5, 29)   # bumped to 2026-06-09 with Pareto scan
    assert len(ts.prints) >= 15            # expanded to 18 in-window prints
    # Primary anchor: the TNK May 2026 age-17 print at $53.5M MUST be present.
    primary = [p for p in ts.prints
               if p.age == 17 and p.price_usd_m == pytest.approx(53.5)]
    assert len(primary) == 1


def test_suezmax_fit_produces_negative_slope_no_fallback():
    """Solver fit on the Suezmax sample: negative slope, in-window n>=2, no clamp."""
    md = load_market_data()
    ts = load_transaction_set(INPUTS_DIR / "market_data" / "transactions" / "suezmax.yaml")
    fit = fit_curve_anchors(md.vessel_value_curves["Suezmax"], ts)
    assert not fit.fallback
    assert fit.slope_per_year < 0           # older = cheaper
    assert fit.n_used >= 4                  # at least 4 in-window prints
    assert fit.note == ""                   # no clamping
    assert fit.new_5yr > fit.new_10yr       # monotone within mid-age window
    # POST-PARETO SCAN (2026-06-09): with 18 in-window prints the regression
    # reveals broker-resale curve was running HOT — fit DROPS both anchors
    # (5yr ~-7%, 10yr ~-13%). The earlier directional expectation ("hot 2025
    # lifts modestly") was an artifact of the thin pre-scan sample. The
    # methodologically-honest reading is that arm's-length disposals settle
    # below the broker market, with broker mark-ups driven by Sinokor's
    # opportunistic premium, see vlcc.yaml header.
    assert fit.delta_5yr_pct < 0
    assert fit.delta_10yr_pct < 0


def test_suezmax_recalibration_lowers_nat_nav():
    """Pure-Suezmax NAT NAV falls with the post-Pareto Suezmax recalibration.

    NOTE: prior test asserted NAV LIFT — that was correct for the thin-sample
    fit. The expanded Pareto sample reveals broker curves were running hot at
    both 5yr and 10yr Suezmax anchors; pure-Suezmax NAT NAV must therefore
    drop with the recalibration. Documented in CLAUDE.md 2026-06-09 entry.
    """
    base = value_company("NAT", "2026-Q2", 6.77, 6.00,
                         use_transaction_anchored=False).nav.nav_per_share
    on = value_company("NAT", "2026-Q2", 6.77, 6.00).nav.nav_per_share
    assert on < base


# --------------------------------------------------------------------------- #
# Freshness tripwire (PRE_REGISTRATION_CRUDE_RESALE_LEVEL.md B.4 / Thread 1C)
# --------------------------------------------------------------------------- #
# The crude mid-age is transaction-anchored (§9.9), and the ~22% gap to the xclusiv
# broker 5yr is documented as INTENDED divergence — but only while the prints are
# fresh. If a crude class's latest S&P print lags the freshest crude print by more
# than ~2 quarters, the mid-age anchor may be STALE (the gap is LAG, not signal), so
# the "intended divergence" claim needs a look (cross-check the 2026W26 xclusiv weekly).
MAX_PRINT_LAG_DAYS = 183  # ~2 quarters

def test_crude_midage_prints_not_stale():
    txs = load_all_transactions(INPUTS_DIR)
    latest = {c: max(p.date for p in txs[c].prints) for c in txs if txs[c].prints}
    crude = ["VLCC", "Suezmax", "Aframax", "LR2"]
    freshest = max(latest[c] for c in crude)
    for c in crude:
        lag = (freshest - latest[c]).days
        assert lag <= MAX_PRINT_LAG_DAYS, (
            f"{c}: latest S&P print {latest[c]} lags the freshest crude print {freshest} by "
            f"{lag}d (> {MAX_PRINT_LAG_DAYS}). The transaction-anchored mid-age may be STALE — the "
            f"22% gap to the xclusiv broker 5yr could be LAG, not intended divergence. Refresh the "
            f"print or cross-check the 2026W26 xclusiv weekly before trusting the gap."
        )
    # WATCH (not a failure): VLCC is the oldest crude print line — flag if it ever
    # becomes the staleness driver. (Currently ~1 quarter behind the active market.)
    assert latest["VLCC"] <= freshest, "sanity: VLCC print not newer than the freshest crude print"
