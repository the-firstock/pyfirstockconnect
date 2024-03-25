from thefirstock.marketConnect.getMultiQuoteLTPFuntionality.execution import *


def firstock_getMultiQuoteLTP(dataToken, userId):
    try:
        getQuotes = firstockGetMultiQuoteLTP(
            dataToken=dataToken,
            userId=userId
        ).firstockGetMultiQuoteLTP()

        return getQuotes

    except Exception as e:
        print(e)
