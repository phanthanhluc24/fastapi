from sqlalchemy.orm import Session

from repositories.bookloan_repository import BookLoanRepository

def create_book_loan(db: Session):
    book_loans = [
        {
            "id": 1,
            "book_id":2,
            "borrower_name": "Hồ Thị A",
            "loan_date": "2024/02/07",
            "return_date": None
        },
                {
            "id": 1,
            "book_id":1,
            "borrower_name": "Hồ Thị B",
            "loan_date": "2024/02/07",
            "return_date": "2024/02/07"
        },
                {
            "id": 1,
            "book_id":3,
            "borrower_name": "Hồ Thị C",
            "loan_date": "2024/02/07",
            "return_date": None
        },
                {
            "id": 1,
            "book_id":4,
            "borrower_name": "Hồ Thị B",
            "loan_date": "2024/02/07",
            "return_date": None
        },
                {
            "id": 1,
            "book_id":5,
            "borrower_name": "Hồ Thị A",
            "loan_date": "2024/02/07",
            "return_date": None
        },
    ]

    book_loan_repo = BookLoanRepository(db)
    for book_loan in book_loans:
        book_loan_repo.create(book_loan)
    db.commit()
    return book_loans
