"""
The model for sending connection request
"""

from typing import Optional
from pydantic import BaseModel
from ...common.enums import RequestSourceType
from ..enums import MessageTopic


class WebsocketConnectionModel(BaseModel):
    """
  The connection request model
  """
    t: MessageTopic = MessageTopic.CONNECTION
    """The message topic"""
    uid: str
    """User ID"""
    actid: str
    """Account id"""
    source: RequestSourceType = RequestSourceType.API
    """Source should be same as login request."""
    susertoken: Optional[str]
    """User Session Token"""
