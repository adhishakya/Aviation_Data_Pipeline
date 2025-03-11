import mysql.connector
from aviation_package.db_connection import connect_to_db
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s - %(message)s')

def insert_aviation_data(**kwargs):
    base_path = os.path.dirname(os.path.abspath(__file__))
    sql_file_path = os.path.join(base_path, 'insert_query.sql')
    try:
        logging.info('Starting to insert aviation data into the database...')

        ti = kwargs['ti']
        values = ti.xcom_pull(task_ids = 'get_aviation_data', key = 'aviation_data')

        if values is None or len(values) == 0:
            logging.warning("No data found in XCom to insert.")
            return

        logging.info(f"Inserting {len(values)} records into the database...")
        
        credentials = connect_to_db()
        
        conn = mysql.connector.connect(
            host = credentials['host'],
            user = credentials['user'],
            password = credentials['password'],
            database = credentials['database'],
        )

        cursor = conn.cursor()

        file = open(sql_file_path,'r')
        query = file.read()
        file.close()

        values = list(map(tuple, values))
        cursor.executemany(query, values)
        conn.commit()
        logging.info('Data inserted successfully!')

        cursor.close()
        conn.close()
    
    except mysql.connector.Error as err:
        logging.error(f"MySQL Error: {err}")
    except Exception as e:
        logging.error(f"Failed to insert data. Error: {str(e)}")
