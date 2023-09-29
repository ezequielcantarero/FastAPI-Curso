from typing import Union
from fastapi import FastAPI
from routers import calculadora

app = FastAPI()

app.include_router(calculadora.router)

@app.get('/')
async def read_root():
    return{'Hello':'World'}