from http import HTTPStatus


class BaseException(Exception):
    http_code: int | str | HTTPStatus
    error_code: str
    message: str
    rollback: bool
