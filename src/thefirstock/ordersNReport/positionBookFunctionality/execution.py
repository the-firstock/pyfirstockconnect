from thefirstock.ordersNReport.positionBookFunctionality.functions import *


class FirstockPositionBook:
    def __init__(self):
        self.positionBook = ApiRequests()

    def firstockPositionBook(self):
        result = self.positionBook.firstockPositionBook()
        return result
