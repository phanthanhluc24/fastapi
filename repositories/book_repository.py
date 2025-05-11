from schemas.res.BookResponse import BookResponse
from models.author import AuthorsModel
from repositories.base_repository import BaseRepository
from models.book import BookModel
class BookRepository(BaseRepository):
    model = BookModel

    def get_book_by_id_and_author(self, book_id: int) -> BookResponse:
        return  (
            self.db.query(
                BookModel.id.label("book_id"),
                BookModel.title, 
                BookModel.published_year,
                AuthorsModel.name,
                AuthorsModel.birth_year
            )
            .select_from(BookModel)
            .join(AuthorsModel, BookModel.author_id == AuthorsModel.id)
            .filter(BookModel.id == book_id)
            .first()
        )._asdict()
    

    def get_book_and_author(self) -> list[BookResponse]:
        res =  (
            self.db.query(
                BookModel.id.label("book_id"),
                BookModel.title, 
                BookModel.published_year,
                AuthorsModel.name,
                AuthorsModel.birth_year
            )
            .select_from(BookModel)
            .join(AuthorsModel, BookModel.author_id == AuthorsModel.id)
            .all()
        )
    
        return [BookResponse(**row._asdict()) for row in res]
    