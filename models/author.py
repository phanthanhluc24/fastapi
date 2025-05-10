from sqlalchemy import Column, Integer, String, Boolean
from models.base import TimeMixin

from db.session import Base
class AuthorsModel(Base, TimeMixin):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    birth_year = Column(Integer, nullable=False)
    is_deleted = Column(Boolean, default= False)
