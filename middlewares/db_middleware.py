from fastapi import Request
from sqlalchemy.exc import DatabaseError
from starlette.middleware.base import BaseHTTPMiddleware

from exceptions.system_exception import DBOperationalError
from utils.dependencies import get_db_session
from utils.response import response_fail


class DatabaseSessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        # Declare a db_session for the request
        request.state.db = get_db_session()

        try:
            response = await call_next(request)
            request.state.db.commit()
            return response
        except DatabaseError as e:
            request.state.db.rollback()
            return response_fail(DBOperationalError())
        finally:
            request.state.db.close()
