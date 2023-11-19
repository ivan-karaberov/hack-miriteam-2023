import time
import random 

import asyncio
from fastapi import FastAPI

app = FastAPI()


def generate_id():
    str_ = f'EU{random.randint(1000, 15000)}'
    #return [str_]
    return ['EUR000094', 'EUR000090']


@app.get('/pallets')
def pallets():
    return generate_id()