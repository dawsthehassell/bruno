import tempfile
import json
import pytest
from pathlib import Path
from click.testing import CliRunner
from bruno.commands.new_entry import new

def test_new_entry_restaurant():
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmp_dir:
        base_dir = Path(tmp_dir)
        data_path = base_dir / "test.json"
        inputs = "\n".join([
            "restaurant",
            "mcdonalds",
            "no",
            "near apartment",
            "big mac",
            "yum",
            "unhealthy",
            "3",
            "yes",
            "#fastfood"
        ])
        result = runner.invoke(new, ["--data-path", str(data_path)], input=inputs)
        assert result.exit_code == 0
        assert data_path.exists()
        assert "New entry added successfully" in result.output
        
        with open(data_path, "r") as f:
            data = json.load(f)
            assert "restaurant" in data
            assert len(data["restaurant"]) == 1
            assert data["restaurant"][0]["name"] == "mcdonalds"

        ### Run pytest tests/test/new_entry.py

