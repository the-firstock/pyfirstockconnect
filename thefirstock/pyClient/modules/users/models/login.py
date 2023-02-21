"""
Request and Response models for login
"""
from thefirstock.pyClient.utils.encoders import password_hash_encoder
from pydantic import BaseModel, IPvAnyAddress, EmailStr, SecretStr, root_validator
from typing import List, Union, Optional
from datetime import date, datetime

from ....utils.encoders import date_encoder
from ....utils.decoders import build_loader, timestamp_decoder, datetime_decoder
from ....common.enums import RequestSourceType, ResponseStatus

__all__ = ['LoginRequestModel', 'LoginResponseModel']


class LoginRequestModel(BaseModel):
    """
  The data model for login request
  """
    apkversion: Optional[str] = "1.0.0"
    """Application Version"""
    uid: str
    """User Id of the login user"""
    pwd: Optional[SecretStr]
    """password for login. It will be automatically hashed during the request"""
    dpin: Optional[SecretStr]
    """The device pin"""
    factor2: str
    """DOB or PAN"""
    vc: str
    """Vendor code"""
    appkey: str
    """The APP Key or the API Key or the Vendor key"""
    imei: Optional[str] = "12345"
    """IMEI for mobile (If desktop it takes the MAC address)"""
    addldivinf: Optional[str]
    """
  Value must be in below format:
    iOS - iosInfo.utsname.machine - iosInfo.systemVersion
    Android - androidInfo.model - androidInfo.version
  examples:
    iOS - iPhone 8.0 - 9.0
    Android - Moto G - 9 PKQ1.181203.01
  """
    ipaddr: Optional[IPvAnyAddress]
    """The IP address of the system"""
    source: Optional[str] = "API"
    """Access Type"""

    @root_validator(allow_reuse=True)
    def validate(cls, values: dict):
        """
    Validate the model. The model should contain either of 'pwd' or 'dpin'
    """
        pwd_is_present = values.get('pwd') is not None
        dpin_is_present = values.get('dpin') is not None
        valid = pwd_is_present or dpin_is_present
        if not valid:
            raise ValueError('Either pwd or dpin should be present')
        return values

    class Config:
        """model configuration"""
        json_encoders = {
            date: date_encoder(),
            SecretStr: password_hash_encoder()
        }


class LoginResponseModel(BaseModel):
    """
  The data model for login response
  """
    stat: ResponseStatus = ResponseStatus.OK
    """Login success or failure status"""
    susertoken: Optional[str]
    """Present only on login success. This key is to be passed in subsequent requests"""
    lastaccesstime: Optional[datetime]
    """Present only on login success."""
    request_time: Optional[datetime]
    """It will be present only on successful login."""
    spasswordreset: Optional[str]
    """If Y Mandatory password reset to be enforced. Otherwise the field will be absent."""
    exarr: Optional[List[str]]
    """list of strings with enabled exchange names"""
    uname: Optional[str]
    """Username"""
    actid: Optional[str]
    """Account Id"""
    email: Optional[EmailStr]
    """Email Id"""
    brkname: Optional[str]
    """Broker Id"""
    emsg: Optional[str]
    """Error message if the login failed"""

    class Config:
        """model configuration"""
        json_loads = build_loader({
            "lastaccesstime": timestamp_decoder(),
            "request_time": datetime_decoder()
        })
