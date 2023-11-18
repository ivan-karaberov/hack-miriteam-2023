from fastapi import FastAPI
from pydantic import BaseModel
import requests

from services.checkDB import add_to_db, update_in_db


app = FastAPI()


class Item(BaseModel):
    data: list[str]


@app.post("/send_id")
async def send_id(data:Item):
    '''Обработка POST запроса от uppConnect'''
    print(data.data)
    for i in data.data:
        await add_to_db(i, 0)
