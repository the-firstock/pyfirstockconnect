from thefirstock.ordersNReport.positionBookFunctionality.execution import *


def firstock_PositionBook(userId):
    try:

        positionBook = FirstockPositionBook(userId).firstockPositionBook()

        return positionBook

    except Exception as e:
        print(e)