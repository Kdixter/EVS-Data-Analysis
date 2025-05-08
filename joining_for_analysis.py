import pandas as pd

# File paths
csv1_path = "joined_2010.csv"  
csv2_path = "joined_2020.csv"  

# Columns to keep (base names)
fields = [
    "system:index", "Impervious_surfaces", "Latitude", "Longitude",
    "SAMPLING_EVENT_IDENTIFIER", "NUMBER_OF_SPECIES", "POINT_LATITUDE", "POINT_LONGITUDE"
]

# Load both CSVs with selected columns
df_2010 = pd.read_csv(csv1_path, usecols=fields)
df_2020 = pd.read_csv(csv2_path, usecols=fields)

# Rename columns with prefixes
df_2010 = df_2010.add_prefix("2010_")
df_2020 = df_2020.add_prefix("2020_")

# Concatenate side by side (column-wise)
merged_df = pd.concat([df_2010, df_2020], axis=1)

# Save the result
merged_df.to_csv("temp_anal.csv", index=False)
print("saved")
