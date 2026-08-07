# Workspace Registry

## Purpose

Register governed workspaces and their authoritative references.

## Responsibility

Maintain the unique inventory of governed workspaces.

## Information Domain

Workspace

## Owner

PM

## Update Trigger

A governed workspace is registered, changed, superseded, or retired.

## Registry Schema

| Field | Meaning |
|---|---|
| Workspace ID | Unique governed workspace identifier |
| Name | Human-readable workspace name |
| Repository | Authoritative GitHub repository identity |
| Local Reference | Verified local working reference; not a portable architecture requirement |
| Owner | Accountable workspace owner |
| Status | Current governed registration status |
| Evidence | Repository identity and verification evidence |

## Registered Workspaces

| Workspace ID | Name | Repository | Local Reference | Owner | Status | Evidence |
|---|---|---|---|---|---|---|
| WS-001 | Governed PVOS Repository | `8nt7h6k229-png/PVOS` | `C:\Users\C00160\Documents\Codex\2026-08-03\vu04y94\work\PVOS` | PM | Active | Git root and `origin` verified on 2026-08-07 at recovery baseline `7a0bf0011c59466cc302db8615ee95ff1b088d99` |

## Verification and Boundaries

- `WS-001` is the only workspace authorized by DPP-2026-08-07-R2 as the current governed PVOS Repository target.
- The local reference records observed evidence only; it does not require another executor or machine to use the same local path.
- `C:\PV_GitHub` is an inspected asset-collection directory, not one Git Repository, and is therefore not registered as a governed workspace.
- No repository, directory, branch policy, or workspace architecture was created, moved, renamed, or restructured by this registration.

## Related Documents

- [Governance File Registry](GOVERNANCE_FILE_REGISTRY.md)
- [Governance Information Architecture](GOVERNANCE_INFORMATION_ARCHITECTURE.md)
- [AIStudioCore Handover](AISTUDIOCORE_HANDOVER.md)

## Status

Registry populated with one verified governed workspace — awaiting PM verification.
