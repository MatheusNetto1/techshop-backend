# app/routes/product_routes.py
from fastapi import APIRouter
from typing import List
from app.controllers import product_controller
from app.models.product import Product

router = APIRouter()

@router.get("/", response_model=List[Product])
def list_products():
    return product_controller.get_all_products()

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: str):
    return product_controller.get_product_by_id(product_id)