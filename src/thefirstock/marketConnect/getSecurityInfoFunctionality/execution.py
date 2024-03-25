from thefirstock.marketConnect.getSecurityInfoFunctionality.functions import *


class FirstockGetSecurityInfo:
    def __init__(self, exch, token, userId):
        self.getSecurityInfo = ApiRequests()
        self.exch = exch
        self.token = token
        self.userId = userId

    def firstockGetSecurityInfo(self):
        result = self.getSecurityInfo.firstockGetSecurityInfo(self.exch, self.token, self.userId)
        return result
