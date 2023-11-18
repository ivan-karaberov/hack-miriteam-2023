from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    id:str


@app.post('/ud')
def ud(data: Item):
    return {"status": 200}