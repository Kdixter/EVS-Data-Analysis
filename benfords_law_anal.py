import pandas as pd
import numpy as np

# Load the dataset (just numeric fields)
df = pd.read_csv('averaged_by_grid_id.csv')

# Drop non-numeric or identifier fields
df_numeric = df.drop(columns=['grid_id'])

# Flatten all values into a single series
all_values = df_numeric.values.flatten()

#As this is only foir positive numbers (sell me meth please)
all_values = all_values[~np.isnan(all_values)]
all_values = all_values[all_values > 0]

# Extract first digit
first_digits = [int(str(x)[0]) for x in all_values if str(x)[0].isdigit() and str(x)[0] != '0']

# Count frequency of digits 1–9
freq_table = pd.Series(first_digits).value_counts().sort_index()

# Normalize to get percentage
percentages = freq_table / freq_table.sum() * 100

# Create DataFrame for output
result_df = pd.DataFrame({
    'Digit': freq_table.index,
    'Frequency': freq_table.values,
    'Percentage': percentages.round(2)
})

# Save to CSV
result_df.to_csv('benford_analysis.csv', index=False)
