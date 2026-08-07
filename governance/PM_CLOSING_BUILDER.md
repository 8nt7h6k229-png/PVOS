# PM Closing Builder

## Purpose

Generate a deterministic, reviewable Daily Closing Package from complete evidence without performing PM approval, Owner approval, or Daily Governed Closing.

## Responsibility

Validate closing inputs, report missing evidence, and render one PM review package at the executor boundary.

## Information Domain

Handover

## Owner

PM

## Input Contract

The Builder accepts one UTF-8 JSON record containing:

- closing identity and date;
- approved Planning Package identity;
- repository, branch, local HEAD, remote HEAD, and working-tree state;
- one or more ordered Queue Issue evidence records;
- PM Review, Owner Review, and Daily Closing gate states.

Each Issue record requires Issue number, Issue ID, executor status, and one or more durable evidence references.

## Validation Gate

Generation stops before writing output when:

- any mandatory field is missing;
- Planning Package status is not `APPROVED`;
- Issue identity is duplicated or evidence is empty;
- an Issue result is outside `READY_FOR_PM_REVIEW`, `BLOCKED`, `REJECTED`, or `GOVERNANCE_CONFLICT`;
- local and remote HEAD differ;
- the working tree is not `CLEAN`; or
- PM Review, Owner Review, or Daily Closing is represented as already completed by Builder input.

## Output Boundary

Valid input produces a deterministic Markdown package with status `READY_FOR_PM_REVIEW`. The Builder never emits `CLOSED`, never updates source records, and never performs GitHub mutations.

## Usage

```text
python governance/closing_builder/pm_closing_builder.py INPUT.json --output PACKAGE.md
```

## Related Documents

- [Handover Standard](HANDOVER_STANDARD.md)
- [Handover Lifecycle](HANDOVER_LIFECYCLE.md)
- [PM Verification Framework](PM_VERIFICATION_FRAMEWORK.md)
- [Evidence Governance](EVIDENCE_GOVERNANCE.md)

## Status

Implemented — awaiting PM review.
