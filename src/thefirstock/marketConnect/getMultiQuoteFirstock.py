from thefirstock.marketConnect.getMultiQuoteFunctionality.execution import *


def firstock_getMultiQuote(dataToken):
    try:
        getQuotes = firstockGetMultiQuote(
            dataToken=dataToken
        ).firstockGetMultiQuote()

        return getQuotes

    except Exception as e:
        print(e)
