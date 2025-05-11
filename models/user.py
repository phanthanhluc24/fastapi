

from pydantic import EmailStr
from sqlalchemy import Column, Integer, String
from db.session import Base
from models.base import TimeMixin


class UserModel(Base, TimeMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(250), nullable=False)
