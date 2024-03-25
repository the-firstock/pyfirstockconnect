from thefirstock.ordersNReport.limitFunctionality.functions import *


class FirstockLimits:
    def __init__(self, userId):
        self.limits = ApiRequests()
        self.userId = userId

    def firstockLimits(self):
        result = self.limits.firstockLimits(self.userId)
        return result
