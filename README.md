# Data Cleaning Project

This project demonstrates a basic data cleaning process using Python and Pandas, created and tested in Google Colab.

## Files Included

- `sample_data.csv` – The original input dataset with missing or messy values.
- `cleaned_data.csv` – The cleaned version of the dataset after processing.
- `data_cleaner.py` – Python script that performs the data cleaning.
- `README.md` – Project documentation (this file).

## What the Script Does

The Python script performs the following tasks:

1. Reads the original CSV file.
2. Strips whitespace from column headers.
3. Removes rows where all values are missing.
4. Fills missing values:
   - `Age` → with the mean age
   - `Name` and `City` → with `"Unknown"`
5. Removes duplicate rows.
6. Saves the cleaned data to `cleaned_data.csv`.

## How to Run

If you're using this locally:

```bash
python data_cleaner.py
