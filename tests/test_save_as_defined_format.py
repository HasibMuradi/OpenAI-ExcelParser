import os
import json
import tempfile
import pytest
from datetime import datetime
from save_as_defined_format import save


# --- Test cases ---

def test_save_valid_data(capsys):
    valid_data = {
        "metadata": {
            "unit": "kWh",
            "source": "Sensor-1",
            "interval": "15min"
        },
        "timeseries": [
            {"timestamp": "2024-01-01T00:00:00", "value": 12.5},
            {"timestamp": "2024-01-01T00:15:00", "value": 13.1},
        ]
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test.json")
        save(valid_data, tmpdir, "test.json")

        # Check print output
        captured = capsys.readouterr()
        assert "✅ JSON successfully validated and saved" in captured.out

        # Confirm file content
        with open(filepath, "r", encoding="utf-8") as f:
            saved = json.load(f)
            assert saved["metadata"]["unit"] == "kWh"
            assert len(saved["timeseries"]) == 2


def test_save_invalid_data(capsys):
    # Missing 'unit' and invalid timestamp
    invalid_data = {
        "metadata": {
            "source": "Sensor-1",
            "interval": "15min"
        },
        "timeseries": [
            {"timestamp": "not-a-date", "value": "NaN"}
        ]
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        save(invalid_data, tmpdir, "test_invalid.json")

        captured = capsys.readouterr()
        assert "❌ Error while validating JSON content" in captured.out

        # File should not be created
        assert not os.path.exists(os.path.join(tmpdir, "test_invalid.json"))


def test_save_autocleans_timestamp(capsys):
    # Timestamp in non-ISO format, should be cleaned by internal logic
    data = {
        "metadata": {
            "unit": "kWh",
            "source": "Device-A",
            "interval": "15min"
        },
        "timeseries": [
            {"timestamp": "2024-01-01 00:00:00", "value": 10.0}
        ]
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "auto_cleaned.json")
        save(data, tmpdir, "auto_cleaned.json")

        with open(filepath, "r", encoding="utf-8") as f:
            result = json.load(f)
            assert data["timeseries"][0]["timestamp"] == "2024-01-01T00:00:00"

        captured = capsys.readouterr()
        assert "✅ JSON successfully validated and saved" in captured.out
