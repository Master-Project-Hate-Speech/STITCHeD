import pandas as pd
# Define file paths
parquet_file = '../data/0000.parquet'
csv_file = '../data/MLMA.csv'

# Read Parquet file into pandas DataFrame
df = pd.read_parquet(parquet_file)

# Write DataFrame to CSV file
df.to_csv(csv_file, index=False)

print(f"Converted {parquet_file} to {csv_file} successfully.")
