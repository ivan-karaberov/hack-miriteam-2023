from fastapi import FastAPI
from pydantic import BaseModel
import requests

from services.checkDB import add_to_db, update_in_db, delete_from_db


app = FastAPI()


class Item(BaseModel):
    data: list[str]


class Camera(BaseModel):
    id: str
    status: int


class DS(BaseModel):
    status: int
    id: str


@app.post("/send_id")
async def send_id(data: Item):
    '''Обработка POST запроса от uppConnect'''
    print(data.data)
    for i in data.data:
        await add_to_db(i, 0)


@app.post("/update_data")
async def update_id(data: Camera):
    '''Обновление данных в БД'''
    if(data.status == 2):
        params={"id":data.id}
        requests.post("http://127.0.0.1:5000/pallets", json=params)
        return {"status": 200}
    else:
        return await update_in_db(data.id, data.status)


@app.post("/data_success")
async def data_success(data: DS):
    '''Обработка ответа от wms и удаление данных из БД'''
    if data.status == 200:
        return await delete_from_db(data.id)