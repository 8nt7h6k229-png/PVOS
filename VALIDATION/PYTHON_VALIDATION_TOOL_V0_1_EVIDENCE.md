# Python Validation Tool v0.1 Evidence

## Control

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #84 — PVOS-502 |
| Dependency | PVOS-501 / commit `379885cb7c8189ecb5d2f1221318be30ae64940a` |
| Tool | `VALIDATION/python/validate.py` |
| Track | External Validation / Support Track only |
| Status | READY_FOR_PM_REVIEW |

## Controlled Tool Result

- Iterates every JSON asset registered in the six-scenario Golden manifest.
- Verifies every registered asset SHA-256.
- Emits stable ordered PVPY-001 through PVPY-008 findings.
- Emits `report_fingerprint`, calculated from evidence content while excluding timestamps.
- Missing prerequisites remain BLOCKED; content or hash mismatch remains FAIL.

## Repeatability

Equivalent evidence commit, environment and findings produce the same report fingerprint even when run timestamps differ. Any evidence-result change produces a different fingerprint.

## Boundary Proof

Python invokes the existing C# CLI externally. It contains no geometry, placement, panel-count, capacity, warning or error calculation and cannot create a Product result. C# remains the sole Mainline and Product behavior authority.

READY_FOR_PM_REVIEW — PYTHON VALIDATION TOOL V0.1 CONTROLLED
