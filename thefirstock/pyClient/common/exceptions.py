"""
Custom exceptions for http requests
"""

from typing import Any
from urllib.error import HTTPError
from http import HTTPStatus


class HttpException(HTTPError):
    """
  The base http exception class
  """

    def __init__(self, url: str, code: HTTPStatus, msg: str, headers={}) -> None:
        super().__init__(url, code, msg, headers, None)


class BadRequestError(HttpException):
    """
  The http error corresponding to 400 status code
  """

    def __init__(self, url: str, msg: str = None, headers: Any = {}) -> None:
        """
    Initialize a BadRequestError
    """
        code = HTTPStatus.BAD_REQUEST
        msg = msg or 'Bad Request'
        super().__init__(url, code, msg, headers)


class UnauthorizedError(HttpException):
    """
  The http error corresponding to 401 status code
  """

    def __init__(self, url: str, msg: str = None, headers: Any = {}) -> None:
        """
    Initialize a BadRequestError
    """
        code = HTTPStatus.UNAUTHORIZED
        msg = msg or 'Unauthorized'
        super().__init__(url, code, msg, headers)


class PaymentRequiredError(HttpException):
    """
  The http error corresponding to 402 status code
  """

    def __init__(self, url: str, msg: str = None, headers: Any = {}) -> None:
        """
    Initialize a BadRequestError
    """
        code = HTTPStatus.PAYMENT_REQUIRED
        msg = msg or 'Payment Required'
        super().__init__(url, code, msg, headers)


class ForbiddenError(HttpException):
    """
  The http error corresponding to 403 status code
  """

    def __init__(self, url: str, msg: str = None, headers: Any = {}) -> None:
        """
    Initialize a BadRequestError
    """
        code = HTTPStatus.FORBIDDEN
        msg = msg or 'Forbidden'
        super().__init__(url, code, msg, headers)


class NotFoundError(HttpException):
    """
  The http error corresponding to 404 status code
  """

    def __init__(self, url: str, msg: str = None, headers: Any = {}) -> None:
        """
    Initialize a BadRequestError
    """
        code = HTTPStatus.NOT_FOUND
        msg = msg or 'Not Found'
        super().__init__(url, code, msg, headers)


class InternalServerError(HttpException):
    """
  The http error corresponding to 500 status code
  """

    def __init__(self, url: str, msg: str = None, headers: Any = {}) -> None:
        """
    Initialize a BadRequestError
    """
        code = HTTPStatus.INTERNAL_SERVER_ERROR
        msg = msg or 'Internal Server Error'
        super().__init__(url, code, msg, headers)
