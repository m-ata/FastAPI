# main.py
from fastapi import FastAPI
from src.routes.auth_jwt import router as auth_router

version = "v1"
app = FastAPI(title="AUTH JWT", description="Auth practicing", version=version)

app.include_router(auth_router, prefix=f"/api/{version}/authJwt", tags=["AUTH JWT"])
