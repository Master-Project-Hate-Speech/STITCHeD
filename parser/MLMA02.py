import pandas as pd
import os
path = r'..\original_data\MLMA02'
files = ['ar_dataset.csv','en_dataset.csv','fr_dataset.csv']

for file in files:
    file_path = os.path.join(path, file)
    data = pd.read_csv(file_path)
    language = {'ar':'ara','en':'eng','fr':'fra'}
    data['language'] = language[file.split('_')[0]]
    csv_path = os.path.join(r'..\data', file)
    data.to_csv(csv_path, index=False)

import json
config = r'..\config_eng_spa.csv'
df = pd.read_csv(config)

dataset_file_name = ';'.join(files)
label_name_definition = {
    'sentiment':'the hostility type of the tweet'
}

new_row = {
    'dataset_file_name': dataset_file_name,
    'dataset_name': 'MLMA02',
    'label_name_definition': json.dumps(label_name_definition),
    'source': '@Twitter',
    'language': 'language',
    'text': 'tweet'
}

new_row = pd.DataFrame([new_row])

df = pd.concat([df, new_row], ignore_index=True)
df.to_csv(config, index=False)