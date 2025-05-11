from fastapi import APIRouter, Depends

from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.req.AuthorRequest import AuthorRequest
from services.author_service import AuthorService
from utils.auth import get_current_user
from utils.response import response_created, response_success


router = APIRouter(dependencies=[Depends(get_current_user)])
@router.post("")
def create_author(data: AuthorRequest, db: Session = Depends(get_db)):
    response = AuthorService(db).create_author(data)
    return response_created(response)

@router.put("/{author_id}")
def update_author(author_id: int, data: AuthorRequest, db: Session = Depends(get_db)):
    response = AuthorService(db).update_author(author_id, data)
    return response_success(response)

@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    response = AuthorService(db).deleted_author(author_id)
    return response_success(response)

@router.get("/all-book-author")
def get_book_of_author(db: Session = Depends(get_db)):
    book_author = AuthorService(db).get_all_book_of_author()
    return response_success(book_author)

@router.get("/{author_id}")
def get_author_by_id(author_id: int, db: Session = Depends(get_db)):
    author = AuthorService(db).get_author_by_id(author_id)
    return response_success(author)

@router.get("")
def get_all_author(db: Session = Depends(get_db)):
    authors = AuthorService(db).get_all_author()
    return response_success(authors)

