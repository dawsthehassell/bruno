import unittest
import json
import tempfile
from click.testing import CliRunner
from bruno.commands.clear_log import clear_all 

class TestNewEntry(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_path = f"{self.temp_dir.name}/test_entry_logs.json"

        sample_data = {
            "restaurant": [
                {
                    "name": "Chipotle",
                    "rating": "5",
                    "visit_again": True
                }
            ]
        }
        with open(self.data_path, "w") as f:
            json.dump(sample_data, f)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_clear_all_dry_run(self):
        result = self.runner.invoke(clear_all, ["--dry-run", "--data-path", self.data_path])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Dry run", result.output)
        self.assertIn("1 total entries", result.output)

        with open(self.data_path, "r") as f:
            data_after = json.load(f)

        self.assertIn("restaurant", data_after)
        self.assertEqual(len(data_after["restaurant"]), 1)
    
    def test_clear_all_with_prompt_yes(self):
        with open(self.data_path, "r") as f:
            data = json.load(f)

        self.assertIn("restaurant", data)
        
        result = self.runner.invoke(clear_all, ["--data-path", self.data_path], input="yes\n")
        self.assertEqual(result.exit_code, 0)
        self.assertIn("All entries have been deleted. Experience Log is now empty.", result.output)

        with open(self.data_path, "r") as f:
            data = json.load(f)
        self.assertEqual(data, {})

    def test_clear_all_with_prompt_no(self):
        with open(self.data_path, "r") as f:
            data = json.load(f)

        self.assertIn("restaurant", data)
        
        result = self.runner.invoke(clear_all, ["--data-path", self.data_path], input="no\n")
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Clear all action cancelled.", result.output)

        with open(self.data_path, "r") as f:
            data = json.load(f)
        self.assertIn("restaurant", data)

    def test_clear_all_with_force_flag(self):
        with open(self.data_path, "r") as f:
            data = json.load(f)

        self.assertIn("restaurant", data)
        
        result = self.runner.invoke(clear_all, ["--force", "--data-path", self.data_path], input="yes\n")
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Clearing all entries immediately with --force...", result.output)

        with open(self.data_path, "r") as f:
            data = json.load(f)
        self.assertEqual(data, {})

if __name__ == "__main__":
    unittest.main()