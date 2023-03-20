from thefirstock.marketConnect.getMultiQuoteLTPFuntionality.execution import *


def firstock_getMultiQuoteLTP(dataToken):
    try:
        getQuotes = firstockGetMultiQuoteLTP(
            dataToken=dataToken
        ).firstockGetMultiQuoteLTP()

        return getQuotes

    except Exception as e:
        print(e)
