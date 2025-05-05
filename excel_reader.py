import pandas as pd


def read_excel_file(filepath: str) -> pd.DataFrame:

    try:
        df = pd.read_excel(filepath)

        if not df.empty:
            print("Successfully read excel file.\n")
            return df
        else:
            print("The excel file is empty.\n")

        return df
    except Exception as e:
        print(f"Error while reading excel file: {e}")
        raise e
