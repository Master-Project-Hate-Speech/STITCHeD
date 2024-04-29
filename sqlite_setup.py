import sqlite3

path = 'H:\\UZH\\Master Project\\Data-Pipeline'
database_name = 'hate_speech_data.db'
conn = sqlite3.connect(path + '\\' + database_name)
# path = 'hate_speech.db'
# conn = sqlite3.connect(path)
c = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON")
#%%
c.execute('''
CREATE TABLE IF NOT EXISTS dataset (
datasetID INTEGER PRIMARY KEY AUTOINCREMENT,
datasetOriginalName TEXT NOT NULL UNIQUE,
datasetName TEXT NOT NULL UNIQUE,
originalPaper TEXT)
''')
#%%
c.execute('''
CREATE TABLE IF NOT EXISTS schema (
    datasetID INTEGER PRIMARY KEY,
    labelName TEXT,
    FOREIGN KEY(datasetID) REFERENCES dataset(datasetID)
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
c.execute('''
CREATE TABLE IF NOT EXISTS language (
    languageID INTEGER PRIMARY KEY AUTOINCREMENT,
    language TEXT UNIQUE
)
''')
#%%
c.execute('''
CREATE TABLE IF NOT EXISTS text (
    datasetID INTEGER,
    textID INTEGER,
    sourceID INTEGER,
    languageID INTEGER,
    text TEXT,
    PRIMARY KEY (datasetID, textID),
    FOREIGN KEY(datasetID) REFERENCES dataset(datasetID)
    FOREIGN KEY(sourceID) REFERENCES textSource(sourceID)
    FOREIGN KEY(languageID) REFERENCES language(languageID)
)
''')
#%%
c.execute('''
CREATE TABLE IF NOT EXISTS label (
    datasetID INTEGER NOT NULL,
    textID INTEGER NOT NULL,
    labelName TEXT NOT NULL,
    labelValue TEXT NOT NULL,
    labelDefinition TEXT,
    PRIMARY KEY (datasetID, textID, labelName),
    FOREIGN KEY(datasetID, textID) REFERENCES text(datasetID, textID)
)
''')
#%%
conn.close()