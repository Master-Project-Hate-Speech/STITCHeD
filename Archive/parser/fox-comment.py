# fox-comment
import os
import pandas as pd

path = r'../original_data'
folder = os.path.join(path, 'annotated-threads')


def extract_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()
        data = []
        for l in lines:
            # append the row list as a record
            data.append([l.strip().split(':')[1], l.strip().split(':')[0]])
        return data


file = os.path.join(folder, 'all-comments.txt')
data = extract_file(file)
columns = ["text", "hateful"]
df = pd.DataFrame(data, columns=columns)
path = r'../data'
csv_file = 'fox-comment.csv'
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
    'dataset_name': 'fox-comment',
    'label_name_definition': json.dumps(label_name_definition),
    'source': '@FoxNews',
    'language': '@eng',
    'text': 'text'
}

new_row = pd.DataFrame([new_row])

df = pd.concat([df, new_row], ignore_index=True)
df.to_csv(config, index=False)
