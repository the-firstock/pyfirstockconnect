from thefirstock.ordersNReport.basketMarginFunctionality.functions import *


class FirstockBasketMargin:
    def __init__(self, basket):
        self.BasketMargin = ApiRequests()
        self.basket = basket

    def firstockBasketMargin(self):
        result = self.BasketMargin.firstockBasketMargin(self.basket)
        return result
