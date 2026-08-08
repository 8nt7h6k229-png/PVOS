#!/usr/bin/env sh
set -u
if [ "$#" -ne 1 ]; then echo "BLOCKED: supply one governed project JSON input" >&2; exit 2; fi
cd "$(dirname "$0")"
python3 SHORT_TRACK/python/pvos_short_track.py "$1" --repo "$PWD" --output "$PWD/SHORT_TRACK_OUTPUT"
