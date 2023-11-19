from fastapi import FastAPI
from pydantic import BaseModel
import requests

from services.checkDB import add_to_db, update_in_db
import stats


app = FastAPI()


class Item(BaseModel):
    data: list[str]


class Camera(BaseModel):
    id: str
    status: int


class DS(BaseModel):
    id: str
    status: int


@app.post("/send_id")
async def send_id(data: Item):
    '''Обработка POST запроса от uppConnect'''
    print("TEst", data.data)
    for i in data.data:
        if i is not None:
            print(i)
            await add_to_db(i, 0)


@app.post("/update_data")
async def update_id(data: Camera):
    '''Обновление данных в БД'''
    if(data.status == 2):
        params={"id":data.id}
        status = requests.post("http://127.0.0.3:8000/ud", json=params)
        print(type(status.status_code))
        if status.status_code == 200:
            return await update_in_db(data.id, data.status)
    else:
        return await update_in_db(data.id, data.status)


@app.get("/get_daily_stat")
async def get_daily_stat():
    return await stats.stat()