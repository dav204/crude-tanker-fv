"""Tests for the fetch_links front door (argparse boundary, 2026-06-12).

The module is ask-gated network surface: argv it doesn't recognize must
exit before any download pass starts. run_fetch_links is bound into the
fetch_links namespace at import, so patches target fetch_links, not sp_scan.
"""

import pytest

from crude_tanker_fv import fetch_links


def _explode():
    raise AssertionError("download pass must not run")


def test_help_exits_zero_without_network(monkeypatch, capsys):
    monkeypatch.setattr(fetch_links, "run_fetch_links", _explode)
    with pytest.raises(SystemExit) as exc:
        fetch_links.main(["--help"])
    assert exc.value.code == 0
    assert "usage:" in capsys.readouterr().out


def test_unknown_flag_exits_nonzero_without_network(monkeypatch):
    monkeypatch.setattr(fetch_links, "run_fetch_links", _explode)
    with pytest.raises(SystemExit) as exc:
        fetch_links.main(["--bogus"])
    assert exc.value.code == 2


def test_no_args_runs_download(monkeypatch, capsys):
    monkeypatch.setattr(fetch_links, "run_fetch_links", lambda: (0, 3, 0))
    assert fetch_links.main([]) == 0
    assert "skipped (already archived) 3" in capsys.readouterr().out
