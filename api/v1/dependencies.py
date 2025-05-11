from fastapi import Request
from sqlalchemy.orm import Session
from db.session import SessionLocal


def get_db(request: Request) -> Session:
    return request.state.db

def get_db_session() -> Session:
    return SessionLocal()
