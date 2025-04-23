from http.client import HTTPResponse
import fastapi 
from fastapi import FastAPI , Depends 
from typing import Annotated 
from pydantic import BaseModel
from .auth_route import router
from fastapi.security import OAuth2PasswordBearer
router2 = fastapi.APIRouter()


class User(BaseModel):
    username: str | None
    fullname: str | None
    email: str | None
    disabled : bool | None
    
auth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



@router2.get("/login2")
def login():
    return {
        "message" : "Login Successful",
        "access_token" : "abc123"
    }
    

def get_current_user(token: Annotated[str, Depends(auth2_scheme)]):
    user = fake_decoded_user(token)
    return {
        "message": "User is valid",
        "user" : user
    }


def fake_decoded_user(token: str):
    return User(
        username= token+"fakedecoded",
        email="john@example.com",
        fullname="John Doe",
        disabled=True
    )



@router2.post("/validate2")
def validate_user(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

    