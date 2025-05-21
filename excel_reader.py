import pandas as pd


def read_excel_file(filepath: str) -> pd.DataFrame:
    """
    Reads an Excel file into a Pandas DataFrame.

    Parameters:
        filepath (str): The path to the Excel file to be read.

    Returns:
        pd.DataFrame: The DataFrame containing the Excel data.

    This function:
    - Tries to load the Excel file at the given path.
    - Prints a success message if data is read and the DataFrame is not empty.
    - Prints a warning if the Excel file is empty.
    - Raises exceptions if reading the file fails (e.g., file not found, corrupted file).
    """
    try:
        # Attempt to read the Excel file into a DataFrame
        df = pd.read_excel(filepath)

        # Check if DataFrame contains any data
        if not df.empty:
            print("Successfully read excel file.\n")
            return df
        else:
            # Inform if the file is empty but still return the empty DataFrame
            print("The excel file is empty.\n")
            return df

    except Exception as e:
        # Catch any error (e.g., file not found, parsing issues) and print it
        print(f"Error while reading excel file: {e}")
        # Re-raise the exception so calling code can handle it if needed
        raise e
