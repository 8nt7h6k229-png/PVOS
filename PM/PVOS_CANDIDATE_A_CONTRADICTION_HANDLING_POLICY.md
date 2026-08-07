# PVOS Candidate A Contradiction Handling Policy

## Decision Identity

| Field | Value |
|---|---|
| Work Unit | CA-305 — Contradiction Handling Policy |
| PM Decision | PRINCIPLE APPROVED |
| Status | POLICY PERSISTED |
| Corrective Authority | Separate explicit PM／Owner authorization required |

## Mandatory Flow

```text
Contradiction Detected
        ↓
Affected Claim Isolation
        ↓
Preserve Competing Evidence
        ↓
Authority Review
        ↓
PM Disposition
        ↓
Separately Authorized Corrective Work
```

## Required Handling

1. Assign a unique contradiction ID and detection time。
2. Identify the smallest affected claim、scenario、field or contract item。
3. Preserve every competing artifact、Product version、test result、manifest and hash。
4. Block only affected claims and dependent decisions。
5. Route evidence to the correct authority; chronology is not authority。
6. Record PM disposition before corrective work。
7. Create correction only under separate explicit authority。
8. Re-run affected Regression and dependencies; do not expand scope automatically。

## Authority Routing

| Contradiction | Authority Review |
|---|---|
| C# test vs Golden evidence | C# Mainline Product Owner + Validation Reviewer + PM if admitted claim affected |
| C# Runtime vs documented claim | C# Mainline Product Owner + PM claim authority |
| Python validator vs C# result／evidence | Validation Owner + C# Mainline Product Owner |
| Result lineage vs manifest／hash | Integrity Artifact Owner + Evidence Reviewer |
| Two accepted documents conflict | PM／Owner; neither latest date nor file order decides automatically |

## Forbidden

- Silently rewriting expected evidence。
- Changing Golden output to make tests pass。
- Python repairing Product result。
- Assuming the newest artifact is authoritative。
- Deleting failed or superseded evidence。
- Expanding corrective work beyond the affected claim without authority。

## CA-G3 Gap Disposition

`CA-G3-GAP-005 — RESOLVED BY APPROVED CONTRADICTION PRINCIPLE AND PERSISTED POLICY`

