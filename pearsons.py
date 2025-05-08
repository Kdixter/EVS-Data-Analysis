import pandas as pd
from scipy.stats import pearsonr

# Load the CSV
df = pd.read_csv("species_with_deltas.csv")

# Ensure numeric types
df["delta_IM"] = pd.to_numeric(df["delta_IM"], errors='coerce')
df["delta_SPECIES"] = pd.to_numeric(df["delta_SPECIES"], errors='coerce')

# Combine both 2010 and 2020 assigned cells to group by either
cell_col = "2020_Assigned_Cell"  # Or "2010_Assigned_Cell" if preferred

# Drop rows with missing cell assignments or NaNs
df = df.dropna(subset=[cell_col, "delta_IM", "delta_SPECIES"])

# Group by cell and compute Pearson r
results = []

for cell_id, group in df.groupby(cell_col):
    if len(group) >= 2:
        r, p = pearsonr(group["delta_IM"], group["delta_SPECIES"])
        results.append({"Cell": cell_id, "r_value": r, "p_value": p, "n_points": len(group)})
    else:
        results.append({"Cell": cell_id, "r_value": None, "p_value": None, "n_points": len(group)})

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Save or print results
results_df.to_csv("cellwise_pearson_r.csv", index=False)
print("✅ Pearson r-values saved to 'cellwise_pearson_r.csv'")
