import json
import os

def display_json(folder: str, name: str) -> None:
    """
    Reads and displays structured JSON files in a human-readable format.

    Args:
        folder (str): Path to the folder containing the file.
        name (str): File name (e.g., "result.json").
    """
    # Construct the full file path
    path = os.path.join(folder, name)

    try:
        # Attempt to open and load the JSON file
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Print the loaded data as pretty-formatted JSON
        print("✅ Successfully read JSON:")
        print(json.dumps(data, indent=2, ensure_ascii=False))

    # Error handling for missing file
    except FileNotFoundError:
        print(f"❌ JSON file not found at path '{path}'.")

    # Error handling for invalid JSON syntax
    except json.JSONDecodeError:
        print(f"❌ Could not parse JSON file at '{path}'.")

    # Catch-all for any other unexpected error
    except Exception as e:
        print(f"❌ Unexpected error while reading JSON file: {e}.")
