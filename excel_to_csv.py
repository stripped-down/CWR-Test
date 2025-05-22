import pandas as pd
import os
import re

# File path
excel_file = 'CWR CISAC Doc/CWR22-0145_CWR_3.1_Lookup_Table_r0_2022-02-03_EN.xlsx'

# Extract a clean reference from the Excel filename
excel_basename = os.path.basename(excel_file)
# Remove extension and clean up
excel_ref = re.sub(r'\.xlsx$', '', excel_basename)
# Create a shorter, cleaner reference
excel_ref = 'CWR3.1_' + re.sub(r'[^a-zA-Z0-9]', '_', excel_ref)[:20]

# Output directory
output_dir = 'csv_output'
os.makedirs(output_dir, exist_ok=True)

# Read all sheets from Excel file
print(f"Reading Excel file: {excel_file}")
all_sheets = pd.read_excel(excel_file, sheet_name=None)

# Convert each sheet to CSV
print(f"Found {len(all_sheets)} sheets. Converting to CSV files...")
for sheet_name, df in all_sheets.items():
    # Clean the sheet name for filename
    clean_name = sheet_name.replace(' ', '_').replace('/', '_')
    csv_filename = os.path.join(output_dir, f"{excel_ref}_{clean_name}.csv")
    df.to_csv(csv_filename, index=False)
    print(f"Created: {csv_filename}")

print("Conversion complete!") 