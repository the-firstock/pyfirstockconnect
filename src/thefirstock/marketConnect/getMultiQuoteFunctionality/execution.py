from thefirstock.marketConnect.getMultiQuoteFunctionality.functions import *


class firstockGetMultiQuote:
    def __init__(self, dataToken, userId):
        self.getQuotes = ApiRequests()
        self.userId = userId
        self.dataToken = dataToken

    def firstockGetMultiQuote(self):
        result = self.getQuotes.firstockGetMultiQuote(self.dataToken, self.userId)
        return result
