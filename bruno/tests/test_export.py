import unittest
import os
import json
import tempfile
from click.testing import CliRunner
from bruno.commands.export import export

class TestExportCommand(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_path = os.path.join(self.temp_dir.name, "entry_logs.json")

        self.initial_data = {
            "restaurant": [
                {
                    "name": "Chipotle",
                    "date": "4/28/25",
                    "location": "Houston",
                    "food_ordered": "bowl",
                    "likes": "Yummy",
                    "dislikes": "none",
                    "rating": 5,
                    "visit_again": True,
                    "tags": ["casual", "quick"]
                }
            ]
        }

        with open(self.data_path, "w") as f:
            json.dump(self.initial_data, f, indent=2)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_export_default_txt(self):
        user_input = "export_test_file\n"
        result = self.runner.invoke(export, ["--data-path", self.data_path], input=user_input)
        
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Entry log successfully exported", result.output)

        export_file_path = os.path.join(self.temp_dir.name, "export_test_file.txt")
        self.assertTrue(os.path.exists(export_file_path))

        with open(export_file_path, "r") as f:
            content = f.read()

        self.assertIn("Chipotle", content)
        self.assertIn("Food_ordered: bowl", content)

    def test_export_csv_file(self):
        user_input = "export_csv_file\n"
        result = self.runner.invoke(export, ["--format", "csv", "--data-path", self.data_path], input=user_input)

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Entry log successfully exported", result.output)

        export_file_path = os.path.join(self.temp_dir.name, "export_csv_file.csv")
        self.assertTrue(os.path.exists(export_file_path))

        with open(export_file_path, "r") as f:
            content = f.read()

        self.assertIn("Category,Name,Date", content)  # checks header exists
        self.assertIn("restaurant,Chipotle,4/28/25", content)   # checks row content

    def test_export_csv_cancel_overwrite(self):
        export_name = "cancel_overwrite_test"
        export_filename = f"{export_name}.csv"
        export_full_path = os.path.join(self.temp_dir.name, export_filename)

        with open(export_full_path, "w") as f:
            f.write("Old content")

        user_input = f"{export_name}\nno\n"

        result = self.runner.invoke(
            export,
            ["--format", "csv", "--data-path", self.data_path],
            input=user_input,
        )

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Export cancelled.", result.output)

        with open(export_full_path, "r") as f:
            content = f.read()
        self.assertEqual(content, "Old content")

    def test_export_txt_confirm_overwrite(self):
        export_name = "confirm_overwrite_test.txt"
        export_filename = f"{export_name}"
        export_full_path = os.path.join(self.temp_dir.name, export_filename)

        with open(export_full_path, "w") as f:
            f.write("Old content that should be overwritten")
        
        user_input = f"{export_name}\nyes\n"

        result = self.runner.invoke(export, ["--data-path", self.data_path], input=user_input)

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Entry log successfully exported", result.output)
        self.assertTrue(os.path.exists(export_full_path))

        with open(export_full_path, "r") as f:
            content = f.read()

        self.assertNotIn("Old content", content)
        self.assertIn("Chipotle", content)
        self.assertIn("Food_ordered: bowl", content)

if __name__ == "__main__":
    unittest.main()