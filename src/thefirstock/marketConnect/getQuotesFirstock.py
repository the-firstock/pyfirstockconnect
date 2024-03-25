from thefirstock.marketConnect.getQuotesFunctionality.execution import *


def firstock_getQuote(exchange, tradingSymbol, userId):
    try:
        getQuotes = FirstockGetQuotes(
            exch=exchange,
            token=tradingSymbol,
            userId=userId
        ).firstockGetQuotes()

        return getQuotes

    except Exception as e:
        print(e)
