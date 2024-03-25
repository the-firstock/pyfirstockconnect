from thefirstock.ordersNReport.limitFunctionality.execution import *


def firstock_Limits(userId):
    try:

        limits = FirstockLimits(userId).firstockLimits()

        return limits

    except Exception as e:
        print(e)
