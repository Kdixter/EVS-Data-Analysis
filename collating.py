import pandas as pd

# Load your combined CSV
df = pd.read_csv('combined_data.csv')

# Group by grid_id
aggregated = df.groupby('grid_id').agg({
    'Impervious_surfaces_2010': 'first',
    'NUMBER_OF_SPECIES_2010': 'mean',
    'Impervious_surfaces_2015': 'first',
    'NUMBER_OF_SPECIES_2015': 'mean',
    'Impervious_surfaces_2020': 'first',
    'NUMBER_OF_SPECIES_2020': 'mean'
}).reset_index()

# Save to new CSV
aggregated.to_csv('averaged_by_grid_id.csv', index=False)
