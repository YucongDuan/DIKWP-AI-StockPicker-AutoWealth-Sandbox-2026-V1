# DIKWP AI StockPicker AutoWealth Sandbox 2026 V1

A standalone, offline-first, compliance-oriented prototype for stock research prioritization and paper portfolio automation.

## What it is

This project demonstrates how an “AI stock picker” and “auto-wealth platform” can be rebuilt as a safe research, suitability, paper-trading, and human-review workflow:

Investor suitability → Investment Purpose Contract → Market Evidence Ledger → stock research priority list → factor explanation and rebuttal → paper portfolio → rebalancing draft → stress test → AI Use Log → advisor/compliance review ticket → Investment Research Passport.

## What it is not

It is not an investment-advice service, not a broker, not a fund seller, not a robo-advisor execution system, and not a stock-tip generator. The open-source core never recommends real securities, never connects to a broker, never stores account credentials, and never executes trades.

## Quick start

Open `index.html` in a modern browser. No server, database, model API, account, broker connection, or network is required.

Optional CLI:

```bash
python tools/run_stock_sandbox.py examples/sample_investor_profile.json --universe examples/sample_stock_universe.csv --out outputs
```

## Design lineage

The package extends the DIKWP Evidence Ledger / Action Ticket / Human Review pattern into financial research and suitability preparation.
