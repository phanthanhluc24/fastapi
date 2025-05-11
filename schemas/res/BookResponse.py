from datetime import date
from typing import Optional
from pydantic import BaseModel


class BookResponse(BaseModel):
    book_id: int
    title: str 
    published_year: int
    name: str
    birth_year: int


class BookIsLoanResponse(BaseModel):
    book_id: int
    title: str
    author_name: str
    loan_date: date
    return_date: Optional[date] | None

class BookSummary(BaseModel):
    book_id: int
    book_title: str
    published_year: int


class AuthorWithBooksResponse(BaseModel):
    author_id: int
    author_name: str
    books: list[BookSummary]

