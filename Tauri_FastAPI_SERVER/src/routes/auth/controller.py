from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import jwt # type: ignore
from jwt.exceptions import InvalidTokenError # type: ignore
from src.routes.auth.model import TokenData # type: ignore

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=['bcrypt'] , deprecated="auto") 
SECRET_KEY="nabeelSecretKey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1


def hash_password(passwrod:str)->str:
    return pwd_context.hash(passwrod)

def verify_password(plain_password: str , hash_password:str)->bool:
    return pwd_context.verify(plain_password,hash_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# to auth the user for protect routes 
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    # user_dict = fake_users_db.get(token_data.username)
    # if user_dict is None:
        raise HTTPException(status_code=404, detail="User not found")

    # return UserInDB(**user_dict)
