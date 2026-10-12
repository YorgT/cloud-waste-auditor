# Cloud Waste Auditor

A small, evidence-first tool to help small software teams find avoidable cloud and AI infrastructure spend.

## MVP goal

Start with billing CSV uploads and a transparent rules engine. Produce a reviewable report showing suspected waste, the evidence behind each finding, confidence, and a safe next step. Do not make changes to customer infrastructure automatically.

## Initial scope

- Import normalized CSV billing exports (no cloud credentials required for the first demo).
- Group costs by service, project, and date where those columns exist.
- Flag simple anomalies and unused/idle-resource candidates only when the input data supports that conclusion.
- Show calculations and evidence; label estimates as estimates.
- Export findings to CSV/JSON.

## Open-source foundation and attribution

Research/reference project: [OpenCost](https://github.com/opencost/opencost), an Apache-2.0 cloud cost monitoring project. This repository is a separate MVP scaffold and does **not** currently contain copied OpenCost source code. If OpenCost code or assets are later incorporated, retain all required upstream copyright, license, NOTICE, and dependency attributions; review the exact files and dependencies before distribution. See [OpenCost's license and repository](https://github.com/opencost/opencost).

## Status

Early prototype scaffold. Not production-ready, and no savings are guaranteed. Never connect production accounts or apply changes based solely on an automated recommendation.

## Roadmap

1. Define a documented CSV schema and synthetic fixtures.
2. Implement deterministic findings with unit tests.
3. Add a report UI and export.
4. Validate findings against real, permissioned sample bills before adding cloud integrations.

## License

Original code in this repository is licensed under the MIT License. Third-party components retain their own licenses and notices. See `LICENSE`.