from sqlalchemy.orm import Session
from schemas.req.BookLoanRequest import BookLoanRequest
from schemas.res.BookResponse import BookIsLoanResponse
from schemas.res.BookloanResponse import AuthorLoanHistoryResponse, BookloanResponse
from repositories.author_repository import AuthorRepository
from repositories.book_repository import BookRepository
from repositories.bookloan_repository import BookLoanRepository



class BookLoanService:
    def __init__(self,db:Session):
        self.db = db
        self.book_loan_repository = BookLoanRepository(db)
        self.book_repository = BookRepository(db)
        self.author_repository = AuthorRepository(db)

    def book_loan_by_user(self, data: BookLoanRequest) -> str:
        """_summary_

        Args:
            data (BookLoanRequest): _description_

        Returns:
            str: _description_
        """

        self.book_repository.get_by_id(data.book_id)
        data_dict = data.model_dump()
        self.book_loan_repository.create(data_dict)
        return "Book loan successfully"
    
    def book_loan_by_user_update(self,loan_id: int, data: BookLoanRequest) -> str:
        """_summary_

        Args:
            data (BookLoanRequest): _description_

        Returns:
            str: _description_
        """

        self.book_loan_repository.get_by_id(loan_id)
        data_dict = data.model_dump()
        self.book_loan_repository.update_by_id(loan_id, data_dict)
        return "Update book loan successfully"

    def get_book_loan_detail(self, loan_id: int) -> BookloanResponse: 
        """_summary_

        Args:
            loan_id (int): _description_

        Returns:
            BookloanResponse: _description_
        """

        self.book_loan_repository.get_by_id(loan_id)
        res = self.book_loan_repository.get_bookloans_detail(loan_id)
        return res
    

    def get_all_book_is_loans(self) -> list[BookIsLoanResponse]:
        """_summary_

        Returns:
            list[BookloanResponse]: _description_
        """

        book_loans = self.book_loan_repository.get_all_book_is_loans()
        return book_loans
    

    def get_book_loan_history_of_author(self, author_id: int) -> list[AuthorLoanHistoryResponse]:
        """_summary_

        Args:
            author_id (int): _description_

        Returns:
            list[AuthorLoanHistoryResponse]: _description_
        """
        self.book_repository.get_by_id(author_id)
        res = self.book_loan_repository.get_book_loan_history_of_author(author_id)
        return res
    