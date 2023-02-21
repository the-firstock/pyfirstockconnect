"""
Commonly used enumerators
"""
from enum import Enum


class RequestSourceType(str, Enum):
  API = 'API'


class RestMethod(str, Enum):
  """
  Enumeration for REST methods
  """
  GET = 'get'
  POST = 'post'
  PATCH = 'patch'
  PUT = 'put'
  DELETE = 'delete'
  OPTION = 'option'
  HEAD = 'head'

class ResponseStatus(str, Enum):
  """
  The response success or failure status
  """
  OK = 'Ok'
  NOT_OK = 'Not_Ok'


class AlertType(str, Enum):
  """
  The available alert types
  """
  LTP_A = 'LTP_A'
  LTP_B = 'LTP_B'
  CH_PER_A = 'CH_PER_A'
  CH_PER_B = 'CH_PER_B'
  ATP_A = 'ATP_A'
  ATP_B = 'ATP_B'
  LTP_A_52HIGH = 'LTP_A_52HIGH'
  LTP_B_52LOW = 'LTP_B_52LOW'
  VOLUME_A = 'VOLUME_A'
  OI_A = 'OI_A'
  OI_B = 'OI_B'
  TOI_A = 'TOI_A'
  TOI_B = 'TOI_B'
  LMT_BOS_O = 'LMT_BOS_O'
