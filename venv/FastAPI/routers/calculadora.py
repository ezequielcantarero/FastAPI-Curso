from fastapi import APIRouter

router = APIRouter(prefix="/calculadora",
                   tags=["calculadora"],
                   responses={404: {"message": "No encontrado"}})

@router.get('/')
async def calcular(operando1: float, operando2: float):
    return{'suma': operando1 + operando2}