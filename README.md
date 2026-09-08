# DIKWP AI StockPicker AutoWealth Sandbox 2026 V1

Created by Yucong Duan (段玉聪).

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


<!-- DIKWP-SOURCE-VISIBILITY-START -->
## Browse source / 浏览源码

[Source index / 源码入口](SOURCE_INDEX.md) expands the retained archive distribution into browsable files, with archive hashes and per-project provenance. Runtime tests: NOT_RUN.

原始压缩包 保留；新增可浏览源码、哈希与来源记录。运行与测试尚未执行，详情见源码入口。
<!-- DIKWP-SOURCE-VISIBILITY-END -->


## Related research navigation / 相关研究导航

Research navigation, not verified software dependencies. / 研究导航，不代表已验证的软件依赖关系。

- [DIKWP-IntentEconomy-TransitionOS-2026-V1](https://github.com/YucongDuan/DIKWP-IntentEconomy-TransitionOS-2026-V1)
- [DIKWP-Intention-Economy-BridgeOS-2026-V1](https://github.com/YucongDuan/DIKWP-Intention-Economy-BridgeOS-2026-V1)
- [DIKWP-DesireBalance-OS](https://github.com/YucongDuan/DIKWP-DesireBalance-OS)
- [DIKWP-NietzscheLab-OS](https://github.com/YucongDuan/DIKWP-NietzscheLab-OS)
- [DIKWP-OmegaIntent-Cosmogenesis-OS](https://github.com/YucongDuan/DIKWP-OmegaIntent-Cosmogenesis-OS)

## Current interface presentation

[Open the interface source](source-distribution/dikwp_ai_stockpicker_autowealth_sandbox_2026_v1_system_package-d97da1ed85/source/index.html) from the current repository download. See [interface and authorship notes](INTERFACE_NOTES.md) for English coverage, report generation and validation scope.
