from sqlalchemy.orm import Session

from repositories.author_repository import AuthorRepository

def create_author(db: Session):
    authors = [
        {
            "id": 1,
            "name":"Hồ Văn A",
            "birth_year":2002,
            "is_deleted": False
        },
        {
            "id": 2,
            "name":"Hồ Văn B",
            "birth_year":2002,
            "is_deleted": False
        },
        {
            "id": 3,
            "name":"Hồ Văn C",
            "birth_year":2002,
            "is_deleted": False
        },
        {
            "id": 4,
            "name":"Hồ Văn D",
            "birth_year":2002,
            "is_deleted": False
        },
        {
            "id": 5,
            "name":"Hồ Văn E",
            "birth_year":2002,
            "is_deleted": False
        },
    ]

    author_repo = AuthorRepository(db)
    for author in authors:
        author_repo.create(author)
    db.commit()
    return authors
