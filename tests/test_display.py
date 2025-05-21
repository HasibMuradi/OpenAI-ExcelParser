import os
import json
import tempfile
import pytest
from display import display_json


def test_display_json_success(capsys):
    # Create a temporary JSON file with valid content
    data = {"key": "value", "numbers": [1, 2, 3]}
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f)

        display_json(tmpdir, "test.json")

        captured = capsys.readouterr()
        assert "✅ Successfully read JSON:" in captured.out
        assert json.dumps(data, indent=2, ensure_ascii=False) in captured.out


def test_display_json_file_not_found(capsys):
    with tempfile.TemporaryDirectory() as tmpdir:
        # Try to read a file that doesn't exist
        display_json(tmpdir, "missing.json")
        captured = capsys.readouterr()
        assert "❌ JSON file not found" in captured.out


def test_display_json_invalid_json(capsys):
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "invalid.json")
        # Write invalid JSON content
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("{invalid json")

        display_json(tmpdir, "invalid.json")
        captured = capsys.readouterr()
        assert "❌ Could not parse JSON file" in captured.out
