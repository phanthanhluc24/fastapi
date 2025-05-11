from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt 
from passlib.context import CryptContext

from db.session import get_db
from repositories.user_repository import UserRepository  
from sqlalchemy.orm import Session  


SECRET_KEY = "fastapi-learning"  
ALGORITHM = "HS256"  
ACCESS_TOKEN_EXPIRE_MINUTES = 30  

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login") 


PUBLIC_PATHS = [  
    "/api/auth/login",  
    "/api/users",
    "/docs",  
    "/openapi.json",  
    "/redoc",  
    "/",  
]  

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hashed(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):  
    to_encode = data.copy()  
    if expires_delta:  
        expire = datetime.utcnow() + expires_delta  
    else:  
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  
    to_encode.update({"exp": expire})  
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  
    return encoded_jwt  
  
# Hàm xác thực người dùng  
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):  
    credentials_exception = HTTPException(  
        status_code=status.HTTP_401_UNAUTHORIZED,  
        detail="Could not validate credentials",  
        headers={"WWW-Authenticate": "Bearer"},  
    )  
    try:  
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  
        email: str = payload.get("sub")  
        if email is None:  
            raise credentials_exception  
    except JWTError:  
        raise credentials_exception  
      
    user_repo = UserRepository(db)  
    user = user_repo.get_by_email(email)  
    if user is None:  
        raise credentials_exception  
    return user

def requires_auth(request: Request) -> bool:  
    path = request.url.path  
    return not any(path.startswith(public_path) for public_path in PUBLIC_PATHS)