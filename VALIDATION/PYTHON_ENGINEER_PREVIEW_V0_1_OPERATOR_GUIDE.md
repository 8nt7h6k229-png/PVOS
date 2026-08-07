# PVOS Python Engineer Preview v0.1 — Operator Guide

## Purpose

The Preview gives a Windows engineer a double-click validation workflow. It runs the existing C# PVOS CLI, validates its evidence through Python, and creates readable PASS/FAIL/BLOCKED reports. It does not calculate or repair Product results.

## Prerequisites

- Governed PVOS checkout containing `PVOS.sln` and `VALIDATION/golden-dataset-v1.json`.
- Windows with Git, .NET 8 SDK and Python 3.11 or later on `PATH`.
- Existing Release build available.

## Run

1. Open the governed repository root.
2. Double-click `PVOS-Engineer-Preview-v0.1.bat`.
3. Keep the console open until PASS, FAIL or BLOCKED appears.
4. Review the report path before pressing a key.

The fixed approved evidence entry point is `VALIDATION/golden-dataset-v1.json`. Reports are written under `ENGINEER_PREVIEW_OUTPUT`: `LATEST.md`, an identity-addressed Markdown report, and a matching JSON report.

| Result | Meaning | Operator action |
|---|---|---|
| PASS | Existing C# output matches governed evidence | Submit evidence; PM acceptance remains separate |
| FAIL | Evidence differs from the approved baseline | Preserve reports; do not rewrite Golden assets; escalate |
| BLOCKED | Required tool, asset or Git identity is unavailable | Follow the actionable prerequisite message and rerun |

## Authority Boundary

C#/.NET is the sole Product Behavior Authority. Python only invokes, observes, compares and reports. It does not calculate Placement, create expected Product results, repair C# output, replace Mainline or perform Product Acceptance.

## Known Limitations

- Console/double-click workflow only; no GUI or installer.
- Fixed governed evidence entry point; no arbitrary Project input selection.
- Reports are local run evidence and are not automatically committed, uploaded or accepted.
- Tool discovery depends on Windows `PATH`.
