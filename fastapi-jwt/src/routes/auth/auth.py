# from datetime import datetime, timedelta, timezone
# from passlib.context import CryptContext
# import jwt
# from .config import SECRET_KEY, ALGORITHM

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def verify_password(plain, hashed):
#     return pwd_context.verify(plain, hashed)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
