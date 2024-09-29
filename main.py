import argparse

from tool.database.setup import setupSchema
import sqlite3
from STITCHED.tool.loader.validator import ConfigValidator
from tool.loader.loader import DataLoader

def parse_arguments():
    parser = argparse.ArgumentParser(description="Command line checking config legitimacy and store into database")
    parser.add_argument("--config_path", type=str, required=True, help="Path to config file")
    parser.add_argument("--data_folder_path", type=str, required=True, help="Path to data folder")
    parser.add_argument("--insert_db", action='store_true', help="Insert datasets into db after check-up")
    return parser.parse_args()


if __name__ == '__main__':
    path = '.\\hate_speech_data.db'
    conn = sqlite3.connect(path)
    setupSchema(conn)

    config_path = "Archive/config_new.csv"
    data_folder = "./data"

    args = parse_arguments()

    validator = ConfigValidator(config_file=config_path, data_folder=data_folder)
    loader = DataLoader(conn=conn, validator=validator)

    if args.insert_db:
        loader.storage_datasets()

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
