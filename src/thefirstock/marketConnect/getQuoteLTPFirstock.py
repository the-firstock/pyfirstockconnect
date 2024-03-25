from thefirstock.marketConnect.getQuoteLTPFuntionality.execution import *


def firstock_getQuoteLTP(exchange, tradingSymbol, userId):
    try:
        getQuotes = FirstockGetQuotes(
            exch=exchange,
            token=tradingSymbol,
            userId=userId
        ).firstockGetQuoteLTP()

        return getQuotes

    except Exception as e:
        print(e)
