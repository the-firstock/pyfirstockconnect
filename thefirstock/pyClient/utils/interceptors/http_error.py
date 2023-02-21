"""
The interceptor that throws proper http exceptions based on response status
"""
from typing import Dict, Type
import json

from ...common import exceptions
from .interceptor import Interceptor

__all__ = [
  'HttpErrorInterceptor'
]
