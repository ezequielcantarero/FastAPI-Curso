from fastapi import APIRouter, HTTPException
from typing import Union
from uuid import uuid4 as uuid   #uuid genera ids automaticos 
from models.items_models import Item

router = APIRouter(prefix="/items",
                   tags=["items"],
                   responses={404: {"message": "No encontrado"}})

products = []

@router.get('/')
async def read_products():
    return products

@router.get('/{item_id}')
async def read_item(item_id: str):

    prod_result = list(filter(lambda product: product.id == item_id, products))
    if len(prod_result):
        return prod_result[0]
    
    raise HTTPException(status_code=404, detail=f'El producto con el ID {item_id} no fue encontrado')
    #se optimiza el for de abajo
    #for product in products:
    #    if product.id == item_id:
    #        return product

@router.post('/')
async def create_item(item: Item):
    item.id = str(uuid())
    products.append(item)
    return{'Message': 'Item created successfully'}

@router.put('/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id, 'item_price': item.purchase_price}