from exceptions.base_exception import BaseException


class SystemException(BaseException):
    http_code = 500
    error_code = "INTERNAL_SERVER_ERROR"
    message = "Internal server error!"
    rollback = True


class DBOperationalError(SystemException):
    error_code = "ERR_DB_001"
    message = "Database operation failed!"
