# Daily Improvement Loop

## Purpose

Implement Owner-approved GVR-010 by converting daily evidence into traceable improvement findings without silently changing governance or expanding scope.

## Responsibility

Define improvement inputs, classification, review, authorization, carry-over, and evidence closure.

## Information Domain

Governance

## Owner

PM

## Loop

```text
Completed work, gaps, incidents, review and closing evidence
        ↓
Evidence inventory
        ↓
Keep / Problem / Improve classification
        ↓
PM review and accountable disposition
        ↓
Authorized Planning Package carry-over or no action
        ↓
Later evidence confirms outcome
```

## Improvement Record

| Field | Requirement |
|---|---|
| Improvement ID | Unique daily identifier |
| Date | Evidence date |
| Classification | Keep, Problem, or Improve |
| Evidence | Durable source references |
| Finding | Factual observation only |
| Impact | Observed governance or execution effect |
| Proposed Action | Bounded candidate action; not authorization |
| Owner | Accountable reviewer |
| Disposition | Pending, Accepted for Planning, Rejected, or No Action |
| Carry Over | Planning Package reference when accepted |
| Closure Evidence | Later evidence of the disposition outcome |

## Controls

- Evidence is inventoried before a finding is recorded.
- Findings do not create rules, Issues, architecture, product scope, or execution authority.
- PM reviews every proposed action; Owner approval remains required where governing sources require it.
- Accepted action enters a later approved Planning Package before EOS-017 publication.
- Rejected and no-action findings remain retained as evidence.
- Carry-over preserves the original evidence and disposition; it does not imply completion.

## Related Documents

- [Governance Rules Registry](GOVERNANCE_RULES_REGISTRY.md)
- [Evidence Governance](EVIDENCE_GOVERNANCE.md)
- [Planning Package Governance](PLANNING_PACKAGE_GOVERNANCE.md)
- [PM Closing Builder](PM_CLOSING_BUILDER.md)
- [Development Constitution — Continuous Improvement](../DEVELOPMENT_CONSTITUTION.md#12-continuous-improvement)

## Status

GVR-010 implementation established — awaiting PM review.
