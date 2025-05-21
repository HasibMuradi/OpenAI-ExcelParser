## Flexible Time Series Data Converter using OpenAI
### Project Overview
This project implements a flexible data parser that converts time series data from various Excel formats into a unified Python data structure using the OpenAI API. It is designed to handle inconsistent input formats (fuzzy inputs) and standardize them using the power of large language models.

The parser is robust against formatting differences between files and produces clean, validated structured outputs with metadata and time series content.

### Problem Statement
You are given four Excel files. Each contains time series data with associated metadata, but all have slight structural differences.
Your task is to:
- Define a unified target data format in Python.
- Build a Python program that can:
- Read and preprocess the Excel files.
- Send the data to the OpenAI API for parsing.
- Validate and store the structured data in a predefined schema.
- Output the extracted time series and metadata.

### Features
- Supports fuzzy input structures using OpenAI’s structured output capabilities.
- Converts Excel time series data to a standard JSON format.
- Validates output against a strict Python schema using Pydantic.
- Handles datetime formats and Unicode content correctly.
- CLI-ready and extensible for more input formats.

### Technologies Used
- Python 3.11+
- pytest 8.3.5
- Pandas
- OpenAI Python SDK
- Pydantic v2
- dotenv for environment config

### References
- [Structured output from LLMs](https://www.thoughtworks.com/radar/techniques/structured-output-from-llms)
- [Structured Outputs - OpenAI Platform](https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses)
- [Structured data extraction from unstructured content using LLM schemas](https://simonwillison.net/2025/Feb/28/llm-schemas/#structured-data-extraction-is-a-killer-app-for-llms)