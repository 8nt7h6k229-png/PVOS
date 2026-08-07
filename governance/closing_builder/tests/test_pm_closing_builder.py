import copy
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE = Path(__file__).parents[1] / "pm_closing_builder.py"
SPEC = importlib.util.spec_from_file_location("pm_closing_builder", MODULE)
BUILDER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BUILDER
SPEC.loader.exec_module(BUILDER)


def valid_input():
    sha = "a" * 40
    return {
        "closing_id": "CLOSE-TEST", "date": "2026-08-07",
        "planning_package_id": "DPP-TEST", "planning_status": "APPROVED",
        "repository": "example/repo", "branch": "agent/test", "head": sha,
        "remote_head": sha, "working_tree": "CLEAN",
        "issues": [{"number": 1, "issue_id": "TEST-001", "status": "READY_FOR_PM_REVIEW", "evidence": ["commit:a"]}],
        "pm_review": "PENDING", "owner_review": "PENDING", "daily_closing": "PENDING",
    }


class ClosingBuilderTests(unittest.TestCase):
    def test_valid_input_and_deterministic_render(self):
        data = valid_input()
        self.assertEqual(BUILDER.render(data), BUILDER.render(copy.deepcopy(data)))

    def test_missing_field_stops(self):
        data = valid_input(); del data["head"]
        with self.assertRaises(BUILDER.ValidationError): BUILDER.validate(data)

    def test_dirty_tree_stops(self):
        data = valid_input(); data["working_tree"] = "DIRTY"
        with self.assertRaises(BUILDER.ValidationError): BUILDER.validate(data)

    def test_head_mismatch_stops(self):
        data = valid_input(); data["remote_head"] = "b" * 40
        with self.assertRaises(BUILDER.ValidationError): BUILDER.validate(data)

    def test_builder_cannot_complete_gates(self):
        for gate in ("pm_review", "owner_review", "daily_closing"):
            data = valid_input(); data[gate] = "COMPLETE"
            with self.assertRaises(BUILDER.ValidationError): BUILDER.validate(data)

    def test_duplicate_issue_stops(self):
        data = valid_input(); data["issues"].append(copy.deepcopy(data["issues"][0]))
        with self.assertRaises(BUILDER.ValidationError): BUILDER.validate(data)

    def test_main_writes_review_package(self):
        import json
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "input.json"; output = Path(directory) / "output.md"
            source.write_text(json.dumps(valid_input()), encoding="utf-8")
            self.assertEqual(0, BUILDER.main([str(source), "--output", str(output)]))
            self.assertIn("READY_FOR_PM_REVIEW", output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
