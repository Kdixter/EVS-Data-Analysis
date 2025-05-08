import pandas as pd
import re

def parse_grid_cells(file_path):
    grid_cells = []
    with open(file_path, 'r') as f:
        for line in f:
            try:
                coords = re.findall(r"\[([0-9\.\-]+),\s*([0-9\.\-]+)\]", line)
                corners = [(float(lon), float(lat)) for lon, lat in coords]
                if len(corners) != 4:
                    continue
                lons = [pt[0] for pt in corners]
                lats = [pt[1] for pt in corners]
                lon_min, lon_max = min(lons), max(lons)
                lat_min, lat_max = min(lats), max(lats)
                grid_cells.append({
                    "bbox": (lon_min, lat_min, lon_max, lat_max),
                    "id": f"{lon_min:.6f}_{lat_min:.6f}"  # unique ID for grouping
                })
            except Exception as e:
                print(f"Skipping line due to error: {e}\nLine: {line}")
                continue
    return grid_cells

def get_cell_id(lon, lat, grid_cells):
    for cell in grid_cells:
        lon_min, lat_min, lon_max, lat_max = cell["bbox"]
        if lon_min <= lon < lon_max and lat_min <= lat < lat_max:
            return cell["id"]
    return None

# --- Load grid cells ---
grid_cells_file = "grid_cells_with_data.txt"
grid_cells = parse_grid_cells(grid_cells_file)

# --- Load new data CSV ---
input_csv = "data_2020_CSV_updated.csv"
df = pd.read_csv(input_csv)

# --- Tag each row with cell ID (or None if outside all cells) ---
df["grid_cell_id"] = df.apply(
    lambda row: get_cell_id(row["LONGITUDE"], row["LATITUDE"], grid_cells),
    axis=1
)

# --- Drop rows outside all grid cells ---
df = df.dropna(subset=["grid_cell_id"])

# --- Keep max 25 per cell ---
filtered_df = df.groupby("grid_cell_id").head(60).drop(columns=["grid_cell_id"])

# --- Save to CSV ---
output_csv = "2020_BIRDS_data_max4_9.csv"
filtered_df.to_csv(output_csv, index=False)

print(f"Saved limited filtered data to '{output_csv}'")
