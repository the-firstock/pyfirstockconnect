from thefirstock.marketConnect.timePriceSeriesFunctionality.execution import *


def firstock_TimePriceSeries(exchange, token, startTime, endTime, interval):
    try:

        timePrice = FirstockTimePriceSeries(
            exch=exchange,
            token=token,
            st=startTime,
            et=endTime,
            intrv=interval
        ).firstockTimePriceSeries()

        return timePrice

    except Exception as e:
        print(e)
