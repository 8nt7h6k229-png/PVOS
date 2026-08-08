# Python Short-Track v0.1 Input Contract

This is the `GAP-017` experimental operator JSON adapter, not a formal PVOS Product contract or permanent input architecture. Copy `SHORT_TRACK_INPUT/project-input-template.json` to a new filename and replace every `OWNER_TO_SUPPLY` value. UTF-8 JSON must contain `caseId`, `linearUnit: "mm"`, and a non-empty `partitions` list. `inputAcquisition.sourceType`, when supplied, must be `OPERATOR_SUPPLIED_JSON`; provenance, de-identification and manual/CAD reference method are carried into evidence. Each partition requires:

- unique `partitionId`;
- simple non-zero `boundary` polygon as `{x,y}` vertices;
- `localAxis.origin` and finite `rotationDegrees`;
- positive `physicalWidthMm` and `physicalLengthMm`;
- `orientation`: `WidthAlongLocalX` or `LengthAlongLocalX`;
- non-negative `gapXmm`, `gapYmm`, and optional `edgeMarginMm` (default 0).

The tool does not infer units, axis, module orientation or missing engineering values. Invalid/missing input is `BLOCKED` with exit code 2.
