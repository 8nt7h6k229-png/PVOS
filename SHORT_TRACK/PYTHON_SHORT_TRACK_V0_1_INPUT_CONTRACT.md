# Python Short-Track v0.1 Input Contract

This is an experimental file adapter, not a formal PVOS Product contract. UTF-8 JSON must contain `caseId`, `linearUnit: "mm"`, and a non-empty `partitions` list. Each partition requires:

- unique `partitionId`;
- simple non-zero `boundary` polygon as `{x,y}` vertices;
- `localAxis.origin` and finite `rotationDegrees`;
- positive `physicalWidthMm` and `physicalLengthMm`;
- `orientation`: `WidthAlongLocalX` or `LengthAlongLocalX`;
- non-negative `gapXmm`, `gapYmm`, and optional `edgeMarginMm` (default 0).

The tool does not infer units, axis, module orientation or missing engineering values. Invalid/missing input is `BLOCKED` with exit code 2.
