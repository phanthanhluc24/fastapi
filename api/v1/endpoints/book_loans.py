from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.req.BookLoanRequest import BookLoanRequest
from services.bookloan_service import BookLoanService
from utils.auth import get_current_user
from utils.response import response_created, response_success


router = APIRouter(dependencies=[Depends(get_current_user)])

@router.post("")
def book_loan_by_user(data: BookLoanRequest, db: Session = Depends(get_db)):
    response = BookLoanService(db).book_loan_by_user(data)
    return response_created(response)

@router.put("/{loan_id}")
def book_loan_by_user_update(loan_id: int, data: BookLoanRequest, db: Session = Depends(get_db)):
    response = BookLoanService(db).book_loan_by_user_update(loan_id, data)
    return response_success(response)

@router.get("/all")
def get_all_book_is_loans(db: Session = Depends(get_db)):
    bookloans = BookLoanService(db).get_all_book_is_loans()
    return response_success(bookloans)

@router.get("/history/{author_id}")
def get_history_book_loan_of_author(author_id: int, db: Session = Depends(get_db)):
    history = BookLoanService(db).get_book_loan_history_of_author(author_id)
    return response_success(history)

@router.get("/{loan_id}")
def get_bookloan_detail(loan_id: int, db: Session = Depends(get_db)):
    bookloan = BookLoanService(db).get_book_loan_detail(loan_id)
    return response_success(bookloan)

