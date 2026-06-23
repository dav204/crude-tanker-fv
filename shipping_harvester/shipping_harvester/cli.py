"""Command line entry point.

  run       crawl -> dedupe -> select per quarter -> download -> parse -> store
  inspect   dump a single PDF's tables + text, to help you build/repair a parser
  coverage  print marks coverage (quarter x kind) from the stored panel
"""
from __future__ import annotations

import argparse
from dataclasses import replace

from . import config, crawl, download, quarters, store
from .models import MarketMarks
from .net import PoliteSession
from .parse import dispatch_parse, implemented, versions_for
from .parse import base
from .quarters import quarter_of


def _empty_marks(ref) -> MarketMarks:
    return MarketMarks(
        broker_id=ref.broker_id,
        report_date=ref.published,
        quarter=quarter_of(ref.published),
        source_post=ref.post_url,
        source_pdf=ref.pdf_url,
        parser="none",
        parser_ok=False,
        marks=[],
    )


def cmd_run(args: argparse.Namespace) -> None:
    session = PoliteSession()

    print(f"[crawl] HSN (max_pages={args.max_pages}) ...")
    refs = crawl.crawl_hsn(session, max_pages=args.max_pages)
    if args.capitallink:
        print("[crawl] Capital Link ...")
        refs += crawl.crawl_capitallink(session)
    print(f"[crawl] {len(refs)} raw issues")

    refs = download.dedupe(refs)
    lo, hi = quarters.quarter_start(args.since), quarters.quarter_end(args.until)
    refs = [r for r in refs if lo <= r.published <= hi]
    print(f"[dedupe] {len(refs)} issues within {args.since}..{args.until}")
    print(f"[parsers] implemented: {sorted(implemented())} "
          f"(others fall back to generic)")
    multi = {b: versions_for(b) for b in sorted(implemented()) if len(versions_for(b)) > 1}
    if multi:
        print(f"[parsers] multi-format (dispatched by probe+date): {multi}")

    labels = quarters.quarter_range(args.since, args.until)
    parsed: dict[tuple, MarketMarks] = {}
    saved = 0
    for label in labels:
        chosen = quarters.select_for_quarter(refs, label, stale_after_days=args.stale_days)
        for broker_id, (ref, stale) in chosen.items():
            key = (broker_id, ref.published)
            mm = parsed.get(key)
            if mm is None:
                pdf = download.download_pdf(session, ref)
                if pdf:
                    mm, confident = dispatch_parse(broker_id, pdf, ref)
                else:
                    mm, confident = _empty_marks(ref), True
                parsed[key] = mm
                flag = "  STALE" if stale else ""
                warn = "" if confident else "  [!] low-confidence format"
                detail = (f"{len(mm.marks)} marks via {mm.parser}" if mm.parser_ok
                          else f"NO marks ({mm.parser})")
                print(f"  {label} {broker_id:11s} {ref.published} -> {detail}{flag}{warn}")
            store.save_marks(replace(mm, quarter=label))
            saved += 1

    df = store.build_panel()
    print(f"\n[store] {saved} (broker,quarter) mark sets -> {config.PANEL_PARQUET}")
    if not df.empty:
        print("\n[coverage] marks by quarter x kind:")
        print(store.coverage_report(df).to_string())
    else:
        print("[store] no marks extracted yet -- implement/repair parsers, "
              "then re-run (PDFs are cached, so this is fast).")


def cmd_inspect(args: argparse.Namespace) -> None:
    tables = base.extract_tables(args.pdf)
    print(f"{len(tables)} table(s) found in {args.pdf}\n")
    for i, t in enumerate(tables):
        width = max((len(r) for r in t), default=0)
        print(f"--- table {i}: {len(t)} rows x {width} cols ---")
        for row in t[: args.rows]:
            print("   " + " | ".join((c or "")[:16] for c in row))
        print()
    text = base.extract_text(args.pdf)
    print(f"--- text sample ({len(text)} chars total) ---")
    print(text[:1500])


def cmd_coverage(args: argparse.Namespace) -> None:
    df = store.build_panel(write=False)
    if df.empty:
        print("no stored marks")
        return
    print(store.coverage_report(df).to_string())


