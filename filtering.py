import pandas as pd
import numpy as np

# Load the eBird data
# Replace 'your_file.xlsx' with your actual file path
file_path = 'Bird_data_1.xlsx'
df = pd.read_excel(file_path)

# Keep only the fields we're interested in
columns_to_keep = [
    'SAMPLING EVENT IDENTIFIER', 
    'LATITUDE', 
    'LONGITUDE', 
    'COMMON NAME', 
    'SCIENTIFIC NAME', 
    'TAXON CONCEPT ID', 
    'OBSERVATION DATE',
    'OBSERVATION COUNT'
]

# Check if all columns exist in the dataframe
missing_columns = [col for col in columns_to_keep if col not in df.columns]
if missing_columns:
    print(f"Warning: These columns are missing from the dataframe: {missing_columns}")
    # Only keep columns that exist in the dataframe
    columns_to_keep = [col for col in columns_to_keep if col in df.columns]

# Filter the dataframe to keep only these columns
filtered_df = df[columns_to_keep].copy()

# Calculate the number of unique species per checklist
species_count_per_checklist = filtered_df.groupby('SAMPLING EVENT IDENTIFIER')['TAXON CONCEPT ID'].nunique().reset_index()
species_count_per_checklist.rename(columns={'TAXON CONCEPT ID': 'NUMBER OF SPECIES'}, inplace=True)

# Merge the species count back into the main dataframe
result_df = pd.merge(filtered_df, species_count_per_checklist, on='SAMPLING EVENT IDENTIFIER', how='left')

# Since this merge will duplicate the species count for each species in a checklist,
# we can also create a summary dataframe that has one row per checklist
checklist_summary = filtered_df.groupby('SAMPLING EVENT IDENTIFIER').agg({
    'LATITUDE': 'first',  # Take the first lat/long value for each checklist
    'LONGITUDE': 'first',
    'OBSERVATION DATE': 'first'
}).reset_index()

# Merge the species count into this summary
checklist_summary = pd.merge(checklist_summary, species_count_per_checklist, on='SAMPLING EVENT IDENTIFIER')

# Save the results
result_df.to_excel('filtered_ebird_data_with_species_count.xlsx', index=False)
checklist_summary.to_excel('ebird_checklist_summary_1.xlsx', index=False)

print("Processing complete!")
print(f"Full data saved to 'filtered_ebird_data_with_species_count.xlsx'")
print(f"Checklist summary saved to 'ebird_checklist_summary.xlsx'")