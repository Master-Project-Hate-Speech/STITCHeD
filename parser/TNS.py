import pandas as pd

# Define the file paths
xlsx_file_path = '../data/Türkçe Nefret Söylemi Veri Seti v1.xlsx'
csv_file_path = '../data/TNS.csv'
sheet_name = '1000 Tweet'  # Replace with the actual sheet name

# Read the specific sheet
df = pd.read_excel(xlsx_file_path, sheet_name=sheet_name, engine='openpyxl')

# Optionally, select a specific range or table within the sheet
# Assuming the table starts from row 2 to the end, and columns A to D (0-based indexing)
# Adjust the range based on your table's actual location
df_table = df.iloc[1:, 0:4]  # Adjust the row and column slicing as needed

# Write the DataFrame to a CSV file
df_table.to_csv(csv_file_path, index=False)

print(f"Converted table from sheet '{sheet_name}' to {csv_file_path} successfully.")

