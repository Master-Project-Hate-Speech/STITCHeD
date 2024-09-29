import pandas as pd
path = "path"
# df_en = pd.read_csv(path + "Dynamically Generated Hate Dataset v0.2.3.csv")
# df_de = pd.read_csv(path + "gahd.csv")
df = pd.read_csv(path + "multilingual_all_data.csv") # Generate using pipeline
#%%
df = df[df['label_name'] == 'label']
df['label_value'] = df['label_value'].replace({'hate': 1, 'nothate': 0})
#%%
from sampling import balanced_downsampling
resampled_df = balanced_downsampling(df, 'label_value', second_col='language')
resampled_df['label_value'] = resampled_df['label_value'].astype(int)

label_value_dist = len(resampled_df[resampled_df['label_value'] == 1]) / len(resampled_df)
language_dist_eng = len(resampled_df[resampled_df['language'] == 'eng']) / len(resampled_df)
language_dist_ger = len(resampled_df[resampled_df['language'] == 'ger']) / len(resampled_df)

print(f"Distribution of label_value == 1: {label_value_dist}")
print(f"Distribution of language == 'eng': {language_dist_eng}")
print(f"Distribution of language == 'ger': {language_dist_ger}")
#%%
df_en = resampled_df[resampled_df['language'] == 'eng']
df_de = resampled_df[resampled_df['language'] == 'ger']

resampled_df.to_csv("FINAL_resampled_multilingual_all_data.csv", index = False)

