import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

# def get_connection():
#     return pymysql.connect(
#         host = os.getenv('DB_HOST'),
#         user = os.getenv('DB_USER'),
#         password = os.getenv('DB_PASSWORD'),
#         database = os.getenv('DB_DBNAME')
#     )

def get_connection():
    conn = pymysql.connect(
    host=os.getenv("MYSQLHOST"),
    port=int(os.getenv("MYSQLPORT")),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQLDATABASE")
    )
    return conn
