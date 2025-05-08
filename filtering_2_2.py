import pandas as pd
import os
from datetime import datetime

# Create output directory if it doesn't exist
output_dir = "Seperated_by_year_data_2"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}")

# Ask user for input file path or use default
input_file = "ebird_summary_proxy.xlsx"

try:
    # Read the Excel file
    print(f"Reading data from {input_file}...")
    df = pd.read_excel(input_file)
    
    # Ensure Date column exists
    if 'Date' not in df.columns:
        raise ValueError("The Excel file must have a 'Date' column")
    
    # Convert Date column to datetime if it's not already
    if not pd.api.types.is_datetime64_any_dtype(df['Date']):
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        
    # Check for any conversion failures
    if df['Date'].isna().any():
        print("Warning: Some dates could not be parsed. They will be excluded from the output.")
        df = df.dropna(subset=['Date'])
    
    # Extract year from Date
    df['Year'] = df['Date'].dt.year
    
    # Get unique years
    years = df['Year'].unique()
    
    # Count of records and years found
    print(f"Found {len(df)} records across {len(years)} years")
    
    # Group by year and save to separate files
    for year in years:
        year_df = df[df['Year'] == year].copy()
        # Remove the Year column before saving (as it wasn't in the original data)
        year_df = year_df.drop(columns=['Year'])
        
        # Create output file path
        output_file = os.path.join(output_dir, f"data_{int(year)}.xlsx")
        
        # Save to Excel
        year_df.to_excel(output_file, index=False)
        print(f"Saved {len(year_df)} records for year {int(year)} to {output_file}")
    
    print(f"Successfully processed data and saved {len(years)} files to the '{output_dir}' folder")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found. Please check the file path and try again.")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")