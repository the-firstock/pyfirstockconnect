from thefirstock.ordersNReport.tradeBookFunctionality.functions import *


class FirstockTradeBook:
    def __init__(self, userId):
        self.tradeBook = ApiRequests()
        self.userId = userId

    def firstockTradeBook(self):
        result = self.tradeBook.firstockTradeBook(self.userId)
        return result
