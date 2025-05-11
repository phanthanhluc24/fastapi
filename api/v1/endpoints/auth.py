from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.session import get_db
from repositories.user_repository import UserRepository
from schemas.req.UserRequest import TokenResponse
from utils.auth import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, verify_password


router = APIRouter()

@router.post("/login", response_model=TokenResponse)  
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):  
    user_repo = UserRepository(db)  
    user = user_repo.get_by_email(form_data.username)  
      
    if not user or not verify_password(form_data.password, user.password):  
        raise HTTPException(  
            status_code=status.HTTP_401_UNAUTHORIZED,  
            detail="Incorrect email or password",  
            headers={"WWW-Authenticate": "Bearer"},  
        )  
      
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  
    access_token = create_access_token(  
        data={"sub": user.email}, expires_delta=access_token_expires  
    )  
      
    return {"access_token": access_token, "token_type": "bearer"}
