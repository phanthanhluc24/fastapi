from schemas.res.BookResponse import BookIsLoanResponse
from schemas.res.BookloanResponse import AuthorLoanHistoryResponse, BookloanResponse
from exceptions.app_exception import NotFoundException
from models.author import AuthorsModel
from models.book import BookModel
from models.bookloan import BookLoanModel
from repositories.base_repository import BaseRepository


class BookLoanRepository(BaseRepository):
    model = BookLoanModel

    def get_bookloans_detail(self, loan_id) -> BookloanResponse:
        return (
            self.db.query(
                BookLoanModel.id.label("loan_id"),
                BookModel.title.label("book_title"),
                AuthorsModel.name.label("author_name"),
                BookLoanModel.borrower_name,
                BookLoanModel.loan_date,
                BookLoanModel.return_date
            )
            .select_from(BookLoanModel)
            .join(BookModel, BookModel.id == BookLoanModel.book_id)
            .join(AuthorsModel, AuthorsModel.id == BookModel.author_id)
            .filter(BookLoanModel.id==loan_id)
            .first()
        )._asdict()

    def get_all_book_is_loans(self) -> list[BookIsLoanResponse]:
        response = (
            self.db.query(
                BookModel.id.label("book_id"),
                BookModel.title.label("title"),
                AuthorsModel.name.label("author_name"),
                BookLoanModel.borrower_name,
                BookLoanModel.loan_date,
                BookLoanModel.return_date
            )
            .select_from(BookLoanModel)
            .join(BookModel, BookModel.id == BookLoanModel.book_id)
            .join(AuthorsModel, AuthorsModel.id == BookModel.author_id)
            .filter(BookLoanModel.return_date.is_(None))
            .all()
        )

        return [BookIsLoanResponse(**row._asdict()) for row in response]
    
    def get_book_loan_history_of_author(self, author_id: int) -> list[AuthorLoanHistoryResponse]:
        response = (
            self.db.query(
                BookModel.title.label("book_title"),
                BookLoanModel.borrower_name,
                BookLoanModel.loan_date,
                BookLoanModel.return_date
            )
            .select_from(BookLoanModel)
            .join(BookModel, BookModel.id == BookLoanModel.book_id)
            .join(AuthorsModel, AuthorsModel.id == BookModel.author_id)
            .filter(AuthorsModel.id == author_id)
            .all()
        )

        return [AuthorLoanHistoryResponse(**row._asdict()) for row in response]
