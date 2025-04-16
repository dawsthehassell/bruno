import unittest
import json
import tempfile
from pathlib import Path
from click.testing import CliRunner
from bruno.commands.new_entry import new

class TestNewEntryCommand(unittest.TestCase):
    def test_new_entry_restaurant(self):
        runner = CliRunner()

        with tempfile.TemporaryDirectory() as tmp_dir:
            data_path = Path(tmp_dir) / "test.json"
            
            # Simulated user input
            inputs = "\n".join([
                "restaurant",         # category
                "mcdonalds",          # name
                "2024-04-10",         # date
                "near apartment",     # location
                "big mac",            # food_ordered
                "yum",                # likes
                "unhealthy",          # dislikes
                "3",                  # rating
                "yes",                # visit_again
                "#fastfood"           # tags
            ])

            # Run the command with simulated input and custom data path
            result = runner.invoke(new, ["--data-path", str(data_path)], input=inputs)
            
            self.assertEqual(result.exit_code, 0)
            self.assertIn("New entry added successfully", result.output)
            self.assertTrue(data_path.exists())

            with open(data_path, "r") as f:
                data = json.load(f)
                self.assertIn("restaurant", data)
                self.assertEqual(len(data["restaurant"]), 1)
                entry = data["restaurant"][0]
                self.assertEqual(entry["name"], "mcdonalds")
                self.assertEqual(entry["rating"], "3")
                self.assertTrue(entry["visit_again"])

if __name__ == "__main__":
    unittest.main()
