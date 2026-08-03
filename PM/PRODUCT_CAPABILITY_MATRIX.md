# PVOS 1.0 Product Capability Matrix

Status meanings:

- **Existing**: present on a default branch or merged through a PR.
- **Planned**: represented by an open Issue or open PR.
- **Future**: branch-only or proposed by an open architecture/roadmap document; not committed to PVOS 1.0.
- **Not evidenced**: no affirmative GitHub evidence recovered.

| Capability | Existing evidence | Planned evidence | Future evidence | PVOS 1.0 decision |
|---|---|---|---|---|
| 2D points/polygons/rectangles | [PVOS Core](https://github.com/8nt7h6k229-png/PVOS/tree/main/src/PVOS.Core); [Geometry PR #2](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/2) | Geometry Core [issue #1](https://github.com/8nt7h6k229-png/PVOS/issues/1) extends primitives | Computational Geometry [PR #8](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/8) | Included only at existing baseline boundary |
| Local Axis transform | [`AxisTransform.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/AxisTransform.cs), existing imported [design note](https://github.com/8nt7h6k229-png/PvLayoutPlugin/blob/main/src/r5d_src/README_V0.4a-r5c_RoofSetbackLocalAxisFix.txt) | None | Later branch lineage in [PR #1](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/1) | Included at explicit-axis boundary |
| Rectangular layout grid | [`LayoutEngine.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Layout/LayoutEngine.cs) | None | String Break/Layout Block/Placement V2 in [V5.3 branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/v5.3-placement-v2-analyzer) | Included only at current deterministic grid boundary |
| Boundary containment | [PVOS geometry and tests](https://github.com/8nt7h6k229-png/PVOS/tree/main/tests) | None | Advanced solver boundary in [platform branch](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/pvos-platform-bootstrap) | Included at existing test boundary |
| Panel count and installed kWp | [`Domain.cs`](https://github.com/8nt7h6k229-png/PVOS/blob/main/src/PVOS.Core/Domain.cs) | None | Engineering summaries on historical branch | Included |
| AutoCAD product host | [PvLayoutPlugin `main`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main) | Architecture/testing [PRs #6–#7](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pulls) | Product-host evolution described in branch docs | Existing asset; integration with standalone PVOS not claimed |
| AutoCAD geometry conversion | [Adapter PR #3](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/3) | DWG unit normalization [issue #10](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/10) | Additional adapters proposed in PR #6 | Existing conversion boundary included; normalization excluded |
| Roof Detection | None | None | None recovered | Not evidenced; excluded |
| Multi-roof / Roof Region | None on default branches as an approved product baseline | Open historical [PR #1](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/1) | [`bd3ba2f`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/bd3ba2f61b7bd7ea0b81f2565d68908c353c1918) and V5 branch docs | Future; excluded |
| DXF Import | None | None | None recovered | Not evidenced; excluded |
| DXF Export | None | None | None recovered | Not evidenced; excluded |
| DWG unit normalization | None | [Issue #10](https://github.com/8nt7h6k229-png/PvLayoutPlugin/issues/10) | None | Planned; excluded |
| Obstacles/shading/walkways | No evidence in the bounded standalone PVOS core | None | Tagged/branch history indexed by [PM-002 PR #5](https://github.com/8nt7h6k229-png/PVOS/pull/5) | Future; excluded |
| Rule Engine | None on default branch baseline | None | [`ca0bdee`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/ca0bdee227a47cfd5780a39dec7f150d83b6ba53), branch ADR/rule book | Future; excluded |
| Constraint optimization | None | None | [`1352ed5`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/1352ed5d317f2c01b7df9a61fb64657fb26675b3) | Future; excluded |
| Electrical planning | None in bounded PVOS core | None | V5 branch string/MPPT/voltage documents | Future; excluded |
| Construction planning | None | None | V5 branch construction/ladder/cable-tray documents | Future; excluded |
| Runtime dashboard | None | None | [`d1a209b`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/d1a209bcb9013135ed39538a46739733e4c19b8b) | Future; excluded |
| Placement Engine V2 | None | None | [`2298448`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/229844818d76295ef8c95659bfa0d8e7ae815518), [`9dc296b`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/commit/9dc296bd20e94a21acbabb805c4b0342d474866d) | Future; excluded |
| Golden Dataset / validation platform | No approved default-branch product baseline | Testing [PR #7](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/7) | [platform bootstrap](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/feature/pvos-platform-bootstrap) | Planned/Future support capability; excluded from MVP |
| AI Studio / Repository Intelligence | [AIStudio `main`](https://github.com/8nt7h6k229-png/PvLayoutPlugin/tree/main/AIStudio), merged PRs #9 and #17–#21 | Open issue cleanup remains | AI-assisted product planning only proposed in PR #6 | Existing internal engineering support; not an end-user MVP capability |
| Steel / Cloud / Web products | None | Open architecture PR only | [PR #6](https://github.com/8nt7h6k229-png/PvLayoutPlugin/pull/6) names these future families | Future; excluded |

## Product-state summary

| Question | Answer |
|---|---|
| What is PVOS 1.0? | The bounded existing deterministic 2D PV placement baseline defined in [PRODUCT_BASELINE.md](PRODUCT_BASELINE.md). |
| What is included? | Explicit partition and Local Axis, module parameters, rectangular contained placement, result summary, existing core/test assets, and recognition of the existing AutoCAD host/adapter boundary. |
| What is excluded? | All not-evidenced, open/planned, or branch-only advanced capabilities listed above. |
| What is MVP? | The caller-supplied-partition → Local Axis → deterministic grid → contained panels workflow in [MVP_DEFINITION.md](MVP_DEFINITION.md). |
| What is Product Complete? | The governed approval/validation/release state defined in [PRODUCT_BASELINE.md](PRODUCT_BASELINE.md); it is not yet achieved. |
