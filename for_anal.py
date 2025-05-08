import pandas as pd

# Load your CSV
df = pd.read_csv('averaged_by_grid_id.csv')

# Add new columns for changes
df["Change in Impervious_surfaces"] = df["Impervious_surfaces_2020"] - df["Impervious_surfaces_2010"]
df["Change in NUMBER_OF_SPECIES"] = df["NUMBER_OF_SPECIES_2020"] - df["NUMBER_OF_SPECIES_2010"]

# Save the updated CSV
df.to_csv('updated_with_changes.csv', index=False)
