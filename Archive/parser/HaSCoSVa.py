import os
import pandas as pd
import json

file = 'hascosva_2022_anonymized.tsv'

# write config file
config = r'..\config_eng_spa.csv'
df = pd.read_csv(config)

dataset_file_name = file
label_name_definition = {
    'label':'hateful/non-hateful'
}

new_row = {
    'dataset_file_name': dataset_file_name,
    'dataset_name': 'HaSCoSVa',
    'label_name_definition': json.dumps(label_name_definition),
    'source': '@Twitter',
    'language': '@spa',
    'text': 'text'
}

new_row = pd.DataFrame([new_row])

df = pd.concat([df, new_row], ignore_index=True)
df.to_csv(config, index=False)