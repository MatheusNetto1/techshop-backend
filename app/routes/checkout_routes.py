# app/routes/checkout_routes.py
from fastapi import APIRouter
from app.models.checkout import CheckoutRequest, CheckoutResponse

router = APIRouter()

@router.post("/", response_model=CheckoutResponse)
def checkout_route(order: CheckoutRequest):
    # lógica fake (aqui você poderia validar estoque, processar pagamento, etc.)
    return {"status": "success", "message": "Pedido processado com sucesso"}