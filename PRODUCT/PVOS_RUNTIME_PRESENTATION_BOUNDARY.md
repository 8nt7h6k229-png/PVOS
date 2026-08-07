# PVOS Runtime Result Presentation Boundary

## Authority and Dependency

| Field | Value |
|---|---|
| Execution Source | GitHub Issue #74 — PVOS-303 |
| Planning Source | `PPP-PVOS-1.1-RUNTIME-PRODUCTIZATION-2026-08-07` — Owner Approved |
| Dependency | PVOS-302 / Issue #73 / commit `9fce955af31f0f639022a1e06eb1dba480c4c6ce` |
| Primary Capability | `VIS-001` |
| Product Result Source | Existing C# `LayoutResult` |
| Status | READY_FOR_PM_REVIEW |

## Purpose

Define the Product integrity boundary between the deterministic Runtime result, its presentation, and validation evidence. Presentation makes existing results reviewable. It does not own, alter, complete, filter, score, repair, or recalculate Product behavior.

## Integrity Principle

```text
Existing C# Layout Runtime
        ↓ owns
LayoutResult
        ↓ read-only consumption
Result Presentation
        ↓ traceable capture
Validation Evidence
```

Only the C# Runtime creates `LayoutResult`. Presentation may select a textual or visual representation and apply deterministic display formatting, but the meaning and values remain owned by the Runtime result.

## Result Presentation Rules

| Rule ID | Rule | Required Behavior | Prohibited Behavior |
|---|---|---|---|
| PRS-001 | Source integrity | Consume one completed `LayoutResult` and identify its request | Creating a substitute result or merging separate runs |
| PRS-002 | Status integrity | Display `Accepted` or `Rejected` exactly as returned | Promoting, suppressing, or inferring status |
| PRS-003 | Partition integrity | Display the Runtime-provided partition identity when present | Inferring a different partition from geometry |
| PRS-004 | Panel collection integrity | Preserve Runtime panel membership | Adding, removing, filtering, deduplicating, or selecting panels |
| PRS-005 | Ordering integrity | Preserve Runtime collection order, placement order, row, column, and panel IDs | Sorting, renumbering, grouping, or reordering as Product truth |
| PRS-006 | Geometry integrity | Display the Runtime-provided corner sequence and coordinates | Moving, rotating, snapping, clipping, or recomputing corners |
| PRS-007 | Count integrity | Display `LayoutResult.PanelCount` | Counting displayed shapes as an alternative Product calculation |
| PRS-008 | Capacity integrity | Display `LayoutResult.InstalledCapacityKwp` | Multiplying count and power in presentation |
| PRS-009 | Warning integrity | Preserve warning code, message, and optional row | Hiding, promoting, merging, or rewriting warning meaning |
| PRS-010 | Error integrity | Preserve error code and message | Suppressing errors or presenting a rejected result as success |
| PRS-011 | Empty-result integrity | Represent Accepted no-fit and Rejected input as different states | Treating every empty panel collection as the same outcome |
| PRS-012 | Format transparency | Apply only documented display formatting | Changing semantic value through rounding, unit conversion, or derived calculation |

## Result-to-Presentation Traceability

| Product Value | Runtime Source | Current CLI Presentation | Allowed Formatting | Recalculation Boundary |
|---|---|---|---|---|
| Request | `LayoutResult.RequestId` | `Request: <value>` | Label and exact string | No inference |
| Status | `LayoutResult.Status` | `Status: <enum>` | Enum text | No status derivation |
| Partition | `LayoutResult.PartitionId` | `Partition: <value>` | Label and exact identity | No geometry-based selection |
| Panel count | `LayoutResult.PanelCount` | `PanelCount: <integer>` | Integer text | Do not recount in presentation |
| Installed capacity | `LayoutResult.InstalledCapacityKwp` | `InstalledCapacityKwp: <F3>` | Invariant-culture three-decimal display | Formatting only; do not multiply or sum |
| Panel identifier | `Panel.Id` | One ordered line per panel | Exact identity | Do not renumber |
| Placement order | `Panel.PlacementOrder` | `order=<integer>` | Integer text | Do not reorder |
| Candidate index | `Panel.CandidateIndex` | Not displayed by current Demo CLI | May remain undisplayed when not required by current presentation claim | Do not reconstruct |
| Row / column | `Panel.Row`, `Panel.Column` | `row=<integer> column=<integer>` | Integer text | Do not derive from coordinates |
| Corners | `Panel.Corners` | Ordered `(x,y)` pairs | Invariant-culture three-decimal display | Do not transform or rebuild geometry |
| Warnings | `LayoutResult.Warnings` | `none` or code/message list | Labels and line structure | Do not infer missing warnings |
| Errors | `LayoutResult.Errors` | Error code/message lines when present | Labels and line structure | Do not suppress or translate into success |

