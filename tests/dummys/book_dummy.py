from sqlalchemy.orm import Session

from repositories.book_repository import BookRepository

def create_book(db: Session):
    books = [
        {
            "id":1,
            "title":"Anh yêu em 1",
            "author_id":1,
            "published_year":2006,
            "is_deleted": 0
        },
                {
            "id":2,
            "title":"Anh yêu em 2",
            "author_id":2,
            "published_year":2006,
            "is_deleted": 0
        },
                {
            "id":3,
            "title":"Anh yêu em 3",
            "author_id":1,
            "published_year":2006,
            "is_deleted": 0
        },
                {
            "id":4,
            "title":"Anh yêu em 4",
            "author_id":2,
            "published_year":2006,
            "is_deleted": 0
        },
                {
            "id":5,
            "title":"Anh yêu em 5",
            "author_id":3,
            "published_year":2006,
            "is_deleted": 0
        },
    ]

    book_repo = BookRepository(db)
    for book in books:
        book_repo.create(book)
    db.commit()
    return books