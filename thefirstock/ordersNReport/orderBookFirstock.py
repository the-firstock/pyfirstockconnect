from thefirstock.ordersNReport.orderBookFunctionality.execution import *


def firstock_orderBook():
    try:
        orderBook = FirstockOrderBook().firstockOrderBook()

        return orderBook

    except Exception as e:
        print(e)
