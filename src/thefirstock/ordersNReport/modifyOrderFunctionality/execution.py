from thefirstock.ordersNReport.modifyOrderFunctionality.functions import *


class FirstockModifyOrder:
    def __init__(self, qty, orderNumber, trgprc, prc, exchange, tradingSymbol, priceType,userId):
        self.modifyOrder = ApiRequests()
        self.qty = qty
        self.orderNumber = orderNumber
        self.trgprc = trgprc
        self.prc = prc
        self.exchange = exchange
        self.tradingSymbol = tradingSymbol
        self.priceType = priceType
        self.userId=userId

    def firstockModifyOrder(self):
        result = self.modifyOrder.firstockModifyOrder(self.qty, self.orderNumber, self.trgprc, self.prc, self.exchange,
                                                      self.tradingSymbol, self.priceType, self.userId)
        return result
