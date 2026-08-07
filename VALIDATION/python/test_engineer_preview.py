import tempfile
import unittest
from pathlib import Path
from unittest import mock

import engineer_preview

REPO_ROOT = Path(__file__).resolve().parents[2]


def synthetic(result: str, fingerprint: str = "A" * 64) -> dict:
    return {"result": result, "evidence_commit": "1" * 40,
            "checks": [{"check_id": "PVPY-001", "result": result, "actual": result}], "report_fingerprint": fingerprint}


class EngineerPreviewTests(unittest.TestCase):
    def test_pass_scenario_writes_reports(self) -> None:
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(engineer_preview, "preflight", return_value=[]), mock.patch.object(
            engineer_preview, "resolve_head", return_value="1" * 40):
            code, report, paths = engineer_preview.execute(REPO_ROOT, Path(directory), 3, runner=lambda _r, _c: synthetic("PASS"))
            rendered = paths[1].read_text(encoding="utf-8")
        self.assertEqual(0, code)
        self.assertEqual("PASS", report["result"])
        self.assertIn("**PASS**", rendered)
        self.assertEqual(3, report["validation"]["repeatability"]["runs"])

    def test_intentional_fail_is_visible(self) -> None:
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(engineer_preview, "preflight", return_value=[]), mock.patch.object(
            engineer_preview, "resolve_head", return_value="1" * 40):
            code, report, paths = engineer_preview.execute(REPO_ROOT, Path(directory), 1, runner=lambda _r, _c: synthetic("FAIL"))
            rendered = paths[1].read_text(encoding="utf-8")
        self.assertEqual(1, code)
        self.assertEqual("FAIL", report["result"])
        self.assertIn("Action Required", rendered)

    def test_intentional_blocked_preflight_is_actionable(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            code, report, paths = engineer_preview.execute(Path(directory) / "missing", Path(directory) / "reports", 1)
            rendered = paths[1].read_text(encoding="utf-8")
        self.assertEqual(2, code)
        self.assertEqual("BLOCKED", report["result"])
        self.assertIn("does not exist", rendered)

    def test_report_identity_is_stable(self) -> None:
        self.assertEqual(engineer_preview.preview_report(synthetic("PASS", "B" * 64))["report_identity"],
                         engineer_preview.preview_report(synthetic("PASS", "B" * 64))["report_identity"])


if __name__ == "__main__":
    unittest.main()
