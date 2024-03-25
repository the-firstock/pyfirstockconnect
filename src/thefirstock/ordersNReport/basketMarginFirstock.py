from thefirstock.ordersNReport.basketMarginFunctionality.execution import *


def firstock_BasketMargin(basket, userId):
    try:
        placeOrder = FirstockBasketMargin(
            basket=basket,
            userId=userId
        )

        result = placeOrder.firstockBasketMargin()
        return result

    except Exception as e:
        print(e)
