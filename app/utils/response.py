# app/utils/response.py
from fastapi.responses import JSONResponse

def success_response(data, message="Success"):
    return JSONResponse(status_code=200, content={"message": message, "data": data})

def error_response(message="Error", status_code=400):
    return JSONResponse(status_code=status_code, content={"message": message})