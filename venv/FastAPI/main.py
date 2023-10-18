from fastapi import FastAPI
from routers import calculadora, productos

app = FastAPI()

app.include_router(calculadora.router)
app.include_router(productos.router)

@app.get('/')
async def read_root():
    return{'Mensaje':'Bienvenidos a la API'}

@app.get('/porcentaje')
async def aumento_porcentaje(base: float, porcentaje: float ,dias: int):
    valor_final = base
    for x in range(dias):
        valor_final = valor_final + valor_final * (porcentaje / 100)    
    return valor_final