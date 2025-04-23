# from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
# from datetime import timedelta
# # from jwt import DecodeError
# from auth.auth import verify_password, create_access_token
# from auth.users import get_user
# from auth.models import Token, TokenData, User
# from config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
# import jwt

# router = APIRouter()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# @router.post("/token", response_model=Token)
# def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = get_user(form_data.username)
#     if not user or not verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(data={"sub": user.username}, expires_delta=token_expires)
#     return {"access_token": access_token, "token_type": "bearer"}

# @router.get("/users/me", response_model=User)
# def read_users_me(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid token payload")
#     except :
#     # except (jwt.ExpiredSignatureError, DecodeError):
#         raise HTTPException(status_code=401, detail="Token is invalid or expired")

#     user = get_user(username)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
