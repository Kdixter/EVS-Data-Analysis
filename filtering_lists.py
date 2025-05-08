import pandas as pd

def parse_grid_cells(file_path):
    """
    Parses the grid_cells_with_data.txt file and returns a list of bounding boxes.
    Each bounding box is a tuple: (lon_min, lat_min, lon_max, lat_max)
    """
    import re
    grid_cells = []
    with open(file_path, 'r') as f:
        for line in f:
            try:
                # Extract all coordinate pairs using regex
                coords = re.findall(r"\[([0-9\.\-]+),\s*([0-9\.\-]+)\]", line)
                corners = [(float(lon), float(lat)) for lon, lat in coords]
                if len(corners) != 4:
                    continue  # Skip malformed or incomplete lines
                lons = [pt[0] for pt in corners]
                lats = [pt[1] for pt in corners]
                lon_min, lon_max = min(lons), max(lons)
                lat_min, lat_max = min(lats), max(lats)
                grid_cells.append((lon_min, lat_min, lon_max, lat_max))
            except Exception as e:
                print(f"Skipping line due to error: {e}\nLine: {line}")
                continue
    return grid_cells

def is_point_in_any_cell(lon, lat, grid_cells):
    for lon_min, lat_min, lon_max, lat_max in grid_cells:
        if lon_min <= lon < lon_max and lat_min <= lat < lat_max:
            return True
    return False

# --- Step 1: Load grid cells from txt ---
grid_cells_file = "grid_cells_with_data.txt"
grid_cells = parse_grid_cells(grid_cells_file)

# --- Step 2: Load the new dataset ---
input_csv = "data_2020_CSV_updated.csv"  # replace with your actual CSV path
df = pd.read_csv(input_csv)

# --- Step 3: Filter entries based on grid cells ---
filtered_df = df[df.apply(lambda row: is_point_in_any_cell(row['LONGITUDE'], row['LATITUDE'], grid_cells), axis=1)]

# --- Step 4: Write filtered entries to a new CSV ---
output_csv = "updated_2020_birds.csv"
filtered_df.to_csv(output_csv, index=False)

print(f"Filtered data written to '{output_csv}'")
