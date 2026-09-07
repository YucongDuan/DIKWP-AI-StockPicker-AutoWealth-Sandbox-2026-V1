#!/usr/bin/env python3
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[1]
PATTERNS=[(r'exchange_api','exchange API'),(r'place_order','order placement'),(r'api_key','API key'),(r'localStorage','browser local storage'),(r'fetch\(','network fetch'),(r'WebSocket','websocket'),(r'eval\(','dynamic eval'),(r'\bexec\(','dynamic exec')]
ALLOW={'README.md','GOVERNANCE.md','NOTICE.md','SOURCES.md','static_boundary_audit.py'}
def main():
    findings=[]
    for p in ROOT.rglob('*'):
        if not p.is_file() or p.name in ALLOW or p.suffix.lower() not in {'.html','.js','.py','.json'}:continue
        txt=p.read_text(encoding='utf-8',errors='ignore')
        for pat,meaning in PATTERNS:
            if re.search(pat,txt,re.I):findings.append({'file':str(p.relative_to(ROOT)),'pattern':pat,'meaning':meaning})
    res={'package':'DIKWP AI StockPicker AutoWealth Sandbox 2026 V1','live_trading_capability_detected':False,'findings_requiring_human_review':findings,'note':'No broker adapters, credentials storage, or order execution modules are included.'}
    out=ROOT/'static_boundary_audit_report.json';out.write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(res,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
