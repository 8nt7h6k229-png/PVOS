# PVOS 1.0 Product Scope

## In scope

PVOS 1.0 product scope is limited to existing, deterministic 2D PV layout foundations.

| Scope area | Included boundary | Status | Evidence |
|---|---|---|---|
| Product purpose | Produce reviewable 2D PV module placements from explicit geometry and parameters | Existing | [PVOS README](https://github.com/8nt7h6k229-png/PVOS/blob/main/README.md) |
| Geometry input | Caller-provided 2D polygon/partition; millimetre-based geometry in PvLayoutPlugin Geometry | Existing | [PVOS Core](https://github.com/8nt7h6k229-png/PVOS/tree/main/src/PVOS.Core), [Geometry README](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/src/r5d_src/PVOS.Geometry/README.md) |
| Coordinate system | Explicit partition-specific Local Axis | Existing | [`Domain.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/Domain.cs), [`AxisTransform.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/AxisTransform.cs) |
| Placement | Deterministic rectangular grid with dimensions, gaps and edge margin | Existing | [`LayoutEngine.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Layout/LayoutEngine.cs) |
| Output | Panel geometry, count, installed kWp and warning | Existing | [`Domain.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/Domain.cs) |
| Execution surfaces | Core library and CLI; existing AutoCAD host and adapter are recognized assets | Existing, but cross-repository integration unverified | [PVOS solution](https://github.com/8nt7h6k229-png/PVOS/tree/main), [PvLayoutPlugin](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main) |
| Quality boundary | Existing unit tests plus governed evidence/review workflow | Existing | [PVOS tests](https://github.com/8nt7h6k229-png/PVOS/tree/main/tests), [governance](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/PM/DEVELOPMENT_GOVERNANCE.md) |

## Planned but not included

| Item | Evidence | State |
|---|---|---|
| Additional geometry primitives/algorithms | [PVOS issue #1](https://github.com/8nt7h6k229-png/PVOS/issues/1), [`feature/geometry-core`](https://github.com/8nt7h6k229-png/PVOS/tree/feature/geometry-core) | Planned / unmerged |
| DWG unit normalization | [PvLayoutPlugin issue #10](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/10) | Planned / no unique branch commit |
| Architecture specification | [PR #6](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/6) | Planned / open PR |
| Testing platform | [PR #7](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/7) | Planned / open stacked PR |
| Computational Geometry Phase 2 | [PR #8](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/8) | Planned / open draft PR |

## Out of scope for PVOS 1.0

| Excluded area | Evidence-based reason |
|---|---|
| Roof Detection | PM-002 found no explicit commit, Issue, PR or document establishing it: [PR #5](https://github.com/8nt7h6k229-png/PVOS/pull/5) |
| Advanced Roof Region/Zone workflow | First implementation and later normalization remain on the V5 branch lineage: [`bd3ba2f`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/bd3ba2f61b7bd7ea0b81f2565d68908c353c1918), [V5.3 branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer) |
| DXF Import and DXF Export | No explicit verified assets found by PM-001/PM-002: [PR #3](https://github.com/8nt7h6k229-png/PVOS/pull/3), [PR #5](https://github.com/8nt7h6k229-png/PVOS/pull/5) |
| Rule Engine and optimization | Branch-only commits/documents: [`ca0bdee`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/ca0bdee227a47cfd5780a39dec7f150d83b6ba53), [`1352ed5`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/1352ed5d317f2c01b7df9a61fb64657fb26675b3) |
| Electrical and construction engines | Branch-only product history: [V5.3 branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer) |
| Runtime dashboard and Placement V2 | Branch-only successor commits: [`d1a209b`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/d1a209bcb9013135ed39538a46739733e4c19b8b), [`9dc296b`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/9dc296bd20e94a21acbabb805c4b0342d474866d) |
| Golden Dataset and platform validation | Branch-only platform bootstrap: [`e8ef6ea`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/e8ef6ea1899336a00ffeb2ede2d3b28ff8a2f59a) |
| Steel, AI product decisions, Cloud and Web products | Only future families in open architecture [PR #6](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/6) |
| General geometry engine | Existing Geometry README explicitly excludes offset, clipping, Boolean operations, triangulation and spatial indexing from v0.1: [document](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/src/r5d_src/PVOS.Geometry/README.md) |

## Scope-change rule

Nothing moves from Planned or Future into the PVOS 1.0 baseline by reference alone. Inclusion requires a separate governed Issue, accepted implementation/recovery evidence, validation, PR approval, merge, and baseline-version update. PM-003 does not authorize those actions.
