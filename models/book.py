from sqlalchemy import Column, Integer, String, Boolean
from models.base import TimeMixin

from db.session import Base
class BookModel(Base, TimeMixin):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250),index=True)
    author_id = Column(Integer, nullable= False)
    published_year = Column(Integer)
    is_deleted = Column(Boolean, default = False)
    