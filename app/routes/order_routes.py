# app/routes/order_routes.py
from fastapi import APIRouter
from app.models.order import OrderResponse

router = APIRouter()

@router.get("/confirmation", response_model=OrderResponse)
def order_confirmation():
    return {
        "order_id": "ABC123",
        "status": "confirmed",
        "message": "Seu pedido foi confirmado!"
    }