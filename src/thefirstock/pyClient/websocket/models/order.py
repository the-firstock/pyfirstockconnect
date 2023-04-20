"""
The model for sending order subscription & unsubscription request
"""

from typing import List
from pydantic import BaseModel

from ..enums import MessageTopic
from ...utils.encoders import build_dumber, list_encoder


class OrderSubscribeModel(BaseModel):
    """
  The order subscription request model
  """
    t: MessageTopic = MessageTopic.ORDER_SUB
    """Always 'o' for order update task"""
    actid: str
    """Account id based on which order updated to be sent."""


class OrderUnsubscribeModel(BaseModel):
    """
  The depth subscription request model
  """
    t: MessageTopic = MessageTopic.ORDER_UNSUB
    """Always 'uo' for unsubscribe order update task"""

    class Config:
        """The model config"""
        json_dumps = build_dumber({
            "k": list_encoder("|")
        })