def cmd_factor(args: argparse.Namespace) -> None:
    import json
    from . import factor

    policy = replace(
        factor.DEFAULT_POLICY, mode=args.mode, spread_warn_pct=args.spread_warn
    )
    resolved, panel = factor.load_and_resolve(policy)
    if resolved.empty:
        print("[factor] no marks to resolve -- run `run` first")
        return

    config.FACTOR_PARQUET.parent.mkdir(parents=True, exist_ok=True)
    resolved.to_parquet(config.FACTOR_PARQUET, index=False)
    print(f"[factor] {len(resolved)} resolved marks ({args.mode}) -> {config.FACTOR_PARQUET}")
    print("\n[coverage] resolved marks by segment x field:")
    print(resolved.groupby(["segment", "field"]).size().unstack(fill_value=0).to_string())

    dis = factor.disagreements(resolved)
    if not dis.empty:
        print(f"\n[disagreements] {len(dis)} groups exceed {args.spread_warn:.0%} cross-broker spread:")
        print(dis.to_string(index=False))

    if args.quarter:
        schema = factor.to_schema_dict(resolved, panel)
        print(f"\n[schema] {args.quarter}:")
        print(json.dumps(schema.get(args.quarter, {}), indent=2))


def cmd_export(args: argparse.Namespace) -> None:
    """Resolve the stored panel and write the engine bridge JSON that
    backtest/build_vintage.py reads (a flat list of resolved marks). `--brokers`
    restricts the source houses (e.g. xclusiv for the validated single-vendor
    value series); omitted = all brokers via the default precedence policy."""
    import json
    import math
    from . import factor

    panel = store.build_panel(write=False)
    if panel.empty:
        print("[export] no marks -- run `run` first")
        return
    if args.brokers:
        panel = panel[panel["broker"].isin(set(args.brokers.split(",")))]
    resolved = factor.to_factor_marks(panel, factor.DEFAULT_POLICY)
    recs = []
    for _, r in resolved.iterrows():
        a = r["anchor"]
        recs.append({
            "quarter": r["quarter"], "segment": r["segment"],
            "vessel_class": r["vessel_class"], "field": r["field"],
            "anchor": None if (a is None or (isinstance(a, float) and math.isnan(a))) else a,
            "value": float(r["value"]),
        })
    from pathlib import Path
    Path(args.out).write_text(json.dumps(recs, indent=1))
    print(f"[export] {len(recs)} resolved marks "
          f"({args.brokers or 'all brokers'}) -> {args.out}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="shipping_harvester")
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="full crawl->parse->store pipeline")
    r.add_argument("--since", required=True, help="e.g. 2024Q1")
    r.add_argument("--until", required=True, help="e.g. 2026Q2")
    r.add_argument("--max-pages", type=int, default=40, help="HSN listing pages to crawl")
    r.add_argument("--stale-days", type=int, default=14,
                   help="flag a quarter mark if the issue is >N days before quarter-end")
    r.add_argument("--capitallink", action="store_true", help="also crawl Capital Link")
    r.set_defaults(func=cmd_run)

    i = sub.add_parser("inspect", help="dump a PDF's tables+text to build parsers")
    i.add_argument("pdf")
    i.add_argument("--rows", type=int, default=6, help="header rows to preview per table")
    i.set_defaults(func=cmd_inspect)

    c = sub.add_parser("coverage", help="print stored marks coverage")
    c.set_defaults(func=cmd_coverage)

    fa = sub.add_parser("factor", help="resolve the broker panel onto the factor schema")
    fa.add_argument("--mode", choices=["precedence", "median", "mean"],
                    default="precedence", help="how to reconcile multi-broker values")
    fa.add_argument("--spread-warn", type=float, default=0.10,
                    help="flag groups whose cross-broker spread exceeds this (fraction)")
    fa.add_argument("--quarter", help="also print the schema dict for this quarter (e.g. 2026Q2)")
    fa.set_defaults(func=cmd_factor)

    ex = sub.add_parser("export-marks", help="write the engine bridge JSON (build_vintage reads it)")
    ex.add_argument("--out", required=True, help="output path, e.g. ../backtest/vintages/_factor_marks.json")
    ex.add_argument("--brokers", help="comma-separated source houses to keep (e.g. xclusiv); omit = all")
    ex.set_defaults(func=cmd_export)
    return p


def main(argv=None) -> None:
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
