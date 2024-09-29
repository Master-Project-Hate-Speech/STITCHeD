import os
import pandas as pd

path = r'../original_data'
file = 'HateNet_labeled_corpus_6K.txt'

file_path = os.path.join(path, file)

with open(file_path, encoding='utf-8') as f:
    lines = f.readlines()
    data = []
    for l in lines:
        data.append(l.strip().split(';||;')[1:])

columns = ["text", "hateful"]
df = pd.DataFrame(data, columns=columns)
path = r'../data'
csv_file = 'HateNet_labeled.csv'
df.to_csv(os.path.join(path,csv_file), index=False)

import json

# write config file
config = r'..\config_eng_spa.csv'
df = pd.read_csv(config)

dataset_file_name = csv_file
label_name_definition = {
    'hateful':'hateful/non-hateful'
}

new_row = {
    'dataset_file_name': dataset_file_name,
    'dataset_name': 'HateNet',
    'label_name_definition': json.dumps(label_name_definition),
    'source': '@Twitter',
    'language': '@spa',
    'text': 'text'
}

new_row = pd.DataFrame([new_row])

df = pd.concat([df, new_row], ignore_index=True)
df.to_csv(config, index=False)