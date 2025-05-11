from datetime import date
from typing import Optional
from pydantic import BaseModel


class BookLoanRequest(BaseModel):
    book_id: int
    borrower_name: str
    loan_date: date
    return_date: Optional[date]
