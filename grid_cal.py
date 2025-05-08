import numpy as np

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
            grid_cells.append(cell)

    return grid_cells

# Define the bounding box for Bengaluru Urban + Rural
bengaluru_bounds = (77.18155967598723, 12.386521429543823, 78.12089073067473, 13.622870023243257)
delta = 0.0225
grid = create_grid(bengaluru_bounds, delta)

# Write to a text file
output_file = "bengaluru_grid_cells.txt"
with open(output_file, "w") as f:
    for idx, cell in enumerate(grid):
        cell_str = ', '.join([f"[{lon:.6f}, {lat:.6f}]" for lon, lat in cell])
        f.write(f"Cell {idx + 1}: {cell_str}\n")

print(f"Grid cell coordinates written to '{output_file}'")

