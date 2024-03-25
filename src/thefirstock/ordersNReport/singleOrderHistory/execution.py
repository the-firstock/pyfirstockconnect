from thefirstock.ordersNReport.singleOrderHistory.functions import *


class FirstockSingleOrderHistory:
    def __init__(self, orderNumber, userId):
        self.singleOrderHistory = ApiRequests()
        self.userId=userId
        self.orderNumber = orderNumber

    def firstockSingleOrderHistory(self):
        result = self.singleOrderHistory.firstockSingleOrderHistory(self.orderNumber, self.userId)
        return result
