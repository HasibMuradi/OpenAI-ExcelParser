import pandas as pd
import os


def display(folder: str, name: str) -> None:

    # Read CSV-Data
    path = os.path.join(folder, name)
    try:
        df = pd.read_csv(path)
        # Print the CSV-Data
        print("Successfully read CSV:")
        print(df.to_csv(index=False))
    except FileNotFoundError:
        print(f"CSV file not found at path '{path}'.")
    except pd.errors.EmptyDataError:
        print(f"CSV file at '{path}' is empty.")
    except pd.errors.ParserError:
        print(f"Could not parse the CSV file at '{path}',")
    except Exception as e:
        print(f"Unexpected error during reading CSV file: {e}.")


