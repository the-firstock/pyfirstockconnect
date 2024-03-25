from thefirstock.marketConnect.getIndexListFunctionality.execution import *


def firstock_getIndexList(exchange, userId):
    try:
        getIndexList = FirstockGetIndexList(
            exch=exchange,
            userId = userId
        )

        result = getIndexList.firstockGetIndexList()
        return result

    except Exception as e:
        print(e)
