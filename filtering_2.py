import pandas as pd
import os

# Load the Excel file
input_file = 'ebird_checklist_summary_1.xlsx'  # Change to your actual file name
df = pd.read_excel(input_file)

# Convert 'OBSERVATION DATE' to datetime
df['OBSERVATION DATE'] = pd.to_datetime(df['OBSERVATION DATE'])

# Extract year
df['YEAR'] = df['OBSERVATION DATE'].dt.year

# Create output directory to store year-based files
output_dir = 'separated_by_year_files'
os.makedirs(output_dir, exist_ok=True)

# Save each year's data into a separate file
for year in df['YEAR'].unique():
    year_df = df[df['YEAR'] == year].drop(columns='YEAR')
    output_path = os.path.join(output_dir, f"{year}_data.xlsx")
    year_df.to_excel(output_path, index=False)

print(f"Separate files created for each year in '{output_dir}'")
