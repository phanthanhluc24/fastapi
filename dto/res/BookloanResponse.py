from datetime import date
from typing import Optional
from pydantic import BaseModel


class BookloanResponse(BaseModel):
    loan_id: int
    book_title: str
    author_name: str
    loan_date: date
    return_date: Optional[date] | None

class AuthorLoanHistoryResponse(BaseModel):
    book_title: str
    borrower_name: str
    loan_date: date
    return_date: Optional[date] = None
    