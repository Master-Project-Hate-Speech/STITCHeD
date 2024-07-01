import pandas as pd
import numpy as np
original_file_path = '.\\original_data\\'
file_path = '.\\data\\'

df = pd.read_csv(original_file_path + 'german hatespeech refugees.csv')

df['HatespeechOrNot (Aggregated)'] = np.where(
    df['HatespeechOrNot (Expert 1)'] == df['HatespeechOrNot (Expert 2)'], 
    df['HatespeechOrNot (Expert 1)'], 
    np.nan
)


df.to_csv(file_path + 'german hatespeech refugees.csv', index = False)
