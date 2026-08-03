# Demo-001 Input

Demo-001 exercises one complete approved deterministic layout request. The executable definition is in [`src/PVOS.Cli/Program.cs`](../src/PVOS.Cli/Program.cs).

| Contract field | Value |
|---|---|
| Placement request | `LAYOUT-REQ-001` |
| Geometry request | `GEO-REQ-001` |
| Geometry set | `GEO-SET-001` |
| Coordinate system | `GLOBAL` |
| Linear unit | `mm` |
| Roof | `ROOF-001` rectangle: `(0,0)`, `(6000,0)`, `(6000,4000)`, `(0,4000)` |
| Selected partition | `PART-001`, equal to the roof boundary |
| Local Axis | `AXS-001`, origin `(0,0)`, rotation `0` degrees |
| Module | `MOD-001` |
| Physical width | `1000 mm` |
| Physical length | `1500 mm` |
| Orientation | `WidthAlongLocalX` |
| Column gap | `100 mm` |
| Row gap | `100 mm` |
| Edge margin | `200 mm` |
| Rated power | `500 Wp` |

Run from the repository root:

```powershell
dotnet run --project .\src\PVOS.Cli\PVOS.Cli.csproj --configuration Release
```

No file import, JSON adapter, UI, rendering, DXF, or export behavior is used.
