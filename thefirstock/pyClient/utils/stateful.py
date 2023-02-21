"""
The base stateful class to inherit sub classes from
"""

from typing import Any, Dict

__all__ = ['Stateful']


class Stateful:
    """
  The base stateful class to inherit sub classes from
  """

    def __init__(self, initial_state: Dict[str, Any] = {}) -> None:
        """
    Initialize the stateful class with a state
    """
        self.__state__ = initial_state

    @property
    def state(self):
        """The current app state"""
        return self.__state__

    def get_state(self, key: str, override: Any = None, default: Any = None) -> Any:
        """
    Get a value from the state

    Args:
      key (str): The name of the state var
      override (Any): The value to override the recieved value from
      default (Any): The default value to return if key do not exist

    Returns:
      Any: The value
    """
        return self.state.get(key, default) if override is None else override

    def set_state(self, key: str, value: Any):
        """
    Set a state value

    Args:
      key (str): The name of the state value
      value (Any): The new value to set
    """
        return self.state.update({key: value})
