# Architecture Decision Registry

## Purpose

Register architecture decisions and their authoritative records.

## Responsibility

Maintain the unique index of architecture decision records.

## Information Domain

Decision

## Owner

PM

## Update Trigger

An architecture decision is proposed, accepted, superseded, or retired.

## Registry Schema

| Field | Meaning |
|---|---|
| Decision ID | Repository-qualified unique identifier |
| Original ID | Identifier used by the source record |
| Subject | Subject stated by the source filename |
| Status | Governed classification, not inferred approval |
| Source | Authoritative repository path and immutable source commit |
| Approved By | Recorded approval authority, or `Not evidenced` |
| Effective Date | Recorded effective date, or `Not evidenced` |
| Supersedes | Explicit supersession reference, or `None evidenced` |

## Namespace Policy

The historical V5 lineage and the platform-bootstrap lineage both use `ADR-0001` onward. This registry prevents collision by qualifying each Decision ID:

- `PVLP-V5-ADR-*` — `docs/architecture/adr` at commit `9dc296b`;
- `PVLP-PLATFORM-ADR-*` — `docs/adr` at commit `e8ef6ea`.

Qualification resolves registry identity only. It does not merge, approve, supersede, or promote either branch-only namespace. The collision remains recorded as `GAP-010` in [Gap Analysis](../PM/GAP_ANALYSIS.md).

## Decision Index

