import pandas as pd

# Load the CSV file (update filename as necessary)
df = pd.read_csv("FINAL_2.csv")

# Ensure columns are numeric (handle any string import issues)
df["2010_Impervious_surfaces"] = pd.to_numeric(df["2010_Impervious_surfaces"], errors='coerce')
df["2020_Impervious_surfaces"] = pd.to_numeric(df["2020_Impervious_surfaces"], errors='coerce')
df["2010_NUMBER_OF_SPECIES"] = pd.to_numeric(df["2010_NUMBER_OF_SPECIES"], errors='coerce')
df["2020_NUMBER_OF_SPECIES"] = pd.to_numeric(df["2020_NUMBER_OF_SPECIES"], errors='coerce')

# Create the delta columns
df["delta_IM"] = df["2020_Impervious_surfaces"] - df["2010_Impervious_surfaces"]
df["delta_SPECIES"] = df["2020_NUMBER_OF_SPECIES"] - df["2010_NUMBER_OF_SPECIES"]

# Save to new CSV (or overwrite)
df.to_csv("species_with_deltas.csv", index=False)

print("Done! Added 'delta_IM' and 'delta_SPECIES' columns.")
