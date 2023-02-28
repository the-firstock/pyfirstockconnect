from thefirstock.ordersNReport.orderBookFunctionality.functions import *


class FirstockOrderBook:
    def __init__(self):
        self.orderBook = ApiRequests()

    def firstockOrderBook(self):
        result = self.orderBook.firstockOrderBook()
        return result

