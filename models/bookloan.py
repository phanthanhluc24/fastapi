from sqlalchemy import Column, Integer, String, Date

from db.session import Base
from models.base import TimeMixin

class BookLoanModel(Base, TimeMixin):
    __tablename__ = "bookloans"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    borrower_name = Column(String(200))
    loan_date = Column(Date)
    return_date = Column(Date, nullable=True)
