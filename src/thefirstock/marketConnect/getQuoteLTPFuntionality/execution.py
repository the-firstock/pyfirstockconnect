from thefirstock.marketConnect.getQuoteLTPFuntionality.functions import *


class FirstockGetQuotes:
    def __init__(self, exch, token, userId):
        self.getQuotes = ApiRequests()
        self.userId = userId
        self.exch = exch
        self.token = token

    def firstockGetQuoteLTP(self):
        result = self.getQuotes.firstockGetQuoteLTP(self.exch, self.token, self.userId)
        return result
