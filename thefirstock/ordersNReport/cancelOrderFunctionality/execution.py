from thefirstock.ordersNReport.cancelOrderFunctionality.functions import *


class FirstockCancelOrder:
    def __init__(self, orderNumber):
        self.cancelOrder = ApiRequests()

        self.orderNumber = orderNumber

    def firstockCancelOrder(self):
        result = self.cancelOrder.firstockCancelOrder(self.orderNumber)
        return result
