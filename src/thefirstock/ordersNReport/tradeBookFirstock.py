from thefirstock.ordersNReport.tradeBookFunctionality.execution import *


def firstock_TradeBook(userId):
    try:
        tradeBook = FirstockTradeBook(userId).firstockTradeBook()
        return tradeBook

    except Exception as e:
        print(e)
