from dto.res.BookResponse import AuthorWithBooksResponse
from models.author import AuthorsModel
from models.book import BookModel
from repositories.base_repository import BaseRepository


class AuthorRepository(BaseRepository):
    model = AuthorsModel
    
    def get_all_book_of_author(self) -> list[AuthorWithBooksResponse]:
        return (
            self.db.query(
                AuthorsModel.id.label("author_id"),
                AuthorsModel.name.label("author_name"),
                BookModel.id.label("book_id"),
                BookModel.title.label("book_title"),
                BookModel.published_year
            )
            .outerjoin(BookModel, BookModel.author_id == AuthorsModel.id)
            .filter(AuthorsModel.is_deleted.is_(False))
            .all()
        )

        # return [AuthorWithBooksResponse(**row._asdict()) for row in res]
