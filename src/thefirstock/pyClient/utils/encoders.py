"""
Available json encoders to be used for different datatypes in models
"""
from datetime import date, datetime
import json
from hashlib import sha256
from typing import Any, Callable, Dict, List

from pydantic.types import SecretStr

__all__ = [
    'date_encoder',
    'password_hash_encoder',
    'list_encoder'
]


def date_encoder(format: str = '%d-%m-%Y'):
    """
  Create a date encoder for the given format

  Args:
      format (str, optional): The date format. Defaults to '%d-%m-%Y'.

  Returns:
      Callable[[date], str]: The date encoder function
  """

    def encode(value: date) -> str:
        """
    Convert a date instance to a string format

    Args:
        value (date): The date instance to convert to

    Returns:
        str: The formatted date
    """
        return value.strftime(format)

    return encode


def timestamp_encoder():
    """
  Create a timestamp encoder

  Returns:
    Callable[[datetime], str]: The password hash encoder function
  """

    def encode(value: datetime) -> str:
        """
    Convert a datetime instance to timestamp (seconds since epoch)

    Args:
        value (date): The date instance to convert to

    Returns:
        str: The timestamp string
    """
        return str(int(value.timestamp()))

    return encode


def password_hash_encoder():
    """
  Create a password hash encoder

  Returns:
    Callable[[str], str]: The password hash encoder function
  """

    def encode(value: SecretStr) -> str:
        """
    Convert a password to its hash

    Args:
      value (str): The password to be hashed

    Returns:
      str: The sha256 hash of the password
    """
        hash_fn = sha256()
        hash_fn.update(value.get_secret_value().encode())
        return hash_fn.hexdigest()

    return encode


def list_encoder(separator: str = ','):
    """
  Create a list encoder

  Args:
    separator (str, optional): The character used to differentiate between list items. Defaults to ','.
  """

    def encode(value: List) -> str:
        """
    Convert a list to a string representation. Each item in the list is converted to a string.

    Args:
      value (List): The list to be converted

    Returns:
      str: The list joined using the seperator
    """
        return separator.join([str(item) for item in value])

    return encode


def build_dumber(encoders: Dict[str, Callable[[Any], Any]]):
    """
  Build a json dumber function from a map of encoders for fields that needs to be encoded differently.

  Args:
    encoders (Dict[str, Callable[[Any], Any]]): The docoder map
  """

    def dumbs(obj: dict, *, default) -> str:
        """
    The json dumbs function for converting dict to json

    Args:
      obj (dict): The dict to be dumped

    Returns:
      str: The converted json string
    """
        # run decoders on the object
        for field, encode in encoders.items():
            # decode the field value
            if field in obj and obj[field] is not None:
                obj[field] = encode(obj[field])
        return json.dumps(obj, default=default)

    return dumbs
