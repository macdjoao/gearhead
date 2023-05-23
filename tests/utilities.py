import requests
import json


def get_token():
    url = "http://localhost:5000/api/v1/login"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({"email": "johndoe@email.com",
                         "password": "johndoe_password"})
    response = (requests.request(
        "POST", url, headers=headers, data=payload)).json()
    return response['access_token']


def generate_headers():
    headers = {'Authorization': f'Bearer {get_token()}',
               'Content-Type': 'application/json'}
    return headers
