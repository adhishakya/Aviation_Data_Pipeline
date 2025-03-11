import mysql.connector
from .db_connection import connect_to_db
import pandas as pd
import warnings
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s - %(message)s')

def insert_cleaned_aviation_data():
    base_path = os.path.dirname(os.path.abspath(__file__))
    sql_file_path = os.path.join(base_path, 'insert_cleaned_data_query.sql')
    try:
        warnings.filterwarnings("ignore", category=UserWarning)
        warnings.filterwarnings("ignore", category=FutureWarning)

        logging.info('Starting to data cleaning process...')
        
        credentials = connect_to_db()
        conn = mysql.connector.connect(
            host = credentials['host'],
            user = credentials['user'],
            password = credentials['password'],
            database = credentials['database'],
        )

        cursor = conn.cursor()
        df = pd.read_sql('SELECT * FROM aviation_data;', conn)
        
        logging.info('Handling missing values...')
        # handling missing values
        df["airline_name"].replace("empty", pd.NA, inplace=True)
        df['arrival_estimated'].fillna(df['arrival_scheduled'], inplace = True) 
        df['departure_estimated'].fillna(df['departure_scheduled'], inplace = True) 
        df['departure_timezone'].fillna(df['arrival_timezone'],inplace = True)
        df["departure_airport"].fillna("Unknown Airport", inplace=True)
        df["arrival_airport"].fillna("Unknown Airport", inplace=True)
        df['arrival_timezone'].fillna("UTC", inplace=True)
        df['airline_name'].fillna('Unknown', inplace = True)
        df['flight_number'].fillna('Unknown', inplace=True)
        df['flight_icao'].fillna('Unknown', inplace=True)

        logging.info('Handling duplicate data...')
        # handling duplicate data
        df = df.drop_duplicates(subset = df.columns.difference(['id']), keep = 'first')
        df = df.reset_index(drop = True)

        logging.info('Reverting datatypes...')
        # reverting to original data type
        df['id'] = df['id'].astype('int64')
        df['flight_date'] = pd.to_datetime(df['flight_date'], errors='coerce')
        df['departure_scheduled'] = pd.to_datetime(df['departure_scheduled'], errors='coerce')
        df['departure_estimated'] = pd.to_datetime(df['departure_estimated'], errors='coerce')
        df['arrival_scheduled'] = pd.to_datetime(df['arrival_scheduled'], errors='coerce')
        df['arrival_estimated'] = pd.to_datetime(df['arrival_estimated'], errors='coerce')
        
        logging.info('Truncating table data...')
        truncate_query = 'TRUNCATE TABLE aviation_data_cleaned;'
        cursor.execute(truncate_query)
        conn.commit()

        file = open(sql_file_path,'r')
        query = file.read()
        file.close()

        values = [tuple(row) for row in df.itertuples(index=False, name=None)]
        cursor.executemany(query, values)
        conn.commit()
        logging.info('Cleaned data inserted successfully...')


        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        logging.error(f"MySQL Error: {err}")
    except Exception as e:
        logging.error(f"Failed to insert data. Error: {str(e)}")

insert_cleaned_aviation_data()