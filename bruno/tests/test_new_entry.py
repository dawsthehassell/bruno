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

    def test_create_new_restaurant_entry(self):
        fake_inputs = (
            "restaurant\n"
            "Chipotle\n"
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

        result = self.runner.invoke(new, ["--data-path", self.data_path], input=fake_inputs)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("New entry added successfully!", result.output)

        with open(self.data_path, "r") as f:
            data = json.load(f)

        self.assertIn("restaurant", data)
        self.assertEqual(len(data["restaurant"]), 1)
        self.assertEqual(data["restaurant"][0]["name"], "Chipotle")
        self.assertEqual(data["restaurant"][0]["rating"], "5")
        self.assertEqual(data["restaurant"][0]["visit_again"], True)

if __name__ == "__main__":
    unittest.main()