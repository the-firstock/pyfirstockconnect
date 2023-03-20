from thefirstock.marketConnect.getMultiQuoteLTPFuntionality.functions import *


class firstockGetMultiQuoteLTP:
    def __init__(self, dataToken):
        self.getQuotes = ApiRequests()

        self.dataToken = dataToken

    def firstockGetMultiQuoteLTP(self):
        result = self.getQuotes.firstockGetMultiQuoteLTP(self.dataToken)
        return result
