#!/usr/bin/env python3
"""Validate a Daily Planning Package and publish its GitHub Issue queue."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any, Callable


PACKAGE_FIELDS = ("package_id", "date", "status", "approved_by", "repository", "issues")
ISSUE_FIELDS = (
    "issue_id",
    "title",
    "capability_ids",
    "objective",
    "scope",
    "out_of_scope",
    "deliverables",
    "acceptance_criteria",
    "required_evidence",
    "dependencies",
    "status",
)
NONEMPTY_LIST_FIELDS = (
    "capability_ids",
    "scope",
    "out_of_scope",
    "deliverables",
    "acceptance_criteria",
    "required_evidence",
)
REPOSITORY_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class ValidationError(ValueError):
    """Raised when a package cannot be admitted to publication."""


class PublicationError(RuntimeError):
    """Raised when GitHub fails after publication has started."""

    def __init__(self, message: str, created: list[dict[str, Any]]):
        super().__init__(message)
        self.created = created


def _is_nonempty(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value)
    return value is not None


def validate_package(package: dict[str, Any], repository_override: str | None = None) -> None:
    errors: list[str] = []
    for field in PACKAGE_FIELDS:
        if field not in package or not _is_nonempty(package[field]):
            errors.append(f"package.{field} is required")

    if errors:
        raise ValidationError("; ".join(errors))
    if package["status"] != "APPROVED":
        errors.append("package.status must be APPROVED")
    if not DATE_PATTERN.fullmatch(package["date"]):
        errors.append("package.date must use YYYY-MM-DD")
    if not REPOSITORY_PATTERN.fullmatch(package["repository"]):
        errors.append("package.repository must use owner/name")
    if repository_override and repository_override != package["repository"]:
        errors.append("command repository does not match package.repository")
    if not isinstance(package["issues"], list):
        errors.append("package.issues must be a list")
    if errors:
        raise ValidationError("; ".join(errors))

    seen: set[str] = set()
    for index, issue in enumerate(package["issues"], start=1):
        prefix = f"issues[{index}]"
        if not isinstance(issue, dict):
            errors.append(f"{prefix} must be an object")
            continue
        for field in ISSUE_FIELDS:
            if field not in issue:
                errors.append(f"{prefix}.{field} is required")
        if any(field not in issue for field in ISSUE_FIELDS):
            continue
        for field in ("issue_id", "title", "objective", "status"):
            if not isinstance(issue[field], str) or not issue[field].strip():
                errors.append(f"{prefix}.{field} must be a non-empty string")
        for field in NONEMPTY_LIST_FIELDS:
            if not isinstance(issue[field], list) or not issue[field] or not all(
                isinstance(item, str) and item.strip() for item in issue[field]
            ):
                errors.append(f"{prefix}.{field} must be a non-empty string list")
        if not isinstance(issue["dependencies"], list) or not all(
            isinstance(item, str) and item.strip() for item in issue["dependencies"]
        ):
            errors.append(f"{prefix}.dependencies must be a string list")
            dependencies: list[str] = []
        else:
            dependencies = issue["dependencies"]
        issue_id = issue["issue_id"]
        if issue_id in seen:
            errors.append(f"{prefix}.issue_id duplicates {issue_id}")
        if issue["status"] != "READY":
            errors.append(f"{prefix}.status must be READY")
        for dependency in dependencies:
            if dependency == issue_id:
                errors.append(f"{prefix} cannot depend on itself")
            elif dependency not in seen:
                errors.append(f"{prefix}.dependencies references missing or later Issue {dependency}")
        seen.add(issue_id)

    if errors:
        raise ValidationError("; ".join(errors))


def render_issue_body(
    package: dict[str, Any], issue: dict[str, Any], resolved: dict[str, dict[str, Any]]
) -> str:
    def bullets(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items)

    dependencies = []
    for dependency in issue["dependencies"]:
        published = resolved.get(dependency)
        dependencies.append(
            f"{dependency} — #{published['number']}" if published else dependency
        )
    dependency_text = bullets(dependencies) if dependencies else "- None"
    return f"""## Source
{package['package_id']} — APPROVED — {package['date']} — Approved by {package['approved_by']}

## Queue Identity
- Issue ID: {issue['issue_id']}
- Queue Status: {issue['status']}
- Order: {package['issues'].index(issue) + 1}

## Capability
{bullets(issue['capability_ids'])}

## Objective
{issue['objective']}

## Dependencies
{dependency_text}

## Scope
{bullets(issue['scope'])}

## Out of Scope
{bullets(issue['out_of_scope'])}

## Deliverables
{bullets(issue['deliverables'])}

## Acceptance Criteria
{bullets(issue['acceptance_criteria'])}

## Required Evidence
{bullets(issue['required_evidence'])}

