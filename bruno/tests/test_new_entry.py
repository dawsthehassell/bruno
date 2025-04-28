import unittest
import json
import tempfile
from click.testing import CliRunner
from bruno.commands.new_entry import new

class TestNewEntry(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_path = f"{self.temp_dir.name}/test_entry_logs.json"

    def tearDown(self):
        self.temp_dir.cleanup()

    def create_and_check_entry(self, category, expected_fields, extra_inputs):
        ### Helper function to create and verify any new entry ###
        fake_inputs = f"{category}\n{expected_fields['name']}\n{extra_inputs}"
        
        result = self.runner.invoke(new, ["--data-path", self.data_path], input=fake_inputs)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("New entry added successfully!", result.output)

        with open(self.data_path, "r") as f:
            data = json.load(f)

        self.assertIn(category, data)
        self.assertEqual(len(data[category]), 1)
        
        entry = data[category][0]

        for key, value in expected_fields.items():
            self.assertEqual(entry.get(key), value)

    def test_create_new_restaurant_entry(self):
        expected_fields = {
            "name": "Chipotle",
            "rating": "5",
            "visit_again": True,
        }
        extra_inputs = (
            "4/28/25\n"
            "No\n"
            "Beltway 8\n"
            "bowl\n"
            "Yummy\n"
            "nothing\n"
            "5\n"
            "yes\n"
            "\n"
        )
        self.create_and_check_entry("restaurant", expected_fields, extra_inputs)

    def test_create_new_bar_entry(self):
        expected_fields = {
            "name": "Axelrad",
            "rating": "5",
            "visit_again": True,
        }
        extra_inputs = (
        "4/28\n"
        "Joe\n"
        "Midtown\n"
        "Beer\n"
        "Yes, jazz\n"
        "busy\n"
        "chill\n"
        "5\n"
        "yes\n"
        "\n"
        )
        self.create_and_check_entry("bar", expected_fields, extra_inputs)

if __name__ == "__main__":
    unittest.main()