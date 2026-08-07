#!/usr/bin/env python3
"""Engineer-facing orchestration around the existing C# evidence validator."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable

import validate

PREVIEW_VERSION = "0.1"
REQUIRED_PATHS = (Path("PVOS.sln"), Path("src/PVOS.Cli/PVOS.Cli.csproj"), Path("VALIDATION/golden-dataset-v1.json"))


def preflight(repo_root: Path) -> list[str]:
    if not repo_root.is_dir():
        return [f"Governed repository root does not exist: {repo_root}"]
    problems = [f"Required governed asset is missing: {path}" for path in REQUIRED_PATHS if not (repo_root / path).is_file()]
    problems.extend(f"Required executable is unavailable on PATH: {name}" for name in ("git", "dotnet") if shutil.which(name) is None)
    return problems


def resolve_head(repo_root: Path) -> str | None:
    result = subprocess.run(["git", "-C", str(repo_root), "rev-parse", "HEAD"], capture_output=True, text=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else None


def blocked_report(problems: list[str]) -> dict[str, Any]:
    return {"preview": "PVOS Python Engineer Preview", "version": PREVIEW_VERSION, "result": "BLOCKED", "evidence_commit": None,
            "report_identity": "BLOCKED-PREFLIGHT", "summary": "Prerequisite or governed evidence preflight did not pass.",
            "problems": problems, "validation": None}


def preview_report(validation_report: dict[str, Any]) -> dict[str, Any]:
    result = validation_report["result"]
    fingerprint = validation_report["report_fingerprint"]
    summaries = {
        "PASS": "Approved evidence and the existing C# result matched all bounded checks.",
        "FAIL": "At least one bounded evidence check did not match the approved baseline.",
        "BLOCKED": "Validation could not complete because required evidence or tooling was unavailable.",
    }
    return {"preview": "PVOS Python Engineer Preview", "version": PREVIEW_VERSION, "result": result,
            "evidence_commit": validation_report["evidence_commit"], "report_identity": f"PEP-{fingerprint[:16]}",
            "summary": summaries[result], "problems": [f"{c['check_id']}: {c['actual']}" for c in validation_report["checks"] if c["result"] != "PASS"],
            "validation": validation_report}


def markdown(report: dict[str, Any]) -> str:
    lines = ["# PVOS Python Engineer Preview v0.1 Report", "", f"**{report['result']}**", "",
             f"- Report Identity: `{report['report_identity']}`", f"- Evidence Commit: `{report['evidence_commit'] or 'UNAVAILABLE'}`",
             f"- Summary: {report['summary']}", ""]
    if report["problems"]:
        lines += ["## Action Required", "", *[f"- {item}" for item in report["problems"]], ""]
    validation_report = report.get("validation")
    if validation_report:
        lines += ["## Checks", "", "| Check | Result | Actual |", "|---|---|---|"]
        for check in validation_report["checks"]:
            actual = str(check["actual"]).replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {check['check_id']} | {check['result']} | {actual} |")
        repeatability = validation_report.get("repeatability")
        if repeatability:
            lines += ["", "## Repeatability", "", f"- Result: {repeatability['result']}", f"- Runs: {repeatability['runs']}",
                      f"- All fingerprints match: {repeatability['all_fingerprints_match']}"]
    lines += ["", "## Authority Boundary", "",
              "C#/.NET is the sole Product Behavior Authority. Python performs validation, orchestration and evidence reporting only.", ""]
    return "\n".join(lines)


def write_reports(output_dir: Path, report: dict[str, Any]) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    identity = report["report_identity"]
    json_path, markdown_path = output_dir / f"{identity}.json", output_dir / f"{identity}.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    rendered = markdown(report)
    markdown_path.write_text(rendered, encoding="utf-8")
    (output_dir / "LATEST.md").write_text(rendered, encoding="utf-8")
    return json_path, markdown_path


def execute(repo_root: Path, output_dir: Path, repeatability_runs: int,
            runner: Callable[[Path, str], dict[str, Any]] = validate.run_validation) -> tuple[int, dict[str, Any], tuple[Path, Path]]:
    repo_root = repo_root.resolve()
    problems = preflight(repo_root)
    commit = resolve_head(repo_root) if not problems else None
    if commit is None and not problems:
        problems.append("Current immutable Git commit could not be resolved.")
    if problems:
        report = blocked_report(problems)
    else:
        runs = [runner(repo_root, commit) for _ in range(repeatability_runs)]
        validation_report = runs[-1]
        validation_report["repeatability"] = validate.repeatability_summary(runs)
        if validation_report["repeatability"]["result"] == "FAIL":
            validation_report["result"] = "FAIL"
        report = preview_report(validation_report)
    paths = write_reports(output_dir, report)
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[report["result"]], report, paths


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the bounded PVOS Python Engineer Preview.")
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--repeatability-runs", type=int, default=3)
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    if args.repeatability_runs < 1:
        parser.error("--repeatability-runs must be at least 1")
    code, report, paths = execute(args.repo_root, args.output_dir, args.repeatability_runs)
    print(f"[{report['result']}] {report['summary']}")
    print(f"Report Identity: {report['report_identity']}")
    print(f"Human-readable report: {paths[1]}")
    print(f"Machine-readable report: {paths[0]}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
