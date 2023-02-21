"""
The base class for creating interceptors
"""

from typing import Generic, TypeVar

C = TypeVar('C')

class Interceptor(Generic[C]):
  """
  The abstract base interceptor.
  Other interceptors should inherit from this.

  Args:
      C: The type of context
  """
  def before(self, context: C) -> C:
    """
    This hook runs before the request is send.
    You can modify the context here to augment the request

    Args:
        context (C): The request context
    """
    return context

  def after(self, context: C) -> C:
    """
    This hook runs after the request is completed and the response is recieved.
    You can modify the response to transform the result.
    Augmenting the request parameters does not do anything.

    Args:
      context (C): The request context
    """
    return context