# Python Short-Track v0.1 Operator Guide

## Use

1. Copy `SHORT_TRACK_INPUT/project-input-template.json`, rename the copy for the case, and replace every `OWNER_TO_SUPPLY` value. Do not edit validator files or label synthetic/Golden data as a real case.
2. Windows: drag the JSON onto `PVOS-Python-Short-Track-v0.1.bat`.
3. Linux: run `./PVOS-Python-Short-Track-v0.1.sh path/to/input.json`.
4. Review `SHORT_TRACK_OUTPUT/LATEST.md` and `LATEST.json`.
5. Confirm each partition's Local Axis, orientation, count and corners against the manual/CAD reference before submitting evidence.

## Limitations

No DWG/DXF parser, axis inference, geometry repair, obstacles, walkways, shading, electrical, structural, optimization, UI or formal Product result. Concave boundaries are supported only through complete rectangle containment. Edge margin is explicit, not derived. Python is a rapid experiment; C# remains authority.

The JSON adapter is an experimental response to `GAP-017`. It does not establish CAD-to-JSON, DXF/DWG import, project persistence, or a permanent PVOS input architecture.

## Real-case evidence requirements

Record lawful provenance/de-identification, reference tool/manual method, expected count, orientation, per-partition behavior and reviewer. Without these, execution may be technical evidence but is not PM Short-Track acceptance evidence.
