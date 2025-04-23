from typing import Optional
from pydantic import BaseModel

class REGISTER_FormData (BaseModel):
    password:str
    username:str
    fullname:str
    email:str
    
class LOGIN_FormData (BaseModel):
    password:str 
    username: Optional[str] = None
    email: Optional[str] = None
    
class USER_MODEL(BaseModel):
    id:str  # will add by UUID
    username:str
    fullname:str
    email:str
    

class DB_USER_MODEL(USER_MODEL):
    hashpassword: str
    
    
class DB_ALL_USERS_MODEL(DB_USER_MODEL):
    users : list[USER_MODEL]
    
    

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    email: str | None = None
