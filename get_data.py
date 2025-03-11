import requests
from config import getUrl
from db_operation import insert_aviation_data

def get_aviation_data():
    try:
        limit = 100
        response = requests.get(getUrl(limit))
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

        insert_aviation_data(values)
    
    except:
        print('Failed to fetch data.')
