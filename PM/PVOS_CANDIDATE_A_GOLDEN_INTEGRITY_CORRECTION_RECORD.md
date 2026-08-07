# PVOS Candidate A Golden Integrity Correction Record

## Decision Identity

| Field | Value |
|---|---|
| Authority | Owner / PM Governance Stop Recovery |
| Affected Golden IDs | PVOS-GOLDEN-004 through PVOS-GOLDEN-008 |
| Recovery classification | D — line-ending normalization |
| Status | RECOVERY VALIDATED — READY TO RESUME CLOSING |
| Admission record | `PM/PVOS_CANDIDATE_A_GOLDEN_ADMISSION_RECORD.md` |
| Merged evidence commit | `917ea7242d5da62c292beb5a155a07ca78c17e6b` |

## Root Cause and Provenance

Git stores all ten affected input/output assets with LF bytes. Every registered SHA-256 exactly matches its `HEAD` Git blob. Windows system Git configuration has `core.autocrlf=true`; after merge and checkout, the worktree materialized those newly tracked assets with CRLF. The content model, C# expected-result source, bounded claim, Git blob, and registry did not change.

`git ls-files --eol` evidence before correction: `i/lf w/crlf attr/` for all ten assets. No `.gitattributes` policy existed.

## Integrity Inventory

| Golden | Asset | Registered / admitted Git-blob SHA-256 | Pre-correction worktree SHA-256 | Git blob |
|---|---|---|---|---|
| 004 | input | `67E48C5948454CF3C80EEFC047B54B2C5C27136A97BAF0E4BE5794828740C6E5` | `69873F68A70233DA6158C6686104A226AEB377A0A9D5C6EF7FC9031194D5D7E8` | `df984ed6432697ce1955d49a4ac2858d1162b289` |
| 004 | output | `A145A13FC71F9B96C4140C71B339D1E652234DA3CF015CC854E64463731FFA8C` | `034CCAC839EA83D1BE4A91D44FB2D1705903C1955A270B03F3A186FBDD63CB29` | `54e0eb4b3c6ec091a84f4f5078aa8fe5424bc9ca` |
| 005 | input | `6EF22D6EE4F164A3402A01D91A3002584FB573192ECFAF35BD5553651A77455F` | `39E8A2C52CAAE8E10315D10C2E0C6CA6510A40155672C7016F1E70389501588B` | `a7a191a8c28b05ab0b1cd924afdd0a5834dc5f4d` |
| 005 | output | `41E294D16F2007565C6667736CED1262714B16EA1D7E7C20873D7BFBF2FBB3D0` | `5E309CB08C753FB2AC78C14909E1DEF90E09EC9982F8DA9C129637A1F83AE48E` | `add989a7518d89e7491fd484d192e7458e852507` |
| 006 | input | `A3EA9FFAA7E1F8514D0ABDAA832041BFD2AE4D3EB660569F1C6FD7B7A6C0F746` | `5FAF5363C3279296D56E80AAC60A0C459925B06223F15ED8B19C841DA7FD5C08` | `88ecc7fbef714358c302f84b2d71c0fe73e3d234` |
| 006 | output | `B5AB42978A7AB63057546BE44F20E342BDCFC869920A88DE806BEC7E6874060A` | `882E84880E4043164E5D173C1DB42593CD4870405155B72B27D97E5CEE543C97` | `bc9fd12b33266d63dbdc1235bc8e1f9f714248d6` |
| 007 | input | `C66A656840614764A40574AF490A05E9BD8785F64FF8D59E8584B5C243C4931E` | `DFAD8D8DD6A8E15D48F43CEA818872E6B8F06F43F308EC847A893B3B25DCD177` | `5ae6f4acd60b48c1d0b177eab2d34eb06e6b204e` |
| 007 | output | `8E9A23C11537AA5199AE38D41502C2E06D69EAD40FEEE6254CD6A9FDBE921626` | `797A848A4DACFD8C0F533C2104250574D076637F89EA0E7C4ABBCF31F6E1443B` | `4a66861a2b88e98d3498efa5f691c51f0c76dbe0` |
| 008 | input | `76951BD19A8712BE574501196AB89E9A3EA40BFA1CDBCC2826C1ECC2F351DDC3` | `95ED0191C61D489DCFC065B0B8B0932CE42CEE584182224B5FF11E354B44E3C3` | `3f8cd500b2db27fdfdbe3c2e8b670b589fdac9d8` |
| 008 | output | `C6E6A847957433E5F655766DE6816E88118FC674495C5D31235306A4B21DAA4C` | `DCE0A26F2A1CCF80F7DEDFE7871DBE962BD82FC9A824B063C9F0A95C51DB568F` | `6ae7b7ca08cbf6709814c8567eb8ebacb863ffd2` |

## Authority / Provenance Determination

| Golden | Admitted asset | Registry corresponds to admitted blob | Current merged blob authoritative | Result |
|---|---|---|---|---|
| PVOS-GOLDEN-004 | identified | yes | yes | EVIDENCED |
| PVOS-GOLDEN-005 | identified | yes | yes | EVIDENCED |
| PVOS-GOLDEN-006 | identified | yes | yes | EVIDENCED |
| PVOS-GOLDEN-007 | identified | yes | yes | EVIDENCED |
| PVOS-GOLDEN-008 | identified | yes | yes | EVIDENCED |

Expected-result authority and bounded-claim sources remain the admitted C# tests, regression comparisons, manifest claims, and Golden Admission Record. No authoritative sources conflict.

## Controlled Correction

The correction adds targeted `.gitattributes` rules fixing only Golden 004–008 JSON checkout representation to `text eol=lf`. It restores the already-admitted Git-blob bytes in the worktree. Registry hashes and scenario assets in Git are not changed.

- Before hash: the ten pre-correction worktree hashes listed above.
- After hash: each registered/admitted SHA-256 listed above.
- Source authority: PM Golden Admission Record plus exact merged Git blobs.
- Bounded claims unchanged: YES.
- Product behavior unchanged: YES.
- Re-admission required: NO.
- Product Scope changed: NO.

## Retained Boundary

C#/.NET remains Product Behavior Authority. Python validates only. No expected result, Product behavior, Domain capability, Legacy/Canonical asset, API, UI, Cloud, or PVOS Scope is introduced.

## Final Validation

| Check | Result |
|---|---|
| Release Build | PASS — 0 warnings, 0 errors |
| C# tests | PASS — 27/27 |
| Python tests | PASS — 9/9 |
| Golden 001–008 | PASS — all registered asset hashes and bounded C# regression results match |
| Repeatability | PASS — 3/3 identical fingerprints |
| Repeatability fingerprint | `488C0D2AB5748FD9B1FB5909E0EBB5AD1D7730E1AFFAD468C4C04FDAAC2805A6` |
| Result Lineage | PASS — Candidate A integrity test included in 27/27 |
| Failure Identity | PASS — Candidate A integrity test included in 27/27 |

Validation evidence commit: `75c18575bb8a470a34965a805874e7fb9034cf70`.

Final recommendation: `RESUME_CANDIDATE_A_CLOSING`.
