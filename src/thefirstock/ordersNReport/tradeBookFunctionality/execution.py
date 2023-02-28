from thefirstock.ordersNReport.tradeBookFunctionality.functions import *


class FirstockTradeBook:
    def __init__(self):
        self.tradeBook = ApiRequests()

    def firstockTradeBook(self):
        result = self.tradeBook.firstockTradeBook()
        return result
