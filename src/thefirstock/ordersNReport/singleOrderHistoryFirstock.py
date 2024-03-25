from thefirstock.ordersNReport.singleOrderHistory.execution import *


def firstock_SingleOrderHistory(orderNumber, userId):
    try:
        singleOrderHistory = FirstockSingleOrderHistory(
            orderNumber=orderNumber,
            userId=userId
        ).firstockSingleOrderHistory()

        return singleOrderHistory

    except Exception as e:
        print(e)
