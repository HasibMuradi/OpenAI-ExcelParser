import pandas as pd
import os
from io import StringIO


def write_csv_file(parsed: str, folder: str, name: str) -> None:

    # Save CSV
    df = pd.read_csv(StringIO(parsed))
    path = os.path.join(folder, name)
    df.to_csv(path, index=False)

    print(f"CSV saved in folder {folder}.\n")

