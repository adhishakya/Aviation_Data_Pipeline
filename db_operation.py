import mysql.connector
from dotenv import load_dotenv
import os
from db_connection import connect_to_db

#TODO: Exception handling
def insert_aviation_data(values):
    
    credentials = connect_to_db()
    
    conn = mysql.connector.connect(
        host = credentials['host'],
        user = credentials['user'],
        password = credentials['password'],
        database = credentials['database'],
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
