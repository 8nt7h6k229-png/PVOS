# Demo-001 Revalidation Report — 2026-08-07

## Authority and Boundary

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #61 — PVOS-103 |
| Planning Source | DPP-PVOS-1.1-PRODUCT-EVOLUTION-2026-08-07 — Owner Approved |
| Capabilities | QUA-001, QUA-002, VIS-001 |
| Dependency Evidence | PVOS-102 / Issue #60 / commit `7640aa1e54deaa7006fd99a492ac9e3e7cca16c6` |
| Result | PASS |

This revalidation executes the existing Demo-001 workflow and compares its output with committed evidence. It does not modify Product code, Demo behavior, input, expected output, visualization, Blueprint, or Product Acceptance status.

## Commands and Results

| Check | Result |
|---|---|
| `dotnet restore .\PVOS.sln` | PASS |
| `dotnet build .\PVOS.sln --configuration Release --no-restore` | PASS — 0 warnings, 0 errors |
| `dotnet test .\PVOS.sln --configuration Release --no-build --no-restore` | PASS — 14 passed, 0 failed, 0 skipped |
| Release CLI run with `--no-build` | PASS |
| CLI text comparison with `DEMO/DEMO-001_OUTPUT.txt` after newline normalization | PASS — exact match |

## Golden Demo Comparison

| Field | Expected | Actual | Result |
|---|---:|---:|---|
| Status | Accepted | Accepted | PASS |
| Partition | PART-001 | PART-001 | PASS |
| Panel count | 10 | 10 | PASS |
| Installed capacity | 5.000 kWp | 5.000 kWp | PASS |
| Panel identifiers | PNL-000001 through PNL-000010 | PNL-000001 through PNL-000010 | PASS |
| Ordering | Two rows, five columns, row-major | Exact match | PASS |
| Placement warnings | none | none | PASS |

## Golden Evidence Integrity

| Asset | SHA-256 |
|---|---|
| `DEMO/demo-input.json` | `6CCEFB3867501639F4FD8D1283B9989C472219EB74184B1D71F64C2D3E79D0EC` |
| `DEMO/DEMO-001_OUTPUT.txt` | `2DCF0A369A11DD61EFD719515860812D5CD960228605D242C27C7D9057B3C798` |
| `DEMO/demo-output.json` | `FBAC211CB90C3A471B5119FBE421B306E4048BCC6CADB0B6F2E0560F8011A3AD` |
| `DEMO/demo-output.svg` | `1AA1B9048A19D1E30FA8CD51BFBC25284E1CBD2B6A2804B53CB8AE79B5FBE12A` |
| `DEMO/demo-output.png` | `543A4597D19A9B1A5B4ABF12450C20830BBF04FE131881ADEF2E5E4B0E740222` |
| `DEMO/demo-summary.md` | `DA1677553CBA48FE79F983F35C2C89429701F0827F2C052DDCB2B96833B9287B` |

These hashes identify the committed Golden Demo review assets inspected during revalidation. The CLI is the executable source for the text result; JSON, SVG, PNG, and Markdown remain static review artifacts rather than runtime adapters or UI functionality.

## Capability Findings

| Capability | Finding |
|---|---|
| QUA-001 | Identical approved input reproduces the committed ordered text result |
| QUA-002 | Existing Release build and 14-test suite pass reproducibly |
| VIS-001 | Existing JSON, SVG, PNG, and summary present the approved result boundary without adding behavior |

## Remaining Boundaries

- Static JSON evidence does not establish a runtime JSON adapter.
- SVG and PNG evidence do not establish a Product UI or rendering framework.
- Demo-001 covers one approved deterministic scenario; it does not prove excluded or future capabilities.
- PASS makes the evidence eligible for PM review but does not perform Product Acceptance.

## Scope Confirmation

No tracked file under `src/`, `tests/`, `PRODUCT/`, or `DEMO/` changed during this revalidation. Generated Release directories remain untracked build artifacts and are excluded from the evidence commit.

## Status

READY_FOR_PM_REVIEW — GOLDEN DEMO REVALIDATION PASS — PRODUCT ACCEPTANCE PENDING
