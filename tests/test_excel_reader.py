import os
import pandas as pd
import tempfile
import pytest
from excel_reader import read_excel_file


def test_read_valid_excel(capsys):
    data = {'Name': ['Alice', 'Bob'], 'Age': [30, 25]}
    df = pd.DataFrame(data)

    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test_valid.xlsx")
        df.to_excel(filepath, index=False)

        result_df = read_excel_file(filepath)

        captured = capsys.readouterr()
        assert "Successfully read excel file." in captured.out
        pd.testing.assert_frame_equal(result_df, df)


def test_read_empty_excel(capsys):
    empty_df = pd.DataFrame()

    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "test_empty.xlsx")
        empty_df.to_excel(filepath, index=False)

        result_df = read_excel_file(filepath)

        captured = capsys.readouterr()
        assert "The excel file is empty." in captured.out
        assert result_df.empty


def test_read_missing_excel():
    with pytest.raises(FileNotFoundError):
        read_excel_file("nonexistent_file.xlsx")
