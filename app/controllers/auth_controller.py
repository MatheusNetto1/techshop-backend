# app/controllers/auth_controller.py
from fastapi import HTTPException
from app.models.auth import UserLogin, UserResponse
from app.utils.jwt_handler import create_access_token

fake_user = {"id": 1, "username": "admin", "password": "1234"}

def login(user: UserLogin) -> UserResponse:
    if user.username == fake_user["username"] and user.password == fake_user["password"]:
        token = create_access_token({"sub": user.username})
        return UserResponse(id=fake_user["id"], username=user.username, token=token)
    raise HTTPException(status_code=401, detail="Invalid credentials")