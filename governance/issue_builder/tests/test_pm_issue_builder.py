import copy
import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "pm_issue_builder.py"
SPEC = importlib.util.spec_from_file_location("pm_issue_builder", MODULE_PATH)
BUILDER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BUILDER
SPEC.loader.exec_module(BUILDER)


def valid_package():
    return {
        "package_id": "DPP-TEST-001",
        "date": "2026-08-06",
        "status": "APPROVED",
        "approved_by": "Owner",
        "repository": "example/repo",
        "issues": [
            {
                "issue_id": "EOS-DEMO-001",
                "title": "DEMO — First",
                "capability_ids": ["EOS-016"],
                "objective": "Demonstrate first queue entry.",
                "scope": ["First scope"],
                "out_of_scope": ["Product changes"],
                "deliverables": ["First evidence"],
                "acceptance_criteria": ["First accepted"],
                "required_evidence": ["First result"],
                "dependencies": [],
                "status": "READY",
            },
            {
                "issue_id": "EOS-DEMO-002",
                "title": "DEMO — Second",
                "capability_ids": ["EOS-016"],
                "objective": "Demonstrate dependent queue entry.",
                "scope": ["Second scope"],
                "out_of_scope": ["Product changes"],
                "deliverables": ["Second evidence"],
                "acceptance_criteria": ["Second accepted"],
                "required_evidence": ["Second result"],
                "dependencies": ["EOS-DEMO-001"],
                "status": "READY",
            },
        ],
    }


class ValidationTests(unittest.TestCase):
    def test_valid_package(self):
        BUILDER.validate_package(valid_package())

    def test_unapproved_package_is_rejected(self):
        package = valid_package()
        package["status"] = "DRAFT"
        with self.assertRaises(BUILDER.ValidationError):
            BUILDER.validate_package(package)

    def test_missing_required_field_is_rejected(self):
        package = valid_package()
        del package["issues"][0]["required_evidence"]
        with self.assertRaises(BUILDER.ValidationError):
            BUILDER.validate_package(package)

    def test_duplicate_issue_id_is_rejected(self):
        package = valid_package()
        package["issues"][1]["issue_id"] = package["issues"][0]["issue_id"]
        with self.assertRaises(BUILDER.ValidationError):
            BUILDER.validate_package(package)

    def test_forward_dependency_is_rejected(self):
        package = valid_package()
        package["issues"][0]["dependencies"] = ["EOS-DEMO-002"]
        with self.assertRaises(BUILDER.ValidationError):
            BUILDER.validate_package(package)

    def test_repository_override_must_match(self):
        with self.assertRaises(BUILDER.ValidationError):
            BUILDER.validate_package(valid_package(), "other/repo")


class QueueTests(unittest.TestCase):
    def test_dry_run_preserves_order_without_calling_creator(self):
        def fail_creator(*_args):
            raise AssertionError("creator must not run during dry run")

        queue = BUILDER.build_queue(valid_package(), publish=False, creator=fail_creator)
        self.assertEqual("DRY_RUN", queue["status"])
        self.assertEqual(["EOS-DEMO-001", "EOS-DEMO-002"], [i["issue_id"] for i in queue["issues"]])

    def test_render_contains_all_execution_sections(self):
        package = valid_package()
        body = BUILDER.render_issue_body(package, package["issues"][0], {})
        for heading in (
            "## Objective",
            "## Scope",
            "## Out of Scope",
            "## Deliverables",
            "## Acceptance Criteria",
            "## Required Evidence",
        ):
            self.assertIn(heading, body)
        self.assertIn("sole Execution Source", body)

    def test_publish_returns_queue_ready_and_resolves_dependency(self):
        calls = []

        def creator(repository, title, body):
            calls.append((repository, title, body))
            number = 100 + len(calls)
            return {"number": number, "url": f"https://example.test/issues/{number}"}

        queue = BUILDER.build_queue(
            valid_package(), publish=True, creator=creator, finder=lambda *_args: None
        )
        self.assertEqual("QUEUE_READY", queue["status"])
        self.assertEqual(2, len(calls))
        self.assertIn("EOS-DEMO-001 — #101", calls[1][2])

    def test_validation_finishes_before_publication(self):
        package = valid_package()
        package["issues"][1]["acceptance_criteria"] = []
        called = False

        def creator(*_args):
            nonlocal called
            called = True
            return {}

        with self.assertRaises(BUILDER.ValidationError):
            BUILDER.build_queue(
                package, publish=True, creator=creator, finder=lambda *_args: None
            )
        self.assertFalse(called)

    def test_publish_reuses_existing_issue_without_duplicate(self):
        creator_called = False

        def creator(*_args):
            nonlocal creator_called
            creator_called = True
            return {}

        def finder(_repository, issue_id):
            number = 201 if issue_id == "EOS-DEMO-001" else 202
            return {
                "number": number,
                "url": f"https://example.test/issues/{number}",
                "title": issue_id,
            }

        queue = BUILDER.build_queue(
            valid_package(), publish=True, creator=creator, finder=finder
        )
        self.assertFalse(creator_called)
        self.assertTrue(all(item["reused"] for item in queue["issues"]))
        self.assertEqual([201, 202], [item["number"] for item in queue["issues"]])


if __name__ == "__main__":
    unittest.main()
