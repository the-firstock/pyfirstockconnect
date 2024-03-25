from thefirstock.ordersNReport.positionBookFunctionality.functions import *


class FirstockPositionBook:
    def __init__(self, userId):
        self.positionBook = ApiRequests()
        self.userId= userId

    def firstockPositionBook(self):
        result = self.positionBook.firstockPositionBook(self.userId)
        return result
