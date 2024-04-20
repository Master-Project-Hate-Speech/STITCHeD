import sqlite3

path = 'H:\\UZH\\Master Project\\Data-Pipeline'
database_name = 'hate_speech_data.db'
conn = sqlite3.connect(path + '\\' + database_name)
c = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON")
#%%
c.execute('''
CREATE TABLE IF NOT EXISTS dataset (
    datasetID INTEGER PRIMARY KEY,
    datasetOriginalName TEXT,
    datasetName TEXT
)
''')
#%%
c.execute('''
CREATE TABLE IF NOT EXISTS schema (
    datasetID INTEGER,
    labelName TEXT,
    FOREIGN KEY(datasetID) REFERENCES dataset(datasetID)
)
''')
#%%
c.execute('''
CREATE TABLE IF NOT EXISTS text (
    textID INTEGER,
    datasetID INTEGER,
    sourceID INTEGER,
    text TEXT,
    PRIMARY KEY (textID, datasetID),
    FOREIGN KEY(datasetID) REFERENCES dataset(datasetID)
)
''')
#%%
c.execute('''
CREATE TABLE IF NOT EXISTS label (
    datasetID INTEGER,
    textID INTEGER,
    labelName TEXT,
    labelValue TEXT,
    labelDefinition TEXT,
    PRIMARY KEY (datasetID, textID, labelName),
    FOREIGN KEY(datasetID, textID) REFERENCES text(datasetID, textID)
)
''')
#%%
c.execute('''
CREATE TABLE IF NOT EXISTS textSource (
    sourceID INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT
)
''')
#%%
conn.close()