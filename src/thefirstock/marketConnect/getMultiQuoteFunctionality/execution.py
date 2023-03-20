from thefirstock.marketConnect.getMultiQuoteFunctionality.functions import *


class firstockGetMultiQuote:
    def __init__(self, dataToken):
        self.getQuotes = ApiRequests()

        self.dataToken = dataToken

    def firstockGetMultiQuote(self):
        result = self.getQuotes.firstockGetMultiQuote(self.dataToken)
        return result
