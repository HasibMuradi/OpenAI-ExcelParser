import pandas as pd

def read_excel_file(filepath: str) -> pd.DataFrame:
    try:
        df = pd.read_excel(filepath)

        if not df.empty:
            print(f"Datei erfolgreich eingelesen!")
            return df
        else:
            print("Die Excel-Datei ist leer!")

        return df
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei: {e}")
        raise e
