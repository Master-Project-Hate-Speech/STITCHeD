import pandas as pd
original_file_path = 'H:\\UZH\\Master Project\\Data-Pipeline\\original_data\\'
file_path = 'H:\\UZH\\Master Project\\Data-Pipeline\\data\\'

df1 = pd.read_csv(original_file_path + 'Ethos_Dataset_Binary.csv', sep=';')
df1.to_csv(file_path + 'Ethos_Dataset_Binary.csv', index = False)

df2 = pd.read_csv(original_file_path + 'Ethos_Dataset_Multi_Label.csv', sep=';')
df2.to_csv(file_path + 'Ethos_Dataset_Multi_Label.csv', index = False)
