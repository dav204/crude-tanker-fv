"""Smoke test for the throwaway context probe (WO2 0.5): one run, one line,
every field present. Probes degrade gracefully off-macOS (CI runs this)."""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_probe_writes_one_complete_line(tmp_path):
    log = tmp_path / "ctxprobe.log"
    r = subprocess.run([str(ROOT / "scripts" / "ctxprobe" / "context_probe.sh")],
                       env={"HOME": str(tmp_path), "PATH": "/usr/sbin:/usr/bin:/sbin:/bin",
                            "CTXPROBE_LOG": str(log)},
                       capture_output=True, text=True, timeout=30)
    assert r.returncode == 0, r.stderr
    lines = log.read_text().strip().splitlines()
    assert len(lines) == 1
    for key in ("initiator=", "console_user=", "switched_in=", "secs_since_wake=",
                "default_route=", "http_ok=", "secrets_readable=", "power="):
        assert key in lines[0], f"missing {key}: {lines[0]}"
