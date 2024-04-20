import sqlite3

path = 'H:\\UZH\\Master Project\\Data-Pipeline'
database_name = 'hate_speech_data.db'
conn = sqlite3.connect(path + '\\' + database_name)
c = conn.cursor()
#%%
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()

for table_name in tables:
    print(f"Contents of table: {table_name[0]}")
    c.execute(f"SELECT * FROM {table_name[0]}")
    rows = c.fetchall()
    for row in rows:
        print(row)
    print()  
#%%
# def clear_all_data(db_file):
#     conn = sqlite3.connect(db_file)
#     c = conn.cursor()

#     c.execute("SELECT name FROM sqlite_master WHERE type='table'")
#     tables = c.fetchall()

#     for table in tables:
#         print(f"Clearing table {table[0]}")
#         c.execute(f"DELETE FROM {table[0]}")

#     conn.commit()
#     conn.close()
#     print("All data has been cleared.")
    
# clear_all_data(database_name)    
#%%
conn.close()
