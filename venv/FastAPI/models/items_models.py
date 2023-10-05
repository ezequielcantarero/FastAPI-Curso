from typing import Union, Optional
from pydantic import BaseModel

class Item(BaseModel):
    id: Optional[str] = None 
    name: str
    description: Union[str, None] = None
    purchase_price: float
    sales_price: float
    vendor: str
    is_offer: Union[bool, None] = None
    tax: Union[float, None] = None
    #Si no pones el = None la funcion no te deja no pasarle el parametro y te va a dar error 