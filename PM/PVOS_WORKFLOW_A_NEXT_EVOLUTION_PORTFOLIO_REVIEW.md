# PVOS Workflow A Next Evolution Portfolio Review

## Identity and Baseline

| Field | Value |
|---|---|
| Authority | Owner Approved; PM Authorized |
| Baseline branch | `main` |
| Baseline HEAD | `373779baebd424f20d9e00476e463684c605b878` |
| Local / remote match | PASS |
| Tracked working tree | CLEAN |
| Candidate A | CLOSED with retained boundaries |
| Rooftop Gate 2 | EXTERNAL EVIDENCE HOLD |
| Review status | READY_FOR_PM_DECISION |

## Candidate Portfolio

### Candidate B — Python Validation / Evidence Automation

Current evidence already provides `VALIDATION/python/validate.py`, nine tests, explicit PASS/FAIL/BLOCKED exit codes, deterministic fingerprints, three-run repeatability and invocation of the existing C# Release CLI. The current usability gap is operational: engineers must use command-line arguments, manually identify the repository/commit/output, and interpret JSON console output.

Mandatory sub-candidate **Python Engineer Preview v0.1** is viable as a same-day/short-track deliverable:

`Approved Input / Evidence → controlled Windows launcher → existing C# PVOS CLI → Python validation → readable PASS / FAIL / BLOCKED report`

Bounded work may add a Windows double-click launcher, obvious input/evidence convention, human-readable summary, deterministic report identity, preflight/error handling and minimal operator instructions. Python must not calculate placement, define expected Product behavior, repair C# output or become a second Engine.

Classification: **Engineering support capability**, not Product capability.

### Candidate C — Result Package Evolution

Existing evidence defines a useful read-only logical package, result/evidence lineage, compatibility questions and no-recalculation rules. It is eligible for a separately governed contract proposal. However, a next implementation requires unresolved decisions about actual consumers, version identity, compatibility promises and whether any serialization format becomes binding. Those decisions have greater architecture and maintenance impact than the Preview.

Classification: potential **Mainline Product contract capability**, currently proposal/evidence ready rather than implementation ready.

### Candidate N — Evidence-Backed New Mainline Needs

| Need | Evidence | Disposition |
|---|---|---|
| Cross-platform evidence-byte stability | Candidate A Golden recovery proved Windows EOL checkout can invalidate hashes | Fold into validation preflight/reporting; no new Product behavior |
| Integrity artifact maintenance visibility | Candidate A retained boundary requires updates after authorized C# contract changes | Future maintenance automation candidate; not enough evidence for Product implementation |
| Failure/lineage audit orchestration | Candidate A introduced machine-readable integrity artifacts and tests | Can be surfaced by Candidate B reporting; no separate candidate needed |
| New Product feature | No factual gap requiring new behavior was found | Not proposed |

Candidate N introduces no independent investment candidate in this cycle.

## Comparison

Ratings are relative within this bounded portfolio.

| Criterion | B — Engineer Preview | C — Result Package | N — Maintenance automation |
|---|---|---|---|
| Capability type | Engineering support | Product contract candidate | Engineering support |
| Product value | Medium | High long-term | Medium |
| Engineer/user value | High and immediate | Medium until consumer identified | Medium |
| Time-to-usable-output | Short | Medium/long | Medium |
| Mainline fit | Indirect; observes C# | Direct | Indirect |
| Dual-line fit | High | Medium | High |
| Evidence readiness | High | Medium | Medium-low |
| Implementation effort | Low | Medium/high | Medium |
| Architecture risk | Low | Medium/high | Low/medium |
| Maintenance cost | Low/medium | Medium/high | Medium |
| Scope risk | Low with explicit boundary | Medium due format/API inference | Medium |
| External Domain dependency | None | None, but consumer evidence missing | None |

## Selection

Selected candidate: **Candidate B — Python Engineer Preview v0.1**.

Why selected:

1. It converts already-proven validation into an engineer-usable Windows workflow without changing Product behavior.
2. C# authority and Golden integrity are now durable, removing the main reason Candidate B was previously deferred.
3. It has the shortest path to measurable usable output and no dependency on Rooftop Gate 2.
4. It can surface Result Lineage, Failure Identity, Golden integrity and repeatability without creating a Result Package contract.

Candidate C is deferred until consumer identity, version/compatibility authority and delivery format are separately decided. Candidate N is deferred because its evidenced needs are either included in Candidate B preflight/reporting or lack a distinct bounded Definition of Done.

## Bounded Objective and Definition of Done

Objective: enable a Windows engineer to double-click a controlled launcher that invokes existing C# PVOS authority, runs the existing Python validator and produces a deterministic, human-readable PASS/FAIL/BLOCKED evidence report.

Definition of Done:

1. Launcher works from a governed checkout without requiring Python command construction by the operator.
2. Preflight distinguishes missing prerequisites/input/evidence as BLOCKED.
3. Existing C# CLI remains the only Product result source.
4. Python validator remains comparison/reporting only.
5. Report states PASS/FAIL/BLOCKED, immutable commit, run identity, check summary, evidence reference and actionable error.
6. Repeated unchanged runs produce the same deterministic evidence fingerprint where applicable.
7. Existing 27 C# and 9 Python tests remain green; new launcher/report tests cover success and bounded failure paths.
8. Source/changed-scope audit confirms no Product, Domain, API, UI, Cloud or Canonical capability.

## Authorization Classification

Path: **B — Validation / Engineering Support Short-Track Candidate**.

Portfolio review, planning and queue preparation are authorized. Actual launcher/report implementation requires explicit PM Short-Track Implementation Authorization. This review does not authorize implementation.

