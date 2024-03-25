from thefirstock.ordersNReport.orderBookFunctionality.execution import *


def firstock_orderBook(userId):
    try:
        orderBook = FirstockOrderBook(userId).firstockOrderBook()

        return orderBook

    except Exception as e:
        print(e)
