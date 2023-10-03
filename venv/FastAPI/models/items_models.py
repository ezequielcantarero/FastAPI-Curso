from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    is_offer: Union[bool, None] = None
    tax: Union[float, None] = None