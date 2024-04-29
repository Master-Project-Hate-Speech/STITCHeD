import sqlite3
def read_table(conn, table_name):
    c = conn.cursor()
    # Query the total number of rows in the table
    c.execute(f"SELECT COUNT(*) FROM {table_name}")
    total_rows = c.fetchone()[0]
    print(f"========== Contents of table: {table_name} ( {total_rows} rows ) ==========")
    # Query column names of the table
    c.execute(f"PRAGMA table_info({table_name})")
    column_names = [column[1] for column in c.fetchall()]
    print(column_names)
    # Query the first 5 rows of the table
    c.execute(f"SELECT * FROM {table_name} LIMIT 5")
    rows = c.fetchall()
    for row in rows:
        print(row)


def read_all_tables(conn):
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    for table_name in tables:
        read_table(conn, table_name[0])
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