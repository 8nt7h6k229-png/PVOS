# PVOS Golden Dataset / Regression Foundation

## Authority and Dependency

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #67 — PVOS-202 |
| Planning Source | PVOS 1.1 Implementation Planning Package — Owner Approved |
| Dependency | PVOS-201 / commit `367f8868dca6a3fa6fcec9a2a05daea93e162489` |
| Dataset | `PVOS-GOLDEN-001` |
| Status | READY_FOR_PM_IMPLEMENTATION_REVIEW |

## Purpose

Provide one machine-readable registry for the existing Demo-001 Golden Input, Golden Output, static review assets, integrity hashes, and bounded regression expectations. This foundation registers evidence; it does not regenerate evidence or change PVOS behavior.

## Golden Dataset Contract

`VALIDATION/golden-dataset-v1.json` is the regression manifest. Repository-relative paths are resolved from the governed PVOS root. SHA-256 values are exact, uppercase hexadecimal identifiers for the committed assets.

The executable regression source is the existing C# CLI. `DEMO/demo-input.json` and `DEMO/demo-output.json` remain static evidence captures and are not runtime adapters.

## Regression Sequence

```text
Resolve governed repository and immutable evidence commit
        ↓
Load and validate the Golden Dataset manifest
        ↓
Verify all registered asset paths and SHA-256 values
        ↓
Build the existing C# Mainline
        ↓
Invoke the existing Release CLI externally
        ↓
Normalize newline representation only
        ↓
Compare exact CLI output and bounded result fields
        ↓
Record PASS, FAIL, or BLOCKED evidence
```

## Fixed Assertions

| Assertion | Expected Result |
|---|---|
| Dataset identity | `PVOS-GOLDEN-001` |
| Request | `LAYOUT-REQ-001` |
| Status | `Accepted` |
| Partition | `PART-001` |
| Panel count | `10` |
| Installed capacity | `5.000 kWp` |
| Panel identifiers | `PNL-000001` through `PNL-000010`, unique and ordered |
| Placement warnings | none |
| CLI comparison | Exact after CRLF/LF normalization |
| Asset integrity | Every registered SHA-256 matches |

## Result Semantics

| Result | Meaning |
|---|---|
| PASS | All registered assets, hashes, executable output, and bounded assertions match |
| FAIL | Executed evidence contradicts one or more registered expectations |
| BLOCKED | Required repository identity, dependency, asset, or execution environment is unavailable |

A failure does not authorize automatic repair, Golden Asset replacement, or Product code modification.

## Scope Boundary

- One existing dataset only; no additional Product scenario is claimed.
- No Product Scope, Capability, Blueprint, EOS, Governance, or release status is changed.
- No Python or alternative placement engine is introduced by this foundation.
- A future validator may consume the manifest externally but may not calculate placement.
- PM retains Product Acceptance authority.

## Verification

| Check | Result |
|---|---|
| Manifest parses as JSON | PASS |
| Six registered assets exist | PASS |
| Six registered hashes match | PASS |
| Fixed assertions match existing Demo evidence | PASS |
| Existing Golden files changed | No |

## Result

READY_FOR_PM_IMPLEMENTATION_REVIEW — GOLDEN REGRESSION FOUNDATION ESTABLISHED — PRODUCT ACCEPTANCE NOT PERFORMED
