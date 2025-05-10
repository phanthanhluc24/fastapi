from db.session import engine
from db.base import Base

def init_db():
    # Tạo tất cả các bảng dựa trên model
    Base.metadata.create_all(bind=engine)