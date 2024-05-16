import pandas as pd
from dataTransformation import DataFrameConverter
from sqlite_setup import create_tables
from read_data import read_table, read_all_tables
import myGlobals
conn = myGlobals.connect()
create_tables(conn)
read_all_tables(conn)

# df = pd.read_csv("./OLID_2019/olid-training-v1.0.tsv", sep="\t")
# converter = DataFrameConverter(df, conn)
# ## dictionary key:table name; value:df
# formatted_df = converter.format_for_sql()
# def insert_data(conn, df, table_name):
#     try:
#         df.to_sql(table_name, conn, if_exists='append', index=False)
#     except Exception as e:
#         print(e)

# for k,v in formatted_df.items():
#     insert_data(conn, v, k)
#     conn.commit()

# # conn = myGlobals.connect()
# read_all_tables(conn)


from readConfig import final_config
from readConfig import read_dataframe
config_path = "config.csv"
data_folder = "./data"

config = final_config(config_path, data_folder)
for index, row in config.iterrows():
    file_names = row['dataset_file_name'].split(', ')
    
    for file_name in file_names:
        full_path = data_folder + '/' + file_name.strip()  
        try:
            df = read_dataframe(full_path)
            converter = DataFrameConverter(row, df, conn)
            formatted_df = converter.format_for_sql()
            print(formatted_df)
        except FileNotFoundError:
            print(f"File not found: {full_path}")
        except Exception as e:
            print(f"An error occurred: {e}")