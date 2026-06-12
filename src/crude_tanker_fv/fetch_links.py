"""Download Pareto linked reports from the daily-link inventory — the
NETWORK half of the linked-report harvest, split out of sp_scan on
purpose (2026-06-12).

Why a separate entry point: permission allowlists for agent sessions are
prefix matchers, so a network-touching FLAG on an otherwise-local module
(`sp_scan --fetch-links`) leaks through any open-ended allow rule the
moment the flags are reordered (`sp_scan --since X --fetch-links`).
Keeping every sp_scan mode local-only and giving the download its own
module makes the boundary structural: `sp_scan *` is safe to allow,
this module is the thing that prompts.

All download logic lives in sp_scan.run_fetch_links (inventory dedupe,
report-id write-back, polite spacing); this is just the front door.

CLI:
    python -m crude_tanker_fv.fetch_links
"""

from __future__ import annotations

import argparse

from crude_tanker_fv.sp_scan import run_fetch_links


def main(argv: list[str] | None = None) -> int:
    # Zero options by design: this is an ask-gated network module, and any
    # unrecognized argv must error out before a download pass starts
    # (2026-06-12: `--help` silently ran a real pass when there was no parser).
    ap = argparse.ArgumentParser(
        prog="python -m crude_tanker_fv.fetch_links",
        description="Download Pareto linked reports from the daily-link inventory "
                    "(network half of the harvest; sp_scan stays local-only)")
    ap.parse_args(argv)

    got, skipped, failed = run_fetch_links()
    print(f"downloaded {got}, skipped (already archived) {skipped}, failed {failed}")
    if got:
        print("rebuild the manifest: python -m crude_tanker_fv.pareto_archive --build-manifest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
