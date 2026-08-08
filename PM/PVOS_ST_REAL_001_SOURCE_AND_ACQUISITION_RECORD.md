# PVOS-ST-REAL-001 Source and Acquisition Record

## Registration

| Field | Value |
|---|---|
| Case ID | `PVOS-ST-REAL-001` |
| Source Type | `DWG` |
| Source Status | `OWNER_SUPPLIED_REAL_ENGINEERING_SOURCE` |
| Purpose | Python Short Track v0.1 real-case validation |
| Source SHA-256 | `e75a20d807f18069cd34dcb396423296bfc00196b31bd0c24a1b4431404f0b2d` |
| Privacy boundary | New repository evidence uses Case ID only; source remains external and is not committed |
| Knowledge Gap | `GAP-017` / `EK-GAP-017` |

Owner authorization establishes lawful source provenance. It does not establish a permanent DWG/DXF input architecture.

## Direct inspection decision

The supplied file was identified as an AutoCAD 2018/2019/2020 DWG. The Linux execution environment has no AutoCAD, ODA File Converter, LibreDWG, or other verified DWG entity parser. Container identification is not sufficient evidence for geometry extraction. Direct extraction is therefore `ENVIRONMENT_BLOCKED`; no geometry, Local Axis, module parameters, or reference count was inferred.

## Minimum bounded acquisition

`SHORT_TRACK/acquisition/PVOS-ST-REAL-001-EXPORT.lsp` is an experimental operator-assisted exporter for this case only. In AutoCAD it:

1. accepts one closed, flat, straight-segment `LWPOLYLINE` partition;
2. accepts one straight `LINE` or picked `LWPOLYLINE` segment as Local Axis;
3. prompts for module width/length, orientation, X/Y gaps, explicit margin, and CAD/manual reference count;
4. writes `PVOS-ST-REAL-001-project-input.json` using the existing experimental adapter contract.

It intentionally rejects bulged/elevated partitions, does not scan layers, and does not import title blocks, annotations, electrical, structural, shading, or project metadata. It is not a general-purpose importer.

## Current gate

Status: `ACQUISITION_TOOL_READY — OPERATOR_EXTRACTION_REQUIRED`

No project input, Short-Track result, or comparison claim exists until the operator runs the exporter in the supplied DWG and returns the generated JSON. The required CAD reference count is captured by the same command and must not be guessed.

C# Mainline authority remains preserved.
