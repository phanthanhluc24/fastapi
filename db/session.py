from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings
from typing import TypeVar

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

engine = create_engine(settings.database_url,echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
ModelType = TypeVar("ModelType", bound=Base)
