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
    return pymysql.connect(
        host = os.getenv('rail_host'),
        user = os.getenv('rail_db_user'),
        password = os.getenv('rail_pass'),
        database = os.getenv('rail_db_name'),
        port= int(os.getenv('rail_port'))
    )