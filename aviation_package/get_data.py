import requests
from aviation_package.config import getUrl
from aviation_package.db_operation import insert_aviation_data
from airflow.models import Variable
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s - %(message)s')

def get_aviation_data(**kwargs):
    try:
        logging.info('Starting to fetch aviation data...')
        limit = 100
        response = requests.get(getUrl(limit))

        if response.status_code != 200:
            logging.error(f"Failed to fetch data. HTTP status code: {response.status_code}")
            return
        
        response_json = response.json()

        values = []
        for i in range (0,limit):
            values.append(
                [
                response_json['data'][i]['flight_date'],
                response_json['data'][i]['flight_status'],
                response_json['data'][i]['departure']['airport'],
                response_json['data'][i]['departure']['timezone'],
                response_json['data'][i]['departure']['scheduled'],
                response_json['data'][i]['departure']['estimated'],
                response_json['data'][i]['arrival']['airport'],
                response_json['data'][i]['arrival']['timezone'],
                response_json['data'][i]['arrival']['scheduled'],
                response_json['data'][i]['arrival']['estimated'],
                response_json['data'][i]['airline']['name'],
                response_json['data'][i]['flight']['number'],
                response_json['data'][i]['flight']['icao']
                ]
            )

        kwargs['ti'].xcom_push(key='aviation_data', value = values)

        logging.info(f"Fetched {len(values)} records and pushed to XCom.")
    
    except Exception as e:
        logging.error(f"Failed to fetch data. Error: {str(e)}")