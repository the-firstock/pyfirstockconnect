"""
The model for sending depth subscription & unsubscription request
"""

from typing import List
from pydantic import BaseModel

from ..enums import MessageTopic
from ...utils.encoders import build_dumber, list_encoder


class DepthSubscribeModel(BaseModel):
    """
  The depth subscription request model
  """
    t: MessageTopic = MessageTopic.DEPTH_SUB
    """Always 'd' for depth task"""
    k: List[str] = []
    """One or more scriplist for subscription"""

    class Config:
        """The model config"""
        json_dumps = build_dumber({
            "k": list_encoder("|")
        })


class DepthUnsubscribeModel(BaseModel):
    """
  The depth subscription request model
  """
    t: MessageTopic = MessageTopic.DEPTH_UNSUB
    """Always 'ud' for unsubscribe depth task"""
    k: List[str] = []
    """One or more scriplist for unsubscription"""

    class Config:
        """The model config"""
        json_dumps = build_dumber({
            "k": list_encoder("|")
        })
