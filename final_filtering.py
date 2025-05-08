import pandas as pd

# Load your CSV
df = pd.read_csv('joined_2020.csv')

# Keep only the desired columns
filtered_df = df[['grid_id', 'Impervious_surfaces', 'NUMBER_OF_SPECIES']]

# Save to new CSV if needed
filtered_df.to_csv('filtered_output_2020.csv', index=False)
