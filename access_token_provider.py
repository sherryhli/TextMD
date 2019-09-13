import requests
import json
import secrets

def get_access_token():
    api_url = 'https://authservice.priaid.ch/login'
    api_key = secrets.API_MEDIC_KEY
    hashed_credentials = secrets.API_MEDIC_HASHED_CREDENTIALS
    headers = {'Authorization': 'Bearer ' + api_key + ':' + hashed_credentials}
    response = requests.post(api_url, headers=headers).json()
    access_token = response["Token"]
    return access_token