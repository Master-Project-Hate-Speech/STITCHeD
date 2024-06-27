import pandas as pd
original_file_path = '.\\original_data\\'
file_path = '.\\data\\'

df1 = pd.read_csv(original_file_path + 'Ethos_Dataset_Binary.csv', sep=';')

df2 = pd.read_csv(original_file_path + 'Ethos_Dataset_Multi_Label.csv', sep=';')
merged_df = pd.merge(df1, df2, on='comment', how='left')

merged_df.to_csv(file_path + 'Ethos_merged.csv', index = False)
