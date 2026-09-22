"""Render the frozen experiment and its exceptions for owner review."""
import json
from pathlib import Path

P=Path(__file__).resolve().parent
O=P/'results'
METHODS=('legacy','cash','reference','risk','smooth','cash_reference','cash_reference_risk','combined','reference_risk_smooth')


def fmt(x, n=2):
    return 'unavailable' if x is None else f'{x:,.{n}f}'


def main():
    cfg=json.loads((P/'assumptions.json').read_text())
    data={m:json.loads((O/(m+'.json')).read_text()) for m in METHODS}
    comp=json.loads((O/'comparison.json').read_text())
    events=json.loads((O/'governor_events.json').read_text())
    checks=json.loads((O/'identity_checks.json').read_text())
    drifts=json.loads((O/'drift_checks.json').read_text())
    funding=json.loads((O/'funding_exceptions.json').read_text())
    manifest=json.loads((P/'frozen/manifest.json').read_text())
    lines=['# Economic-method owner review · frozen 22 September 2026','',
      'Research package; no production adoption, publication, baseline reset or orders. All values are USD per share, including 2343.', '',
      '## Recommendation', '',
      'Keep production methods unchanged. The isolated engine and full-book experiment are implemented, but the package is **not ready for blanket adoption**. The cash/reference/risk numbers below are assumption-led diagnostics. Their missing inputs are adoption blockers, not resolved by passing tests.', '',
      '| Method | Result | Recommendation |', '|---|---|---|',
      '| Payout/cash bridge | Quarterly ledger, policy variants, terminal claims and sensitivities implemented; 22 provisional standalone valuations; three hybrids withheld | Defer every name until source schedules, financing and distribution basis reconcile. Current hybrid corporate cash is shown once; joint-scenario FV remains unavailable. |',
      '| Fixed scenario references | FFA-only invariance passes across all 25 names and hybrid sleeves; base migration delta zero | Defer adoption until vessel-mark/reference historical pairings are evidenced. The frozen current pair is a proposal, not recovered history. |',
      '| D-M2 risk | External broad-transportation calibration, issuer leverage and propagation implemented | Defer every name. Six separate shipping-sector asset-risk calibrations remain unfinished; financing, cash and preferred/NCI conventions need review. Do not adopt the proxy as if independently calibrated by sector. |',
      '| D-M4 smoothing | Independent and combined effects computed; continuous interpolation, existing labels retained | Mechanically ready for review. Adopt only through the ruled D1 round, after LR1 sequencing and explicit approval of outer anchors 0.30/1.70. |',
      '| D-M3 parity | VOID under the original >=80% class-source-coverage kill condition | Retain historical denominators. Only 10/19 current classes are calculable (52.6%, an upper bound on dated coverage). Three-vintage stability/reconciliation was not performed after this stop. No narrower post-hoc adoption. |', '',
      '## Before/after, independent effects and interactions', '',
      'The ordered combination is cash → reference → risk → smoothing. Independent deltas are against legacy; interaction equals combined delta less their sum. Low/high assumption corners are not confidence intervals or guaranteed FV bounds. The reference base delta is zero for every name; its ±10% uncertainty stress is in the detailed results.', '',
      '| Ticker | Legacy FV | Cash Δ | Risk Δ | Smooth Δ | Combined FV | Combined Δ% | Interaction |', '|---|---:|---:|---:|---:|---:|---:|---:|']
    for t,c in comp.items():
        f,d=c['fv'],c['delta'];pct=None if d['combined'] is None else d['combined']/f['legacy']*100
        lines.append(f"| {t} | {fmt(f['legacy'],3)} | {fmt(d['cash'],3)} | {fmt(d['risk'],3)} | {fmt(d['smooth'],3)} | {fmt(f['combined'],3)} | {fmt(pct)} | {fmt(c['interaction'],3)} |")
    lines += ['', 'Cash and risk effects can offset. They are not additive because discounting, retained cash, payout caps and cycle weights interact. CCEC is the largest combined decline in this frozen base corner; TNK is the largest dollar increase. These are model comparisons, not revised actionable price targets.', '',
      '## Existing thresholds and restrictions', '',
      'Independent current NAV is exactly unchanged in every available experiment. Broker matched pairs and prices are unchanged, so this work does not alter the broker-NAV spread or its multiplier. Baseline reproduction includes all governed numeric fields, intervals, labels, cycles, blend and hybrid contributions, not just rounded headline FV.', '',
      'The existing >2pp EV, >2% NAV and >0.05 broker-multiplier drift thresholds are retained. The table below lists forcing breaches versus the committed producer baseline; raw states remain UNEXPLAINED pending owner acceptance, with no research re-ratification. An inside-interval band change is described as inside-interval, not proof of a price-only cause.', '',
      '| Experiment | Forcing breaches | Missing computations |', '|---|---|---|']
    for m,rs in drifts.items():
        lines.append('| '+m+' | '+('; '.join(r['ticker']+': '+','.join(r['breaches']) for r in rs if r['status']=='UNEXPLAINED') or 'none')+' | '+(', '.join(r['ticker'] for r in rs if r['status']=='missing') or 'none')+' |')
    lines += ['', 'The mechanically attributed source of each method move is its registered equation, with all other determinants fixed. Forcing moves are listed for review; the protocol has not been widened. Method-specific capital/retained-cash and discount-rate rows are in [DETAILS.md](DETAILS.md); scenario-level cash ledgers and vessel multipliers are in `results/<method>.json`.', '',
      'Governor comparison uses the frozen review registry through the real checker with in-memory shadow envelopes. It does not consume live publications or update last-observed/review state. Construction tiers remain frozen input-quality classifications; they do not certify the new methods. All shadow documents carry an explicit research-only adoption gate.', '',
      '| Experiment | New or changed conditions versus legacy | Conditions absent in that shadow only |', '|---|---|---|']
    be={e['id']:e for e in events['legacy']['events']}
    for m in METHODS[1:]:
        cur={e['id']:e for e in events[m]['events']}
        changed=[e['id']+' ('+e['severity']+')' for k,e in cur.items() if k not in be or e['value']!=be[k]['value']]
        gone=[k for k in be if k not in cur]
        lines.append('| '+m+' | '+('; '.join(changed) or 'none')+' | '+('; '.join(gone) or 'none')+' |')
    lines += ['', 'No shadow recovery lifts SB sign-instability, SBLK read caps, candidate restrictions, war/thesis gates, or missing review-baseline attestations in production. Existing filing and quarterly follow-ups remain open. Owner review must distinguish data movement from acceptance of a new model.', '',
      '## Financing and data exceptions', '',
      '| Experiment | Names with a funding gap or intended-dividend shortfall in at least one case |', '|---|---|']
    for m in METHODS:
        lines.append('| '+m+' | '+(', '.join(funding[m]) or 'none in computed cases')+' |')
    lines += ['', 'See `results/funding_exceptions.json` for each quarter/case and amount. Negative cash identifies required financing and is not an assumed borrowing facility. Zero modeled draws, sales, buybacks or issuance do not certify that no documented obligations/events exist. Full schedule verification remains open. Preferred/NCI and restricted-cash treatment are especially material for TEN, BWLP and the newbuilding names.', '',
      'The normalized justified-P/NAV earnings diagnostic remains explicitly labelled as the legacy pre-depreciation proxy. Cash-strip accounting EPS has separate versioned semantics. Completing a reconciled normalized accounting-EPS diagnostic is an additional adoption task; changing its label alone would not fix the underlying definition.', '',
      '## Evidence and reproducibility', '',
      f"Production input commit: `{manifest['production_commit']}`. Accepted publication retained: `{manifest['accepted_publication_id']}`. Governor registry frozen from `{manifest['governor_commit']}`.", '',
      'The preregistration was committed at `e533134` before changed fair values were evaluated. It freezes formulas, rates, source cutoff, analyst ranges, expected directions and invariants. Later source observations are recorded separately in [SOURCE_SUPPLEMENT.md](SOURCE_SUPPLEMENT.md); they have not been slipped into the comparison.', '',
      f"Identity checks passed over {checks['cash_identity_rows']:,} current/scenario ledger rows. All 25 baseline fair values and governed handoff fields reproduce. Full verification commands and test receipts are in [VERIFICATION.md](VERIFICATION.md). A real committed shadow fixture is rejected by the publication validator as research; no SMTP or healthcheck transport was enabled.", '',
      'Review [PARAMETERS.md](PARAMETERS.md) for issuer policy/rate assumptions, [DETAILS.md](DETAILS.md) for each name and sleeve, and `results/sensitivity.json` for frozen low/high corners. `results/comparison.json` retains every ordered experiment and interaction. `results/parity.json` records the void and unevaluated vintages.', '',
      '## Owner decisions and adoption sequence', '',
      '1. Complete issuer cash/claim schedules and verified accounting-to-distributable adjustments; resolve financing gaps and hybrid joint-scenario mapping. Replace proxy depreciation and reserve estimates with disclosed bases. Re-register source changes separately before recalculating effects.',
      '2. Recover historical vessel-mark/reference pairings, or review an explicit alternative reference range as a new decision. Current-reference invariance proves the mechanism, not the historical calibration.',
      '3. Finish independent shipping-sector asset-risk calibration; review the numerical rate table, funding rates, cash risk, leases, tax-shield and preferred/NCI treatment. Keep the 11% comparator and separate 11% newbuild / 8% parity rates.',
      '4. Complete the overdue LR1 anchor round as its own attributed input leg. Then take the single ruled D1 cycle round: parity remains historical following VOID; review smoothing and its proposed outer anchors separately.',
      '5. Only after scoped owner adoption: regenerate at a newly frozen live price/input vintage, explain existing-threshold breaches, review all governor events and expressly ratify any changed producer or governor review baseline. Processing/emailing a study never ratifies it.', '',
      '## Rollback / storage', '',
      'Implementation is retained on local branch `codex/economic-method-review`; production receives only review artifacts and operational status. Research code requires an isolated checkout, and research-marked handoffs cannot publish. To abandon the study, keep production as it is and stop invoking the research runner. Preserve the frozen package and receipts. Any later activation needs a separately reviewable commit and a recorded previous accepted-publication pointer; reverting that adoption must not erase receipts or reset governor baselines.', '']
    (P/'REVIEW.md').write_text('\n'.join(lines))
    aggregates={}
    details=['# Full-book method detail','', 'USD per share; current-market strips below are distinct from scenario-weighted headline FV. Legacy terminal cash is the old implied cash-plus-retained-earnings amount; it is not a reconciled balance sheet. Research terminal cash/debt comes from the last explicit ledger quarter. The legacy extra terminal discount quarter is retained. Hybrid current-ledger common horizon is in `results/hybrid_current_cash.json`; new hybrid scenario cash FV is unavailable.', '']
    params=['# Proposed parameters · not approved for production','', 'The broad Transportation asset-risk grid is 6.9216% / 7.6894% / 9.6505% for all six sectors. This does **not** satisfy separate shipping-sector calibration. Base = 4.75% risk-free + 0.71 × 4.14% ERP. Low/high combine an analyst ±0.10 beta sensitivity with published alternative ERP constructions; they are not confidence limits. Source dates: beta January 2026; risk-free/ERP September 1, 2026.', '',
      '[Damodaran current premium inputs](https://pages.stern.nyu.edu/adamodar/New_Home_Page/home.htm), [industry betas](https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/Betas.html). Exact formula and conventions: [PREREGISTRATION.md](PREREGISTRATION.md).', '',
      '| Ticker | Policy forecast | rE low/base/high % | Funding % | D&A per quarter $m | Evidence basis |', '|---|---|---:|---:|---:|---|']
    for t,c in cfg['companies'].items():
        src=c.get('source',c.get('policy_source'))
        policy=c['policy']['base']
        params.append(f"| {t} | {policy['basis']}; ratio {policy['ratio']}; base DPS {policy['base_dps']} | "+'/'.join(fmt(100*c['risk'][p]) if c['risk'][p] is not None else 'unavailable' for p in ('low','base','high'))+f" | {fmt(c['funding_cost']*100)} | {fmt(c['quarterly_depreciation']/1e6)} | {c['depreciation_basis']} |")
        details += [f'## {t}', '', '**Recommendation:** defer cash/reference/risk adoption; smoothing only via owner-approved D1/LR1 sequence. Parity stays historical.', '',
          'Blockers: '+'; '.join(comp[t]['blockers'])+'.', '',
          '| Method | Weighted FV | Interval | Position | Sign stable | Read flag | rE % |', '|---|---:|---|---|---|---|---:|']
        for m in METHODS:
            r=data[m][t]
            if r['fv'] is None:details.append(f"| {m} | unavailable | — | — | — | — | — |");continue
            h=r['handoff']
            details.append(f"| {m} | {fmt(r['fv'],4)} | {fmt(h['fv_low'])}–{fmt(h['fv_high'])} | {h['position']} | {h['weight_sign_stable']} | {h['read_flag']} | {fmt(r['discount_rate']*100)} |")
        aggregates[t]={}
        details += ['', '| Method | Scenario-weighted Σ DPS | Terminal cash $m | Debt+leases $m | Scenario-weighted terminal PV/share |', '|---|---:|---:|---:|---:|']
        for m in METHODS:
            r=data[m][t]
            if r['fv'] is None:
                aggregates[t][m]=dict(status='unavailable',reason=r['reason']);continue
            shares=c['clean_nav']/r['nav']
            totals=dict(dps=0.0,terminal_pv=0.0,terminal_cash=0.0,terminal_debt=0.0)
            has_bridge=False
            for sector,sl in r['sleeves'].items():
                sc=sl['scenarios']['scenarios'];den=sum(x['weight'] for x in sc)
                for case in sc:
                    detail=case.get('economic_research')
                    if detail is None:raise ValueError('missing scenario strip trace')
                    st=detail['strip'];w=case['weight']/den
                    totals['dps']+=w*sum(st['dps_by_quarter'])
                    totals['terminal_pv']+=w*st['discounted_terminal_value']
                    if st['cash_bridge']:
                        has_bridge=True;last=st['cash_bridge'][-1]
                        totals['terminal_cash']+=w*last['closing_cash']
                        totals['terminal_debt']+=w*(last['debt']+last['leases'])
                    else:
                        totals['terminal_cash']+=w*sum(e-d for e,d in zip(st['eps_by_quarter'],st['dps_by_quarter']))*shares
            if not has_bridge:
                totals['terminal_cash']+=c['opening']['cash']
                totals['terminal_debt']=c['opening']['debt']+c['opening']['leases']
            totals['cash_basis']='reconciled forecast' if has_bridge else 'legacy cash plus pre-depreciation retained proxy'
            totals['aggregation']='marginal sector expectations; not joint cash-policy evaluation' if c['hybrid'] else 'scenario probability weighted'
            aggregates[t][m]=totals
            details.append(f"| {m} | {fmt(totals['dps'],4)} | {fmt(totals['terminal_cash']/1e6)} | {fmt(totals['terminal_debt']/1e6)} | {fmt(totals['terminal_pv'],4)} |")
        details += ['', '| Method / sleeve | Current NAV | Σ current DPS | Terminal cash $m | Debt+leases $m | Terminal value/share | Cycle ratio / label |', '|---|---:|---:|---:|---:|---:|---|']
        for m in ('legacy','cash','risk','smooth','combined','reference_risk_smooth'):
            r=data[m][t]
            if r['fv'] is None:continue
            for sector,s in r['sleeves'].items():
                strip=s['strip'];ledger=strip['cash_bridge'];cycle=s['cycle']
                if ledger:cash=ledger[-1]['closing_cash'];debt=ledger[-1]['debt']+ledger[-1]['leases']
                elif not c['hybrid']:
                    shares=c['clean_nav']/r['nav']
                    cash=c['opening']['cash']+sum(e-d for e,d in zip(strip['eps_by_quarter'],strip['dps_by_quarter']))*shares
                    debt=c['opening']['debt']+c['opening']['leases']
                else:cash=None;debt=None
                details.append(f"| {m} / {sector} | {fmt(r['nav'],4)} issuer | {fmt(sum(strip['dps_by_quarter']),4)} | {fmt(cash/1e6) if cash is not None else 'corporate; see joint ledger'} | {fmt(debt/1e6) if debt is not None else 'corporate'} | {fmt(strip['terminal_value'])} | {fmt(cycle['cycle_position'],4)} / {cycle['band_label']} |")
        details += ['', 'Independent and ordered method deltas, low/high parameter corners, per-scenario vessel multipliers, strip cash/earnings and reference identity are retained in the matching JSON artifacts. A source-mapped schedule is required before interpreting the provisional change as an adopted FV.', '']
    params += ['', 'Policy source dates/URLs, all quarterly schedule values, low/base/high policy details, corporate opening claims, sector asset weights and reference mark hashes are in `assumptions.json`. One reference is stored per issuer/sleeve. Sources or zero/default forecast entries must not be promoted as verified schedules.', '',
      'Cycle proposal: ratio/NAV weight/terminal multiplier = (0.30,0.30,1.10), (0.65,0.40,1.05), (1.00,0.50,1.00), (1.35,0.60,0.95), (1.70,0.70,0.90). Clamp outside. Existing labels and categorical boundaries remain unchanged.', '']
    params += ['## Frozen issuer policy sources', '', 'These are source observations, not certifications of the entire forecast schedule. Later observations are kept in SOURCE_SUPPLEMENT.md.', '', '| Issuer | Source date | Reference / observation |', '|---|---|---|']
    for t,c in cfg['companies'].items():
        source=c['source']
        params.append(f"| {t} | {source['date']} | [{source['finding']}]({source['url']}) |")
    params += ['', 'Exact base policy parameters (all remain forecasts subject to the stated source gaps):', '']
    for t,c in cfg['companies'].items():
        params.append('- '+t+': `'+json.dumps(c['policy']['base'],sort_keys=True)+'`')
    params.append('')
    (O/'scenario_aggregates.json').write_text(json.dumps(aggregates,indent=2)+'\n')
    (P/'DETAILS.md').write_text('\n'.join(details));(P/'PARAMETERS.md').write_text('\n'.join(params))


if __name__=='__main__':main()
