from thefirstock.marketConnect.getSecurityInfoFunctionality.execution import *


def firstock_getSecurityInfo(token, exchange):
    try:

        securityInfo = FirstockGetSecurityInfo(
            exch=exchange,
            token=token
        ).firstockGetSecurityInfo()

        return securityInfo

    except Exception as e:
        print(e)
