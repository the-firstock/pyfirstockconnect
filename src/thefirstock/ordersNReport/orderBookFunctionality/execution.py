from thefirstock.ordersNReport.orderBookFunctionality.functions import *


class FirstockOrderBook:
    def __init__(self, userId):
        self.orderBook = ApiRequests()
        self.userId = userId

    def firstockOrderBook(self):
        result = self.orderBook.firstockOrderBook(self.userId)
        return result
