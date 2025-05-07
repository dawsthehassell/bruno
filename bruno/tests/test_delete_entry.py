import unittest
import json
import tempfile
from click.testing import CliRunner
from bruno.commands.delete_entry import delete_entry

class TestNewEntry(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_path = f"{self.temp_dir.name}/test_entry_logs.json"

        self.initial_data = {
            "restaurant": [
                {"name": "Chipotle", "date": "4/28/25"},
                {"name": "Torchy's", "date": "4/27/25"}
            ]
        }

        with open(self.data_path, "w") as f:
            json.dump(self.initial_data, f, indent=2)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_delete_entry_success(self):
        self.initial_data = {
            "restaurant": [
                {"name": "Chipotle", "date": "4/28/25"},
                {"name": "Torchy's", "date": "4/27/25"}
            ]
        }

        with open(self.data_path, "w") as f:
            json.dump(self.initial_data, f, indent=2)
        
        user_input = (
            "restaurant\n"
            "1\n"
            "yes\n"
        )
        result = self.runner.invoke(delete_entry, ["--data-path", self.data_path], input=user_input)

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Selected entry has been deleted successfully.", result.output)

        with open(self.data_path, "r") as f:
            final_data = json.load(f)
        
        self.assertEqual(len(final_data["restaurant"]), 1)
        self.assertEqual(final_data["restaurant"][0]["name"], "Torchy's")

if __name__ == "__main__":
    unittest.main()

    # test currently fails btw