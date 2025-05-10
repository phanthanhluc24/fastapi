from http import HTTPStatus

from exceptions.base_exception import BaseException


class AppException(BaseException):
    rollback = False


class AuthException(AppException):
    http_code = HTTPStatus.UNAUTHORIZED
    error_code = "ERR_AUTH_001"
    message = "Unauthorized request!"

    def __init__(self, message: str = None):
        if message:
            self.message = message  # Override the message if provided
        super().__init__(self.message)


class AuthTokenMissingException(AuthException):
    error_code = "ERR_AUTH_002"
    message = "Authorization token missing!"


class LoginException(AuthException):
    error_code = "ERR_AUTH_003"
    message = "Username or password wrong!"


class RefreshTokenMissingException(AuthException):
    error_code = "ERR_AUTH_004"
    message = "Refresh token missing!"


class NotFoundException(AppException):
    http_code = HTTPStatus.NOT_FOUND
    error_code = "ERR_RES_001"
    message = "Resource not found!"

    def __init__(self, message: str = None):
        if message:
            self.message = message  # Override the message if provided
        super().__init__(self.message)


class InternalException(AppException):
    http_code = HTTPStatus.INTERNAL_SERVER_ERROR
    error_code = "ERR_RES_001"
    message = "Internal Error"

    def __init__(self, message: str = None):
        if message:
            self.message = message  # Override the message if provided
        super().__init__(self.message)


class ConflictException(AppException):
    http_code = HTTPStatus.CONFLICT
    error_code = "ERR_RES_001"
    message = "Conflict Error"

    def __init__(self, message: str = None):
        if message:
            self.message = message  # Override the message if provided
        super().__init__(self.message)


class BadRequestException(AppException):
    http_code = HTTPStatus.BAD_REQUEST
    error_code = "ERR_BODY_001"
    message = "Bad Request"

    def __init__(self, message: str = None):
        if message:
            self.message = message  # Override the message if provided
        super().__init__(self.message)


class ForbiddenException(AppException):
    http_code = HTTPStatus.FORBIDDEN
    error_code = "ERR_BODY_001"
    message = "Forbidden"

    def __init__(self, message: str = None):
        if message:
            self.message = message  # Override the message if provided
        super().__init__(self.message)


class EntityTooLargeException(AppException):
    http_code = HTTPStatus.REQUEST_ENTITY_TOO_LARGE
    error_code = "ERR_FILE_001"
    message = "File size exceeds the limit"

    def __init__(self, message: str = None):
        if message:
            self.message = message  # Override the message if provided
        super().__init__(self.message)
