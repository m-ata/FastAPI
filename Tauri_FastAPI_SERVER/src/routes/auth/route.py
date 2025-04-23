from datetime import timedelta
from typing import Annotated
import uuid
import fastapi 
from fastapi import Form 
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from pydantic import BaseModel
from .query import GET_USERS_DB, LOGIN_USER_DB, REGISTER_USER_DB
from .model import DB_ALL_USERS_MODEL, DB_USER_MODEL , REGISTER_FormData, LOGIN_FormData
import sqlite3

# controllers 
from .controller import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, verify_password , hash_password
router = fastapi.APIRouter()

# class FormData (BaseModel):
#     username:str
#     password:str
    
# class USER_MODEL(BaseModel):
#     id:str
#     username:str
#     fullname:str
#     email:str

# class DB_USER_MODEL(USER_MODEL):
#     hashpassword: str
    
@router.post("/register")
def register(data: Annotated[REGISTER_FormData, Form()]):
    
    hashPassword = hash_password(data.password)
    print("HASPASSWORD *******************" , hashPassword)
    # verifyPassword = verify_password(data.password , hashPassword)
    # print("Verify PASSWORD *******************" , hashPassword)
    
    # if verifyPassword:
    #     print("TRUE")
    # else:
    #     print("FALSE")

        
    user = DB_USER_MODEL(
        id=str(uuid.uuid4()),
        username=data.username,
        fullname=data.fullname,
        email=data.email,
        hashpassword=hashPassword 
    )

    REGISTER_USER_DB(user)
        
    return {
        "success" : True,
        "data": {"user": data},
        "message" : "User registered successfully.",
        "errors":None

    }
    
@router.get("/users")
async def get_users():

    result=  GET_USERS_DB()
        
    return {
        "success" : True,
        "data": {"users": [user.dict() for user in result]},
        "message" : "Users get successfully.",
        "errors":None

    }
    
    
@router.post("/login")
async def login_user(login_data: Annotated[LOGIN_FormData, Form()] ):
    # print(login_data.username)
    # print(login_data.email)
    result =  LOGIN_USER_DB(login_data)
    print("RESULT ****" , result)
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": login_data.username},  # 'sub' = subject (standard JWT claim)
        expires_delta=access_token_expires
    )
    if result==False:
        return {
            "success" : False,
            "data": {"user": None},
            "message" : "Worng username/email or password.",
            "errors":"Wrong Credientials"
        }
    if result==None:
        return {
            "success" : False,
            "data": {"user": None},
            "message" : "Invalid Credientials.",
            "errors":"No User found"
        }
            
    return {
        "success" : True,
        "data": {"user": [result], "access_token": access_token, "token_type": "bearer"},
        "message" : "User login successfully.",
        "errors":None
    }