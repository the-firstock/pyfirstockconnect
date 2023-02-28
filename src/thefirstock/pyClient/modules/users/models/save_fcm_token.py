"""
Request and response models for save fcm token
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['SaveFCMTokenRequestModel', 'SaveFCMTokenResponseModel']


class SaveFCMTokenRequestModel(BaseModel):
    """
  The request model for logout endpoint
  """
    uid: str
    """The user id of the login user"""
    fcmtkn: str
    """FCM token collected from device"""


class SaveFCMTokenResponseModel(BaseModel):
    """
  The response model for logout endpoint
  """
    stat: "OK"
    """The logout success or failure status"""
    request_time: Optional[datetime]
    """It will be present only on successful response."""
    emsg: Optional[str]
    """Error message if the request failed"""

    class Config:
        """model configuration"""
        json_loads = build_loader({
            "request_time": datetime_decoder()
        })
