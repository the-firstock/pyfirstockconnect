from thefirstock.marketConnect.getIndexListFunctionality.functions import *


class FirstockGetIndexList:
    def __init__(self, exch):
        self.getIndexList = ApiRequests()
        self.exch = exch

    def firstockGetIndexList(self):
        result = self.getIndexList.firstockGetIndexList(self.exch)
        return result
