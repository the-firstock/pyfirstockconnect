import json
import ast

from enum import Enum
from typing import List, Optional
from datetime import date, datetime

from thefirstock.pyClient import Client
from thefirstock.pyClient.utils.encoders import date_encoder
from thefirstock.pyClient.utils.encoders import password_hash_encoder
from pydantic import BaseModel, IPvAnyAddress, EmailStr, SecretStr, root_validator
from thefirstock.pyClient.utils.decoders import build_loader, timestamp_decoder, datetime_decoder


SOCKET_URL = r'wss://norenapi.thefirstock.com/NorenWSTP/'

try:
    client = Client(socket_url=SOCKET_URL)
except Exception as e:
    print(e)


class ResponseStatus(str, Enum):
    OK = 'Ok'
    NOT_OK = 'Not_Ok'


class LoginRequestModel(BaseModel):
    apkversion: Optional[str] = "1.0.0"

    uid: str

    pwd: Optional[SecretStr]

    dpin: Optional[SecretStr]

    factor2: str

    vc: str

    appkey: str

    imei: Optional[str] = "12345"

    addldivinf: Optional[str]

    ipaddr: Optional[IPvAnyAddress]

    source: Optional[str] = "API"

    @root_validator(allow_reuse=True)
    def validate(cls, values: dict):
        pwd_is_present = values.get('pwd') is not None
        dpin_is_present = values.get('dpin') is not None
        valid = pwd_is_present or dpin_is_present
        if not valid:
            raise ValueError('Either pwd or dpin should be present')
        return values

    class Config:
        json_encoders = {
            date: date_encoder(),
            SecretStr: password_hash_encoder()
        }


class LoginResponseModel(BaseModel):
    status: ResponseStatus = ResponseStatus.OK

    susertoken: Optional[str]

    spasswordreset: Optional[str]

    exarr: Optional[List[str]]

    uname: Optional[str]

    actid: Optional[str]

    email: Optional[EmailStr]

    brkname: Optional[str]

    emsg: Optional[str]

    class Config:
        json_loads = build_loader({
            "lastaccesstime": timestamp_decoder(),
            "request_time": datetime_decoder()
        })


def webSocketLogin():
    with open("config.json") as file:
        data = json.load(file)

    client.login(data)

    return client
