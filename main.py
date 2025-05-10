from typing import Union
from controller.bookloan_controller import bookloan_router as bookloan_router
from controller.author_controller import author_router as author_router
from controller.book_controller import book_router as book_router
from controller.user_controller import user_router as user_router
from exceptions.app_exception import AppException
from exceptions.handler import app_exception_handler, system_exception_handler
from exceptions.system_exception import SystemException
from middlewares.db_middleware import DatabaseSessionMiddleware
from fastapi import APIRouter, FastAPI
from db.init_db import init_db
app = FastAPI()

api_router = APIRouter()
api_router.include_router(author_router, prefix="/authors", tags=["authors"])
api_router.include_router(book_router, prefix="/books", tags=["books"])
api_router.include_router(bookloan_router, prefix="/bookloans", tags=["bookloan"])
api_router.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(api_router, prefix="/api")

__EXCEPTION_HANDLERS__ = [
    (AppException, app_exception_handler),
    (SystemException, system_exception_handler),
]

for exc, handler in __EXCEPTION_HANDLERS__:
    app.add_exception_handler(exc, handler)


__MIDDLEWARES__ = [ DatabaseSessionMiddleware ]

for middleware in __MIDDLEWARES__.__reversed__():
    app.add_middleware(middleware)


@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

