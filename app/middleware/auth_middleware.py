# app/middleware/auth_middleware.py
from fastapi import Request, HTTPException
from app.utils.jwt_handler import SECRET_KEY, ALGORITHM
import jwt

PUBLIC_PATHS = [
    "/",
    "/auth/login",
    "/auth/register",
    "/products"
]

async def auth_middleware(request: Request, call_next):
    if any(request.url.path.startswith(path) for path in PUBLIC_PATHS):
        return await call_next(request)

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    token = auth_header.split(" ")[1]
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return await call_next(request)