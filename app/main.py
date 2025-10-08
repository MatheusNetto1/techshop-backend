# app/main.py
from fastapi import FastAPI
from app.routes import auth_routes, product_routes

app = FastAPI(title="Python Backend")

# Rotas
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(product_routes.router, prefix="/products", tags=["Products"])