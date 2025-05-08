import numpy as np
import pandas as pd

def create_grid(bounds, delta):
    min_lon, min_lat, max_lon, max_lat = bounds
    lon_count = int(np.round((max_lon - min_lon) / delta))
    lat_count = int(np.round((max_lat - min_lat) / delta))

    grid_cells = []
    for i in range(lon_count):
        for j in range(lat_count):
            lon1 = min_lon + i * delta
            lat1 = min_lat + j * delta
            lon2 = lon1 + delta
            lat2 = lat1 + delta
            cell = [[lon1, lat1], [lon2, lat1], [lon2, lat2], [lon1, lat2]]
            grid_cells.append((i, j, cell))  # Include grid index (i,j) for reference
    return grid_cells

def point_in_cell(lon, lat, cell):
    lon_min = cell[0][0]
    lat_min = cell[0][1]
    lon_max = cell[2][0]
    lat_max = cell[2][1]
    return lon_min <= lon < lon_max and lat_min <= lat < lat_max

# --- Load CSV ---
csv_path = "2010_data_CSV.csv"  # Replace with CSV file path
df = pd.read_csv(csv_path)

# --- Grid Config ---
bengaluru_bounds = (77.18155967598723, 12.386521429543823, 78.12089073067473, 13.622870023243257)
delta = 0.0225
grid = create_grid(bengaluru_bounds, delta)

# --- Find cells with data points ---
cells_with_data = set()
for _, row in df.iterrows():
    lon, lat = row['LONGITUDE'], row['LATITUDE']
    for i, j, cell in grid:
        if point_in_cell(lon, lat, cell):
            cells_with_data.add((i, j))  # Store the grid cell index
            break

# --- Write result to a file ---
output_file = "grid_cells_with_data.txt"
with open(output_file, "w") as f:
    for i, j in sorted(cells_with_data):
        lon1 = bengaluru_bounds[0] + i * delta
        lat1 = bengaluru_bounds[1] + j * delta
        lon2 = lon1 + delta
        lat2 = lat1 + delta
        corners = [[lon1, lat1], [lon2, lat1], [lon2, lat2], [lon1, lat2]]
        corner_str = ', '.join([f"[{lon:.6f}, {lat:.6f}]" for lon, lat in corners])
        f.write(f"Grid Cell ({i}, {j}): {corner_str}\n")

print(f"Written grid cells with data to '{output_file}'")
