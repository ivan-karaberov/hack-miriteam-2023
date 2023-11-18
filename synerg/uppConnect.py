import requests
import json

def get_id():
    '''Получение id-паллета с системы upp'''
    request = requests.get("http://127.0.0.1:5000/pallets")
    id = []
    if request.status_code == 200:
        id = request.json()["id"]
    return id


def send_id():
    '''Полученные данные отправляем POST'''
    data = get_id()
    if len(data):
        params={"data": data}
        requests.post("http://127.0.0.1:8000/send_id", json=params)