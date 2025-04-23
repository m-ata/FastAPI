from email import message
import fastapi
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

router = fastapi.APIRouter()

oauth_scheme= OAuth2PasswordBearer(tokenUrl="token")

@router.get("/login")
def home():
    return {"message" : "Hellow world" , "access_token": "abc123"}

@router.post("/validate")
def validate(token:Annotated[str, Depends(oauth_scheme)]):
    if token !="abc123":
        raise HTTPException(
            status_code=404,
            detail="UnAuthorized",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"message": "Access granted", "your_token": token}
