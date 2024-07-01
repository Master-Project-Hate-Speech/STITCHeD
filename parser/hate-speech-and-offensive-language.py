import pandas as pd
original_file_path = '.\\original_data\\'
file_path = '.\\data\\'

df = pd.read_csv(original_file_path + 'labeled_data.csv')
replace_values = {1: 'hate_speech', 2: 'offensive_language', 0: 'neither'}
df['class'] = df['class'].replace(replace_values)

df.to_csv(file_path + 'HSAOL.csv', index = False)
