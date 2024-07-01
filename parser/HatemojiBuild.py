import os
import shutil
import pandas as pd

path = r'..\original_data\HatemojiBuild'
files = ['train.csv','test.csv','validation.csv']

dest_path = r'..\data'
prefix = 'HatemojiBuild_'

dest_files = []

for file in files:
    src_file = os.path.join(path, file)
    dest_file = os.path.join(dest_path, prefix + file)
    dest_files.append(prefix + file)
    if os.path.exists(src_file):
        shutil.copy(src_file, dest_file)

import json
config = r'..\config_eng_spa.csv'
df = pd.read_csv(config)

dataset_file_name = ';'.join(dest_files)
label_name_definition = {
    'label_gold':'The gold standard label (hateful/non-hateful) of the test case.',
    'type':'The type of hate assigned to hateful entries.'
}

new_row = {
    'dataset_file_name': dataset_file_name,
    'dataset_name': 'HatemojiBuild',
    'label_name_definition': json.dumps(label_name_definition),
    'source': '@Dynabench',
    'language': '@eng',
    'text': 'text'
}

new_row = pd.DataFrame([new_row])

df = pd.concat([df, new_row], ignore_index=True)
df.to_csv(config, index=False)

