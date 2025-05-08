import csv
import re
import os
import pandas as pd

def parse_bounds_from_txt(txt_file_path):
    """
    Parse the bounds information from the text file.
    Returns a dictionary mapping cell number to bounds coordinates.
    """
    cell_bounds = {}
    
    with open(txt_file_path, 'r') as file:
        for line in file:
            # Extract cell number and coordinates using regex
            match = re.match(r'Cell\s+(\d+):\s+(.*)', line.strip())
            if match:
                cell_number = match.group(1)
                bounds_text = match.group(2)
                
                # Store the bounds text as is
                cell_bounds[cell_number] = bounds_text
    
    return cell_bounds

def update_csv_with_bounds(csv_file_path, cell_bounds, output_csv_path):
    """
    Read the CSV file, add bounds information, and write to a new CSV file.
    """
    # Read the CSV using pandas for easier handling
    df = pd.read_csv(csv_file_path)
    
    # Convert Cell column to string for matching
    df['Cell'] = df['Cell'].astype(str)
    
    # Add a new column for bounds
    df['bounds'] = df['Cell'].map(cell_bounds)
    
    # Write to new CSV file
    df.to_csv(output_csv_path, index=False)
    
    return len(df[df['bounds'].notna()])

def main():
    # Input file paths
    csv_file_path = input("Enter the path to your CSV file: ")
    txt_file_path = input("Enter the path to your text file with bounds: ")
    
    # Output file path
    output_dir = os.path.dirname(csv_file_path)
    output_file = os.path.join(output_dir, "updated_" + os.path.basename(csv_file_path))
    
    # Parse bounds from text file
    print("Parsing bounds from text file...")
    cell_bounds = parse_bounds_from_txt(txt_file_path)
    print(f"Found bounds for {len(cell_bounds)} cells")
    
    # Update CSV with bounds
    print("Updating CSV with bounds information...")
    matches = update_csv_with_bounds(csv_file_path, cell_bounds, output_file)
    
    print(f"Successfully matched {matches} cells with bounds")
    print(f"Updated CSV saved to: {output_file}")

if __name__ == "__main__":
    main()