## Execution Control
This GitHub Issue is the sole Execution Source for Codex. Stop at `READY_FOR_PM_REVIEW`; PM owns review and closing.
"""


def _github_create(repository: str, title: str, body: str) -> dict[str, Any]:
    command = [
        "gh",
        "api",
        "--method",
        "POST",
        f"/repos/{repository}/issues",
        "-f",
        f"title={title}",
        "-f",
        f"body={body}",
        "--jq",
        "{number: .number, url: .html_url, title: .title}",
    ]
    completed = subprocess.run(
        command, check=True, capture_output=True, text=True, encoding="utf-8"
    )
    return json.loads(completed.stdout)


def _github_find(repository: str, issue_id: str) -> dict[str, Any] | None:
    command = [
        "gh",
        "issue",
        "list",
        "--repo",
        repository,
        "--state",
        "all",
        "--limit",
        "100",
        "--json",
        "number,url,title,body",
    ]
    completed = subprocess.run(
        command, check=True, capture_output=True, text=True, encoding="utf-8"
    )
    needle = f"- Issue ID: {issue_id}"
    matches = [
        issue for issue in json.loads(completed.stdout) if needle in (issue.get("body") or "")
    ]
    if len(matches) > 1:
        raise RuntimeError(f"multiple existing Issues found for {issue_id}")
    return matches[0] if matches else None


def build_queue(
    package: dict[str, Any],
    publish: bool = False,
    creator: Callable[[str, str, str], dict[str, Any]] = _github_create,
    finder: Callable[[str, str], dict[str, Any] | None] = _github_find,
) -> dict[str, Any]:
    validate_package(package)
    created: list[dict[str, Any]] = []
    resolved: dict[str, dict[str, Any]] = {}
    for issue in package["issues"]:
        body = render_issue_body(package, issue, resolved)
        entry: dict[str, Any] = {
            "issue_id": issue["issue_id"],
            "title": issue["title"],
            "capability_ids": issue["capability_ids"],
            "dependencies": issue["dependencies"],
            "body": body,
        }
        if publish:
            try:
                existing = finder(package["repository"], issue["issue_id"])
                result = existing or creator(package["repository"], issue["title"], body)
            except Exception as exc:
                raise PublicationError(
                    f"publication failed for {issue['issue_id']}: {exc}", created
                ) from exc
            entry.update(result)
            entry["reused"] = existing is not None
            resolved[issue["issue_id"]] = entry
        created.append(entry)
    return {
        "package_id": package["package_id"],
        "repository": package["repository"],
        "status": "QUEUE_READY" if publish else "DRY_RUN",
        "issues": created,
    }


def select_daily_package(packages_dir: Path, package_date: str) -> tuple[Path, dict[str, Any]]:
    """Select exactly one approved Daily Planning Package for a governed date."""
    if not DATE_PATTERN.fullmatch(package_date):
        raise ValidationError("automatic date must use YYYY-MM-DD")
    candidates: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(packages_dir.glob("*_daily_planning_package.json")):
        try:
            package = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValidationError(f"cannot read Daily Planning Package {path}: {exc}") from exc
        if package.get("date") == package_date and package.get("status") == "APPROVED":
            validate_package(package)
            candidates.append((path, package))
    if not candidates:
        raise ValidationError(
            f"no approved Daily Planning Package found for {package_date} in {packages_dir}"
        )
    if len(candidates) > 1:
        names = ", ".join(path.name for path, _package in candidates)
        raise ValidationError(
            f"multiple approved Daily Planning Packages found for {package_date}: {names}"
        )
    return candidates[0]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", nargs="?", type=Path, help="Approved Daily Planning Package JSON")
    parser.add_argument("--repository", help="Must match package.repository when supplied")
    parser.add_argument("--publish", action="store_true", help="Create Issues through GitHub API")
    parser.add_argument("--output", type=Path, help="Write Queue Ready JSON")
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Select today's unique approved package, publish it, and write Queue Ready evidence",
    )
    parser.add_argument("--date", help="Governed date for --auto; defaults to the local date")
    parser.add_argument(
        "--packages-dir",
        type=Path,
        default=Path(__file__).parent / "packages",
        help="Directory searched by --auto",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        if args.auto and args.package:
            raise ValidationError("use either PACKAGE.json or --auto, not both")
        if args.date and not args.auto:
            raise ValidationError("--date requires --auto")
        if args.packages_dir != Path(__file__).parent / "packages" and not args.auto:
            raise ValidationError("--packages-dir requires --auto")
        if args.auto:
            governed_date = args.date or date.today().isoformat()
            _package_path, package = select_daily_package(args.packages_dir, governed_date)
            publish = True
            output = args.output or args.packages_dir / f"{governed_date}_issue_queue_ready.json"
        else:
            if not args.package:
                raise ValidationError("PACKAGE.json or --auto is required")
            package = json.loads(args.package.read_text(encoding="utf-8"))
            publish = args.publish
            output = args.output
        validate_package(package, args.repository)
        queue = build_queue(package, publish=publish)
    except (OSError, json.JSONDecodeError, ValidationError, PublicationError) as exc:
        print(f"QUEUE_NOT_PUBLISHED: {exc}", file=sys.stderr)
        if isinstance(exc, PublicationError) and exc.created:
            print(json.dumps({"created_before_failure": exc.created}, indent=2), file=sys.stderr)
        return 2

    rendered = json.dumps(queue, indent=2, ensure_ascii=False)
    if output:
        output.write_text(rendered + "\n", encoding="utf-8")
    print(f"{queue['status']}: {queue['package_id']} ({len(queue['issues'])} Issues)")
    for item in queue["issues"]:
        suffix = f" #{item['number']} {item['url']}" if "number" in item else ""
        print(f"- {item['issue_id']}: {item['title']}{suffix}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
