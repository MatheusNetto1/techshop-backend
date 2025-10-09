# app/main.py
from fastapi import FastAPI
from app.routes import auth_routes, product_routes, checkout_routes, order_routes
from app.middleware.error_middleware import add_error_handlers
from app.middleware.not_found_middleware import not_found_middleware
from app.middleware.auth_middleware import auth_middleware

app = FastAPI(title="Python Backend")

# Middlewares
app.middleware("http")(not_found_middleware)
app.middleware("http")(auth_middleware)

# Rotas
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(product_routes.router, prefix="/products", tags=["Products"])
app.include_router(checkout_routes.router, prefix="/checkout", tags=["Checkout"])
app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])

# Tratamento de erros
add_error_handlers(app)