| Decision ID | Original ID | Subject | Status | Source | Approved By | Effective Date | Supersedes |
|---|---|---|---|---|---|---|---|
| PVLP-V5-ADR-0001 | ADR-0001 | Golden Core | HISTORICAL_BRANCH_ONLY | [`ADR-0001-Golden-Core.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0001-Golden-Core.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0002 | ADR-0002 | Read-only Engineering | HISTORICAL_BRANCH_ONLY | [`ADR-0002-ReadOnly-Engineering.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0002-ReadOnly-Engineering.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0003 | ADR-0003 | Rule Engine | HISTORICAL_BRANCH_ONLY | [`ADR-0003-Rule-Engine.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0003-Rule-Engine.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0004 | ADR-0004 | EngineContext | HISTORICAL_BRANCH_ONLY | [`ADR-0004-EngineContext.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0004-EngineContext.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0005 | ADR-0005 | Electrical Pipeline | HISTORICAL_BRANCH_ONLY | [`ADR-0005-Electrical-Pipeline.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0005-Electrical-Pipeline.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0006 | ADR-0006 | Electrical String Boundary | HISTORICAL_BRANCH_ONLY | [`ADR-0006-Electrical-String-Boundary.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0006-Electrical-String-Boundary.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0007 | ADR-0007 | Taiwan vs Company Rule | HISTORICAL_BRANCH_ONLY | [`ADR-0007-Taiwan-vs-Company-Rule.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0007-Taiwan-vs-Company-Rule.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0008 | ADR-0008 | Product Direction | HISTORICAL_BRANCH_ONLY | [`ADR-0008-Product-Direction.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0008-Product-Direction.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0009 | ADR-0009 | Runtime State SSoT | HISTORICAL_BRANCH_ONLY | [`ADR-0009-Runtime-State-SSoT.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0009-Runtime-State-SSoT.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0010 | ADR-0010 | Construction Layer Architecture | HISTORICAL_BRANCH_ONLY | [`ADR-0010-Construction-Layer-Architecture.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0010-Construction-Layer-Architecture.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0011 | ADR-0011 | Runtime Auto Execution Bridge | HISTORICAL_BRANCH_ONLY | [`ADR-0011-Runtime-Auto-Execution-Bridge.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0011-Runtime-Auto-Execution-Bridge.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0012 | ADR-0012 | Product Acceptance | HISTORICAL_BRANCH_ONLY | [`ADR-0012-Product-Acceptance.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0012-Product-Acceptance.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0013 | ADR-0013 | Roof Zone Relationship Normalization | HISTORICAL_BRANCH_ONLY | [`ADR-0013-Roof-Zone-Relationship-Normalization.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0013-Roof-Zone-Relationship-Normalization.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0014 | ADR-0014 | Construction Zone Graph | HISTORICAL_BRANCH_ONLY | [`ADR-0014-Construction-Zone-Graph.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0014-Construction-Zone-Graph.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0015 | ADR-0015 | Construction Workflow | HISTORICAL_BRANCH_ONLY | [`ADR-0015-Construction-Workflow.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0015-Construction-Workflow.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0016 | ADR-0016 | Walkway Planning Architecture | HISTORICAL_BRANCH_ONLY | [`ADR-0016-Walkway-Planning-Architecture.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0016-Walkway-Planning-Architecture.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0017 | ADR-0017 | Walkway Routing | HISTORICAL_BRANCH_ONLY | [`ADR-0017-Walkway-Routing.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0017-Walkway-Routing.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0018 | ADR-0018 | Maintenance Route | HISTORICAL_BRANCH_ONLY | [`ADR-0018-Maintenance-Route.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0018-Maintenance-Route.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0019 | ADR-0019 | Ladder Planning | HISTORICAL_BRANCH_ONLY | [`ADR-0019-Ladder-Planning.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0019-Ladder-Planning.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0020 | ADR-0020 | Cable Tray Planning | HISTORICAL_BRANCH_ONLY | [`ADR-0020-Cable-Tray-Planning.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0020-Cable-Tray-Planning.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0021 | ADR-0021 | Runtime Pipeline Inspector | HISTORICAL_BRANCH_ONLY | [`ADR-0021-Runtime-Pipeline-Inspector.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0021-Runtime-Pipeline-Inspector.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0022 | ADR-0022 | Runtime Dashboard | HISTORICAL_BRANCH_ONLY | [`ADR-0022-Runtime-Dashboard.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0022-Runtime-Dashboard.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-V5-ADR-0023 | ADR-0023 | Panel Placement Engine V2 Strategy | HISTORICAL_BRANCH_ONLY | [`ADR-0023-Panel-Placement-Engine-V2-Strategy.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/9dc296bd20e94a21acbabb805c4b0342d474866d/docs/architecture/adr/ADR-0023-Panel-Placement-Engine-V2-Strategy.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0001 | ADR-0001 | Solver Foundation Freeze | HISTORICAL_BRANCH_ONLY | [`ADR-0001-solver-foundation-freeze.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0001-solver-foundation-freeze.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0002 | ADR-0002 | Layered Architecture | HISTORICAL_BRANCH_ONLY | [`ADR-0002-layered-architecture.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0002-layered-architecture.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0003 | ADR-0003 | Validation Boundary | HISTORICAL_BRANCH_ONLY | [`ADR-0003-validation-boundary.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0003-validation-boundary.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0004 | ADR-0004 | Dependency Direction | HISTORICAL_BRANCH_ONLY | [`ADR-0004-dependency-direction.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0004-dependency-direction.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0005 | ADR-0005 | Application Workflow Pipeline | HISTORICAL_BRANCH_ONLY | [`ADR-0005-Application-Workflow-Pipeline.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0005-Application-Workflow-Pipeline.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0006 | ADR-0006 | Constraint-Driven Layout | HISTORICAL_BRANCH_ONLY | [`ADR-0006-Constraint-Driven-Layout.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0006-Constraint-Driven-Layout.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0007 | ADR-0007 | Module Catalog Domain | HISTORICAL_BRANCH_ONLY | [`ADR-0007-Module-Catalog-Domain.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0007-Module-Catalog-Domain.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0008 | ADR-0008 | Module Placement Domain | HISTORICAL_BRANCH_ONLY | [`ADR-0008-Module-Placement-Domain.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0008-Module-Placement-Domain.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0009 | ADR-0009 | Solver Contract Domain | HISTORICAL_BRANCH_ONLY | [`ADR-0009-Solver-Contract-Domain.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0009-Solver-Contract-Domain.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0010 | ADR-0010 | Deterministic Solver Pipeline | HISTORICAL_BRANCH_ONLY | [`ADR-0010-Deterministic-Solver-Pipeline.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0010-Deterministic-Solver-Pipeline.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0011 | ADR-0011 | Obstacle Constraint Evaluation | HISTORICAL_BRANCH_ONLY | [`ADR-0011-Obstacle-Constraint-Evaluation.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0011-Obstacle-Constraint-Evaluation.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0012 | ADR-0012 | Maintenance Walkway Constraint | HISTORICAL_BRANCH_ONLY | [`ADR-0012-Maintenance-Walkway-Constraint.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0012-Maintenance-Walkway-Constraint.md) | Not evidenced | Not evidenced | None evidenced |
| PVLP-PLATFORM-ADR-0013 | ADR-0013 | Engineering Layout MVP | HISTORICAL_BRANCH_ONLY | [`ADR-0013-Engineering-Layout-MVP.md`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a/docs/adr/ADR-0013-Engineering-Layout-MVP.md) | Not evidenced | Not evidenced | None evidenced |

## Gaps Preserved

- Both namespaces remain branch-only and are not part of the PVOS `main` baseline.
- Approval authority, effective dates, and supersession links are not evidenced by the existing index and therefore remain explicitly unset.
- No current PVOS-repository ADR file exists on the inspected branch.
- Repository ownership across PVOS and PvLayoutPlugin remains `GAP-012` and requires a separate accountable decision.

## Verification Boundary

EOS-004 verifies architecture-decision **registration**, not approval of the registered historical decisions. The qualified Decision IDs, immutable source commits, explicit `HISTORICAL_BRANCH_ONLY` status, and `Not evidenced` authority fields prevent unsupported promotion while preserving provenance. The gaps above are controlled registry findings, not missing registry fields and not permission to infer approval, effective dates, supersession, ownership, or current Product architecture.

PM final verification may assess EOS-004 against this bounded registration responsibility without resolving or promoting the historical decisions themselves.

## Related Documents

- [Governance Rules Registry](GOVERNANCE_RULES_REGISTRY.md)
- [Governance Information Architecture](GOVERNANCE_INFORMATION_ARCHITECTURE.md)
- [Architecture Index](../PM/ARCHITECTURE_INDEX.md)

## Status

Formal historical decision index established — awaiting PM review.
