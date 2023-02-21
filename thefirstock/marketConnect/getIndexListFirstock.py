from thefirstock.marketConnect.getIndexListFunctionality.execution import *


def firstock_getIndexList(exchange):
    try:
        getIndexList = FirstockGetIndexList(
            exch=exchange
        )

        result = getIndexList.firstockGetIndexList()
        return result

    except Exception as e:
        print(e)
