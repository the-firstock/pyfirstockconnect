"""
The context models required for datasource
"""
from typing import Dict, Optional
from pydantic import BaseModel
from requests.models import Response
from ....common.enums import RestMethod

class RestContext(BaseModel):
  """
  The context for RestDataSource
  """
  url: str
  method: RestMethod
  data: Optional[str]
  params: Dict[str, str]
  headers: Dict[str, str]
  result: Optional[str]
  response: Optional[Response]

  class Config:
    arbitrary_types_allowed = True