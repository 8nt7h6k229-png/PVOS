# GitHub Portfolio Asset Inventory

Inventory ID: PM-001

Inventory date: 2026-08-03

Scope: `8nt7h6k229-png/PVOS`, `8nt7h6k229-png/PvLayoutPlugin`

Authority: GitHub repository state and reachable Git history

Work item: [PVOS issue #2](https://github.com/8nt7h6k229-png/PVOS/issues/2)

## Inventory rules

- This is a recovery index, not a design document.
- An asset is `baseline` only when present on the repository default branch.
- `branch-only` means the asset is reachable on GitHub but is not in the default branch.
- Issue and PR text is classified as intent or workflow evidence, not proof that implementation is in the default branch.
- Commit links identify immutable evidence; branch links identify the recoverable collection.

## Repository inventory

| Repository | Visibility | Default branch | Role observed in history | Evidence |
|---|---|---|---|---|
| PVOS | Public | `main` | Small standalone .NET geometry/layout baseline; portfolio index host | [repository](https://github.com/8nt7h6k229-png/PVOS), [baseline commit](https://github.com/8nt7h6k229-png/PVOS/commit/f6120eefb6eae89c220c7303a4d4d40fe7a0538a) |
| PvLayoutPlugin | Private | `main` | AutoCAD rooftop PV product, historical product documentation, PVOS platform work, AI Studio and governance | [repository](https://github.com/8nt7h6k229-png/PvLayoutPlugin), [main head](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/1d908c6e5d11e0352ad367a8647005c106b6c6ab) |

## Branch inventory

### PVOS

| Branch | Head | Classification | Evidence |
|---|---|---|---|
| `main` | `f6120ee` | baseline, tagged `v0.1.0-baseline` | [branch](https://github.com/8nt7h6k229-png/PVOS/tree/main) |
| `develop` | `f6120ee` | same head as `main` | [branch](https://github.com/8nt7h6k229-png/PVOS/tree/develop) |
| `feature/geometry-core` | `1323988` | branch-only geometry continuation: Point2D, Vector2D, BoundingBox, Line2D | [branch](https://github.com/8nt7h6k229-png/PVOS/tree/feature/geometry-core), [head](https://github.com/8nt7h6k229-png/PVOS/commit/13239884c85609faccb59dcd9d1be1a32c23fe71) |

### PvLayoutPlugin

| Branch | Head | Recovered asset collection | Evidence |
|---|---|---|---|
| `main` | `1d908c6` | baseline plugin snapshot, AI Studio, governance, AI specifications | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main) |
| `develop` | `aaa9c58` | geometry-engine integration baseline | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/develop) |
| `docs/pvos-testing-platform` | `2173d27` | testing strategy, matrix, runtime validation and quality gates | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/docs/pvos-testing-platform) |
| `feature/ai-studio-foundation` | `15f8286` | AI Studio and Roslyn symbol intelligence foundation | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/ai-studio-foundation) |
| `feature/construction-intelligence` | `0106f22` | product documentation through construction foundation V5.1c | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/construction-intelligence) |
| `feature/plugin-v07-geometry-integration` | `fd99ad9` | PVOS Software Architecture Specification v1.0 | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/plugin-v07-geometry-integration), [PR #6](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/6) |
| `feature/pvos-geometry-phase2` | `af682cc` | computational geometry phase 2 | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/pvos-geometry-phase2), [PR #8](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/8) |
| `feature/pvos-platform-bootstrap` | `e8ef6ea` | PVOS platform, ADRs, datasets, validation and release governance | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/pvos-platform-bootstrap), [tag](https://github.com/8nt7h6k229-png/PvLayoutPlugin/releases/tag/v0.1.0-platform-bootstrap) |
| `feature/roof-setback-local-axis` | `0106f22` | long-lived product lineage through V5.1c | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/roof-setback-local-axis), [PR #1](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/1) |
| `feature/unit-normalize` | `aaa9c58` | unit-normalization work target; head currently equals `develop` | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/unit-normalize), [issue #10](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/10) |
| `feature/v5.1d-ladder-planning` | `0d72746` | ladder planning documentation and ADR-0019 | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.1d-ladder-planning) |
| `feature/v5.1e-cable-tray-planning` | `6b130f3` | cable tray planning, runtime inspector ADRs | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.1e-cable-tray-planning) |
| `feature/v5.2-runtime-dashboard` | `d1a209b` | runtime dashboard | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.2-runtime-dashboard) |
| `feature/v5.3-placement-v2-foundation` | `2298448` | placement engine V2 foundation | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-foundation) |
| `feature/v5.3-placement-v2-analyzer` | `9dc296b` | V1 adapter and V2 analyzer | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer) |
| `recovery/ri-002-reference-preservation` | `2b03c23` | unmerged original Repository Intelligence sequence | [branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/recovery/ri-002-reference-preservation), [issue #15](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/15) |

No listed branch was protected when queried on 2026-08-03.

## Issue inventory

| Repository | Issue | State | Classification |
|---|---|---|---|
| PVOS | [#1 Geometry Core](https://github.com/8nt7h6k229-png/PVOS/issues/1) | Open | Geometry product work |
| PVOS | [#2 PM-001 GitHub Portfolio Asset Inventory](https://github.com/8nt7h6k229-png/PVOS/issues/2) | Open | Portfolio governance / this recovery |
| PvLayoutPlugin | [#10 Normalize imported geometry to millimeters](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/10) | Open | Geometry / DXF-DWG input units |
| PvLayoutPlugin | [#11 Method Intelligence MVP](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/11) | Open | AI Studio / Repository Intelligence |
| PvLayoutPlugin | [#12 Method Intelligence MVP](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/12) | Closed | Repository Intelligence recovery |
| PvLayoutPlugin | [#13 Call Graph MVP](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/13) | Closed | Repository Intelligence recovery |
| PvLayoutPlugin | [#14 Call Graph Analysis MVP](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/14) | Closed | Repository Intelligence recovery |
| PvLayoutPlugin | [#15 Reconcile missing Repository Intelligence sprints](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/15) | Closed | Recovery program umbrella |
| PvLayoutPlugin | [#16 Development workflow governance audit](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/16) | Open | Governance; unresolved controls and open-PR disposition |
| PvLayoutPlugin | [#23 AI System Prompt Specification](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/23) | Open | AI knowledge; implementation merged in PR #25 but issue remains open |

## Pull request inventory

PVOS had no pull requests before PM-001.

| PR | State | Head → base | Asset evidence |
|---|---|---|---|
| [PvLayoutPlugin #1](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/1) | Open | `feature/roof-setback-local-axis` → `main` | roof setback/local-axis and historical product lineage |
| [#2](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/2) | Merged | geometry foundation → `main` | PVOS geometry foundation |
| [#3](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/3) | Merged | AutoCAD adapter → `main` | AutoCAD geometry adapter |
| [#4](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/4) | Merged | domain model → `main` | PVOS domain model |
| [#5](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/5) | Merged | geometry engine → `main` | geometry engine foundation |
| [#6](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/6) | Open | architecture specification → `main` | architecture document set |
| [#7](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/7) | Open | testing docs → architecture branch | testing platform; non-main base |
| [#8](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/8) | Open draft | geometry phase 2 → `main` | computational geometry |
| [#9](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/9) | Merged | AI Studio foundation → `main` | AI Studio foundation and symbol intelligence |
| [#17](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/17) | Merged | recovery RI-003 → `main` | method intelligence |
| [#18](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/18) | Merged | recovery RI-004 → `main` | reference intelligence |
| [#19](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/19) | Merged | recovery RI-005 → `main` | call graph |
| [#20](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/20) | Merged | recovery RI-006 → `main` | call graph analysis |
| [#21](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/21) | Merged | recovery RI-007 → `main` | repository impact analysis |
| [#22](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/22) | Merged | AI benchmark → `main` | AI benchmark specification |
| [#24](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/24) | Closed | system prompt → `main` | superseded PR |
| [#25](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/25) | Merged | system prompt → `main` | AI system prompt specification |

## Document collections

The branch union contains 261 tracked `.md`/`.txt` paths in PvLayoutPlugin and one `README.md` in PVOS. The complete recoverable document namespace is classified below; each link is a GitHub tree that exposes every member without copying or redesigning it.

| Collection | Status | Contents | Evidence |
|---|---|---|---|
| PvLayoutPlugin baseline docs | baseline | README, changelogs, geometry/adapter READMEs | [main](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main) |
| Governance | baseline | `PM/DEVELOPMENT_GOVERNANCE.md`, decisions, daily log, next action, EOD template, incident report, Issue/PR templates | [PM](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main/PM), [.github](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main/.github) |
| AI Studio | baseline plus branch history | README, installation, AGENTS, project memory, task packet; Repository Intelligence generated outputs and implementation history | [AIStudio](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main/AIStudio), [PRs #9, #17–#21](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pulls?q=is%3Apr+is%3Amerged+AIStudio) |
| AI specifications | baseline | benchmark and system prompt specifications | [docs/ai](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main/docs/ai) |
| Historical product specifications | branch-only | versioned `docs/PV_*.md` family covering layout, constraints, roof, walkway, electrical, construction, runtime and placement | [V5.3 analyzer tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer/docs) |
| Historical architecture/ADR set | branch-only | architecture registry, bibles, roadmap, diagrams, ADR-0001 through ADR-0023 | [architecture tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer/docs/architecture) |
| Engineering knowledge base | branch-only | rule book, standards, validation framework, sample rules, coverage and roadmaps | [engineering tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer/docs/engineering) |
| PVOS architecture specification | branch-only | layer architecture, modules, dependencies, repository architecture, quality and release governance | [architecture branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/plugin-v07-geometry-integration/docs/architecture) |
| Testing platform | branch-only | strategy, classification, matrix, CI guide, runtime validation, quality gates | [testing branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/docs/pvos-testing-platform/docs/testing) |
| PVOS platform bootstrap | branch-only, tagged | 13 ADRs, 10 geometry datasets, developer/repository/release docs, Golden Core/Dataset, validation pipeline and closeout report | [platform tree](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/pvos-platform-bootstrap), [release tag](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/v0.1.0-platform-bootstrap) |
| PVOS standalone | baseline plus branch-only source evidence | README and geometry/layout implementation/tests | [main](https://github.com/8nt7h6k229-png/PVOS/tree/main), [geometry branch](https://github.com/8nt7h6k229-png/PVOS/tree/feature/geometry-core) |

## Release and history anchors

- PvLayoutPlugin has 18 named tags, from `v0.4a-r5d-buildable` through `v0.1.0-platform-bootstrap`; [tags](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tags).
- Product-history anchors include [v0.5b obstacle avoidance](https://github.com/8nt7h6k229-png/PvLayoutPlugin/releases/tag/v0.5b-obstacle-avoidance), [v0.6a multi-roof-zone](https://github.com/8nt7h6k229-png/PvLayoutPlugin/releases/tag/v0.6a-multi-roof-zone), [V1.0a string-break layout](https://github.com/8nt7h6k229-png/PvLayoutPlugin/releases/tag/V1.0a-String-Break-Layout-Engine), [v4.1c architecture stable](https://github.com/8nt7h6k229-png/PvLayoutPlugin/releases/tag/v4.1c-architecture-stable), and [v5.1c construction foundation](https://github.com/8nt7h6k229-png/PvLayoutPlugin/releases/tag/v5.1c-construction-foundation).
- The authoritative commit sequence is the repository commit graph; branch-only evidence must not be presented as merged baseline.

## Category coverage

| Required category | Primary index/evidence |
|---|---|
| Repository, Branch, Issues, Pull Requests, Documents | this document |
| Architecture | [ARCHITECTURE_INDEX.md](ARCHITECTURE_INDEX.md) |
| Product Knowledge | [PRODUCT_KNOWLEDGE_INDEX.md](PRODUCT_KNOWLEDGE_INDEX.md) |
| AI Studio / Repository Intelligence | product index and PRs #9, #17–#21 |
| Governance / Recovery Program | this document, issue #16, issue #15, governance and incident documents |
| Gaps | [GAP_ANALYSIS.md](GAP_ANALYSIS.md) |
