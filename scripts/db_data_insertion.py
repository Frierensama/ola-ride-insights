import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
from db_config import get_connection

load_dotenv()
try:
    df = pd.read_csv(os.getenv('clean_csv_path'))

    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = pd.to_datetime(df['Time'],format="%H:%M:%S").dt.time

    df = df.replace({np.nan:None})

    conn = get_connection()
    cursor = conn.cursor()

    columns = ", ".join(df.columns)
    rows = df.values.tolist()
    placeholder = ", ".join( ['%s'] * len(df.columns) )

    insert_query = f"insert into ola_t ({columns}) values ({placeholder})"

    cursor.executemany(insert_query, rows)
    conn.commit()

    print('Data Insertion Successful')

except Exception as e:
    print(f"error : {e}")

finally:
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()