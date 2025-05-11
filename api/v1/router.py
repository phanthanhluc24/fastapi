from fastapi import APIRouter  
from api.v1.endpoints import authors, books, book_loans, users, auth
  
api_router = APIRouter()  
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])  
api_router.include_router(authors.router, prefix="/authors", tags=["authors"])  
api_router.include_router(books.router, prefix="/books", tags=["books"])  
api_router.include_router(book_loans.router, prefix="/book-loans", tags=["book-loans"])  
api_router.include_router(users.router, prefix="/users", tags=["users"])
