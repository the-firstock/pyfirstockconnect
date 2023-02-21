from thefirstock.marketConnect.getSecurityInfoFunctionality.functions import *


class FirstockGetSecurityInfo:
    def __init__(self, exch, token):
        self.getSecurityInfo = ApiRequests()
        self.exch = exch
        self.token = token

    def firstockGetSecurityInfo(self):
        result = self.getSecurityInfo.firstockGetSecurityInfo(self.exch, self.token)
        return result
