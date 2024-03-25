from thefirstock.ordersNReport.cancelOrderFunctionality.functions import *


class FirstockCancelOrder:
    def __init__(self, orderNumber, userId):
        self.cancelOrder = ApiRequests()
        self.userId = userId
        self.orderNumber = orderNumber

    def firstockCancelOrder(self):
        result = self.cancelOrder.firstockCancelOrder(self.orderNumber, self.userId)
        return result
