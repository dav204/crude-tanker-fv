import copy
import json
import subprocess
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

from crude_tanker_fv import vie_trial as v
from crude_tanker_fv.calendar import construct_panel
from crude_tanker_fv.runtime import atomic_json, commit_paths


def setup(tmp_path):
    cfg = json.loads((Path(__file__).parents[1] / v.CONFIG).read_text())
    # The live trial is paused by the 2026-09-24 producer freeze; these tests exercise the enabled trial.
    cfg['enabled'] = True
    for panel in v.PANELS:
        cfg['contracts'][panel] = dict(identity=panel+'-test', vessel_spec='test-vessel',
                                      evidence=['fixture'], quote_basis='mid')
    atomic_json(tmp_path / v.CONFIG, cfg)
    artifact = tmp_path / 'raw.txt'
    artifact.write_text('test raw quotes')
    entry = dict(version=1, provider='test', source_date='2026-09-23',
                 observed_at='2026-09-23T17:00:00+00:00', retrieved_at='2026-09-23T18:00:00+00:00',
                 units='USD/day', quote_basis='mid', contracts=cfg['contracts'], provenance={'test':True},
                 raw_artifact='raw.txt', raw_sha256=v.digest(artifact.read_bytes()), quotes=[])
    for panel in v.PANELS:
        for label, rate in {'sep':30000,'oct':29000,'q4':28000,'q1':25000,'cal27':24000}.items():
            kind, period = v.normalize(label, date(2026,9,23))
            entry['quotes'].append(dict(panel=panel, original_label=label, kind=kind, period=period, rate=rate))
    return cfg, entry


NOW = datetime(2026,9,24,tzinfo=timezone.utc)


def test_normalized_replay_parity(tmp_path):
    cfg, row = setup(tmp_path)
    result = v.validate_record(row, cfg, tmp_path, NOW)
    expected = construct_panel('2026-09-23', {'sep':30000,'oct':29000,'q4':28000,'q1':25000,'cal27':24000}, (-500,-500))
    assert result['Cape'] == expected
    assert all(not any(c['delta']) for c in v.compare_records(row, row, cfg, tmp_path, NOW)['classes'])


@pytest.mark.parametrize('change', ['contract','time','hash','nan','panel','period','conflict','fraction'])
def test_invalid_records_block(tmp_path, change):
    cfg, row = setup(tmp_path)
    if change == 'contract': row['contracts'] = dict(row['contracts'], cape=None)
    if change == 'time': row['observed_at'] = '2026-09-23T17:00:00'
    if change == 'hash': row['raw_sha256'] = 'bad'
    if change == 'nan': row['quotes'][0]['rate'] = float('nan')
    if change == 'fraction': row['quotes'][0]['rate'] = 30000.5
    if change == 'panel': row['quotes'] = [q for q in row['quotes'] if q['panel'] != 'pmax']
    if change == 'period': row['quotes'][0]['period'] = '2027-09'
    if change == 'conflict': row['quotes'].append(dict(row['quotes'][0], rate=1))
    with pytest.raises((ValueError, TypeError)):
        v.validate_record(row, cfg, tmp_path, NOW)


def test_unknown_legacy_and_stale_print_block(tmp_path):
    cfg, row = setup(tmp_path)
    cfg['contracts']['cape'] = None
    with pytest.raises(ValueError, match='unconfirmed'):
        v.validate_record(row, cfg, tmp_path, NOW)
    cfg, row = setup(tmp_path)
    with pytest.raises(ValueError, match='stale'):
        v.validate_record(row, cfg, tmp_path, datetime(2026,10,5,tzinfo=timezone.utc))


def test_richer_feed_selects_calendar_not_positions(tmp_path):
    cfg, row = setup(tmp_path)
    expected = v.panel_subset(row, 'cape')
    for label in ('nov26','cal28'):
        kind, period = v.normalize(label, date(2026,9,23))
        row['quotes'].insert(0,dict(panel='cape', original_label=label, kind=kind, period=period,rate=20000))
    assert v.panel_subset(row, 'cape') == expected
    row['quotes'].append(dict(panel='cape',original_label='q227',kind='quarter',period='2027-Q2',rate=22000))
    result=v.panel_subset(row,'cape')
    node=next(n for n in result['nodes'] if n['period']=='2027-Q2')
    assert node['rate']==22000 and node['kind']=='quoted'


@pytest.mark.parametrize('day,panel', [
    ('2026-10-02',{'oct':20000,'nov':20000,'q426':21000,'q127':19000,'cal27':18000}),
    ('2026-11-25',{'dec26':20000,'jan27':20000,'q426':21000,'q127':19000,'cal27':18000}),
    ('2026-12-30',{'dec26':20000,'jan27':20000,'q127':21000,'q227':19000,'cal27':18000}),
    ('2027-01-04',{'jan27':20000,'feb27':20000,'q127':21000,'q227':19000,'cal28':18000}),
])
def test_rollovers(day,panel):
    original = construct_panel(day,panel,(-500,-500))
    assert original == construct_panel(day,panel,(-500,-500),strict_widget=False)


def test_direct_quarter_without_months():
    r = construct_panel('2026-10-02',{'q426':21000,'q127':19000,'cal27':18000},(-500,-500),strict_widget=False)
    assert r['values'][0] == 21000
    assert r['nodes'][0]['kind'] == 'quoted'
    with pytest.raises(ValueError,match='remaining-quarter'):
        construct_panel('2026-11-02',{'q127':21000,'q227':19000,'cal27':18000},(-500,-500),strict_widget=False)


