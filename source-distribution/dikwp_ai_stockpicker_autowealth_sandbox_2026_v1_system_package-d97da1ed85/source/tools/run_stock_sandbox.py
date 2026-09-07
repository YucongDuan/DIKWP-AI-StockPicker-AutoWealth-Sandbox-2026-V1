#!/usr/bin/env python3
"""Offline synthetic stock research sandbox. No investment advice or live trading."""
from __future__ import annotations
import argparse,csv,json
from pathlib import Path
from datetime import datetime,timezone

def load_universe(path:Path):
    with open(path,encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def score(row):
    q=float(row.get('quality',0));v=float(row.get('value',0));g=float(row.get('growth',0));m=float(row.get('momentum',0));r=float(row.get('risk',0));l=float(row.get('liquidity',0));d=float(row.get('data_quality',0));a=float(row.get('ai_exposure',0))
    return round((q+v+g+m+l+d+a*.4-r*.8)/6.4+25)
def main():
    p=argparse.ArgumentParser();p.add_argument('profile',type=Path);p.add_argument('--universe',type=Path,required=True);p.add_argument('--out',type=Path,default=Path('outputs'));args=p.parse_args()
    profile=json.loads(args.profile.read_text(encoding='utf-8'));rows=load_universe(args.universe)
    result=[]
    for row in rows:
        s=score(row);decision='research_priority' if s>=70 else 'observe_or_request_evidence' if s>=55 else 'not_research_priority'
        if profile.get('risk_level')=='R1' and float(row.get('risk',0))>55:decision='not_suitable_for_discussion'
        result.append({'id':row['id'],'name':row['name'],'sector':row['sector'],'score':s,'decision':decision,'boundary':'research priority, not buy/sell advice'})
    result=sorted(result,key=lambda x:x['score'],reverse=True)
    passport={'version':'DIKWP AI StockPicker AutoWealth Sandbox CLI','generated_at':datetime.now(timezone.utc).isoformat(),'investor':profile,'research_list':result,'boundaries':{'live_trading':False,'investment_advice':False,'real_stock_recommendation':False,'human_review_required':True}}
    args.out.mkdir(exist_ok=True,parents=True);target=args.out/'stock_research_passport.json';target.write_text(json.dumps(passport,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Output:',target);print('Boundary: research sandbox only; no real-stock recommendation or live trading.')
if __name__=='__main__':main()
