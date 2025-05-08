import pandas as pd
import json
from shapely.geometry import Point, Polygon
import numpy as np

# Function to check if a point is within a polygon
def is_point_in_polygon(point, polygon_json):
    try:
        # Parse the GeoJSON
        geojson = json.loads(polygon_json)
        
        # Extract coordinates
        coords = geojson["coordinates"][0]
        
        # Create shapely polygon
        polygon = Polygon(coords)
        
        # Check if point is within polygon
        return polygon.contains(point)
    except Exception as e:
        print(f"Error processing polygon: {e}")
        return False

# Load CSVs
df_l = pd.read_csv('data_LULC_grid_2020.csv')
df_s = pd.read_csv('2020_BIRDS_data_max_60.csv')

# Initialize a list to store the matches
matches = []

# Create Point objects from the CSV_S data
for idx_s, row_s in df_s.iterrows():
    point = Point(row_s['LONGITUDE'], row_s['LATITUDE'])
    
    # Check each polygon in CSV_L
    for idx_l, row_l in df_l.iterrows():
        if is_point_in_polygon(point, row_l['.geo']):
            # Add matching row from CSV_L along with data from CSV_S
            match_data = {
                # Fields from CSV_L
                'system:index': row_l['system:index'],
                'Bare_areas': row_l['Bare_areas'],
                'Cropland': row_l['Cropland'],
                'Forest': row_l['Forest'],
                'Grassland': row_l['Grassland'],
                'Impervious_surfaces': row_l['Impervious_surfaces'],
                'Latitude': row_l['Latitude'],
                'Longitude': row_l['Longitude'],
                'Permanent_ice_and_snow': row_l['Permanent_ice_and_snow'],
                'Shrubland': row_l['Shrubland'],
                'Water_body': row_l['Water_body'],
                'Wetlands': row_l['Wetlands'],
                'grid_id': row_l['grid_id'],
                '.geo': row_l['.geo'],
                
                # Fields from CSV_S
                'SAMPLING_EVENT_IDENTIFIER': row_s['SAMPLING EVENT IDENTIFIER'],
                'OBSERVATION_DATE': row_s['OBSERVATION DATE'],
                'NUMBER_OF_SPECIES': row_s['NUMBER OF SPECIES'],
                'POINT_LATITUDE': row_s['LATITUDE'],
                'POINT_LONGITUDE': row_s['LONGITUDE']
            }
            matches.append(match_data)

# Create the result dataframe
if matches:
    df_j = pd.DataFrame(matches)
    
    # Save to CSV
    df_j.to_csv('joined_2020.csv', index=False)
    print(f"Successfully created CSV_J.csv with {len(df_j)} records")
else:
    print("No matches found between the datasets")