from datetime import timedelta
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.req.UserRequest import TokenResponse, UserRequest
from models.user import UserModel
from repositories.user_repository import UserRepository
from services.user_service import UserService
from utils.auth import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_user, verify_password
from utils.response import response_created


router = APIRouter()

@router.post("")
def create_user(data: UserRequest,background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    response = UserService(db).create_user(data, background_tasks)
    return response_created(response)

@router.get("/me")  
def get_current_user_info(current_user: UserModel = Depends(get_current_user)):  
    return {  
        "id": current_user.id,  
        "fullname": current_user.fullname,  
        "email": current_user.email  
    }

