import pandas as pd
from scipy.stats import shapiro

# Load CSV file
df = pd.read_csv("2020_BIRDS_data_max_60.csv")  

# Extract the relevant column
column_name = "SAMPLING EVENT IDENTIFIER"
data = df[column_name].dropna()  # Drop missing values

# Ensure it's numeric
data = pd.to_numeric(data, errors='coerce').dropna()

# Apply Shapiro-Wilk Test
stat, p = shapiro(data)
print(f"Shapiro-Wilk Test:\nStatistic = {stat:.4f}, p-value = {p:.4f}")

# Interpretation
if p > 0.05:
    print("Data appears to be normally distributed (fail to reject H0).")
else:
    print("Data is not normally distributed (reject H0).")
