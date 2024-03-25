from thefirstock.marketConnect.timePriceSeriesFunctionality.functions import *


class FirstockTimePriceSeries:
    def __init__(self, exch, token, et, st, intrv, userId):
        self.timePriceSeries = ApiRequests()

        self.exch = exch
        self.token = token
        self.et = et
        self.st = st
        self.intrv = intrv
        self.userId = userId

    def firstockTimePriceSeries(self):
        result = self.timePriceSeries.firstockTimePriceSeries(self.exch, self.token, self.st, self.et, self.intrv, self.userId)
        return result
