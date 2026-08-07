# PVOS 1.1 Golden Dataset Expansion Package

## Authority and Boundary

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #77 — PVOS-401 |
| Planning Source | `PPP-PVOS-1.1-PRODUCTION-READINESS-2026-08-07` — Owner Approved |
| Primary Capability | `QUA-002` |
| Existing Dataset | `PVOS-GOLDEN-001` — accepted placement |
| Added Scenarios | `PVOS-GOLDEN-002`, `PVOS-GOLDEN-003` |
| Product Authority | Existing C# Mainline and current C# tests |
| Status | READY_FOR_PM_REVIEW |

## Purpose

Expand the Golden review set from one successful placement into the three currently evidenced terminal-state families required for Production Readiness planning. No new Runtime input, Product behavior, validation code, error code, or capability is introduced.

## Existing Asset Inspection

| Existing Evidence | Finding | Reuse Decision |
|---|---|---|
| `PVOS-GOLDEN-001` / Demo-001 | Accepted result with 10 ordered panels, 5.000 kWp, and no warnings | Preserve unchanged as accepted-placement baseline |
| `Generate_NoFit_ReturnsAcceptedEmptyResultAndRequiredWarnings` | Existing C# test proves valid no-fit is Accepted with two bounded warnings | Admit as `PVOS-GOLDEN-002` review capture |
| `Generate_InvalidAxisAndModule_ReturnsSpecificationCodes` | Existing C# test proves invalid module width/gap produces bounded rejection errors | Narrow to module-only rejection as `PVOS-GOLDEN-003` review capture |
| `VALIDATION/golden-dataset-v1.json` | Existing machine-readable Dataset registry | Extend in place; do not create a competing registry |

## Scenario Coverage Matrix

| Scenario | Existing Capability Coverage | Bounded Claim | Terminal State | Golden Input | Golden Output | Regression Rule |
|---|---|---|---|---|---|---|
| `PVOS-GOLDEN-001` | `GEO-001`, `GEO-002`, `AXS-001`, `LAY-001`–`LAY-004`, `RES-001`–`RES-004`, `QUA-001` | Existing rectangular Demo produces stable ordered panels | Accepted with panels | `DEMO/demo-input.json` | `DEMO/DEMO-001_OUTPUT.txt`; static result evidence | Exact CLI text after newline normalization plus manifest hashes |
| `PVOS-GOLDEN-002` | `LAY-001`, `LAY-002`, `RES-002`–`RES-004`, `QUA-001` | Valid oversized module returns Accepted empty result and required no-fit warnings | Accepted no-fit | `VALIDATION/scenarios/PVOS-GOLDEN-002/input.json` | `VALIDATION/scenarios/PVOS-GOLDEN-002/output.json` | C# result fields, warning code/order, repeatability, JSON and hash integrity |
| `PVOS-GOLDEN-003` | `LAY-001`, `RES-002`–`RES-004`, `QUA-002` | Invalid module width/gap returns Rejected result without panels, warnings, or capacity | Rejected input | `VALIDATION/scenarios/PVOS-GOLDEN-003/input.json` | `VALIDATION/scenarios/PVOS-GOLDEN-003/output.json` | C# status, error code/order, zero-result fields, repeatability, JSON and hash integrity |

## Golden Admission Rules

- Inputs and outputs are immutable review captures registered by path and SHA-256.
- Product result claims must be validated through the existing C# Mainline or C# tests.
- Static JSON remains evidence and is not a runtime JSON adapter.
- Warning and error ordering is part of the bounded expected result for these scenarios.
- A scenario failure is isolated to that scenario and its dependent claims.
- Changes to an admitted Golden asset require separate review; automatic regeneration is prohibited.

## Evidence Integrity

The expanded assets are registered in `VALIDATION/golden-dataset-v1.json`. The manifest identifies their roles, SHA-256 values, terminal states, comparison rules, and existing C# evidence sources.

## Non-Claims

- No rotated-Axis Golden output is admitted by this Issue; existing test evidence remains available but is not promoted to a Golden asset.
- No concave-partition, unknown-selection, geometry-rejection, AutoCAD, DXF, UI, Cloud, Electrical, Construction, or PVOS 2.x behavior is claimed by the expanded set.
- Three terminal-state families improve coverage but do not prove every valid or invalid input combination.
- Dataset admission does not perform Product or Production Readiness acceptance.

## Verification

| Check | Result |
|---|---|
| Accepted, Accepted no-fit, and Rejected input families represented | PASS |
| Added scenarios map to existing C# behavior and Capability IDs | PASS |
| Input/output JSON parses | PASS |
| Assets registered with SHA-256 | PASS after manifest validation |
| Product source or Product Scope changed | No |

## Result

READY_FOR_PM_REVIEW — GOLDEN DATASET EXPANDED — PRODUCT BEHAVIOR UNCHANGED
