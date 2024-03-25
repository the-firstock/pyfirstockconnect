from thefirstock.marketConnect.getMultiQuoteFunctionality.execution import *


def firstock_getMultiQuote(dataToken, userId):
    try:
        getQuotes = firstockGetMultiQuote(
            dataToken=dataToken,
            userId=userId
        ).firstockGetMultiQuote()

        return getQuotes

    except Exception as e:
        print(e)
