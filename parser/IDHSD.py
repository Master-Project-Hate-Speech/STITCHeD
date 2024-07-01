import pandas as pd
import csv

# Define the file paths
txt_file_path = '../data/IDHSD_RIO_unbalanced_713_2017.txt'
csv_file_path = '../data/IDHSD_RIO_unbalanced_713_2017.csv'

# Read the TXT file
with open(txt_file_path, 'r', encoding='utf-8', errors='replace') as txt_file:
    lines = txt_file.readlines()

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Process the first line as header
    header = lines[0].strip().split('\t')  # Adjust the delimiter as necessary
    writer.writerow(header)

    # Process the remaining lines as data rows
    for line in lines[1:]:
        row = line.strip().split('\t')  # Adjust the delimiter as necessary
        writer.writerow(row)

print(f"Converted {txt_file_path} to {csv_file_path} successfully.")

pd.read_csv('../data/IDHSD_RIO_unbalanced_713_2017.csv')