Display rounding is presentation formatting only. Validation requiring exact Product values must compare the underlying result or an approved canonical evidence representation, not reverse-engineer values from pixels or rounded text.

## Presentation State Matrix

| Runtime State | Required Presentation | Required Distinction |
|---|---|---|
| Accepted with panels | Status, partition, ordered panels, count, capacity, warnings | Product result and any warnings remain visible |
| Accepted no-fit | Accepted status, zero count/capacity, no-fit warnings | Must not appear as input rejection |
| Rejected input | Rejected status, zero count/capacity, validation errors | Must not appear as valid no-fit or successful placement |
| Execution failure without `LayoutResult` | Process/build failure evidence | Must not fabricate Product status or result fields |
| Evidence blocker | Missing evidence identified separately | Must not alter a valid Runtime result |

## Evidence Output Rules

| Evidence Type | Source and Rule | Product Claim Boundary |
|---|---|---|
| CLI standard output | Direct formatting of current `LayoutResult` by existing C# CLI | Executable text presentation for the bounded scenario |
| `DEMO/DEMO-001_OUTPUT.txt` | Committed Golden text compared after newline normalization | Expected CLI evidence; not Product code |
| `DEMO/demo-output.json` | Static review capture | Not a runtime JSON adapter or executable Runtime output |
| `DEMO/demo-output.svg` | Static presentation evidence | Not a rendering engine or UI |
| `DEMO/demo-output.png` | Static presentation evidence | Pixel evidence; not a source for Product recalculation |
| `DEMO/demo-summary.md` | Static human-readable summary | Review aid; not Product authority |
| `VALIDATION/golden-dataset-v1.json` | Paths, SHA-256 values, and bounded expected fields | Evidence registry; not Runtime input or output |
| Python validation report | External observation of CLI and Golden evidence | Validation evidence only; Python cannot create Product results |

Every evidence output must identify or be traceable to an immutable commit and the relevant Runtime or Golden evidence source. A presentation artifact without provenance cannot establish Product acceptance.

## No-Recalculation Verification

| Product Concern | Runtime Owner | Presentation Check | Result |
|---|---|---|---|
| Placement | `LayoutEngine.Generate` | No presentation path invokes candidate generation or containment | PASS |
| Panel identity/order | Runtime panel construction | CLI iterates returned panel collection without sorting or renumbering | PASS |
| Panel geometry | Runtime plus Axis transform | CLI formats returned corners only | PASS |
| Panel count | `LayoutResult.PanelCount` | CLI reads property directly | PASS |
| Installed capacity | Runtime calculation | CLI reads value and applies `F3` display formatting only | PASS |
| Warnings/errors | Runtime validation/warning construction | CLI iterates returned collections | PASS |
| Static visual evidence | Committed Demo evidence | Classified as static review artifacts | PASS |

## Presentation Acceptance Boundary

Presentation is eligible for PM review when:

1. every claimed field is traceable to `LayoutResult` or immutable validation metadata;
2. Runtime membership, ordering, identifiers, geometry, status, warnings, and errors are preserved;
3. display formatting is documented and does not become Product calculation;
4. static artifacts remain correctly classified as review evidence;
5. Accepted no-fit, Rejected input, process failure, and evidence blocker remain distinguishable; and
6. excluded UI, delivery, integration, and Product scopes remain absent from the changed files.

This eligibility does not perform Product Acceptance.

## Explicit Exclusions

- No UI, visualization framework, renderer, dashboard, interaction model, or deployment channel.
- No Product result calculation, alternative engine, optimization, or geometry transformation.
- No runtime JSON adapter, Cloud, network service, full AutoCAD integration, DXF, Electrical, Construction, or PVOS 2.x.
- No Product Scope, Product Blueprint, Capability status, EOS, Governance, or Legacy promotion.

## Verification

| Check | Result |
|---|---|
| Result fields mapped to Runtime sources | PASS |
| Formatting and recalculation separated | PASS |
| Runtime states remain distinguishable | PASS |
| Evidence outputs correctly classified | PASS |
| UI or Product behavior implemented | No |

## Result

READY_FOR_PM_REVIEW — PRESENTATION BOUNDARY DEFINED — NO PLACEMENT RECALCULATION
