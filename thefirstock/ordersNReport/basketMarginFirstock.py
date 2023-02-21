from thefirstock.ordersNReport.basketMarginFunctionality.execution import *


def firstock_BasketMargin(basket):
    try:
        placeOrder = FirstockBasketMargin(
            basket=basket,
        )

        result = placeOrder.firstockBasketMargin()
        return result

    except Exception as e:
        print(e)
