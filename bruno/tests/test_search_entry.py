import unittest
import json
import tempfile
from click.testing import CliRunner
from bruno.commands.search_entries import search_entries

class TestSearchEntry(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_path = f"{self.temp_dir.name}/test_entry_logs.json"

        data = {
            "restaurant": [
                {
                    "name": "Chipotle",
                    "date": "4/28/25",
                    "company": "No",
                    "location": "Beltway 8",
                    "food_ordered": "bowl",
                    "likes": "Yummy",
                    "dislikes": "nothing",
                    "rating": "5",
                    "visit_again": True,
                    "tags": []
                }
            ],
            "bar": [
                {
                    "name": "Axelrad",
                    "date": "4/28",
                    "company": "Joe",
                    "location": "Midtown",
                    "drink_ordered": "Beer",
                    "live_events": "Yes, jazz",
                    "dislikes": "busy",
                    "vibe": "chill",
                    "rating": "5",
                    "visit_again": False,
                    "tags": ["#livemusic"]
                }
            ]
        }


        with open(self.data_path, "w") as f:
            json.dump(data, f, indent=2)
    
    def tearDown(self):
        self.temp_dir.cleanup()

    def test_search_by_term(self):
        result = self.runner.invoke(search_entries, ["--term", "chipotle", "--data-path", self.data_path])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Chipotle", result.output)

    def test_search_by_category(self):
        result = self.runner.invoke(search_entries, ["--category", "bar", "--data-path", self.data_path])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("bar", result.output)
        self.assertIn("Axelrad", result.output)

    def test_search_by_visit_again(self):
        result = self.runner.invoke(search_entries, ["--visit_again", "--data-path", self.data_path])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Chipotle", result.output)
        self.assertNotIn("Axelrad", result.output)

    def test_search_by_all(self):
        result = self.runner.invoke(search_entries, ["--term", "chipotle", "--category", "restaurant", "--visit_again", "--data-path", self.data_path])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Chipotle", result.output)
        self.assertIn("restaurant", result.output)

if __name__ == "__main__":
    unittest.main