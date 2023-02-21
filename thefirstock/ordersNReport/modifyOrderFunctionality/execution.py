from thefirstock.ordersNReport.modifyOrderFunctionality.functions import *


class FirstockModifyOrder:
    def __init__(self, qty, orderNumber, trgprc, prc, exchange, tradingSymbol, priceType):
        self.modifyOrder = ApiRequests()
        self.qty = qty
        self.orderNumber = orderNumber
        self.trgprc = trgprc
        self.prc = prc
        self.exchange = exchange
        self.tradingSymbol = tradingSymbol
        self.priceType = priceType

    def firstockModifyOrder(self):
        result = self.modifyOrder.firstockModifyOrder(self.qty, self.orderNumber, self.trgprc, self.prc, self.exchange,
                                                      self.tradingSymbol, self.priceType)
        return result
