#!/usr/bin/env python3
"""Validate evidence and render a PM-review Daily Closing Package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


FIELDS = (
    "closing_id", "date", "planning_package_id", "planning_status",
    "repository", "branch", "head", "remote_head", "working_tree",
    "issues", "pm_review", "owner_review", "daily_closing",
)
ISSUE_FIELDS = ("number", "issue_id", "status", "evidence")
ISSUE_STATES = {"READY_FOR_PM_REVIEW", "BLOCKED", "REJECTED", "GOVERNANCE_CONFLICT"}
SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")


class ValidationError(ValueError):
    """Raised when closing evidence is not ready for package generation."""


def validate(data: dict[str, Any]) -> None:
    errors: list[str] = []
    for field in FIELDS:
        if field not in data or data[field] in (None, "", []):
            errors.append(f"{field} is required")
    if errors:
        raise ValidationError("; ".join(errors))
    if data["planning_status"] != "APPROVED":
        errors.append("planning_status must be APPROVED")
    if data["working_tree"] != "CLEAN":
        errors.append("working_tree must be CLEAN")
    if not SHA_PATTERN.fullmatch(str(data["head"])):
        errors.append("head must be a 40-character Git SHA")
    if data["head"] != data["remote_head"]:
        errors.append("head and remote_head must match")
    for gate in ("pm_review", "owner_review", "daily_closing"):
        if data[gate] != "PENDING":
            errors.append(f"{gate} must be PENDING; Builder cannot complete approval gates")
    if not isinstance(data["issues"], list):
        errors.append("issues must be a list")
    else:
        seen_numbers: set[int] = set()
        seen_ids: set[str] = set()
        for index, issue in enumerate(data["issues"], start=1):
            prefix = f"issues[{index}]"
            if not isinstance(issue, dict):
                errors.append(f"{prefix} must be an object")
                continue
            for field in ISSUE_FIELDS:
                if field not in issue or issue[field] in (None, "", []):
                    errors.append(f"{prefix}.{field} is required")
            if any(field not in issue for field in ISSUE_FIELDS):
                continue
            if issue["number"] in seen_numbers or issue["issue_id"] in seen_ids:
                errors.append(f"{prefix} duplicates Issue identity")
            seen_numbers.add(issue["number"])
            seen_ids.add(issue["issue_id"])
            if issue["status"] not in ISSUE_STATES:
                errors.append(f"{prefix}.status is invalid")
            if not isinstance(issue["evidence"], list) or not all(
                isinstance(item, str) and item.strip() for item in issue["evidence"]
            ):
                errors.append(f"{prefix}.evidence must be a non-empty string list")
    if errors:
        raise ValidationError("; ".join(errors))


def render(data: dict[str, Any]) -> str:
    validate(data)
    rows = "\n".join(
        f"| #{item['number']} | {item['issue_id']} | {item['status']} | "
        f"{'<br>'.join(item['evidence'])} |" for item in data["issues"]
    )
    return f"""# PM Daily Closing Package — {data['date']}

## Identity

| Field | Value |
|---|---|
| Closing ID | {data['closing_id']} |
| Planning Package | {data['planning_package_id']} |
| Repository | {data['repository']} |
| Branch | {data['branch']} |
| HEAD / Remote HEAD | `{data['head']}` |
| Working Tree | {data['working_tree']} |

## Queue Evidence

| Issue | Issue ID | Executor Status | Evidence |
|---|---|---|---|
{rows}

## Accountable Gates

| Gate | Status |
|---|---|
| PM Review | PENDING |
| Owner Review | PENDING |
| Daily Governed Closing | PENDING |

## Status

READY_FOR_PM_REVIEW
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        output = render(data)
        args.output.write_text(output, encoding="utf-8")
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"CLOSING_PACKAGE_NOT_GENERATED: {exc}", file=sys.stderr)
        return 2
    print(f"PM_CLOSING_PACKAGE_READY: {data['closing_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
