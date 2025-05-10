from fastapi import BackgroundTasks
from sqlalchemy.orm import Session

from dto.req import UserRequest
from repositories.user_repository import UserRepository
from utils.mail import generate_otp, send_otp_email

class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def create_user(self, data: UserRequest, background_tasks: BackgroundTasks) -> str:
        """_summary_

        Args:
            data (UserRequest): _description_
        """

        data_dict = data.model_dump()
        self.user_repository.create(data_dict)
        otp = generate_otp()
        background_tasks.add_task(send_otp_email(data.email, otp))
        return "Create user successfully"
    