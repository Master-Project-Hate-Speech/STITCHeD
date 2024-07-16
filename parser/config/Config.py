import pandas as pd
import json
from abc import ABC, abstractmethod


class ConfigBase(ABC):
    def __init__(self, config_file, mode='append'):
        self.config = config_file
        self.df = pd.read_csv(self.config)
        self.mode = mode

    @abstractmethod
    def new_row(self, *args, **kwargs):
        pass


class Config(ConfigBase):
    def new_row(self, dataset_file_name, dataset_name, label_name_definition, source, language, text):
        # Read the existing config file
        try:
            df = pd.read_csv(self.config)
        except FileNotFoundError:
            # If the file does not exist, create a new empty DataFrame with the required columns
            df = pd.DataFrame(
                columns=['dataset_file_name', 'dataset_name', 'label_name_definition', 'source', 'language', 'text'])

        assert isinstance(label_name_definition,
                          dict), f"Expected label_name_definition to be a dictionary, got {type(label_name_definition)}"
        # Create a new row dictionary
        new_row = {
            'dataset_file_name': dataset_file_name,
            'dataset_name': dataset_name,
            'label_name_definition': json.dumps(label_name_definition),
            'source': source,
            'language': language,
            'text': text
        }

        # Convert the dictionary to a DataFrame
        new_row_df = pd.DataFrame([new_row])

        if self.mode == 'append':
            # Append the new row to the existing DataFrame
            df = pd.concat([df, new_row_df], ignore_index=True)

        # Save the updated DataFrame back to the config file
        df.to_csv(self.config, index=False)
