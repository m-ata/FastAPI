# src/routes/auth_jwt.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {"access_token": "abc123", "token_type": "bearer"}
