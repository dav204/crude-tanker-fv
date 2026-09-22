"""Legacy production-path replay in the isolated checkout at the frozen price date."""
import json
import runpy
import sys
from datetime import datetime
from pathlib import Path
from unittest.mock import patch
from crude_tanker_fv.price_refresh import is_fresh

ROOT=Path(__file__).resolve().parents[2]
if ROOT.resolve()==Path('/Users/dan_personal/Projects/crude-tanker-fv'):
    raise SystemExit('regeneration refuses production checkout')
baseline=json.loads((ROOT/'research/economic-methods/frozen/book_scorecard.json').read_text())
now=datetime.fromisoformat(baseline['generated_at'].replace('Z','+00:00'))
sys.argv=['pipeline','2026-Q2','--valuation-date','2026-09-22']
with patch('crude_tanker_fv.price_refresh.is_fresh',side_effect=lambda stamp:is_fresh(stamp,now=now)):
    runpy.run_module('crude_tanker_fv.pipeline',run_name='__main__')
