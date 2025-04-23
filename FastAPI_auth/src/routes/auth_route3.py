from fastapi import FastAPI , Depends, HTTPException,status
import fastapi
from pydantic import BaseModel   
from fastapi.security import  OAuth2PasswordBearer , OAuth2PasswordRequestForm 
from typing import Annotated 

router3 = fastapi.APIRouter()

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecretjohndoe",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecretalice",
        "disabled": True,
    },
}

Oauth_Sceheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str|None
    full_name: str|None
    email: str | None
    disabled:bool
    
class User_in_DB(User):
    hashed_password: str | None


def fakehashed_password(username:str):
    return "fakehashedsecret"+username


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return User_in_DB(**user_dict)


def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(Oauth_Sceheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@router3.get("/register")
def register():
    return {
        "message" : "Register successfully",
    }
    
@router3.post("login")
def login(form_data:Annotated[  OAuth2PasswordRequestForm , Depends()] ): #self calling with form_data
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict :
        raise HTTPException(
            
            detail="Wrong username or password",
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "Bearer"},

        )
    db_user = User_in_DB(**user_dict) # **args all arguments of user dictionary username , fullname etc 
    hashPassword = fakehashed_password(form_data.password)
    if not hashPassword == db_user.hashed_password:
        raise HTTPException(
            detail="Wrong username or password",
            status_code=400
        )
    return {"access_token": db_user.username, "token_type": "bearer"}

    
        
    
@router3.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user
    
    # return {
    #     "message" : "login successfully",
    #     "access_token" : "abc123"
    #     # "user": User()

    # }
