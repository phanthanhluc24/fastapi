from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    fullname: str
    email: EmailStr
    