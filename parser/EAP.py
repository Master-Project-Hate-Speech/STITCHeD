import json
import pandas as pd

config = r'..\config_eng_spa.csv'
df = pd.read_csv(config)

dataset_file_name = 'hs_AsianPrejudice_20kdataset_cleaned_anonymized.tsv'
label_name_definition = {
    'expert':''#need rename
}

new_row = {
    'dataset_file_name': dataset_file_name,
    'dataset_name': 'EAP',
    'label_name_definition': json.dumps(label_name_definition),
    'source': '@Twitter',
    'language': '@eng',
    'text': 'text.clean'
}

new_row = pd.DataFrame([new_row])

df = pd.concat([df, new_row], ignore_index=True)
df.to_csv(config, index=False)