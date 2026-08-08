# Python Short-Track v0.1 — Input Acquisition Evidence

## Status

`IMPLEMENTATION_READY — REAL_CASE_SOURCE_REQUIRED`

## Governed knowledge

- Knowledge Gap: `EK-GAP-017` / `GAP-017`
- Confirmed fact: PVOS has no governed Engineering Input Acquisition pipeline.
- The adapter introduced here is `EXPERIMENTAL_OPERATOR_JSON_ADAPTER` only.
- It establishes no CAD-to-JSON, DXF/DWG import, persistence, or permanent Product architecture.

## Operator workflow

1. Copy `SHORT_TRACK_INPUT/project-input-template.json` and rename it for the de-identified case.
2. Replace every `OWNER_TO_SUPPLY` value and zero placeholder with actual engineering data.
3. Drag the completed JSON onto `PVOS-Python-Short-Track-v0.1.bat`, or pass it to the Linux launcher.
4. Review `SHORT_TRACK_OUTPUT/LATEST.json` and `LATEST.md`.
5. Compare partition count, Local Axis, module orientation, counts, and obvious boundary violations with the named manual/CAD reference.

The operator does not edit Python, validator, Golden, or internal evidence files.

## Required real-case source

- lawful source and de-identification confirmation;
- de-identified Case ID;
- one or more Partition IDs and boundary vertices in millimetres;
- explicit Local Axis origin and rotation per Partition;
- module physical width and length;
- `WidthAlongLocalX` or `LengthAlongLocalX` orientation;
- X and Y gaps;
- optional explicit edge margin;
- manual or CAD reference method, expected per-partition count, and orientation.

## Validation record

| Check | Result |
|---|---|
| Short-Track unit/behavior tests | PASS — 6/6 |
| Valid multi-partition input | PASS |
| Missing field | PASS — BLOCKED as required |
| Invalid geometry | PASS — BLOCKED as required |
| Unsupported acquisition source | PASS — BLOCKED as required |
| Local Axis / orientation / X-Y gaps | PASS |
| Serialization / report generation | PASS |
| Deterministic repeat execution | PASS |
| Ready-to-fill template preflight | PASS — BLOCKED until Owner values are supplied |
| Existing Python validation suite | 12/13; existing Golden hash mismatch retained, not repaired |
| C# regression | ENVIRONMENT_BLOCKED — `dotnet` unavailable; C# files unchanged |

## Acceptance boundary

No legitimate real project data is stored in this branch. Golden, Demo, and tests were not used as real-case evidence. Completion remains gated by `REAL_CASE_SOURCE_REQUIRED`.

Python remains `ENGINEERING PREVIEW / SHORT TRACK`; C# Mainline authority is preserved. Promotion requires real project use, evidence, PM review, Mainline candidacy, and separately authorized C# implementation.
