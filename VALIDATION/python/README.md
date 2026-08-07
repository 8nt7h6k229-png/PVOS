# PVOS Python Validation Product v0.1

## Boundary

This Short Track prototype invokes the existing C# Release CLI as an external process and validates its output against `VALIDATION/golden-dataset-v1.json`. It does not import PVOS assemblies, calculate layout, accept runtime JSON, change Golden Assets, or replace the C# Mainline.

## Prerequisites

- Python 3.11 or later
- Git
- .NET SDK with the existing PVOS solution restored and built in Release configuration

## Execute

```powershell
$commit = git rev-parse HEAD
python .\VALIDATION\python\validate.py `
  --repo-root . `
  --evidence-commit $commit `
  --output .\validation-report.json
```

The JSON report is written only to the caller-selected path and is also emitted to standard output. Generated reports are run evidence and should not be committed unless separately authorized.

## Tests

```powershell
python -m unittest discover -s .\VALIDATION\python -p "test_*.py" -v
```

## Exit Codes

| Code | Result |
|---:|---|
| 0 | PASS |
| 1 | FAIL |
| 2 | BLOCKED |

PASS confirms only the bounded evidence checks PVPY-001 through PVPY-008. PM retains Product Acceptance authority.
