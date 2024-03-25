from thefirstock.marketConnect.getQuotesFunctionality.functions import *


class FirstockGetQuotes:
    def __init__(self, exch, token, userId):
        self.getQuotes = ApiRequests()
        self.userId = userId
        self.exch = exch
        self.token = token

    def firstockGetQuotes(self):
        result = self.getQuotes.firstockGetQuotes(self.exch, self.token, self.userId)
        return result
