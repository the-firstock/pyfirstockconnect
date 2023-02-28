from thefirstock.ordersNReport.holdingsFunctionality.functions import *


class FirstockHoldings:
    def __init__(self):
        self.holdings = ApiRequests()

    def firstockHoldings(self):
        result = self.holdings.firstockHoldings()
        return result
