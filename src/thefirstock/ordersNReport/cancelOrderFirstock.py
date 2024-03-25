from thefirstock.ordersNReport.cancelOrderFunctionality.execution import *


def firstock_cancelOrder(orderNumber, userId):
    try:
        cancelOrder = FirstockCancelOrder(
            orderNumber=orderNumber,
            userId=userId
        ).firstockCancelOrder()

        return cancelOrder

    except Exception as e:
        print(e)
