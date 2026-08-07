# Python Validation Tool Evolution Evidence

## Control

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #89 — PVOS-601 |
| Source Tool | `VALIDATION/python/validate.py` v0.1 |
| Track | Validation / Support Track only |
| Status | READY_FOR_PM_REVIEW |

## Reusable Workflow

```text
python VALIDATION/python/validate.py \
  --repo-root . \
  --evidence-commit <immutable-commit> \
  --repeatability-runs 2 \
  --output <caller-selected-report.json>
```

The command validates prerequisites, the C# CLI, Golden text/fields/panel order, every registered JSON asset and every registered SHA-256. It then repeats the complete evidence run and requires matching deterministic fingerprints.

## Report Enhancement

The report retains PVPY-001–PVPY-008 and adds a `repeatability` summary containing run count, result, all fingerprints and an equality flag. Timestamps remain observable but excluded from the evidence fingerprint.

## Team Usage Model

| Role | Responsibility |
|---|---|
| Engineer | Select immutable commit and report path; do not edit evidence during execution |
| Validator maintainer | Maintain validator/report compatibility and negative tests only |
| PM reviewer | Decide which findings support acceptance; tool PASS is not Product Acceptance |
| C# Product owner | Retains sole authority for Product behavior and results |

## Maintenance Boundary

- Validator changes require tests for PASS, FAIL and BLOCKED semantics.
- Report/check identity changes require an explicit compatibility review.
- Golden assets remain controlled by scenario admission, not by the tool.
- Python may observe the C# CLI and static evidence only.
- Python may not calculate or repair Product results or replace C# Mainline.

READY_FOR_PM_REVIEW — REPEATABLE VALIDATION WORKFLOW EVIDENCED
