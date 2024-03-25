from thefirstock.marketConnect.getSecurityInfoFunctionality.execution import *


def firstock_getSecurityInfo(tradingSymbol, exchange, userId):
    try:

        securityInfo = FirstockGetSecurityInfo(
            exch=exchange,
            token=tradingSymbol,
            userId=userId
        ).firstockGetSecurityInfo()

        return securityInfo

    except Exception as e:
        print(e)
