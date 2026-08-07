#!/usr/bin/env python3
"""PVOS Python Validation Product v0.1.

This validator observes the existing C# CLI and committed Golden evidence. It
does not implement or calculate PVOS Product behavior.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


MANIFEST_PATH = Path("VALIDATION/golden-dataset-v1.json")
CHECK_IDS = tuple(f"PVPY-{number:03d}" for number in range(1, 9))


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_newlines(value: str) -> str:
    return value.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def panel_ids(cli_output: str) -> list[str]:
    return re.findall(r"^\s+(PNL-\d{6})\s+order=", cli_output, re.MULTILINE)


def registered_json_paths(manifest: dict[str, Any] | None) -> list[Path]:
    if manifest is None:
        return [Path("DEMO/demo-input.json"), Path("DEMO/demo-output.json")]
    paths = [Path(asset["path"]) for asset in manifest.get("assets", []) if Path(asset["path"]).suffix.lower() == ".json"]
    return list(dict.fromkeys(paths))


def check_record(
    check_id: str,
    result: str,
    expected: str,
    actual: str,
    evidence: list[str],
) -> dict[str, Any]:
    return {
        "check_id": check_id,
        "result": result,
        "expected": expected,
        "actual": actual,
        "evidence": evidence,
    }


def overall_result(checks: list[dict[str, Any]]) -> str:
    results = {check["result"] for check in checks}
    if "FAIL" in results:
        return "FAIL"
    if "BLOCKED" in results:
        return "BLOCKED"
    return "PASS"


def run_validation(repo_root: Path, evidence_commit: str) -> dict[str, Any]:
    started_at = utc_now()
    repo_root = repo_root.resolve()
    manifest_file = repo_root / MANIFEST_PATH
    checks: list[dict[str, Any]] = []
    risks = [
        "Demo-001 covers one bounded deterministic scenario only.",
        "Static JSON and presentation assets are review evidence, not runtime adapters or UI.",
        "PASS is validation evidence and does not perform PM Product Acceptance.",
    ]

    manifest: dict[str, Any] | None = None
    manifest_error: str | None = None
    try:
        manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        manifest_error = str(exc)

    required_paths: list[Path] = [
        MANIFEST_PATH,
        Path("src/PVOS.Cli/PVOS.Cli.csproj"),
        Path("DEMO/DEMO-001_OUTPUT.txt"),
        Path("DEMO/demo-input.json"),
        Path("DEMO/demo-output.json"),
    ]
    if manifest is not None:
        required_paths.extend(Path(asset["path"]) for asset in manifest.get("assets", []))
    required_paths = list(dict.fromkeys(required_paths))
    missing = [str(path) for path in required_paths if not (repo_root / path).is_file()]
    checks.append(
        check_record(
            "PVPY-001",
            "PASS" if not missing and manifest_error is None else "BLOCKED",
            "All bounded input paths resolve and the manifest is readable",
            "all required paths resolved" if not missing and manifest_error is None else f"missing={missing}; manifest_error={manifest_error}",
            [str(MANIFEST_PATH), *[str(path) for path in required_paths]],
        )
    )

    git = shutil.which("git")
    if git is None:
        commit_result = check_record(
            "PVPY-002", "BLOCKED", "One immutable Git commit resolves", "git executable unavailable", ["git cat-file -e <commit>^{commit}"]
        )
    else:
        resolved = subprocess.run(
            [git, "-C", str(repo_root), "cat-file", "-e", f"{evidence_commit}^{{commit}}"],
            capture_output=True,
            text=True,
            check=False,
        )
        commit_result = check_record(
            "PVPY-002",
            "PASS" if resolved.returncode == 0 else "BLOCKED",
            "One immutable Git commit resolves",
            evidence_commit if resolved.returncode == 0 else normalize_newlines(resolved.stderr),
            [f"git cat-file -e {evidence_commit}^{{commit}}"],
        )
    checks.append(commit_result)

    cli_output: str | None = None
    dotnet = shutil.which("dotnet")
    cli_project = repo_root / "src/PVOS.Cli/PVOS.Cli.csproj"
    cli_command = [
        dotnet or "dotnet",
        "run",
        "--project",
        str(cli_project),
        "--configuration",
        "Release",
        "--no-build",
    ]
    if dotnet is None or not cli_project.is_file():
        cli_check = check_record(
            "PVPY-003", "BLOCKED", "Existing Release CLI exits with code 0", "dotnet or CLI project unavailable", [" ".join(cli_command)]
        )
    else:
        completed = subprocess.run(cli_command, cwd=repo_root, capture_output=True, text=True, check=False)
        cli_output = completed.stdout if completed.returncode == 0 else None
        actual = f"exit_code={completed.returncode}"
        if completed.stderr:
            actual += f"; stderr={normalize_newlines(completed.stderr)}"
        cli_check = check_record(
            "PVPY-003",
            "PASS" if completed.returncode == 0 else "FAIL",
            "Existing Release CLI exits with code 0",
            actual,
            [" ".join(cli_command)],
        )
    checks.append(cli_check)

    expected_output_file = repo_root / "DEMO/DEMO-001_OUTPUT.txt"
    if cli_output is None or not expected_output_file.is_file():
        output_check = check_record(
            "PVPY-004", "BLOCKED", "CLI text exactly matches Golden text after newline normalization", "CLI or Golden text unavailable", [str(expected_output_file)]
        )
    else:
        expected_output = expected_output_file.read_text(encoding="utf-8")
        matches = normalize_newlines(cli_output) == normalize_newlines(expected_output)
        output_check = check_record(
            "PVPY-004",
            "PASS" if matches else "FAIL",
            "CLI text exactly matches Golden text after newline normalization",
            "exact match" if matches else "content mismatch",
            [str(expected_output_file), "PVPY-003 stdout"],
        )
    checks.append(output_check)

    field_expectations = (
        "Status: Accepted",
        "Partition: PART-001",
        "PanelCount: 10",
        "InstalledCapacityKwp: 5.000",
        "PlacementWarnings:\n  none",
    )
    if cli_output is None:
        field_check = check_record(
            "PVPY-005", "BLOCKED", "; ".join(field_expectations), "CLI output unavailable", ["PVPY-003 stdout"]
        )
    else:
        normalized = normalize_newlines(cli_output)
        absent = [field for field in field_expectations if field not in normalized]
        field_check = check_record(
            "PVPY-005",
            "PASS" if not absent else "FAIL",
            "; ".join(field_expectations),
            "all required fields matched" if not absent else f"missing={absent}",
            ["PVPY-003 stdout"],
        )
    checks.append(field_check)

    expected_ids = [f"PNL-{number:06d}" for number in range(1, 11)]
    if cli_output is None:
        id_check = check_record(
            "PVPY-006", "BLOCKED", "PNL-000001 through PNL-000010, unique and ordered", "CLI output unavailable", ["PVPY-003 stdout"]
        )
    else:
        actual_ids = panel_ids(cli_output)
        valid_ids = actual_ids == expected_ids and len(actual_ids) == len(set(actual_ids))
        id_check = check_record(
            "PVPY-006",
            "PASS" if valid_ids else "FAIL",
            "PNL-000001 through PNL-000010, unique and ordered",
            ", ".join(actual_ids),
            ["PVPY-003 stdout"],
        )
    checks.append(id_check)

    json_paths = [repo_root / path for path in registered_json_paths(manifest)]
    json_errors: list[str] = []
    for path in json_paths:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            json_errors.append(f"{path}: missing")
        except (OSError, json.JSONDecodeError) as exc:
            json_errors.append(f"{path}: {exc}")
    json_result = "BLOCKED" if any(error.endswith("missing") for error in json_errors) else ("FAIL" if json_errors else "PASS")
    checks.append(
        check_record(
            "PVPY-007",
            json_result,
            "Static input and output evidence are valid UTF-8 JSON",
            "both JSON assets parsed" if not json_errors else "; ".join(json_errors),
            [str(path.relative_to(repo_root)) for path in json_paths],
        )
    )

    if manifest is None:
        hash_check = check_record(
            "PVPY-008", "BLOCKED", "Every selected Golden asset hash is reported and matches", f"manifest unavailable: {manifest_error}", [str(MANIFEST_PATH)]
        )
    else:
        hash_findings: list[str] = []
        hash_blocked = False
        hash_failed = False
        for asset in manifest.get("assets", []):
            relative = Path(asset["path"])
            asset_path = repo_root / relative
            if not asset_path.is_file():
                hash_blocked = True
                hash_findings.append(f"{relative}=MISSING")
                continue
            actual_hash = sha256(asset_path)
            matches = actual_hash == asset["sha256"].upper()
            hash_failed = hash_failed or not matches
            hash_findings.append(f"{relative}={actual_hash}{'' if matches else ' (MISMATCH)'}")
        hash_result = "FAIL" if hash_failed else ("BLOCKED" if hash_blocked else "PASS")
        hash_check = check_record(
            "PVPY-008",
            hash_result,
            "Every selected Golden asset hash is reported and matches",
            "; ".join(hash_findings),
            [str(MANIFEST_PATH)],
        )
    checks.append(hash_check)

    if tuple(check["check_id"] for check in checks) != CHECK_IDS:
        raise RuntimeError("validator check order changed")

    return {
        "validation_product": "PVOS Python Validation Product",
        "version": "0.1",
        "evidence_commit": evidence_commit,
        "started_at": started_at,
        "finished_at": utc_now(),
        "result": overall_result(checks),
        "checks": checks,
        "risks": risks,
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate PVOS Golden evidence through the existing C# CLI.")
    parser.add_argument("--repo-root", type=Path, required=True, help="Governed PVOS repository root")
    parser.add_argument("--evidence-commit", required=True, help="Immutable Git commit to record")
    parser.add_argument("--output", type=Path, help="Optional JSON report path; stdout is always emitted")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    report = run_validation(args.repo_root, args.evidence_commit)
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return {"PASS": 0, "FAIL": 1, "BLOCKED": 2}[report["result"]]


if __name__ == "__main__":
    raise SystemExit(main())
