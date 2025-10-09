# app/middleware/error_middleware.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.constants.messages import MESSAGES

def add_error_handlers(app: FastAPI):
    @app.exception_handler(404)
    async def not_found_handler(request: Request, exc):
        return JSONResponse(
            status_code=404,
            content={"detail": MESSAGES["NOT_FOUND"]},
        )

    @app.exception_handler(500)
    async def internal_error_handler(request: Request, exc):
        return JSONResponse(
            status_code=500,
            content={"detail": MESSAGES["INTERNAL_ERROR"]},
        )