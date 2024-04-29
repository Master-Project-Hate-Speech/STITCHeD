# myGlobals.py
import sqlite3
def connect(path = '.\\hate_speech_data.db'):
    conn = sqlite3.connect(path)
    return conn
