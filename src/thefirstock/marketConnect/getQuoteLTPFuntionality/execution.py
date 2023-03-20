from thefirstock.marketConnect.getQuoteLTPFuntionality.functions import *


class FirstockGetQuotes:
    def __init__(self, exch, token):
        self.getQuotes = ApiRequests()

        self.exch = exch
        self.token = token

    def firstockGetQuoteLTP(self):
        result = self.getQuotes.firstockGetQuoteLTP(self.exch, self.token)
        return result
