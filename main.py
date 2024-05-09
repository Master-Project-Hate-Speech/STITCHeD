import pandas as pd
from dataTransformation import DataFrameConverter
from sqlite_setup import create_tables
from read_data import read_table, read_all_tables
import myGlobals
conn = myGlobals.connect()
create_tables(conn)
read_all_tables(conn)

df = pd.read_csv("./OLID_2019/olid-training-v1.0.tsv", sep="\t")
converter = DataFrameConverter(df, conn)
## dictionary key:table name; value:df
formatted_df = converter.format_for_sql()
def insert_data(conn, df, table_name):
    try:
        df.to_sql(table_name, conn, if_exists='append', index=False)
    except Exception as e:
        print(e)

for k,v in formatted_df.items():
    insert_data(conn, v, k)
    conn.commit()

# conn = myGlobals.connect()
read_all_tables(conn)