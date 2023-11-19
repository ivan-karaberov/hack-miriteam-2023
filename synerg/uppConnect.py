import asyncio

import requests


async def get_id():
    '''Получение id-паллета с системы upp'''
    id = list()
    try:
        request = requests.get("http://127.0.0.2:8000/pallets")
        if request.status_code == 200 and len(request.json()):
            id = request.json()
            print(id)
    except Exception:
        print('Failed Connect')
    return id


async def send_id():
    '''Полученные данные отправляем POST'''
    data = await get_id()
    if len(data):
        params={"data": data}
        requests.post("http://127.0.0.1:8000/send_id", json=params)
    await asyncio.sleep(60)


async def main():
    while True:
        await send_id()


asyncio.run(main())