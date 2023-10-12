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
    return buscar_producto(item_id)
    #Se mejora con una funcion para evitar la multiplicidad del codigo de busqueda

    #prod_result = list(filter(lambda product: product.id == item_id, products))
    #if len(prod_result):
    #    return prod_result[0]
    
    #raise HTTPException(status_code=404, detail=f'El producto con el ID {item_id} no fue encontrado')
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
async def update_item(item_id: str, item: Item):
    #return {'item_name': item.name, 'item_id': item_id, 'item_price': item.purchase_price}

    #Se mejora con una funcion para evitar la multiplicidad del codigo de busqueda
    #prod_result = list(filter(lambda product: product.id == item_id, products))
    #if len(prod_result):
    #item_result = prod_result[0]
    item_result = buscar_producto(item_id)
    item_result.name = item.name
    item_result.description = item.description
    item_result.purchase_price = item.purchase_price
    item_result.sales_price = item.sales_price
    item_result.vendor = item.vendor
    item_result.is_offer = item.is_offer
    item_result.tax = item.tax

    return item_result

@router.delete('/{item_id}')
async def delete_item_id(item_id: str):

    #Se mejora con una funcion para evitar la multiplicidad del codigo de busqueda
    #prod_result = list(filter(lambda product: product.id == item_id, products))
    #if len(prod_result):
    #item_result = prod_result[0]
    item_result = buscar_producto(item_id)
    products.remove(item_result)
    return{'message': f'El producto con el ID {item_id} fue eliminado'}

    
def buscar_producto(item_id: str):
    product_result = list(filter(lambda product: product.id == item_id, products))
    if len(product_result):
        return product_result[0]
    raise HTTPException(status_code=404, detail=f'El producto con el ID {item_id} no fue encontrado')