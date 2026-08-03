# PVOS 1.0 MVP Definition

## MVP statement

The PVOS 1.0 MVP is the smallest existing, evidenced workflow that accepts an explicit 2D partition, a local axis, and a module specification, then produces deterministic rectangular module placements fully contained by that partition.

The MVP is defined from PVOS `main`; it does not absorb branch-only product history.

## MVP user outcome

Given:

- a caller-supplied polygonal partition;
- an explicit local-axis origin and rotation;
- module width, height, X/Y gaps, edge margin and module power;

the existing core returns:

- panel polygons transformed back to global coordinates;
- panel count;
- installed kWp derived from count and module power; and
- a warning when no panels fit.

Evidence: [`Domain.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/Domain.cs), [`LayoutEngine.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Layout/LayoutEngine.cs).

## Included MVP capabilities

| Capability | Acceptance boundary | Evidence |
|---|---|---|
| Polygon partition input | Explicit polygon supplied by caller; no roof detection claim | [PVOS Core](https://github.com/8nt7h6k229-png/PVOS/tree/main/src/PVOS.Core) |
| Partition-specific Local Axis | Explicit origin and rotation; local/global transforms | [`AxisTransform.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/AxisTransform.cs) |
| Module specification | Positive dimensions; non-negative gaps and margin; module power retained | [`Domain.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/Domain.cs), [`LayoutEngine.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Layout/LayoutEngine.cs) |
| Rectangular grid generation | Axis-aligned grid in local coordinates | [`LayoutEngine.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Layout/LayoutEngine.cs) |
| Boundary containment | Only rectangles fully inside the partition are returned | [geometry implementation](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/Geometry2D.cs), [test](https://github.com/8nt7h6k229-png/PVOS/blob/main/tests/PVOS.Tests/LayoutEngineTests.cs) |
| Deterministic output | Nested X/Y grid order and sequential panel IDs | [`LayoutEngine.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Layout/LayoutEngine.cs) |
| Result summary | Panel count, installed kWp and no-fit warning | [`Domain.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/Domain.cs) |
| Runnable/testable delivery | .NET 8 solution, CLI example and xUnit tests | [PVOS README](https://github.com/8nt7h6k229-png/PVOS/blob/main/README.md), baseline [`f6120ee`](https://github.com/8nt7h6k229-png/PVOS/commit/f6120eefb6eae89c220c7303a4d4d40fe7a0538a) |

## Supporting existing assets, not MVP integration claims

- PvLayoutPlugin `main` is an existing AutoCAD product host: [repository](https://github.com/8nt7h6k229-png/PvLayoutPlugin).
- `PVOS.Geometry` and `PVOS.AutoCAD.Adapter` are existing merged foundations: [PR #2](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/2), [PR #3](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/3).
- No merged evidence establishes that the standalone PVOS MVP execution path is integrated into the AutoCAD host. AutoCAD integration is therefore not an MVP completion assumption.

## MVP exclusions

- Automatic roof detection.
- Multi-roof/roof-region relationships.
- DXF import or DXF export.
- DWG unit normalization.
- Obstacles, shading, walkways and setback rule evaluation beyond the explicit edge margin in the current core.
- Stringing, MPPT, inverter, voltage or other electrical calculations.
- Rule Engine, constraint optimization and placement V2.
- Construction planning, ladders, cable trays and maintenance routing.
- General polygon Boolean operations, general offsets, curves, bulges and 3D geometry.
- Golden Dataset, benchmark, production validation and release certification.
- AI-generated PV design decisions.
- Cloud, Web, Steel and other future product families.

Each exclusion is either absent from current evidence, open/planned, or branch-only as documented in [PM-001 PR #3](https://github.com/8nt7h6k229-png/PVOS/pull/3) and [PM-002 PR #5](https://github.com/8nt7h6k229-png/PVOS/pull/5).

## MVP done

The MVP definition is complete when PM approves this document. The MVP product itself is accepted only when the existing baseline commit and its build/test evidence are reviewed under the governed release workflow. PM-003 performs no implementation or release certification.
