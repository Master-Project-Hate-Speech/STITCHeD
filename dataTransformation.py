import pandas as pd

class DataFrameConverter:
    def __init__(self, config_df, dataframe, connection):
        self.df = dataframe
        self.conn = connection
        self.formatted_df = {}
        self.config = config_df

    def format_for_sql(self):
        self.__format_dataset()
        self.__format_schema()
        self.__format_source()
        self.__format_language()
        self.__format_text()
        self.__format_label()
        return self.formatted_df
    def __format_dataset(self):
        self.dataset_id = self.__get_rowid("dataset")+1
        dataset_data = {
            "dataset_id": [self.dataset_id],
            'dataset_original_name': [self.config['dataset_file_name']],
            'dataset_name': [self.config['dataset_name']]
        }
        dataset_df = pd.DataFrame(dataset_data)
        self.formatted_df['dataset'] = dataset_df
    def __format_schema(self):
        self.label_columns = list((self.config['label_name_definition']).keys())
        data = {
            "dataset_id": [self.dataset_id] * len(self.label_columns),  # Repeat dataset_id for each label column
            "label_name": self.label_columns
        }
        table_schema = pd.DataFrame(data)
        self.formatted_df['schema'] = table_schema
    def __format_source(self):
        self.source_id = self.__get_rowid("text_source")+1
        text_source_data = {
            "source_id": [self.source_id],
            'source': [self.config['source']]
        }
        text_source_df = pd.DataFrame(text_source_data)
        self.formatted_df['text_source'] = text_source_df
    def __format_language(self):
        self.language_id = self.__get_rowid("language")+1
        language_data = {
            'language': [self.config['language']]
        }
        language_df = pd.DataFrame(language_data)
        self.formatted_df['language'] = language_df
    def __format_text(self):
        self.df["dataset_id"] = self.dataset_id
        self.df.rename(columns={'id': 'text_id',
                    'tweet':'text'
                    }, inplace=True)
        table_text = self.df[['dataset_id', 'text_id', 'text']].drop_duplicates()
        table_text['source_id'] = self.source_id
        table_text['language_id'] = self.language_id
        self.formatted_df['text'] = table_text
    def __format_label(self):
        table_label = pd.DataFrame(columns = ['dataset_id', 'text_id', 'label_name', 'label_value'])
        for col in self.label_columns:
            label_value_pair = {
                'dataset_id': self.df['dataset_id'].values,
                'text_id': self.df['text_id'].values,
                'label_name': [col] * len(self.df),
                'label_value': self.df[col].values
            }
            temp_df = pd.DataFrame(label_value_pair)
            table_label = pd.concat([table_label, temp_df], axis=0, ignore_index=True)
        self.formatted_df['label'] = table_label
    def __get_rowid(self, table_name):
        '''Get the ID of the last inserted record in the specified table'''
        c = self.conn.cursor()
        c.execute("SELECT MAX(rowid) FROM {}".format(table_name))
        last_inserted_id = c.fetchone()[0]
        return last_inserted_id


# ### Configuration

# In[3]:


## information we need to know from Config file
# dataset_id = 1
# label_columns = ["subtask_a", "subtask_b", "subtask_c"]
# source_id = 1

# def get_rowid(conn, table_name):
#     '''Get the ID of the last inserted record in the specified table
#     parameter conn: database connection'''
#     c = conn.cursor()
#     c.execute("SELECT MAX(rowid) FROM {}".format(table_name))
#     last_inserted_id = c.fetchone()[0]
#     return last_inserted_id

# def create_dataset_id(conn):
#     last_inserted_id = get_rowid(conn, "dataset")
#     return last_inserted_id + 1

# def get_text_source_id(conn, text_source):
#     last_inserted_id = get_rowid(conn, "text_source")
#     return last_inserted_id + 1

# def get_language_id(conn, language):
#     last_inserted_id = get_rowid(conn, "language")
#     return last_inserted_id + 1


# Create table ***Schema***

# In[4]:


# Create a DataFrame with the specified columns
# data = {
#     "dataset_id": [dataset_id] * len(label_columns),  # Repeat dataset_id for each label column
#     "label_name": label_columns
# }
#
# table_schema = pd.DataFrame(data)

# def generate_temporary_schema(label_columns):
#     data = {
#         "dataset_id": [dataset_id] * len(label_columns),  # Repeat dataset_id for each label column
#         "label_name": label_columns
#     }
#     table_schema = pd.DataFrame(data)
#     return table_schema

# def call_generate_temporary(table_name, *args):
#     function_name = f'generate_temporary_{table_name}'
#     if function_name in globals() and callable(globals()[function_name]):
#         globals()[function_name](*args)
#     else:
#         print("Unsupported table name.")


# In[5]:


# table_schema


# In[6]:


# df["dataset_id"] = dataset_id
# df.rename(columns={'id': 'text_id',
#                    'tweet':'text'
#                    }, inplace=True)



# In[7]:


# df


# Create Table ***text***

# In[8]:


# table_text = df[['dataset_id', 'text_id', 'text']].drop_duplicates()


# In[9]:


# table_text['source_id'] = source_id


# In[10]:


# table_text


# Create Table ***label***

# In[11]:


# table_label = pd.DataFrame(columns = ['dataset_id', 'text_id', 'label_name', 'label_value'])


# In[12]:

#
# table_label


# In[13]:


# for col in label_columns:
#     label_value_pair = {
#     'dataset_id': df['dataset_id'].values,
#     'text_id': df['text_id'].values,
#     'label_name': [col] * len(df),
#     'label_value': df[col].values
#     }
#     temp_df =  pd.DataFrame(label_value_pair)
#     table_label = pd.concat([table_label, temp_df], axis=0, ignore_index=True)


# In[14]:


# table_label


# ### To-be-discussed

# 1. What to include in the Config JSON file, in which format?
# 2. How to handle the data source, also ask the user to include in the config file?
#     - When coming from different sources?
# 3. label explaination
#     - as a tuple in the config file (label_name, label_explaination), or?

# In[14]:




