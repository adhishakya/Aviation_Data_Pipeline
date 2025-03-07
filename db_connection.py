from dotenv import load_dotenv
import os

def connect_to_db():
    load_dotenv()
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    credentials = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }
    return credentials
