"""Read-only cron sentinel (WO1 Task 2) — one manufactured flag per class,
stable routing tags, exit codes, and the spec log format."""

import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import yaml

from crude_tanker_fv.sentinel import collect_flags, main

# Check 5 (NOTIFY-UNCONFIGURED) reads the environ — configured here so the
# content-check tests stay isolated from the machine's real env.
FAKE_ENV = {"CRUDE_FV_SMTP_HOST": "smtp.example.com", "CRUDE_FV_SMTP_USER": "u",
            "CRUDE_FV_SMTP_PASS": "p", "CRUDE_FV_SMTP_TO": "owner@example.com"}


def _fixture(tmp_path: Path, *, trigger_due=False, stale_watchlist=False,
             incoherent=False, static_fallback=False, fresh_prices=True,
             sidecar_stale=False):
    from crude_tanker_fv.scorecard import scenario_inputs_sha

    inputs = tmp_path / "inputs"
    outputs = tmp_path / "outputs"
    (inputs / "market_data").mkdir(parents=True)
    outputs.mkdir()
    (inputs / "scenario_inputs.yaml").write_text("sectors: {}\n")
    sha = "000badc0ffee" if sidecar_stale else scenario_inputs_sha(inputs)
    (outputs / "weight_robustness.yaml").write_text(yaml.safe_dump({
        "computed_against": {"crude": sha},
        "weight_sets": {"crude": {}},
        "names": {"DHT": {"ev_sign_stable": True, "ev_min_pct": 8.0, "ev_max_pct": 20.0}},
    }))
    (inputs / "reweight_triggers.yaml").write_text(yaml.safe_dump({
        "t1": {"sector": "crude", "due": date(2026, 6, 1) if trigger_due else date(2099, 1, 1),
               "observable": "x", "action": "y", "status": "armed", "added": date(2026, 7, 2)},
    }))
    as_of = (date.today() - timedelta(days=40)).isoformat() if stale_watchlist \
        else date.today().isoformat()
    (inputs / "watchlist.yaml").write_text(yaml.safe_dump({
        "DHT": {"current_price": 16.5, "analyst_target": 18.0, "as_of": as_of},
    }))
    fetched = (datetime.now(timezone.utc) - timedelta(days=0 if fresh_prices else 5))
    (inputs / "market_data" / "prices_daily.yaml").write_text(yaml.safe_dump({
        "fetched_at": fetched.isoformat(timespec="seconds"),
        "prices": {"DHT": {"price": 16.5, "asof": fetched.isoformat(timespec="seconds")}},
    }))
    for f in ("vessel_value_curves.yaml", "spot_tce.yaml", "twelve_month_tc.yaml",
              "historical_tce_means.yaml", "ffa_forward_curve.yaml"):
        (inputs / "market_data" / f).write_text("{}\n")
    pb = {"total": 1, "static_fallback": {}, "oldest_static_as_of": None,
          "market_event_review": {}}
    if static_fallback:
        pb["static_fallback"] = {"DHT": {"as_of": "2026-06-04", "reason": "day move -17.2%"}}
    (outputs / "book_scorecard.json").write_text(json.dumps({
        "schema_version": "2.1",
        "price_basis": pb,
        "names": [{"ticker": "DHT", "void": False, "ev_pct": 12.0, "fv": 18.0,
                   "position": "TRIM/SHORT (overvalued)" if incoherent
                   else "BUY (undervalued)"}],
    }))
    # Matching scenario doc so the fv-identity scan has its counterpart surface.
    (outputs / "dht_scenarios.md").write_text(
        "- **Probability-weighted fair value:** $18.00 (+9.1% vs price)\n")
    return inputs, outputs


def test_quiet_when_clean(tmp_path):
    inputs, outputs = _fixture(tmp_path)
    assert collect_flags(inputs, outputs, environ=FAKE_ENV) == []


def test_one_flag_per_class_with_stable_tags(tmp_path):
    inputs, outputs = _fixture(tmp_path, trigger_due=True, stale_watchlist=True,
                               incoherent=True, static_fallback=True, sidecar_stale=True)
    flags = collect_flags(inputs, outputs, environ={})
    tags = {f.split()[0] for f in flags}
    assert tags == {"TRIGGER-DUE", "STALE-INPUT", "SURFACE-INCOHERENT",
                    "PRICE-BASIS", "SIDECAR-STALE", "NOTIFY-UNCONFIGURED"}


def test_notify_unconfigured_flag_alone(tmp_path):
    """WO2 0.1: an otherwise-clean tree with no SMTP env pages nowhere — the
    sentinel nags until ~/.config/crude-tanker-fv.env carries the creds."""
    inputs, outputs = _fixture(tmp_path)
    flags = collect_flags(inputs, outputs, environ={})
    assert len(flags) == 1 and flags[0].startswith("NOTIFY-UNCONFIGURED")
    assert "CRUDE_FV_SMTP_HOST" in flags[0]


def test_sidecar_stale_flag_alone(tmp_path):
    """WO1-F4: a fragility sidecar lagging scenario_inputs.yaml pages on its
    own — the mechanism behind the Jul-2 ⚠-list churn (field lagged engine)."""
    inputs, outputs = _fixture(tmp_path, sidecar_stale=True)
    flags = collect_flags(inputs, outputs, environ=FAKE_ENV)
    assert len(flags) == 1 and flags[0].startswith("SIDECAR-STALE")
    assert "crude" in flags[0]


def test_fv_identity_scan_catches_surface_divergence(tmp_path):
    inputs, outputs = _fixture(tmp_path)
    (outputs / "dht_scenarios.md").write_text(
        "- **Probability-weighted fair value:** $9.27 (+79.0% vs price)\n")
    flags = collect_flags(inputs, outputs)
    assert any(f.startswith("SURFACE-INCOHERENT DHT: JSON fv") for f in flags)


def test_exit_codes_and_log_format(tmp_path, monkeypatch):
    import crude_tanker_fv.sentinel as s

    for k, v in FAKE_ENV.items():
        monkeypatch.setenv(k, v)
    inputs, outputs = _fixture(tmp_path)
    monkeypatch.setattr(s, "INPUTS_DIR", inputs)
    monkeypatch.setattr(s, "OUTPUTS_DIR", outputs)
    log = tmp_path / "state" / "sentinel.log"
    assert main(["--log", str(log)]) == 0
    assert log.read_text().strip().endswith(" OK")

    inputs2, outputs2 = _fixture(tmp_path / "b", trigger_due=True)
    monkeypatch.setattr(s, "INPUTS_DIR", inputs2)
    monkeypatch.setattr(s, "OUTPUTS_DIR", outputs2)
    assert main(["--log", str(log)]) == 1
    last = log.read_text().strip().splitlines()[-1]
    assert " FLAG 1: TRIGGER-DUE" in last
