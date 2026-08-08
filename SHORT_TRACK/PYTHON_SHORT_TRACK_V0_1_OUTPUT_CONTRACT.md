# Python Short-Track v0.1 Output Contract

Each execution writes identity-addressed and `LATEST` JSON/Markdown reports under `SHORT_TRACK_OUTPUT/`. JSON includes case identity, `PASS/BLOCKED`, each partition's axis/module inputs, ordered placement rectangles, per-partition/total counts, warnings, blocked reasons, input hash, source commit, rule sources and authority disclaimer.

Exit meanings: `0 PASS`, `1 FAIL` (reserved for contradictory executed evidence), `2 BLOCKED` (input/environment cannot produce an honest result). Output is Engineering Preview evidence only.