def archive(root, day='2026-09-18'):
    p = root / ('inputs/research_mb/dry_bulk_weekly/2026/'+day+'_Weekly.pdf')
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(b'%PDF sample')
    manifest = root/'shipping_harvester/data/manifest.jsonl'
    manifest.parent.mkdir(parents=True,exist_ok=True)
    manifest.write_text('')
    return p


def test_backlog_survives_age_and_duplicates(tmp_path):
    p=archive(tmp_path)
    calls=[]
    def extract(path):
        calls.append(path)
        return [dict(page=1,kind='transaction',text='Vessel sold')],[]
    first=v.scan_documents(tmp_path,date(2026,9,24),extract)
    duplicate=p.with_name('2026-09-19_duplicate.pdf'); duplicate.write_bytes(p.read_bytes())
    second=v.scan_documents(tmp_path,date(2026,9,24),extract)
    assert len(calls)==1 and len(second['documents'])==1
    assert len(next(iter(second['documents'].values()))['sources'])==2
    old=v.scan_documents(tmp_path,date(2027,2,1),extract)
    assert len(old['documents'])==1 and next(iter(old['documents'].values()))['disposition'] is None


def test_malformed_manifest_and_extraction_failure(tmp_path):
    archive(tmp_path)
    def fail(path): raise ValueError('layout unreadable')
    result=v.scan_documents(tmp_path,date(2026,9,24),fail)
    assert next(iter(result['documents'].values()))['review']=='pending_repair'
    (tmp_path/'shipping_harvester/data/manifest.jsonl').write_text('bad')
    with pytest.raises(ValueError,match='manifest line'):
        v.scan_documents(tmp_path,date(2026,9,24),fail)


def test_run_receipts_unique_and_restart(tmp_path):
    setup(tmp_path); archive(tmp_path)
    first=v.run(tmp_path,NOW,lambda p:([],[]))
    second=v.run(tmp_path,NOW,lambda p:([],[]))
    assert first['run_id'] != second['run_id']
    assert first['status']=='failed'
    assert second['stages']['documents']['pending']==1
    assert len(list((tmp_path/v.STATE/'runs').glob('*.json')))==2
    assert 'legacy_ffa' in v.report(tmp_path)


def test_ack_requires_committed_evidence_and_scoped_commit(tmp_path):
    archive(tmp_path)
    d=v.scan_documents(tmp_path,date(2026,9,24),lambda p:([],[]))
    sha=next(iter(d['documents']))
    subprocess.run(['git','init','-q'],cwd=tmp_path,check=True)
    subprocess.run(['git','config','user.email','test@example.com'],cwd=tmp_path,check=True)
    subprocess.run(['git','config','user.name','Test'],cwd=tmp_path,check=True)
    (tmp_path/'disposition.md').write_text('reviewed '+sha)
    with pytest.raises(subprocess.CalledProcessError): v.acknowledge(tmp_path,sha,'disposition.md')
    (tmp_path/'unrelated.txt').write_text('keep staged')
    subprocess.run(['git','add','unrelated.txt'],cwd=tmp_path,check=True)
    commit_paths(tmp_path,['disposition.md'],'disposition')
    v.acknowledge(tmp_path,sha,'disposition.md')
    assert v.read_json(tmp_path/v.STATE/'documents.json')['documents'][sha]['review']=='triaged'
    assert subprocess.check_output(['git','diff','--cached','--name-only'],cwd=tmp_path,text=True).strip()=='unrelated.txt'


def test_twenty_day_window_does_not_reset_on_miss():
    cfg={'window_start':'2026-09-23'}
    r=v.trial_window(cfg,[],date(2026,10,21))
    assert r['elapsed_days']==20 and r['spans_month_end'] and len(r['missing'])==20
    rows=[dict(source_date=d,status='complete') for d in r['missing'][1:]]
    assert v.trial_window(cfg,rows,date(2026,10,21))['status']=='pass'
    assert v.trial_window(cfg,rows[1:],date(2026,10,21))['status']=='incomplete'


def test_named_table_rows_preserve_missing_prices():
    text='''S&P
NAME    DWT    BUILT    YARD    SELLER    BUYER    PRICE
Osaka Star       84,947  2016   Sasebo   Seller   Undisclosed   33.25  Eco
China Spirit    35,097  2013   Yard     Seller   Undisclosed          bss TC back
'''
    rows=v.table_candidates(text,3)
    assert len(rows)==2 and rows[0]['vessel']=='Osaka Star' and rows[0]['dwt']==84947
    assert rows[1]['kind']=='transaction_table' and 'bss TC back' in rows[1]['text']
    assert all('price' not in row for row in rows)


def test_queue_limit_never_changes_membership(tmp_path):
    p=archive(tmp_path)
    for n in range(85):
        p.with_name('2026-09-18_report_%d.pdf'%n).write_bytes(b'%PDF '+str(n).encode())
    v.scan_documents(tmp_path,date(2026,9,24),lambda p:([],[]))
    assert v.pending_documents(tmp_path,5)['total_pending']==86
    assert len(v.pending_documents(tmp_path,5)['documents'])==5
    assert len(v.pending_documents(tmp_path,0)['documents'])==86
