from excel_reader import read_excel_file
from parser import parse_with_deepseek

# Path to Excel file
file_path = "ExcelData/Zeitreihe1.xlsx"

# Einlesen einer Excel-Datei
raw_table = read_excel_file(file_path)

# Sending data to API saving it
converted = parse_with_deepseek(raw_table)

# Output of the time series and its metadata
print(converted)

