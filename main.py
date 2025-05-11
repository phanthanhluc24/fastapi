from typing import Union
from exceptions.app_exception import AppException
from exceptions.handler import app_exception_handler, system_exception_handler
from exceptions.system_exception import SystemException
from middlewares.auth_middleware import JWTAuthMiddleware
from middlewares.db_middleware import DatabaseSessionMiddleware
from fastapi import APIRouter, FastAPI
from api.v1.router import api_router
app = FastAPI()
app.include_router(api_router, prefix="/api/v1")

__EXCEPTION_HANDLERS__ = [
    (AppException, app_exception_handler),
    (SystemException, system_exception_handler),
]

for exc, handler in __EXCEPTION_HANDLERS__:
    app.add_exception_handler(exc, handler)


__MIDDLEWARES__ = [ DatabaseSessionMiddleware, JWTAuthMiddleware ]

for middleware in __MIDDLEWARES__.__reversed__():
    app.add_middleware(middleware)

