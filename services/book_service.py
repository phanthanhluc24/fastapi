from sqlalchemy.orm import Session

from schemas.req.BookRequest import BookRequest
from schemas.res.BookResponse import BookResponse
from repositories.author_repository import AuthorRepository
from repositories.book_repository import BookRepository



class BookService:
    def __init__(self, db: Session):
        self.db = db
        self.book_repository = BookRepository(db)
        self.author_repository = AuthorRepository(db)


    def add_new_book(self, data: BookRequest) -> str:
        """_summary_

        Args:
            data (BookRequest): _description_

        Returns:
            str: _description_
        """
        self.author_repository.get_by_id(data.author_id)

        data_dict = data.model_dump()
        self.book_repository.create(data_dict)
        return "Add new book successfully"
    
    def update_book(self, book_id: int, data: BookRequest) -> str:
        """_summary_

        Args:
            book_id (int): _description_
            data (BookRequest): _description_

        Returns:
            str: _description_
        """
        self.book_repository.get_by_id(book_id)
        self.author_repository.get_by_id(data.author_id)
        data_dict = data.model_dump()
        self.book_repository.update_by_id(book_id, data_dict)
        return "Update book successfully"
    
    def delete_book(self, book_id: int) -> str:
        """_summary_

        Args:
            book_id (int): _description_

        Returns:
            str: _description_
        """

        self.book_repository.get_by_id(book_id)
        data_dict = {"is_deleted": True}
        self.book_repository.update_by_id(book_id, data_dict)
        return "Delete book successfully"

    def get_book_by_id(self, book_id: int) -> BookResponse:
        """_summary_

        Args:
            book_id (int): _description_
        """
        self.book_repository.get_by_id(book_id)

        book = self.book_repository.get_book_by_id_and_author(book_id)
        return BookResponse(**book)
    
    def get_book_and_author(self) -> list[BookResponse]:
        """_summary_

        Args:
            book_id (int): _description_
        """
        book = self.book_repository.get_book_and_author()
        return book
