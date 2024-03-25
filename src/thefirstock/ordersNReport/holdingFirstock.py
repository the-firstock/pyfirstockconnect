from thefirstock.ordersNReport.holdingsFunctionality.execution import *


def firstock_Holding(userId):
    try:

        holding = FirstockHoldings(userId).firstockHoldings()
        return holding

    except Exception as e:
        print(e)

