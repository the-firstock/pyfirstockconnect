from thefirstock.ordersNReport.basketMarginFunctionality.functions import *


class FirstockBasketMargin:
    def __init__(self, basket, userId):
        self.BasketMargin = ApiRequests()
        self.basket = basket
        self.userId = userId

    def firstockBasketMargin(self):
        result = self.BasketMargin.firstockBasketMargin(self.basket, self.userId)
        return result
