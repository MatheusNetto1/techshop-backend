# app/middleware/not_found_middleware.py
from fastapi import Request
from fastapi.responses import JSONResponse
from app.constants.messages import MESSAGES

async def not_found_middleware(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"detail": MESSAGES["NOT_FOUND"]}
        )
    return response