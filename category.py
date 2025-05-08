import pandas as pd
import ast
import re

# === Step 1: Load species data ===
species_df = pd.read_csv("temp_anal.csv")  # Replace with your actual file name

# === Step 2: Load and parse cell bounds from TXT ===
cell_bounds = []
with open("bengaluru_grid_cells.txt", "r") as f:  # Replace with your actual file name
    for line in f:
        match = re.match(r"Cell\s+(\d+):\s+(.*)", line.strip())
        if match:
            cell_id = int(match.group(1))
            coord_strs = match.group(2).split("],")
            coords = [ast.literal_eval(coord.strip() + ("]" if not coord.strip().endswith("]") else "")) for coord in coord_strs]
            lons = [c[0] for c in coords]
            lats = [c[1] for c in coords]
            cell_bounds.append({
                'cell_id': cell_id,
                'min_lon': min(lons),
                'max_lon': max(lons),
                'min_lat': min(lats),
                'max_lat': max(lats)
            })

# === Step 3: Function to match point to cell ===
def find_cell(lat, lon, cells):
    for cell in cells:
        if cell['min_lon'] <= lon <= cell['max_lon'] and cell['min_lat'] <= lat <= cell['max_lat']:
            return cell['cell_id']
    return None

# === Step 4: Assign cells to 2010 and 2020 points ===
species_df["2010_Assigned_Cell"] = species_df.apply(
    lambda row: find_cell(row["2010_POINT_LATITUDE"], row["2010_POINT_LONGITUDE"], cell_bounds), axis=1)

species_df["2020_Assigned_Cell"] = species_df.apply(
    lambda row: find_cell(row["2020_POINT_LATITUDE"], row["2020_POINT_LONGITUDE"], cell_bounds), axis=1)

# === Step 5: Save results ===
species_df.to_csv("FINAL_1.csv", index=False)
print("✅ Done!")
