"""
Project: Extracting time series and its metadata from Excel data using OpenAI

Author: Hasibullah Muradi
Email: hasib_muradi@hotmail.com
Date: 05.05.2025

Description:
    This Python program performs the following steps:
    1. Reads data from an Excel file using a helper function.
    2. Sends the data to the OpenAI API to parse and extract structured time series data and metadata.
    3. Saves the parsed data in a defined JSON format.
    4. Displays the saved time series data along with its metadata.

This modular approach separates reading, parsing, saving, and displaying logic into different components for clarity and reusability.
"""

from excel_reader import read_excel_file        # Module to read Excel files into pandas DataFrames
from parser import parse_with_openai            # Module to send data to OpenAI and parse response
from save_as_defined_format import save         # Module to validate and save parsed data as JSON
from display import display_json                # Module to display the saved JSON data in a readable way

# Define the path to the Excel file containing raw time series data
file_path = "Excel_Data/Zeitreihe2.xlsx"

# Step 1: Read the Excel file into a pandas DataFrame
raw_table = read_excel_file(file_path)

# Step 2: Parse the raw table by sending it to OpenAI API to extract structured time series and metadata
parsed = parse_with_openai(raw_table)

# Step 3: Save the parsed data as a JSON file in the specified folder with a given filename
save(parsed, "JSON_Data", "Zeitreihe2.json")

# Step 4: Display the saved JSON file content (time series data + metadata) for verification or review
display_json("JSON_Data", "Zeitreihe2.json")
