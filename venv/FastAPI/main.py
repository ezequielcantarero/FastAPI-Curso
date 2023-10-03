from fastapi import FastAPI
from routers import calculadora, productos

app = FastAPI()

app.include_router(calculadora.router)
app.include_router(productos.router)

@app.get('/')
async def read_root():
    return{'Hello':'World'}

