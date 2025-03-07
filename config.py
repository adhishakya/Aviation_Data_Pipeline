import requests
import os
from dotenv import load_dotenv


def getUrl(limit):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    url = f'https://api.aviationstack.com/v1/flights?access_key={api_key}&limit={limit}'
    return url
