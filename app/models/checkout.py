# app/models/checkout.py
from pydantic import BaseModel
from typing import List

class CheckoutItem(BaseModel):
    product_id: str
    quantity: int

class CheckoutRequest(BaseModel):
    items: List[CheckoutItem]

class CheckoutResponse(BaseModel):
    status: str
    message: str