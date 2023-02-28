from thefirstock.marketConnect.getQuotesFunctionality.functions import *


class FirstockGetQuotes:
    def __init__(self, exch, token):
        self.getQuotes = ApiRequests()

        self.exch = exch
        self.token = token

    def firstockGetQuotes(self):
        result = self.getQuotes.firstockGetQuotes(self.exch, self.token)
        return result
