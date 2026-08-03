# Architecture Index

This is an evidence index of architecture already present in GitHub history. It introduces no new architecture and does not declare branch-only material approved.

## Architecture families

| Family | Existing artifacts | Repository status | Evidence |
|---|---|---|---|
| PVOS standalone layering | `PVOS.Core`, `PVOS.Layout`, `PVOS.Cli`, `PVOS.Tests` | PVOS `main` baseline | [solution](https://github.com/8nt7h6k229-png/PVOS/tree/main), [baseline commit](https://github.com/8nt7h6k229-png/PVOS/commit/f6120eefb6eae89c220c7303a4d4d40fe7a0538a) |
| Plugin + PVOS geometry adapter | `PVOS.Geometry`, `PVOS.AutoCAD.Adapter`, plugin integration | PvLayoutPlugin `main` baseline through PRs #2–#5 | [PR #2](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/2), [#3](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/3), [#4](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/4), [#5](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/5) |
| PVOS Software Architecture Specification v1.0 | layer architecture, module definitions, dependency rules, repository architecture, quality gates, release governance | Branch-only; PR #6 open | [PR #6](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/6), [document tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/plugin-v07-geometry-integration/docs/architecture) |
| Testing platform | testing strategy, classification, execution matrix, CI guide, runtime validation | Branch-only; PR #7 open with non-main base | [PR #7](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/7) |
| Computational geometry phase 2 | computational geometry foundation and phase document | Branch-only; PR #8 open draft | [PR #8](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/8) |
| Historical product architecture | Architecture Registry, two Architecture Bible variants, diagrams, vision, roadmap, ADR-0001–ADR-0023 | Branch-only across long-lived V5 branches | [architecture tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer/docs/architecture) |
| Engineering rule architecture | PEP constitution, standards, rule book, validation framework, coverage and engineering ADR | Branch-only | [engineering tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer/docs/engineering) |
| PVOS platform bootstrap | layered/constraint-driven layout, application workflow, solver, verification, validation, repository and release governance; ADR-0001–ADR-0013 | Branch-only, tagged `v0.1.0-platform-bootstrap` | [tag tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/v0.1.0-platform-bootstrap), [ADRs](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/pvos-platform-bootstrap/docs/adr) |
| AI Studio | local project memory, task packet, Roslyn workspace/semantic providers and deterministic Markdown outputs | `main` baseline | [AIStudio](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main/AIStudio), [PR #9](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/9) |
| Repository Intelligence | semantic method/reference indexes, call graph, graph analysis, impact analysis; recovered as incremental layers | `main` baseline | [PRs #17–#21](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pulls?q=is%3Apr+is%3Amerged+RI-) |
| Development governance | Issue → branch → implementation → commit → push → PR → PM review → merge → close; evidence and closing gates | `main` baseline | [governance](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/PM/DEVELOPMENT_GOVERNANCE.md), [incident](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/PM/INCIDENT_2026-07-31_GOVERNANCE_GAP.md) |

## Historical ADR register

The following existing decisions are recoverable from the V5 branch lineage; their presence here does not merge or re-approve them:

| Range | Subjects | Evidence |
|---|---|---|
| ADR-0001–0005 | Golden Core, read-only engineering, rule engine, EngineContext, electrical pipeline | [ADR tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/construction-intelligence/docs/architecture/adr) |
| ADR-0006–0009 | electrical string boundary, rule-source distinction, product direction, runtime-state SSoT | [ADR tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/construction-intelligence/docs/architecture/adr) |
| ADR-0010–0015 | construction layer, runtime auto-execution, acceptance, roof-zone normalization, zone graph, workflow | [ADR tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/construction-intelligence/docs/architecture/adr) |
| ADR-0016–0018 | walkway planning/routing and maintenance route | [ADR tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/construction-intelligence/docs/architecture/adr) |
| ADR-0019 | ladder planning | [ladder branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.1d-ladder-planning/docs/architecture/adr) |
| ADR-0020–0021 | cable tray planning and runtime pipeline inspector | [cable-tray branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.1e-cable-tray-planning/docs/architecture/adr) |
| ADR-0022 | runtime dashboard | [dashboard branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.2-runtime-dashboard/docs/architecture/adr) |
| ADR-0023 | placement engine V2 strategy | [placement branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer/docs/architecture/adr) |

The separate PVOS platform-bootstrap lineage contains another ADR-0001–ADR-0013 namespace. It covers solver freeze, layered architecture, validation and dependency boundaries, application workflow, constraint-driven layout, catalog/placement/solver contracts, deterministic pipeline, obstacle/walkway constraints and engineering layout MVP. Evidence: [platform ADR index](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/feature/pvos-platform-bootstrap/docs/adr/ADR-INDEX.md).

## Architecture conflicts requiring review, not redesign

- Two independent ADR number spaces exist on separate branches.
- Two `PV_Architecture_Bible` variants coexist on historical branches.
- PVOS standalone and PvLayoutPlugin-contained PVOS projects overlap in geometry/layout responsibility.
- PR #7 targets PR #6's feature branch instead of `main`, creating a dependency chain.
- The most extensive architecture registry and product ADRs are not present on `main`.

These facts are indexed as gaps in [GAP_ANALYSIS.md](GAP_ANALYSIS.md); no resolution is proposed by PM-001.
