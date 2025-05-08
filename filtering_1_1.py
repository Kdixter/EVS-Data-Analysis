import pandas as pd

# Load the Excel file
df = pd.read_excel('Bird_data_2.xlsx', dtype=str)

# Clean column names: strip whitespace and uppercase for consistency
df.columns = df.columns.str.strip()

# Convert date to datetime
df['OBSERVATION DATE'] = pd.to_datetime(df['OBSERVATION DATE'], errors='coerce')

# Filter to include only rows from 2017 onward
df = df[df['OBSERVATION DATE'].dt.year >= 2017]

# Select relevant columns
selected = df[[
    'SAMPLING EVENT IDENTIFIER',
    'OBSERVATION DATE',
    'LATITUDE',
    'LONGITUDE',
    'NUMBER OBSERVERS'
]].copy()

# Rename for clarity
selected.columns = [
    'Unique ID',
    'Date',
    'Latitude',
    'Longitude',
    'Species Proxy (Num Observers)'
]

# Export to Excel
selected.to_excel('ebird_summary_proxy.xlsx', index=False)

print(selected.head())
