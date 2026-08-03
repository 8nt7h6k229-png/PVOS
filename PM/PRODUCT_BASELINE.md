# PVOS 1.0 Product Baseline

Work item: [PM-003 / PVOS issue #6](https://github.com/8nt7h6k229-png/PVOS/issues/6)

Baseline date: 2026-08-03

Status: Proposed product-definition baseline; approval requires PM review of [Draft PR](https://github.com/8nt7h6k229-png/PVOS/pulls)

## Evidence precedence

1. Default-branch files and merged PRs establish **Existing capability**.
2. Open Issues and open PRs establish **Planned capability** only.
3. Branch-only documents and implementations establish **Future/recovery candidates**, not PVOS 1.0 commitments.
4. PM-001 [Draft PR #3](https://github.com/8nt7h6k229-png/PVOS/pull/3) and PM-002 [Draft PR #5](https://github.com/8nt7h6k229-png/PVOS/pull/5) are evidence inputs, not yet-approved baseline content.

## Product vision

PVOS 1.0 is an evidence-driven photovoltaic layout product baseline: it represents a deterministic, reviewable 2D PV module placement core that uses an explicit roof/partition boundary, a partition-specific local axis, and explicit module spacing parameters. It is supported by an existing AutoCAD plugin and geometry-adapter repository, but this baseline does not claim that the two repositories form one proven integrated release.

Evidence:

- PVOS describes itself as an independent .NET 8 PV layout core: [PVOS README](https://github.com/8nt7h6k229-png/PVOS/blob/main/README.md).
- PvLayoutPlugin describes itself as an AutoCAD Rooftop PV Layout Plugin: [PvLayoutPlugin README](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/README.md).
- The existing adapter explicitly separates AutoCAD types from platform-neutral geometry: [adapter README](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/src/r5d_src/PVOS.AutoCAD.Adapter/README.md), merged by [PR #3](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/3).

## Official baseline

The official PVOS 1.0 baseline is the following bounded capability set.

| Baseline element | Included evidence | Capability status |
|---|---|---|
| 2D domain primitives | Point, polygon, rectangle, local axis, partition, module specification, panel, request and result types | Existing in [PVOS `main`](https://github.com/8nt7h6k229-png/PVOS/tree/main/src/PVOS.Core) |
| Local-axis transformation | Transform partition geometry to/from a partition-specific local coordinate system | Existing in [`AxisTransform.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/AxisTransform.cs) and covered by [layout tests](https://github.com/8nt7h6k229-png/PVOS/blob/main/tests/PVOS.Tests/LayoutEngineTests.cs) |
| Deterministic rectangular module placement | Grid candidates derived from module dimensions, gaps and edge margin; candidates retained only when fully inside the partition | Existing in [`LayoutEngine.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Layout/LayoutEngine.cs) |
| Layout results | Ordered panel collection, panel count, installed kWp calculation and no-fit warning | Existing in [`Domain.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/Domain.cs) |
| Runnable and testable core | CLI example plus xUnit geometry and layout tests | Existing in [PVOS solution](https://github.com/8nt7h6k229-png/PVOS/tree/main) at baseline commit [`f6120ee`](https://github.com/8nt7h6k229-png/PVOS/commit/f6120eefb6eae89c220c7303a4d4d40fe7a0538a) |
| Platform-neutral geometry library | Deterministic 2D geometry with documented tolerance and immutable values | Existing in [PvLayoutPlugin `main`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main/src/r5d_src/PVOS.Geometry), merged through [PR #2](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/2) |
| AutoCAD conversion boundary | Deterministic conversion for supported detached AutoCAD geometry; no transaction/database ownership | Existing in [adapter README](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/src/r5d_src/PVOS.AutoCAD.Adapter/README.md), merged through [PR #3](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/3) |
| Domain and geometry-engine foundations | PVOS domain model and geometry engine foundations | Existing via merged [PR #4](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/4) and [PR #5](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/5) |
| Existing AutoCAD product host | Existing PvLayoutPlugin snapshot and stable import | Existing in [PvLayoutPlugin `main`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main/src/r5d_src) |
| Delivery governance | GitHub source of truth, Issue/branch/PR/PM review and completion gates | Existing in [development governance](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/PM/DEVELOPMENT_GOVERNANCE.md) |

## Baseline limitations

- The repositories contain overlapping PVOS geometry/layout responsibilities; PM-001 records that ownership is not yet resolved: [PR #3 gap analysis](https://github.com/8nt7h6k229-png/PVOS/blob/agent/pm-001-github-portfolio-asset-inventory/PM/GAP_ANALYSIS.md).
- No merged evidence proves that standalone PVOS `main` is wired into the AutoCAD product host. The two lanes are therefore included as existing assets, not asserted as one integrated binary.
- The baseline is a product definition, not a release certification. It does not replace build, test, runtime, PM, Product Owner, merge, and Issue-closure evidence.

## Planned capability

Planned means authorized or reviewable work exists in an open Issue or PR; it is not part of the baseline.

| Planned item | Evidence | Exclusion reason |
|---|---|---|
| Complete standalone Geometry Core | [PVOS issue #1](https://github.com/8nt7h6k229-png/PVOS/issues/1), [`feature/geometry-core`](https://github.com/8nt7h6k229-png/PVOS/tree/feature/geometry-core) | Issue open; branch unmerged |
| DWG unit normalization | [PvLayoutPlugin issue #10](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/10) | Issue open; target branch has no unique commit |
| PVOS Software Architecture Specification v1.0 | [PR #6](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/6) | PR open |
| Testing Platform Foundation | [PR #7](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/7) | PR open and stacked on PR #6 |
| Computational Geometry Phase 2 | [PR #8](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/8) | Draft PR open |
| Roof/Local Axis historical product branch disposition | [PR #1](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/1), [PM-002 PR #5](https://github.com/8nt7h6k229-png/PVOS/pull/5) | Open PR and branch-only knowledge |

## Future capability

Future items are evidenced proposals or branch-only historical capabilities. They are not PVOS 1.0 commitments.

- Advanced Roof Region relationships, Rule Engine, optimization, electrical, construction, runtime dashboard and Placement V2: [V5.3 branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer), classified by [PM-002 PR #5](https://github.com/8nt7h6k229-png/PVOS/pull/5).
- Solver platform, Golden Dataset, verification and validation pipelines: [`feature/pvos-platform-bootstrap`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/pvos-platform-bootstrap).
- Steel, broader Electrical, AI product functionality, Cloud, Web and standalone product hosts appear as future product families only in the open architecture [PR #6](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/6).

## Product milestones

| Milestone | Definition | Current evidence state |
|---|---|---|
| M0 — Asset recovery | Portfolio, branch knowledge and gaps indexed | PM-001 [PR #3](https://github.com/8nt7h6k229-png/PVOS/pull/3) and PM-002 [PR #5](https://github.com/8nt7h6k229-png/PVOS/pull/5) awaiting PM review |
| M1 — Product definition | Baseline, scope, MVP and capability states approved | PM-003 / this document awaiting PM review |
| M2 — MVP baseline | Existing bounded capability set accepted with repository/commit/test evidence | Baseline code exists; product approval evidence not yet recorded |
| M3 — Planned-item disposition | Open Issues/PRs #1, #6, #7, #8 and unit-normalization Issue #10 reviewed | Not complete; items remain open |
| M4 — Product Complete | All inclusion criteria below are met; excluded/future items remain explicitly excluded | Not complete |

## Product Complete definition

PVOS 1.0 is **Product Complete** only when:

1. PM approves the baseline, MVP, scope, and capability matrix through the governed PR.
2. Every capability marked Included has an identified repository, commit, document, and validation owner.
3. The cross-repository ownership/integration boundary is explicitly resolved or the two-lane packaging is formally accepted.
4. Required build, test, runtime, deterministic and release evidence is recorded under existing governance.
5. Every planned item is either accepted into a versioned baseline or explicitly deferred; no open branch is silently treated as shipped.
6. Out-of-scope and future capabilities remain excluded from PVOS 1.0 release claims.
7. The release PR is approved and merged and its Issue is closed under [development governance](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/PM/DEVELOPMENT_GOVERNANCE.md).

Product Complete is a governance state, not a claim that all recovered historical capabilities are implemented or included.
