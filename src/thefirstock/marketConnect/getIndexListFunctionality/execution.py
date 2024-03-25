from thefirstock.marketConnect.getIndexListFunctionality.functions import *


class FirstockGetIndexList:
    def __init__(self, exch, userId):
        self.getIndexList = ApiRequests()
        self.exch = exch
        self.userId = userId

    def firstockGetIndexList(self):
        result = self.getIndexList.firstockGetIndexList(self.exch, self.userId)
        return result
