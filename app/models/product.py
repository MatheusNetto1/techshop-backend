# app/models/product.py
from pydantic import BaseModel

class Product(BaseModel):
    id: str
    name: str
    price: float
    imageUrl: str
    description: str