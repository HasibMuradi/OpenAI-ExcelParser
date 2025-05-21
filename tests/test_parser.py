import pandas as pd
import pytest
import json
from unittest.mock import patch, MagicMock
from parser import parse_with_openai


@patch("parser.OpenAI")  # Mock the OpenAI client
@patch("parser.load_dotenv")  # Mock dotenv loading
@patch("parser.os.getenv", return_value="fake-api-key")  # Fake API key
def test_parse_with_openai_success(mock_getenv, mock_dotenv, mock_openai):
    # Create a fake DataFrame
    df = pd.DataFrame({
        "timestamp": ["2024-01-01 00:00:00", "2024-01-01 00:15:00"],
        "value": [10.0, 12.5]
    })

    # Fake response from OpenAI's chat API
    fake_tool_args = {
        "metadata": {
            "unit": "kWh",
            "source": "Test Sensor",
            "interval": "15min"
        },
        "timeseries": [
            {"timestamp": "2024-01-01T00:00:00", "value": 10.0},
            {"timestamp": "2024-01-01T00:15:00", "value": 12.5}
        ]
    }

    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(
            message=MagicMock(
                tool_calls=[
                    MagicMock(function=MagicMock(arguments=json.dumps(fake_tool_args)))
                ]
            )
        )
    ]

    # Configure mock client
    mock_client_instance = MagicMock()
    mock_client_instance.chat.completions.create.return_value = mock_response
    mock_openai.return_value = mock_client_instance

    # Call the function
    result = parse_with_openai(df)

    # Assertions
    assert result["metadata"]["unit"] == "kWh"
    assert len(result["timeseries"]) == 2
    assert result["timeseries"][0]["value"] == 10.0
