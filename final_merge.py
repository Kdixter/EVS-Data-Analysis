import pandas as pd
# Load each CSVs
df_2010 = pd.read_csv('filtered_output_2010.csv').rename(columns={
    'Impervious_surfaces': 'Impervious_surfaces_2010',
    'NUMBER_OF_SPECIES': 'NUMBER_OF_SPECIES_2010'
})

df_2015 = pd.read_csv('filtered_output_2015.csv').rename(columns={
    'Impervious_surfaces': 'Impervious_surfaces_2015',
    'NUMBER_OF_SPECIES': 'NUMBER_OF_SPECIES_2015'
})

df_2020 = pd.read_csv('filtered_output_2020.csv').rename(columns={
    'Impervious_surfaces': 'Impervious_surfaces_2020',
    'NUMBER_OF_SPECIES': 'NUMBER_OF_SPECIES_2020'
})

# Merge all dataframes on 'grid_id'
merged_df = df_2010.merge(df_2015, on='grid_id').merge(df_2020, on='grid_id')

# Save the result
merged_df.to_csv('combined_data.csv', index=False)
