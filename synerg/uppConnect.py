import time

import requests


def get_id():
    '''Получение id-паллета с системы upp'''
    request = requests.get("http://127.0.0.1:8000/pallets")
    id = []
    if request.status_code == 200:
        id = request.json()["buffer_zone"]
    return id