from thefirstock.ordersNReport.singleOrderHistory.execution import *


def firstock_SingleOrderHistory(orderNumber):
    try:
        singleOrderHistory = FirstockSingleOrderHistory(
            orderNumber=orderNumber
        ).firstockSingleOrderHistory()

        return singleOrderHistory

    except Exception as e:
        print(e)
