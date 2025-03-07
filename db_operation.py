import mysql.connector
from dotenv import load_dotenv
import os

#TODO: Exception handling
def insert_aviation_data(values):
    load_dotenv()

    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_database = os.getenv('DB_DATABASE')

    conn = mysql.connector.connect(
        host = db_host,
        user = db_user,
        password = db_password,
        database = db_database,
    )

    cursor = conn.cursor()

    file = open('insert_query.sql','r')
    query = file.read()
    file.close()

    values = list(map(tuple, values))
    cursor.executemany(query, values)
    conn.commit()
    print('Data inserted successfully!')

    cursor.close()
    conn.close()
