import unittest
import os
import json
import tempfile
from click.testing import CliRunner
from bruno.commands.edit_entry import edit_entry

class TestEditEntryCommand(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_path = os.path.join(self.temp_dir.name, "entry_logs.json")

    def tearDown(self):
        self.temp_dir.cleanup() 

    def test_edit_entry_successful_edit(self):
        self.intial_data = {
            "restaurant": [
                {"name": "Old Name", "date": "5/5/25", "visit_again": True}
            ]
        }
        with open(self.data_path, "w") as f:
            json.dump(self.intial_data, f, indent=2)

        user_input = (
            "restaurant\n"  # category
            "1\n"           # entry number
            "New Name\n"    # name update
            "\n"            # keep date the same
            "\n"            # skip visit_again change (stays True)
            "yes\n"         # confirm save
        )
        
        result = self.runner.invoke(edit_entry, ["--data-path", self.data_path], input=user_input)

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Changes have been saved successfully!", result.output)

        with open(self.data_path, "r") as f:
            final_data = json.load(f)

        updated_entry = final_data["restaurant"][0]
        self.assertEqual(updated_entry["name"], "New Name")
        self.assertEqual(updated_entry["date"], "5/5/25")
        self.assertTrue(updated_entry["visit_again"])

    def test_cancel_during_edit(self):
        self.intial_data = {
            "restaurant": [
                {"name": "Old Name", "date": "5/5/25", "visit_again": True}
            ]
        }
        with open(self.data_path, "w") as f:
            json.dump(self.intial_data, f, indent=2)

        user_input = (
            "restaurant\n"  # category
            "1\n"           # entry number
            "New Name\n"    # name update
            "cancel\n"        # cancel exits the edit mode
        )

        result = self.runner.invoke(edit_entry, ["--data-path", self.data_path], input=user_input)

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Edit cancelled. No changes saved.", result.output)

        with open(self.data_path, "r") as f:
            final_data = json.load(f)
        
        self.assertEqual(final_data, self.intial_data)

    def test_no_final_confirmation(self):
        self.intial_data = {
            "restaurant": [
                {"name": "Old Name", "date": "5/5/25", "visit_again": True}
            ]
        }
        with open(self.data_path, "w") as f:
            json.dump(self.intial_data, f, indent=2)

        user_input = (
            "restaurant\n"  # category
            "1\n"           # entry number
            "New Name\n"    # name update
            "\n"            # keep date the same
            "\n"            # skip visit_again change (stays True)
            "no\n"          # DISCARDS all changes
        )
        
        result = self.runner.invoke(edit_entry, ["--data-path", self.data_path], input=user_input)

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Changes have been discarded.", result.output)

        with open(self.data_path, "r") as f:
            final_data = json.load(f)

        self.assertEqual(final_data, self.intial_data)

    def test_invalid_entry_selection(self):
        self.initial_data = {
            "restaurant": [
                {"name": "Old Name", "date": "5/5/25", "visit_again": True}
            ]
        }
        with open(self.data_path, "w") as f:
            json.dump(self.initial_data, f, indent=2)

        user_input = (
            "restaurant\n"  # category
            "4\n"           # INVALID entry number
        )

        result = self.runner.invoke(edit_entry, ["--data-path", self.data_path], input=user_input)

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Invalid selection!", result.output)

        with open(self.data_path, "r") as f:
            final_data = json.load(f)

        self.assertEqual(final_data, self.initial_data)

if __name__ == "__main__":
    unittest.main()
        