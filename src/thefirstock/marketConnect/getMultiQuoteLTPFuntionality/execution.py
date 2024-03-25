from thefirstock.marketConnect.getMultiQuoteLTPFuntionality.functions import *


class firstockGetMultiQuoteLTP:
    def __init__(self, dataToken, userId):
        self.getQuotes = ApiRequests()
        self.userId = userId
        self.dataToken = dataToken

    def firstockGetMultiQuoteLTP(self):
        result = self.getQuotes.firstockGetMultiQuoteLTP(self.dataToken, self.userId)
        return result
