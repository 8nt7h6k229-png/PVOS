# PVOS 1.2 Integration Roadmap Review

## Control

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #87 — PVOS-505 |
| Dependency | PVOS-504 / commit `91c60e365341ce7002cbde1b2b5131cb08c7b4cb` |
| Mode | Review only; non-binding |
| Status | READY_FOR_PM_REVIEW |

## Purpose

Record possible future integration questions, dependencies and evidence prerequisites without creating Product Scope, delivery dates, implementation commitments or acceptance claims.

## Candidate Sequence

```text
Current bounded PVOS Product contracts
        ↓ evidence and ownership review
Adapter / domain contract proposals
        ↓ separate Product baseline authority
Validation prototypes
        ↓ separate PM acceptance
Future implementation consideration
```

Every arrow is conditional. This Review does not approve any downstream step.

## AutoCAD Adapter Roadmap Review

| Concern | Review Finding / Future Evidence Need |
|---|---|
| Responsibility | Translate source-specific geometry into separately approved PVOS inputs; must not own placement |
| Contract | Requires explicit units, coordinate system, geometry/partition identity and error mapping |
| Isolation | Product Core must not depend on AutoCAD APIs |
| Validation | Requires licensed host environment, representative drawings, adapter contract tests and failure evidence |
| Open questions | Supported AutoCAD versions, document lifecycle, transaction boundary and geometry provenance |
| Non-claim | No adapter, host integration or delivery commitment exists here |

## Electrical Roadmap Review

| Concern | Review Finding / Future Evidence Need |
|---|---|
| Responsibility | A future independent Product/domain would consume accepted PVOS layout results |
| Inputs | Panel identity, geometry and rated power may be candidates; ownership is not approved |
| Contract | Requires independent electrical rules, units, errors, acceptance and regulatory authority |
| Open questions | Stringing ownership, inverter/catalog authority, jurisdiction and result compatibility |
| Non-claim | PVOS does not perform electrical design, calculation or validation |

## Shading Roadmap Review

| Concern | Review Finding / Future Evidence Need |
|---|---|
| Responsibility | A future independent analysis domain may consume geometry/results without changing deterministic placement truth |
| Inputs | Solar position, obstruction geometry, time/weather basis and coordinate semantics require authority |
| Result ownership | Shading outputs must remain distinct from PVOS placement and capacity values |
| Open questions | Model accuracy, datasets, tolerances, scenario provenance and validation reference |
| Non-claim | No shading engine, optimization or automatic design is included |

## Cross-Roadmap Entry Gates

- separately approved Product problem and owner;
- one versioned contract with compatibility policy;
- bounded changed-file scope and dependency map;
- representative evidence with explicit provenance;
- failure and BLOCKED semantics;
- no dependency from C# Product Core onto source-specific hosts; and
- separate PM planning, execution and acceptance authority.

## Non-Commitment Boundary

This Roadmap does not create an Implementation Issue, delivery schedule, release allocation, Product Scope change, Product Blueprint change or Product Acceptance claim. AutoCAD, Electrical and Shading remain outside PVOS 1.2 implementation scope.

## Scope Verification

| Check | Result |
|---|---|
| Full AutoCAD integration started | No |
| Electrical or Shading implementation started | No |
| UI, Cloud, Construction, AI Design or PVOS 2.x introduced | No |
| Canonical or Legacy asset promoted | No |
| PVOS 1.1, EOS or Governance status modified | No |

READY_FOR_PM_REVIEW — INTEGRATION ROADMAP REVIEW ONLY
