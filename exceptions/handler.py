from exceptions.app_exception import AppException
from exceptions.system_exception import SystemException
from utils.response import response_fail


async def app_exception_handler(_, exc: AppException):

    return response_fail(exc)


async def system_exception_handler(_, exc: SystemException):

    return response_fail(exc)
