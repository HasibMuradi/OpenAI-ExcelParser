import os
import json
from pydantic import BaseModel, ValidationError, Field
from typing import List
from datetime import datetime


# --- Target data structure using Pydantic models ---

# This class defines the metadata for the time series data
class Metadata(BaseModel):
    unit: str = Field(..., description="Unit, e.g., kWh")
    source: str = Field(..., description="Source, e.g., device name")
    interval: str = Field(..., description="Measurement interval, e.g., 15min")


# This class represents a single data point in the time series
class TimePoint(BaseModel):
    timestamp: datetime  # The timestamp of the measurement
    value: float          # The measured value


# This class represents the complete parsed data structure
class ParsedData(BaseModel):
    metadata: Metadata               # Metadata info (unit, source, interval)
    timeseries: List[TimePoint]      # List of time-value pairs


def save(parsed: dict, folder: str, name: str) -> None:
    """
    Validates and saves structured time series data to a JSON file.

    Parameters:
        parsed (dict): Dictionary containing parsed data to validate and save.
        folder (str): Destination folder to save the file.
        name (str): Name of the JSON file (e.g., "output.json").

    This function:
    - Validates the structure using Pydantic.
    - Creates the target folder if it doesn't exist.
    - Saves the data as pretty-printed JSON (including datetime formatting).
    """

    def clean_timestamps(data):
        from datetime import datetime
        for point in data.get("timeseries", []):
            ts = point.get("timestamp")
            if isinstance(ts, str):
                try:
                    dt = datetime.fromisoformat(ts)
                except ValueError:
                    dt_str = ts.split()[0]
                    try:
                        dt = datetime.fromisoformat(dt_str)
                    except Exception:
                        dt = None
                if dt:
                    point["timestamp"] = dt.isoformat()
        return data

    try:
        parsed = clean_timestamps(parsed)
        parsed_model = ParsedData.parse_obj(parsed)
    except ValidationError as e:
        print("❌ Error while validating JSON content:")
        print(e.json(indent=2))
        return

    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, name)

    # Serialize safely with datetime support
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(parsed_model.model_dump(), indent=2, ensure_ascii=False, default=str))

    print(f"✅ JSON successfully validated and saved to: {path}")

