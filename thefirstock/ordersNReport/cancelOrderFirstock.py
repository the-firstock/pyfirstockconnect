from thefirstock.ordersNReport.cancelOrderFunctionality.execution import *


def firstock_cancelOrder(orderNumber):
    try:
        cancelOrder = FirstockCancelOrder(
            orderNumber=orderNumber
        ).firstockCancelOrder()

        return cancelOrder

    except Exception as e:
        print(e)
