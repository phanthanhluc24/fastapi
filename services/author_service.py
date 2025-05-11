from collections import defaultdict
from sqlalchemy.orm import Session

from schemas.req import AuthorRequest
from schemas.res.BookResponse import AuthorWithBooksResponse, BookSummary
from models.author import AuthorsModel
from repositories.author_repository import AuthorRepository

class AuthorService:
    def __init__(self, db: Session):
        self.db = db
        self.author_repository = AuthorRepository(db)

    def create_author(self, data: AuthorRequest) -> str:
        """_summary_

        Args:
            data (AuthorRequest): _description_
        """

        data_dict = data.model_dump()
        self.author_repository.create(data_dict)
        return "Create author successfully"
    
    def update_author(self, author_id: int, data: AuthorRequest) -> str:
        """_summary_

        Args:
            data (AuthorRequest): _description_

        Returns:
            str: _description_
        """

        self.author_repository.get_by_id(author_id)
        data_dict = data.model_dump()
        self.author_repository.update_by_id(author_id, data_dict)
        return "Update author successfully"
    
    def deleted_author(self, author_id) -> str:
        """_summary_

        Args:
            author_id (_type_): _description_

        Returns:
            str: _description_
        """

        self.author_repository.get_by_id(author_id)
        data_dict = {"is_deleted": True}
        self.author_repository.update_by_id(author_id, data_dict)
        return "Deleted author successfully"
    
    def get_author_by_id(self, author_id) -> AuthorsModel:
        """_summary_

        Args:
            author_id (_type_): _description_

        Returns:
            AuthorsModel: _description_
        """

        author = self.author_repository.get_by_id(author_id)
        return author
    
    def get_all_author(self) -> list[AuthorsModel]:
        """_summary_

        Returns:
            list[AuthorsModel]: _description_
        """
        authors = self.author_repository.get_all()
        return authors
    
    def get_all_book_of_author(self) -> AuthorWithBooksResponse:
        book_authors = self.author_repository.get_all_book_of_author()

        author_dict = defaultdict(lambda: {"author_name": "", "books": []})


        for auth in book_authors:
            author_id = auth.author_id
            author_dict[author_id]["author_name"] = auth.author_name

            if auth.book_id is not None:
                book = BookSummary(
                    book_id= auth.book_id,
                    book_title=auth.book_title,
                    published_year=auth.published_year
                )

                author_dict[author_id]["books"].append(book)
        
        result = []
        for author_id, data in author_dict.items():
            result.append(
                AuthorWithBooksResponse(
                    author_id=author_id,
                    author_name=data["author_name"],
                    books=data["books"]
                )
            )

        return result
        