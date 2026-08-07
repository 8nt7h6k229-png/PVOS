# Python Validation Product v0.1 — Short Track Specification

## Authority and Boundary

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #63 — PVOS-105 |
| Planning Source | DPP-PVOS-1.1-PRODUCT-EVOLUTION-2026-08-07 — Owner Approved |
| Primary Capability | QUA-002 — Geometry and Layout Validation Evidence |
| Dependency Evidence | PVOS-104 / Issue #62 / commit `b0b6146b8e7d018076eae1d90b6d891f3c5025e7` |
| Track | Short Track only |
| Version | v0.1 specification and evidence plan |
| Implementation State | Not implemented by this Issue |

Python Validation Product v0.1 is a bounded external validation surface for existing PVOS evidence. It does not become part of `PVOS.Core`, `PVOS.Layout`, or `PVOS.Cli`; it does not change Product behavior or establish a runtime JSON adapter.

## Product Purpose

Provide a small, repeatable validation path that can:

1. invoke the existing PVOS CLI as an external process;
2. capture its standard output and exit status;
3. compare output with governed Golden Demo evidence;
4. validate static review-artifact consistency where explicitly defined; and
5. emit a machine-readable validation report for PM review.

This is validation tooling, not a placement engine, Product host, adapter, UI, service, or replacement runtime.

## Short Track v0.1 Boundary

| Included | Excluded |
|---|---|
| Existing CLI process execution | Calling internal .NET APIs directly |
| Existing Demo-001 text comparison | Runtime JSON request adapter |
| Existing committed JSON review-artifact inspection | Generating or changing layout results |
| Hash and file-presence checks | Editing Golden Demo assets |
| Deterministic validation report | New PVOS capability or release allocation |
| Clear PASS/FAIL/BLOCKED output | AutoCAD, DXF, database, network, UI, Cloud, or PVOS 2.x work |

## Proposed Inputs

| Input | Requirement |
|---|---|
| Repository root | Existing governed PVOS checkout |
| CLI project | `src/PVOS.Cli/PVOS.Cli.csproj` |
| Configuration | `Release` |
| Expected text | `DEMO/DEMO-001_OUTPUT.txt` |
| Static input evidence | `DEMO/demo-input.json` |
| Static output evidence | `DEMO/demo-output.json` |
| Optional presentation evidence | `DEMO/demo-output.svg`, `demo-output.png`, `demo-summary.md` |
| Evidence baseline | Immutable Git commit supplied to the validation run |

The static JSON files are evidence inputs only. v0.1 shall not send them to PVOS as runtime requests.

## Proposed Output Contract

One UTF-8 JSON validation report:

```json
{
  "validation_product": "PVOS Python Validation Product",
  "version": "0.1",
  "evidence_commit": "<git-commit>",
  "started_at": "<ISO-8601>",
  "finished_at": "<ISO-8601>",
  "result": "PASS | FAIL | BLOCKED",
  "checks": [
    {
      "check_id": "PVPY-001",
      "result": "PASS | FAIL | BLOCKED",
      "expected": "<bounded criterion>",
      "actual": "<observed result>",
      "evidence": ["<path or command>"]
    }
  ],
  "risks": []
}
```

Timestamps record execution evidence and are not part of deterministic result comparison. Check ordering shall be stable.

## v0.1 Validation Checks

| Check ID | Check | Expected Result | Failure Boundary |
|---|---|---|---|
| PVPY-001 | Required evidence files exist | All bounded input paths resolve | BLOCKED if a required file is absent |
| PVPY-002 | Evidence commit resolves | One immutable Git commit is recorded | BLOCKED if identity is unavailable |
| PVPY-003 | Existing Release CLI executes | Exit code 0 | FAIL on non-zero process exit |
| PVPY-004 | CLI text matches Golden text after newline normalization | Exact content match | FAIL with bounded text-difference evidence |
| PVPY-005 | Required result fields exist | Accepted, PART-001, count 10, 5.000 kWp, no warnings | FAIL only the mismatching field |
| PVPY-006 | Panel identity sequence is stable | PNL-000001 through PNL-000010, unique and ordered | FAIL on missing, duplicate, or reordered ID |
| PVPY-007 | Static JSON evidence is parseable | Valid UTF-8 JSON | FAIL without changing the artifact |
| PVPY-008 | Golden asset hashes are reported | Hash recorded for each selected artifact | BLOCKED if hashing cannot complete |

## Validation Flow

```text
Resolve governed repository and evidence commit
        ↓
Verify required static evidence exists
        ↓
Invoke existing Release CLI externally
        ↓
Capture stdout, stderr, and exit code
        ↓
Normalize newline representation only
        ↓
Run PVPY-001 through PVPY-008 in stable order
        ↓
Write one validation report
        ↓
PM reviews report under Acceptance Evidence Framework
```

## Result Semantics

| Result | Meaning |
|---|---|
| PASS | All v0.1 checks match existing bounded evidence |
| FAIL | At least one check produced contradictory evidence |
| BLOCKED | Required environment, identity, or evidence was unavailable |

The overall result is PASS only when every check passes. A failed check does not authorize validation tooling to modify PVOS or repair evidence.

## Acceptance and Non-Regression Criteria

- The validator invokes only the existing CLI and never imports or rewrites PVOS Product code.
- CLI output remains the executable result; Python does not calculate placement, count, capacity, warnings, or geometry.
- Golden evidence remains immutable during validation.
- Repeated validation against the same commit and environment produces the same ordered check findings except timestamps.
- A report identifies exact evidence paths, command, commit, actual result, and retained risks.
- PASS remains validation evidence only and does not perform PM Product Acceptance.

## Implementation Gate

This Issue authorizes the v0.1 bounded specification and evidence plan only. Any implementation shall remain within this Short Track contract and requires PM confirmation that the proposed changed-file set contains no PVOS Product implementation path. Scope exceeding this specification stops for a separate decision.

## Validation of This Specification

| Check | Result |
|---|---|
| Uses existing Capability QUA-002 | PASS |
| Inputs and outputs are explicit | PASS |
| Validation checks and result model are complete | PASS |
| Product behavior remains owned by existing .NET implementation | PASS |
| Runtime JSON adapter claim excluded | PASS |
| PVOS 2.x scope excluded | PASS |

## Status

READY_FOR_PM_REVIEW — SHORT TRACK v0.1 SPECIFICATION PREPARED — IMPLEMENTATION NOT STARTED
