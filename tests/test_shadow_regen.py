"""Shadow build (2026-09-11): a `.yaml.draft` pair is invisible to the live loaders — the
drafts-only doctrine (CLAUDE.md 2026-07-03) holds by construction — and the shadow script
refuses to run without a draft (it must never value a name on the live sheet by accident)."""

import subprocess
from pathlib import Path

import pytest

from crude_tanker_fv import loaders

ROOT = Path(__file__).resolve().parents[1]


def test_draft_sheet_is_invisible_to_resolution(tmp_path):
    bs = tmp_path / "balance_sheets"
    bs.mkdir()
    (bs / "ten_2026-Q2.yaml.draft").write_text("ticker: TEN\nquarter: 2026-Q2\n")
    with pytest.raises(FileNotFoundError):
        loaders.resolve_balance_sheet_path("TEN", "2026-Q2", tmp_path)
    (bs / "ten_2026-Q1.yaml").write_text("ticker: TEN\nquarter: 2026-Q1\n")
    path, vintage = loaders.resolve_balance_sheet_path("TEN", "2026-Q2", tmp_path)
    assert path.name == "ten_2026-Q1.yaml" and vintage == "2026-Q1"


def test_shadow_script_refuses_without_a_draft():
    r = subprocess.run(["bash", "scripts/shadow_regen.sh", "ZZZZ", "2026-Q2"],
                       cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 2 and "NO DRAFT" in r.stdout
