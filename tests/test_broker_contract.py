from types import SimpleNamespace
from crude_tanker_fv.broker_reference import broker_reference
from crude_tanker_fv.scorecard import valuation_index, attach_cycles
from crude_tanker_fv.loaders import load_watchlist
from crude_tanker_fv.reconcile import compute_row


def test_broker_reference_price_invariance_and_reconcile_parity():
    watchlist = load_watchlist()
    for ticker in ('HAFN', 'DHT', 'SBLK', 'TEN'):
        entry = watchlist[ticker]
        ref = broker_reference(entry)
        scenario = SimpleNamespace(ticker=ticker, current_price=entry['current_price'] * 2,
                                   base_nav_per_share=ref['nav'] * .6, probability_weighted_fv=12,
                                   position_recommendation='HOLD', scenarios=[])
        broker = SimpleNamespace(ticker=ticker, consensus_pnav=entry['consensus_pnav'], broker_reference=ref)
        v = valuation_index([], [scenario], [broker])[ticker]
        rec = compute_row(ticker, {'tickers': {ticker: {'nav_per_share': scenario.base_nav_per_share, 'k_broker': 1}}}, None, watchlist)
        assert v.broker_nav == rec.broker_nav == ref['nav']
        scenario.current_price *= 3
        assert valuation_index([], [scenario], [broker])[ticker].broker_nav == ref['nav']
        if ticker == 'HAFN':
            assert v.sanity == 'OK'


def test_cycle_export_has_sleeve_identity_and_engine_values():
    values = {t: SimpleNamespace(cycles=None) for t in ('SB', 'SBLK', 'TEN', 'CMBT', 'INSW')}
    attach_cycles(values, '2026-Q2')
    from crude_tanker_fv.pipeline import value_company
    report = value_company('SB', '2026-Q2', 9, 10)
    assert values['SB'].cycles[0]['ratio'] == report.cycle.cycle_position
    assert {c['sector'] for c in values['TEN'].cycles} == {'crude', 'product', 'lng'}
    assert all(c['scope'] == 'sleeve' for t in ('TEN', 'CMBT', 'INSW') for c in values[t].cycles)
    assert all(c['anchor_basis'] for v in values.values() for c in v.cycles)
