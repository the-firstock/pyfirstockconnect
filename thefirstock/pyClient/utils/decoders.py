"""
Available json decorders to be used for different datatypes in models
"""

import json
from dateutil.parser import parse as parse_date
from datetime import datetime
from typing import Any, Callable, Dict, Union
from pydantic.main import ModelMetaclass


def datetime_decoder(transform: Callable[[datetime], Any] = None, **kwargs):
    """
  Creates a datetime decoder for a given format.

  Args:
    kwargs: The arguments to dateutil.parser.parse method

  Returns:
    Callable[[str], datetime]: The datetime decoder
  """

    def decode(value: str) -> Any:
        """
    Decode the datetime string to datetime instance

    Args:
      value (str): The datetime string

    Returns:
      datetime: The datetime instance
    """
        dt = parse_date(value, **kwargs)
        return dt if transform is None else transform(dt)

    return decode


def nested_model(ModelClass: ModelMetaclass):
    """
  Runs decoders of the nested model

  Returns:
    Callable[[Union[str,int]], datetime]: The datetime decoder
  """

    def decode(value: Any) -> ModelClass:
        """
    Decode nested object into corresponding pydantic model

    Args:
      value (Any): The value as object or list of objects
    """
        if type(value) == list:
            return [ModelClass.parse_raw(json.dumps(val)) for val in value]
        else:
            return ModelClass.parse_raw(json.dumps(value))

    return decode


def timestamp_decoder():
    """
  Creates a timestamp to datetime decoder.

  Returns:
    Callable[[Union[str,int]], datetime]: The datetime decoder
  """

    def decode(value: Union[str, int, float]) -> datetime:
        """
    Decode the timestamp string (or int) to datetime instance

    Args:
      value (Union[str,int]): The timestamp string or number

    Returns:
      datetime: The datetime instance
    """
        return datetime.fromtimestamp(float(value))

    return decode


def build_loader(decoders: Dict[str, Callable[[Any], Any]]):
    """
  Build a json loader function from a map of decoders for fields that needs to be loaded differently.

  Args:
    decoders (Dict[str, Callable[[Any], Any]]): The docoder map
  """

    def loads(json_string: str) -> dict:
        """
    The json loads function for converting json to dict

    Args:
      json_string (str): The json string to load

    Returns:
      dict: The converted python dictionary
    """
        # parse json
        obj = json.loads(json_string)
        # run decoders on the object
        for field, decode in decoders.items():
            # decode the field value
            if field in obj and obj[field] is not None:
                obj[field] = decode(obj[field])
        return obj

    return loads
