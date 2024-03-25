from thefirstock.marketConnect.getOptionChainFunctionality.functions import *


class FirstockGetOptionChain:
    def __init__(self, tsym, exch, strprc, cnt, userId):
        self.getOptionChain = ApiRequests()
        self.userId = userId
        self.tsym = tsym
        self.exch = exch
        self.strprc = strprc
        self.cnt = cnt

    def firstockGetOptionChain(self):
        result = self.getOptionChain.firstockGetOptionChain(self.tsym, self.exch, self.strprc, self.cnt, self.userId)
        return result
