import time
import random 

import asyncio
from fastapi import FastAPI

app = FastAPI()


def generate_id():
    str_ = f'E{random.randint(1000, 15000)}'
    return [str_]


@app.get('/pallets')
def pallets():
    return generate_id()