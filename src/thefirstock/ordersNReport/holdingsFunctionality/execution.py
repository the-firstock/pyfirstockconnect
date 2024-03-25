from thefirstock.ordersNReport.holdingsFunctionality.functions import *


class FirstockHoldings:
    def __init__(self, userId):
        self.holdings = ApiRequests()
        self.userId = userId

    def firstockHoldings(self):
        result = self.holdings.firstockHoldings(self.userId)
        return result
