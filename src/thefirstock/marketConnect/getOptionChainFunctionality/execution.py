from thefirstock.marketConnect.getOptionChainFunctionality.functions import *


class FirstockGetOptionChain:
    def __init__(self, tsym, exch, strprc, cnt):
        self.getOptionChain = ApiRequests()

        self.tsym = tsym
        self.exch = exch
        self.strprc = strprc
        self.cnt = cnt

    def firstockGetOptionChain(self):
        result = self.getOptionChain.firstockGetOptionChain(self.tsym, self.exch, self.strprc, self.cnt)
        return result
