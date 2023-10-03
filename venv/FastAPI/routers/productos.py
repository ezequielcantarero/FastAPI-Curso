from fastapi import APIRouter
from typing import Union
from models.items_models import Item

router = APIRouter(prefix="/items",
                   tags=["items"],
                   responses={404: {"message": "No encontrado"}})

@router.get('/items/{item_id}')
async def read_item(item_id: int, q: Union[str,None] = None):
    return {'item_id': item_id, 'q': q}

@router.post('/items/')
async def create_item(item: Item):
    return{item}

@router.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id, 'item_price': item.price}