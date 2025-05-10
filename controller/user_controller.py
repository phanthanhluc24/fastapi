from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from dto.req.UserRequest import UserRequest
from services.user_service import UserService
from utils.response import response_created


user_router = APIRouter()

@user_router.post("")
def create_user(data: UserRequest,background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    response = UserService(db).create_user(data, background_tasks)
    return response_created(response)
