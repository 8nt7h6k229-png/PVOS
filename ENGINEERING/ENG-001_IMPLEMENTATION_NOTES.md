# ENG-001 Implementation Notes

Work item: [ENG-001 / PVOS Issue #27](https://github.com/8nt7h6k229-png/PVOS/issues/27)

Primary Capability: `LAY-002`

## Implemented contract

ENG-001 implements the approved MVP flow in the existing .NET 8 solution:

1. validate one explicit roof and its user-supplied partition collection;
2. resolve exactly one selected partition without fallback;
3. validate one explicit partition-specific Local Axis;
4. validate one active module definition and derive effective dimensions and pitches;
5. generate candidates by ascending local Y row and ascending local X column;
6. accept only complete rectangles contained by or touching the selected boundary;
7. transform accepted four-corner rectangles to global coordinates;
8. assign deterministic accepted-order identifiers;
9. return panel geometry, count, nameplate kWp, warnings, status, and stable errors.

The implementation follows:

- [`PE-GEO-001_SPEC.md`](PE-GEO-001_SPEC.md)
- [`PE-GEO-002_SPEC.md`](PE-GEO-002_SPEC.md)
- [`PE-AXS-001_SPEC.md`](PE-AXS-001_SPEC.md)
- [`PE-LAY-001_SPEC.md`](PE-LAY-001_SPEC.md)
- [`PE-LAY-002_SPEC.md`](PE-LAY-002_SPEC.md)

## Existing project ownership

| Existing project | ENG-001 responsibility |
|---|---|
| `PVOS.Core` | immutable request/result records, geometry primitives, Local Axis transform, complete-containment behavior |
| `PVOS.Layout` | validation pipeline and deterministic placement workflow |
| `PVOS.Cli` | hard-coded Demo-001 input and human-readable result output |
| `PVOS.Tests` | behavior-level unit tests for geometry, validation, placement, results, warnings, and repeatability |

No new project, adapter, service, storage layer, framework, or architecture was introduced.

## Determinism controls

- submitted collection order is retained;
- candidate order is row-major in the Local Axis coordinate system;
- every candidate receives one containment decision;
- rejected candidates consume no panel identifier;
- panel IDs are contiguous `PNL-000001` style accepted-order identifiers;
- corners retain lower-left, lower-right, upper-right, upper-left local order after global transformation;
- warnings use stable ordering;
- repeated Demo-001 execution is compared as complete text output;
- repeated unit-test requests compare status, geometry, ordering, count, capacity, warnings, and errors.

## Boundary and validation behavior

Full containment checks vertices, edge midpoints, and proper boundary crossings. This prevents a rectangle whose corners are inside a concave polygon from crossing an exterior notch. Boundary contact remains accepted. No clipping, correction, alternative placement, tolerance expansion, or optimization occurs.

Invalid requests return `Rejected` with stable specification codes and no partial panel result. A valid request with no fitting panel returns `Accepted`, zero panels, zero kWp, `PLC_NO_PANEL_FITS`, and `PLC_EMPTY_PLACEMENT_RESULT`.

## Demo-001 evidence

- Input: [`DEMO/DEMO-001_INPUT.md`](../DEMO/DEMO-001_INPUT.md)
- Captured output: [`DEMO/DEMO-001_OUTPUT.txt`](../DEMO/DEMO-001_OUTPUT.txt)
- Result: 10 ordered panels, 5.000 kWp, no placement warnings

## Verification

```powershell
dotnet restore .\PVOS.sln
dotnet build .\PVOS.sln --configuration Release --no-restore
dotnet test .\PVOS.sln --configuration Release --no-build
dotnet run --project .\src\PVOS.Cli\PVOS.Cli.csproj --configuration Release --no-build
```

## Excluded

ENG-001 contains no DXF, AutoCAD, JSON adapter, import/export, UI, rendering, SVG, optimization, AI, roof detection, rule engine, electrical design, structural design, or multi-partition placement. It does not change the Product Baseline.
