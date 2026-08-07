# Demo-001 Revalidation Report — 2026-08-07

## Result

PASS — current executable output exactly matches `DEMO/DEMO-001_OUTPUT.txt` after newline normalization.

## Commands and Results

| Check | Result |
|---|---|
| `dotnet restore .\PVOS.sln` | PASS |
| Release build with `--no-restore` | PASS — 0 warnings, 0 errors |
| Release tests with `--no-build` | PASS — 14 passed, 0 failed, 0 skipped |
| Release CLI run with `--no-build` | PASS |
| Exact text comparison with captured output | `True` |

## Demo Comparison

| Field | Expected | Actual | Result |
|---|---:|---:|---|
| Status | Accepted | Accepted | PASS |
| Partition | PART-001 | PART-001 | PASS |
| Panel count | 10 | 10 | PASS |
| Installed capacity | 5.000 kWp | 5.000 kWp | PASS |
| Panel identifiers | PNL-000001–PNL-000010 | PNL-000001–PNL-000010 | PASS |
| Ordering | Two rows, five columns, row-major | Exact match | PASS |
| Warnings | none | none | PASS |

## Scope Confirmation

No product source, Blueprint, Demo input, expected output, UI, adapter, or acceptance expectation was changed. Build output was cleaned after verification; remaining generated Release directories are untracked build artifacts and are excluded from this evidence commit.

## Status

READY_FOR_PM_REVIEW
