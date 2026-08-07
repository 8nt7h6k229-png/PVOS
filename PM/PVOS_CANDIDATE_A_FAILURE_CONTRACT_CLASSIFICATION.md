# PVOS Candidate A Failure Contract Classification

## Decision Identity

| Field | Value |
|---|---|
| Work Unit | CA-303 — Failure Contract Classification |
| Primary Authority | C# Mainline Product Owner |
| PM Principle | Stable machine-readable Failure Identity may be controlled Product Contract |
| Status | CLASSIFICATION PERSISTED |
| Product Behavior Effect | NONE |

## Classification Model

| Class | Meaning |
|---|---|
| A — Product Contract | Exposed behavior／representation controlled for compatibility and Regression |
| B — Stable Diagnostic Identity | Machine-readable identity is stable; other presentation details may vary |
| C — Internal Diagnostic／Non-contract | No external stability promise; changes still require authorized work and evidence review |
| D — UNKNOWN | Decision required; no inference permitted |

## Applied Classification

| Exposed Item | Classification | Controlled Meaning | Compatibility／Regression Rule |
|---|---|---|---|
| Error `Code` | **A — Product Contract** | Machine-readable failure identity and its bounded semantic | Rename／remove／semantic change requires version、affected-claim review and C# Regression |
| Warning `Code` | **A — Product Contract** | Machine-readable warning identity and bounded semantic | Rename／remove／semantic change requires version、affected-claim review and C# Regression |
| Accepted／Rejected `Status` | **A — Product Contract** | Product terminal-state distinction | Change requires Product contract authority and full affected Regression |
| Error／warning collection separation | **A — Product Contract** | Errors and warnings retain distinct Product meanings | Regression must preserve accepted／rejected and valid-no-fit distinctions |
| Presence rules for admitted bounded scenarios | **A — Product Contract within admitted claim** | Registered expected codes are present／absent as specified | Scenario Regression and PM claim impact review |
| Human-readable `Message` | **C — Internal Diagnostic／Non-contract by default** | Human explanation; no default wording／punctuation stability promise | Authorized wording change must not change Code semantic; evidence comparing text must be reviewed |
| Error／warning collection ordering | **B — Stable Diagnostic Identity within registered comparison evidence** | Existing admitted scenarios may rely on deterministic code order | Order change requires affected Golden／consumer review; not elevated to broad Product semantic beyond bounded evidence |
| `Row` metadata | **B — Stable Diagnostic Identity when applicable** | `PLC_PARTIAL_ROW` row identity is stable for bounded Regression; null elsewhere is diagnostic | Change requires affected scenario／claim review; not a general Domain contract |
| Other exposed diagnostic metadata | **C — Internal Diagnostic／Non-contract unless separately classified** | No inferred stability promise | Any proposal to promote must receive explicit A／B classification and compatibility review |
| Internal validation method／call order | **C — Internal Diagnostic／Non-contract** | Implementation detail | Cannot change Product outputs without separate behavior authority |

## Current Machine-Readable Failure Identity Families

- `PLC_*` request、dependency and placement findings。
- `GEO_*` geometry identity、unit、validity and containment findings。
- `SEL_*` selection findings。
- `AXS_*` axis identity、reference、unit and finite-value findings。
- `MOD_*` module identity、unit、dimension、orientation、gap and margin findings。

This record classifies existing identity semantics; it does not create、rename or modify codes.

## Version and Change Policy

- Class A changes require explicit Product contract authority、compatibility impact、version disposition and Regression plan。
- Class B changes require C# Mainline Product Owner review、affected-claim isolation and Regression evidence。
- Class C changes still require authorized implementation scope and no-behavior-change verification。
- Any unclassified new exposed metadata starts as D and cannot be promoted by inference。
- Python may detect differences but cannot define the correct classification or repair the Product result。

## CA-G3 Gap Disposition

`CA-G3-GAP-003 — RESOLVED BY EXPLICIT FAILURE CONTRACT CLASSIFICATION`

