import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import validate


REPO_ROOT = Path(__file__).resolve().parents[2]


class ValidatorUnitTests(unittest.TestCase):
    def test_normalize_newlines(self) -> None:
        self.assertEqual("a\nb", validate.normalize_newlines("a\r\nb\r\n"))
        self.assertEqual("a\nb", validate.normalize_newlines("a\rb\n"))

    def test_panel_ids_are_extracted_in_order(self) -> None:
        sample = "  PNL-000001 order=1\n  PNL-000002 order=2\n"
        self.assertEqual(["PNL-000001", "PNL-000002"], validate.panel_ids(sample))

    def test_overall_result_precedence(self) -> None:
        self.assertEqual("PASS", validate.overall_result([{"result": "PASS"}]))
        self.assertEqual("BLOCKED", validate.overall_result([{"result": "PASS"}, {"result": "BLOCKED"}]))
        self.assertEqual("FAIL", validate.overall_result([{"result": "BLOCKED"}, {"result": "FAIL"}]))

    def test_registered_json_paths_include_expanded_scenarios(self) -> None:
        manifest = json.loads((REPO_ROOT / "VALIDATION" / "golden-dataset-v1.json").read_text(encoding="utf-8"))
        paths = validate.registered_json_paths(manifest)
        self.assertIn(Path("DEMO/demo-input.json"), paths)
        self.assertIn(Path("DEMO/demo-output.json"), paths)
        self.assertIn(Path("VALIDATION/scenarios/PVOS-GOLDEN-002/input.json"), paths)
        self.assertIn(Path("VALIDATION/scenarios/PVOS-GOLDEN-002/output.json"), paths)
        self.assertIn(Path("VALIDATION/scenarios/PVOS-GOLDEN-003/input.json"), paths)
        self.assertIn(Path("VALIDATION/scenarios/PVOS-GOLDEN-003/output.json"), paths)

    def test_missing_repository_dependencies_are_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            report = validate.run_validation(Path(directory), "missing-commit")
        self.assertEqual("BLOCKED", report["result"])
        self.assertTrue(any(item["result"] == "BLOCKED" for item in report["checks"]))

    def test_registered_hash_mismatch_is_fail(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest_path = root / "VALIDATION" / "golden-dataset-v1.json"
            asset_path = root / "evidence.json"
            manifest_path.parent.mkdir(parents=True)
            asset_path.write_text("{}\n", encoding="utf-8")
            manifest_path.write_text(json.dumps({
                "assets": [{
                    "role": "golden_result_review",
                    "path": "evidence.json",
                    "sha256": "0" * 64
                }]
            }), encoding="utf-8")

            report = validate.run_validation(root, "missing-commit")

        hash_check = next(item for item in report["checks"] if item["check_id"] == "PVPY-008")
        self.assertEqual("FAIL", hash_check["result"])
        self.assertEqual("FAIL", report["result"])


class ValidatorIntegrationTests(unittest.TestCase):
    def test_current_golden_dataset_passes(self) -> None:
        commit = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        with tempfile.TemporaryDirectory() as directory:
            report_path = Path(directory) / "report.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(Path(__file__).with_name("validate.py")),
                    "--repo-root",
                    str(REPO_ROOT),
                    "--evidence-commit",
                    commit,
                    "--output",
                    str(report_path),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, completed.returncode, completed.stderr or completed.stdout)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual("PASS", report["result"])
            self.assertEqual([f"PVPY-{number:03d}" for number in range(1, 9)], [item["check_id"] for item in report["checks"]])
            self.assertTrue(all(item["result"] == "PASS" for item in report["checks"]))


if __name__ == "__main__":
    unittest.main()
