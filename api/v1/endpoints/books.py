from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.req.BookRequest import BookRequest
from services.book_service import BookService
from utils.auth import get_current_user
from utils.response import response_created, response_success


router = APIRouter(dependencies=[Depends(get_current_user)])

@router.post("")
def add_new_book(data: BookRequest, db: Session = Depends(get_db)):
    response = BookService(db).add_new_book(data)
    return response_created(response)

@router.put("/{book_id}")
def update_book(book_id: int, data: BookRequest, db: Session = Depends(get_db)):
    response = BookService(db).update_book(book_id, data)
    return response_success(response)

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    response = BookService(db).delete_book(book_id)
    return response_success(response)

@router.get("/{book_id}")
def get_book_by_id_and_author(book_id: int, db: Session = Depends(get_db)):
    response = BookService(db).get_book_by_id(book_id)
    return response_success(response)

@router.get("")
def get_book_and_author(db: Session = Depends(get_db)):
    response = BookService(db).get_book_and_author()
    return response_success(response)
