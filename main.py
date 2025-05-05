"""
Project: Extracting time series und its metadata from Excel Data using OpenAI

Author: Hasibullah Muradi
Email: hasib_muradi@hotmail.com
Date: 05.05.2025

Description: This Python program reads data from an Excel file,
    sends the data to the OpenAI API for processing,
    saves the parsed data returned by OpenAI into the defined target format (CSV),
    and outputs the resulting time series and its metadata from CSV file.
"""

from excel_reader import read_excel_file
from parser import parse_with_openai
from csv_writer import write_csv_file
from display import display

# Path to Excel file
file_path = "Excel_Data/Zeitreihe4.xlsx"

# Einlesen einer Excel-Datei
raw_table = read_excel_file(file_path)

# Sending data to API to parse it
parsed = parse_with_openai(raw_table)

# Saving the parsed data as CSV format
write_csv_file(parsed, "CSV_Data", "Zeitreihe4.csv")

# Display the parsed time series with its metadata
display("CSV_Data", "Zeitreihe4.csv")

