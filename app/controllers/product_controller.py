# app/controllers/product_controller.py
from fastapi import HTTPException
from app.data.mock_data import products

def get_all_products():
    return products

def get_product_by_id(product_id: str):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")