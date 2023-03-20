from thefirstock.marketConnect.getQuoteLTPFuntionality.execution import *


def firstock_getQuoteLTP(exchange, token):
    try:
        getQuotes = FirstockGetQuotes(
            exch=exchange,
            token=token
        ).firstockGetQuoteLTP()

        return getQuotes

    except Exception as e:
        print(e)
