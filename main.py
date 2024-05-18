import pandas as pd
from dataTransformation import DataFrameConverter
from sqlite_setup import create_tables
from read_data import read_table, read_all_tables
from delete_data import clear_tables
import myGlobals
conn = myGlobals.connect()
clear_tables(conn)
create_tables(conn)

# df = pd.read_csv("./OLID_2019/olid-training-v1.0.tsv", sep="\t")
# converter = DataFrameConverter(df, conn)
# ## dictionary key:table name; value:df
# formatted_df = converter.format_for_sql()
def insert_data(conn, df, table_name):
    df.to_sql(table_name, conn, if_exists='append', index=False)
    # try:
    #     df.to_sql(table_name, conn, if_exists='append', index=False)
    # except Exception as e:
    #     print(f"TABLE {table_name}:\n{df}")
    #     print(e)

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
    file_names = row['dataset_file_name'].split(';')
    first_iter = True
    converter = None
    formatted_df = None
    for file_name in file_names:
        full_path = data_folder + '/' + file_name.strip()
        df = read_dataframe(full_path)
        # create a new converter in the first iter
        if first_iter:
            # print(file_name, "first")
            converter = DataFrameConverter(row, df, conn)
            formatted_df = converter.format_for_sql()
            first_iter = False
        else:
            converter.set_df(df)
            formatted_df = converter.format_for_sql(append=True)
            # formatted_df = {key: pd.concat([formatted_df[key], new_formatted_df[key]], ignore_index=True) for key in formatted_df.keys()}
        # for table_name, df in formatted_df.items():
            # print(f"TABLE {table_name}:\n{df}")
            # print("\n")
        for table_name, df in formatted_df.items():
            insert_data(conn, df, table_name)
            conn.commit()
        # try:
        #     df = read_dataframe(full_path)
        #     converter = DataFrameConverter(row, df, conn)
        #     formatted_df = converter.format_for_sql()
        #     print(formatted_df)
        # except FileNotFoundError:
        #     print(f"File not found: {full_path}")
        # except Exception as e:
        #     print(f"An error occurred: {e}")

read_all_tables(conn)