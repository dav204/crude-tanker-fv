import os
from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
FAMILIES = ['crude_weight_robustness', 'dry_bulk_weight_comparison',
            'lng_weight_comparison', 'lpg_weight_comparison', 'product_weight_comparison']


def run_regen(tmp_path, fail=''):
    (tmp_path / 'scripts').mkdir()
    shutil.copyfile(ROOT / 'scripts/regen.sh', tmp_path / 'scripts/regen.sh')
    (tmp_path / '.venv/bin').mkdir(parents=True)
    python = tmp_path / '.venv/bin/python'
    python.write_text('''#!/bin/sh
printf '%s\\n' "$*" >> calls
case "$*" in
  *"$FAIL_FAMILY"*) [ -z "$FAIL_FAMILY" ] || exit 1 ;;
esac
exit 0
''')
    python.chmod(0o755)
    subprocess.run(['git', 'init', '-q'], cwd=tmp_path, check=True)
    return subprocess.run(['bash', 'scripts/regen.sh', '2026-Q2'], cwd=tmp_path,
                          env=dict(os.environ, FAIL_FAMILY=fail), capture_output=True, text=True)


def test_ordinary_regeneration_refreshes_every_family_before_pipeline(tmp_path):
    result = run_regen(tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    calls = (tmp_path / 'calls').read_text().splitlines()
    assert calls[:5] == ['scripts/' + name + '.py' for name in FAMILIES]
    assert calls[5] == '-m crude_tanker_fv.pipeline 2026-Q2'


def test_failed_family_prevents_partial_pipeline_and_success(tmp_path):
    result = run_regen(tmp_path, 'dry_bulk_weight_comparison')
    assert result.returncode == 4
    calls = (tmp_path / 'calls').read_text()
    assert 'crude_tanker_fv.pipeline' not in calls
    assert 'SIDECAR FAILED: dry_bulk_weight_comparison' in result.stdout
