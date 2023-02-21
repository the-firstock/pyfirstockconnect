"""
The model for sending touchline subscription & unsubscription request
"""

from typing import List
from pydantic import BaseModel

from ..enums import MessageTopic
from ...utils.encoders import build_dumber, list_encoder


class TouchlineSubscribeModel(BaseModel):
    """
  The touchline subscription request model
  """
    t: MessageTopic = MessageTopic.TOUCHLINE_FEED
    """Always 't' for touchline task"""
    k: List[str] = []
    """One or more scriplist for subscription"""

    class Config:
        """The model config"""
        json_dumps = build_dumber({
            "k": list_encoder("|")
        })


class TouchlineUnsubscribeModel(BaseModel):
    """
  The touchline un-subscribe request model
  """
    t: MessageTopic = MessageTopic.UNSUBSCRIBE_FEED
    """Always 'u' for unsubscribe touchline task"""
    k: List[str] = []
    """One or more scriplist for unsubscription"""

    class Config:
        """The model config"""
        json_dumps = build_dumber({
            "k": list_encoder("|")
        })
