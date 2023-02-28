from thefirstock.ordersNReport.tradeBookFunctionality.execution import *


def firstock_TradeBook():
    try:

        tradeBook = FirstockTradeBook().firstockTradeBook()

        return tradeBook

    except Exception as e:
        print(e)
