# app/routes/auth_routes.py
from fastapi import APIRouter
from app.controllers import auth_controller
from app.models.auth import UserLogin, UserResponse

router = APIRouter()

@router.post("/login", response_model=UserResponse)
def login_route(user: UserLogin):
    return auth_controller.login(user)