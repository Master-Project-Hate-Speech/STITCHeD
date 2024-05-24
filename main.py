import argparse

import pandas as pd
from dataTransformation import DataFrameConverter
from sqlite_setup import create_tables
from read_data import read_table, read_all_tables
from delete_data import clear_tables
import myGlobals
from queryInterface import QueryInterface
conn = myGlobals.connect()
clear_tables(conn)
create_tables(conn)

def insert_data(conn, df, table_name):
    df.to_sql(table_name, conn, if_exists='append', index=False)
    # try:
    #     df.to_sql(table_name, conn, if_exists='append', index=False)
    # except Exception as e:
    #     print(f"TABLE {table_name}:\n{df}")
    #     print(e)
def storage_datasets(config):
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

            print(f"{file_name} Insertion Complete")

from readConfig import final_config
from readConfig import read_dataframe

if __name__ == '__main__':
    config_path = "config_new.csv"
    data_folder = "./data"

    parser = argparse.ArgumentParser(description= "Command line checking config legitimacy and store into database")

    parser.add_argument("--config_path", type=str, required=True, help="Path to config file")
    parser.add_argument("--data_folder_path", type=str, required=True, help="Path to data folder")

    parser.add_argument("--insert_db", action='store_true', help="Insert datasets into db after check-up")

    args = parser.parse_args()

    config = final_config(args.config_path, args.data_folder_path)
    # config = final_config("config_new.csv", "./data")
    if args.insert_db:
        storage_datasets(config)

    # Print the arguments to demonstrate
    print(f"Config Path: {args.config_path}")
    print(f"Data Folder: {args.data_folder_path}")
    print(f"Insert Flag: {args.insert_db}")

    '''
        CommandLine:
        Check the config AND Save into db if successful:
            python main.py --config_path config_new.csv --data_folder_path ./data --insert_db
        Check the config:
            python main.py --config_path config_new.csv --data_folder_path ./data
    '''

            # try:
            #     df = read_dataframe(full_path)
            #     converter = DataFrameConverter(row, df, conn)
            #     formatted_df = converter.format_for_sql()
            #     print(formatted_df)
            # except FileNotFoundError:
            #     print(f"File not found: {full_path}")
            # except Exception as e:
            #     print(f"An error occurred: {e}")
    # read_all_tables(conn)
