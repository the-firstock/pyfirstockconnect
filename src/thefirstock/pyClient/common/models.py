"""
Common models used across the project
"""

from datetime import date
from typing import List, Optional
from pydantic import BaseModel

from ..utils.decoders import build_loader, datetime_decoder


class Product(BaseModel):
    """
  The product model
  """
    prd: str
    """The product name"""
    s_prdt_ali: str
    """The product display name"""
    exch: List[str]
    """List of strings with enabled, allowed exchange names"""


class BankDetails(BaseModel):
    """
  The bank details model
  """
    bankn: Optional[str]
    """Bank Name"""
    acctnum: Optional[str]
    """Account Number"""


class DpAccountNumber(BaseModel):
    """
  The dp account number model
  """
    dpnum: Optional[str]


class Scrip(BaseModel):
    """
  The scrip model
  """
    exch: Optional[str]
    """Exchange"""
    tsym: Optional[str]
    """Trading symbol of the scrip (contract)"""
    token: Optional[str]
    """Token of the scrip (contract)"""
    pp: Optional[float]
    """Price precision"""
    ti: Optional[float]
    """Tick size"""
    ls: Optional[float]
    """Lot size"""


class IndexTokenPair(BaseModel):
    """
  The basket criteria pair
  """
    idxname: str
    """The index name"""
    token: str
    """Index token used to subscribe"""


class BasketCriteriaPair(BaseModel):
    """
  The basket criteria pair
  """
    bskt: str
    """The basket name"""
    crt: str
    """The criteria"""


class TBContract(BaseModel):
    """
  Top/Bottom contract
  """
    tsym: Optional[str]
    """Trading symbol"""
    lp: Optional[str]
    """LTP"""
    c: Optional[str]
    """Previous Close price"""
    v: Optional[str]
    """volume"""
    value: Optional[str]
    """Total traded value"""
    oi: Optional[str]
    """Open interest"""
    pc: Optional[str]
    """LTP percentage change"""


class AlertTypeModel(BaseModel):
    """
  The alert type model
  """
    ai_t: str
    """Alert type"""


class TradeDate(BaseModel):
    """
  The trade date model
  """
    trd_date: date

    class Config:
        """The model config"""
        json_loads = build_loader({
            "trd_date": datetime_decoder(transform=lambda dt: dt.date())
        })


class ExchTsym(BaseModel):
    """The exch_tsym model"""
    exch: Optional[str]
    """NSE, BSE, NFO ... Exchange"""
    tsym: Optional[str]
    """Trading symbol of the scrip (contract)"""
    token: Optional[str]
    """Token of the scrip (contract)"""
    pp: Optional[str]
    """Price precision"""
    ti: Optional[float]
    """Tick size"""
    ls: Optional[float]
    """Lot size"""
