# Python Short-Track Engineering v0.1 — Planning Package

## Decision

Build one bounded Engineering Preview that reads governed JSON, performs deterministic per-partition placement, and emits JSON plus Markdown. Python leads discovery; C# remains formal Product behavior authority.

## Reuse assessment

| Classification | Assets | Disposition |
|---|---|---|
| DIRECTLY_REUSABLE | `VALIDATION/python` PASS/FAIL/BLOCKED and reporting concepts; existing launcher conventions | Support infrastructure and operator semantics |
| REUSABLE_WITH_ADAPTER | `AxisTransform.cs`, `Geometry2D.cs`, `Domain.cs`, `LayoutEngine.cs`, PE-LAY-002 | Bounded Python re-expression with named sources; no source copy and no Product-authority claim |
| VALIDATION_ONLY | Golden scenarios, `DEMO-001`, validator and Engineer Preview reports | Regression/comparison only; never presented as a real project |
| HISTORICAL_REFERENCE | Product baseline, plugin references in PM records, Git history | Context only; no Legacy promotion |
| NOT_REUSABLE | Static Demo JSON as runtime/real-case input; DXF/DWG parsing; shading/electrical/structural behavior | Excluded from v0.1 |

## Product definition

One input case contains one or more explicit partitions. Each partition owns its polygon, Local Axis, module dimensions/orientation, X/Y gaps and optional evidenced edge margin. The engine enumerates local bounding-box candidates row-major, accepts only complete rectangles contained by the partition, transforms them to global coordinates and reports counts.

## Authority and differences

- Source behavior: current C# files and `ENGINEERING/PE-LAY-002_SPEC.md`.
- Preview difference: Python accepts a file-based multi-partition wrapper and uses `gapXmm/gapYmm`; C# accepts one typed `LayoutRequest`/selected partition per call and names these column/row gaps.
- Preview status: ENGINEERING PREVIEW / SHORT TRACK.
- Promotion boundary: evidence-proven behavior requires PM review and a separately authorized C# implementation; Python never silently becomes Product authority.
- No full CAD parser, optimization, obstacles, setback derivation, shading, electrical, structural, UI or automatic axis inference.

## Real-case admission gate

Final acceptance requires a lawful real or legitimately de-identified case with provenance, partition polygon(s), explicit axis data, module/gap values and a manual or CAD reference. Golden/demo/test fixtures cannot satisfy this gate.
