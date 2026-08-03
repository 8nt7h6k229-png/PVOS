# Demo-001 Summary

## Result at a glance

- **Roof boundary:** `ROOF-001`, `6000 x 4000 mm`
- **Selected partition:** `PART-001`, same extent as the roof
- **Local Axis:** origin `(0,0)`, rotation `0°`
- **Accepted panels:** `10`, ordered `PNL-000001` through `PNL-000010`
- **Installed capacity:** `5.000 kWp`
- **Placement warnings:** none
- **Placement status:** `Accepted`

## Interpretation

The approved engine placed two rows of five panels. The 100 mm column and row gaps and 200 mm edge margin are visible. Every panel lies inside the selected partition and retains the ENG-001 order. No optimization or manual placement adjustment was applied.

## Evidence chain

`ENG-001 LayoutRequest` -> executable `LayoutResult` -> [`demo-output.json`](demo-output.json) -> [`demo-output.svg`](demo-output.svg) and [`demo-output.png`](demo-output.png)

The visual context uses [`demo-input.json`](demo-input.json) for the roof, selected partition, and Local Axis. Result geometry and statistics come from the executable output. JSON is a static evidence format only; no JSON adapter was implemented.
