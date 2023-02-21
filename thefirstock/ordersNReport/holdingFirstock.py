from thefirstock.ordersNReport.holdingsFunctionality.execution import *


def firstock_Holding():
    try:

        holding = FirstockHoldings().firstockHoldings()

        return holding

    except Exception as e:
        print(e)

